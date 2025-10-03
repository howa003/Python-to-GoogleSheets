"""
This script helps you obtain a refresh token for Google Sheets API access.
This script is ran only once to get the refresh token.
Run this script, follow the link it provides, log in to your Google account,
and authorize the application. It will print out the access and refresh tokens.
Make sure to save the refresh token securely (to access-tokens.json), as it allows long-term access.
"""

from google_auth_oauthlib.flow import InstalledAppFlow

def main():
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]

    # Use the JSON you downloaded from Google Cloud
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes)

    creds = flow.run_local_server(port=0)  # will open browser for login

    print("Access token:", creds.token)
    print("Refresh token:", creds.refresh_token)

if __name__ == "__main__":
    main()
