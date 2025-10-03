"""
Append data to Google Sheets using Google Sheets API v4.
Make sure to set up OAuth 2.0 credentials and obtain a refresh token first (see the get_refresh_token.py script).
"""

### LOAD LIBRARIES AND MODULES  ###

import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

def append_data_to_sheet(spreadsheet_id, target_range, values):
    """
    Append data to a Google Sheet.

    Args:
        spreadsheet_id (str): The ID of the spreadsheet (e.g., "12h3mqZAsV93e5Gva5E1hMoFtKIO17Fc0sn-GqiWjVMk").
        target_range (str): The A1 notation of the range to append the data to (e.g., "Sheet1!A:C").
        values (list of list): The data to append, as a list of rows, where each row is a list of cell values (e.g., [[1, 2, 3], [4, 5, 6]]).
    """

    ### CREDENTIALS SETUP ###

    # Load client secrets
    with open("client_secret.json", "r") as f:
        client_conf = json.load(f)["installed"]

    # Load tokens
    with open("access_tokens.json", "r") as f:
        tokens = json.load(f)

    # Build credentials
    creds = Credentials(
        token=tokens["access_token"],
        refresh_token=tokens["refresh_token"],
        token_uri=client_conf["token_uri"],
        client_id=client_conf["client_id"],
        client_secret=client_conf["client_secret"],
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    ### API SETUP AND USAGE ###

    # Refresh access token if expired
    creds.refresh(Request())

    # Build Sheets API service
    service = build("sheets", "v4", credentials=creds)

    ### Append data to Google Sheets ###

    # Append data to the spreadsheet
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=target_range,  # target columns
        valueInputOption="USER_ENTERED",
        insertDataOption="INSERT_ROWS",
        body={
            "values": values
        }
    ).execute()

    print("Update complete:", result.get("updates", {}).get("updatedRange"))

if __name__ == "__main__":
    # Example usage
    append_data_to_sheet(
        spreadsheet_id="your_spreadsheet_id_here",
        target_range="Sheet1!A:C",
        values=[[1, 2, 3]]
    )