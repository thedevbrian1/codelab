from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googlefileID import getsheetid


def getsheetdata(SPREADSHEET_ID, RANGE_NAME):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('sheetstoken.pickle'):
        with open('sheetstoken.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'content/googleapi/credentialsheets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('sheetstoken.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')

    else:
        rows = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        data = rows.get('values')
        
        return data


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Enter the URL and range of a sample spreadsheet and get data
'''SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1OI3mqi4OhZ6MQlmuNwAbQesXhIkctfc-IhRilYOtTQE/edit?usp=sharing"
RANGE_NAME = 'Pathways!A1:F101'

SPREADSHEET_ID = getsheetid(SPREADSHEET_URL)
data = getsheetdata(SPREADSHEET_ID, RANGE_NAME)

print(data)'''