import httpx
from constants import AWS
import gzip
from io import BytesIO


class AWS_Service:
    async def getS3FileAsStream(self, s3Url):
        httpsUrl = s3Url.replace(
            s3Url,
            AWS.Constants.S3_Object_Url
        )

        async with httpx.AsyncClient(verify=False) as client:
            try:
                response = await client.get(httpsUrl)
                response.raise_for_status()

                # Create a generator to stream the content in chunks
                async def stream_content():
                    buffer = BytesIO(response.content)
                    with gzip.GzipFile(fileobj=buffer, mode='rb') as decompressor:
                        while True:
                            chunk = decompressor.read(8192)  # Each chunk is set to 8 KBs
                            if not chunk:
                                break
                            yield chunk.decode('utf-8')

                return stream_content()

            except httpx.HTTPError as error:
                raise Exception(f"Error fetching S3 file: {error}")
