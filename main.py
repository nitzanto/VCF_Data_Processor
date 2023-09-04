from constants import AWS
from services import AWS_Service

async def main():
    s3_url = AWS.Constants.S3_URL
    S3_Stream = AWS_Service()

    try:
        data = await AWS_Service.getS3File(s3_url)
        print("Retrieved data:")
        print(data.decode('utf-8'))  # Assuming the data is text
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
