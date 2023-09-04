import httpx
import zlib


class AWS_Service:
    async def getS3File(self, s3Url):
        httpsUrl = s3Url.replace(
            "s3://resources.genoox.com",
            "https://resources.genoox.com.s3.amazonaws.com"
        )

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    httpsUrl,
                    headers={"Accept-Encoding": "gzip"},
                    timeout=None  # Adjust the timeout as needed
                )
                response.raise_for_status()

                # Check if content-encoding is gzip and decode accordingly
                if response.headers.get("content-encoding") == "gzip":
                    async for chunk in response.iter_bytes():
                        yield zlib.decompress(chunk).decode('utf-8')
                else:
                    async for chunk in response.iter_bytes():
                        yield chunk
            except httpx.HTTPError as error:
                raise Exception(f"Error fetching S3 file: {error}")
