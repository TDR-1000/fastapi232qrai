import asyncio

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


async def fake_video_streamer():
    for letter in "some fake video bytes some fake video bytes":
        yield letter
        await asyncio.sleep(0.1)


@app.get("/")
async def main():
    return StreamingResponse(fake_video_streamer(), media_type="application/json", status_code=200)


