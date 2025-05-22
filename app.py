from fastapi import FastAPI
from bilimdonai import BilimdonAI

app = FastAPI(
    title="Bilimdon AI",
    docs_url='/',
    redoc_url="/",
    version="1.0.0",
    description="[men](https://t.me/jackson_rodger) tomonimdan yasaldi",
    summary="O'zbekiston maktabidagi fanlarga asoslangan yordamchi Suniy Intellekt. Bu AI o'zbekiston maktablaridagi deyarli barcha fanlarni biladi va shu fanlarga oid mavzular bo'yicha javob beradi",
)

@app.get("/api/v1/start", tags=["Bilimdon AI"], name="Bilimdon AI")
async def start(message: str):
    return {"message": BilimdonAI(message)}
