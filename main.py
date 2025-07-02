# code to implement an armstrong number in fastapi[standard library and connect to github
# FastAPI application to check if a number is an Armstrong number
# localhost:8000/armstrong/{number}
# where {number} is the integer you want to check.


from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/armstrong/{number}")
async def check_armstrong(number: int):
    if number < 0:
        raise HTTPException(status_code=400, detail="Number must be non-negative")

    num_str = str(number)
    num_length = len(num_str)
    armstrong_sum = sum(int(digit) ** num_length for digit in num_str)

    if armstrong_sum == number:
        return {"number": number, "is_armstrong": True}
    else:
        return {"number": number, "is_armstrong": False}


# To run the FastAPI application, use the command:
# uvicorn main:app --reload
# Then access the endpoint at http://
# Run in FastAPI dev main.py

connect  to github