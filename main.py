import calendar
from datetime import datetime

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI(
    title="Deposit",
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, error: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"error": str(error)}),
    )


def add_months(source_date: datetime, months: int) -> datetime:
    month = source_date.month - 1 + months
    year = int(source_date.year + month / 12)
    month = month % 12 + 1
    day = min(source_date.day, calendar.monthrange(year, month)[1])
    return datetime(year, month, day)


class Deposit(BaseModel):
    date: str = Field(default='31.01.2021')
    period: int = Field(ge=1, le=60, default=3)
    amount: int = Field(ge=10000, le=3000000, default=20000)
    rate: int = Field(ge=1, le=8, default=6)


def calc_deposit_(deposit: Deposit):
    date = datetime.strptime(deposit.date, '%d.%m.%Y')
    
    amount = deposit.amount
    rate = deposit.rate / 12 / 100
    res = {}
    for i in range(deposit.period):
        current_date = add_months(date, i)
        if amount > 0:
            res[current_date.strftime('%d.%m.%Y')] = round(amount * (1 + rate), 2)
            amount *= (1 + rate)
    print('calc_deposit_', res)  
    return res



@app.get('/calc_deposit')
def get_deposit(deposit: Deposit):
    try:
        res = calc_deposit_(deposit)
        print('res', res)
        return {"status": 200, "data": res}
    except ValueError:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": "Incorrect date format. Use DD.MM.YYYY."}
        )