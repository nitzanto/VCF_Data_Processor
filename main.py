from constants import AWS
from services.AWS_Service import AWS_Service
import asyncio


async def main():
    S3_Url = AWS.Constants.S3_Url
    aws_service = AWS_Service()

    try:
        stream = await aws_service.getS3FileAsStream(S3_Url)

        async for line in stream:
            print("Read line:")
            print(line)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
