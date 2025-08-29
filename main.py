from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class DataModel(BaseModel):
    data: List[str]

def alternating_caps_reverse(s):
    result = []
    upper = True
    for ch in s[::-1]:
        if upper:
            result.append(ch.upper())
        else:
            result.append(ch.lower())
        upper = not upper
    return "".join(result)

@app.get("/")
async def root():
    return {
        "message": "API is running. Use POST /bfhl with JSON body to test."
    }

@app.get("/bfhl")
async def health_check():
    return {
        "is_success": True,
        "message": "Server is up! Send a POST request with JSON data to this endpoint."
    }

@app.post("/bfhl")
async def process_data(request: DataModel):
    data = request.data
    even_numbers, odd_numbers, alphabets, special_chars = [], [], [], []
    total_sum = 0
    concat_alpha = ""

    for item in data:
        if item.isdigit():
            num = int(item)
            if num % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
            total_sum += num
        elif item.isalpha():
            alphabets.append(item.upper())
            concat_alpha += item
        else:
            special_chars.append(item)

    response = {
        "is_success": True,
        "user_id": "parth_khairnar_22072004",
        "email": "pskhairnar1024@gmail.com",
        "roll_number": "22BCE1771",
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_chars,
        "sum": str(total_sum),
        "concat_string": alternating_caps_reverse(concat_alpha)
    }
    return response