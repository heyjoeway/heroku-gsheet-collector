SAMPLE_RANGE_NAME = 'Sheet1!A:A'

import os
import json
from googleapiclient.discovery import build
from google.oauth2 import service_account

SPREADSHEET_ID = None
if "SPREADSHEET_ID" in os.environ:
    SPREADSHEET_ID = os.environ["SPREADSHEET_ID"]
else:
    with open("spreadsheet_id.txt") as f:
        SPREADSHEET_ID = f.readline()

credentialsRaw = None
if "GOOGLE_CREDENTIALS" in os.environ:
    credentialsRaw = json.loads(os.environ["GOOGLE_CREDENTIALS"])
else:
    with open("google_credentials.json") as f:
        credentialsRaw = json.load(f)

service = build(
    'sheets', 'v4',
    credentials=service_account.Credentials.from_service_account_info(credentialsRaw)
)

# =============================================================================

from flask import Flask, request
app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit():
    if "coffee" in request.data:
        return "I'm a teapot", 418

    try:
        sheetRequest = service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=SAMPLE_RANGE_NAME,
            valueInputOption="RAW",
            body={
                "values": [ request.data["values"] ]
            }
        )
        sheetRequest.execute()
        return { "status": "success" }, 200
    except:
        return { "status": "error" }, 400
        pass