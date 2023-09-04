from constants import AWS
from services.AWS_Service import AWS_Service
from services.HttpxWrapper import HttpxWrapper
import asyncio
import sys
import pandas as pd

aws_service = AWS_Service()
httpxWrapper = HttpxWrapper()
parser = pd


async def getS3FileStream(S3_Url):
    try:
        fileStream = aws_service.getS3FileAsStream(S3_Url)
        return fileStream
    except Exception as e:
        print("Error fetching S3 File:", e)
        sys.exit(1)


async def processVcfFile(stream, start, end, minDP, limit, deNovo):
    try:
        vcfProcessor = VcfProcessor(stream, parser, httpxWrapper)
        await VcfProcessor.loadFromStream(start, end, minDP, limit, deNovo)
    except Exception as e:
        print("Error processing VCF File:", e)
        sys.exit(1)


async def main():
    S3_Url = AWS.Constants.S3_Url

    try:
        stream = await aws_service.getS3FileAsStream(S3_Url)

        async for line in stream:
            print("Read line:")
            print(line)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
