import os

from googleapiclient.discovery import build

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
SPREADSHEET_ID = os.environ["SPREADSHEET_ID"]

service = build('sheets', 'v4', developerKey=GOOGLE_API_KEY)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(
    spreadsheetId=SPREADSHEET_ID,
    range=SAMPLE_RANGE_NAME
).execute()

values = result.get('values', [])

if not values:
    print('No data found.')

print('Name, Major:')
for row in values:
    # Print columns A and E, which correspond to indices 0 and 4.
    print('%s, %s' % (row[0], row[4]))

# =============================================================================

from flask import Flask
app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit():
    return "Hello World!"
