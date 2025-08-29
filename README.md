# BFHL FastAPI REST API

## Created By
- Parth Khairnar – VIT Chennai
- Email: pskhairnar1024@gmail.com

## Frameworks / Tools Used
- FastAPI
- Uvicorn
- Vercel (Hosting)

## Hosted API Endpoint
[https://fastapi-bfhl-six.vercel.app/](https://fastapi-bfhl-six.vercel.app/)

## Run Locally
```bash
git clone https://github.com/ParthKhairnar101/fastapi_bfhl.git
cd fastapi_bfhl
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

## Example Request (POST /bfhl)
```json
{
  "data": ["a", "1", "334", "4", "R", "$"]
}
```

## Example Response
```json
{
  "is_success": true,
  "user_id": "parth_khairnar_22072004",
  "email": "pskhairnar1024@gmail.com",
  "roll_number": "22BCE1771",
  "odd_numbers": ["1"],
  "even_numbers": ["334","4"],
  "alphabets": ["A","R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

## Usage

Send POST request on https://fastapi-bfhl-six.vercel.app/bfhl.
