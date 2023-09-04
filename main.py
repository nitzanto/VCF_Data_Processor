from constants import AWS
from services.AWS_Service import AWS_Service
from services.HttpxWrapper import HttpxWrapper
from services.VcfProcessor import VcfProcessor
import asyncio
import sys
import pandas as pd

aws_service = AWS_Service()
httpxWrapper = HttpxWrapper()
parser = pd


async def getS3FileStream(S3_Url):
    try:
        fileStream = await aws_service.getS3FileAsStream(S3_Url)
        return fileStream
    except Exception as e:
        print("Error fetching S3 File:", e)
        sys.exit(1)


async def processVcfFile(stream, start, end, minDP, limit, deNovo):
    try:
        vcfProcessor = VcfProcessor(stream, parser, httpxWrapper)
        return await vcfProcessor.loadFromStream(start, end, minDP, limit, deNovo)
    except Exception as e:
        print("Error processing VCF File:", e)
        sys.exit(1)


async def main():
    S3_Url = AWS.Constants.S3_Url

    try:
        stream = await aws_service.getS3FileAsStream(S3_Url)
        return await processVcfFile(stream, 2059966, 5059966, 5, 5, True)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
