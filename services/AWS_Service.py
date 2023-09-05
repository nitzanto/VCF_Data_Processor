import zlib

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
                decompressor = zlib.decompressobj(32 + zlib.MAX_WBITS)
                async with client.stream('GET', httpsUrl, timeout=None) as response:
                    response.raise_for_status()
                    # Read and decode the response content in chunks
                    async for chunk in response.aiter_bytes():
                        decompressed_chunk = decompressor.decompress(chunk)
                        if decompressed_chunk:
                            yield decompressed_chunk.decode('utf-8')

            except httpx.HTTPError as error:
                raise Exception(f"Error fetching S3 file: {error}")
