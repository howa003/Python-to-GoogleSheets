# Python-to-GoogleSheets

## Initial setup

### Google setup

1) Create a GoogleCloud project (see, e.g.,: [YouTube1](https://www.youtube.com/watch?v=Mz9JG9CUXXY)).
2) Enable Google Sheets API (see, e.g.,: [YouTube1](https://www.youtube.com/watch?v=Mz9JG9CUXXY)).
3) Enable API (see, e.g.,: [YouTube2](https://www.youtube.com/watch?v=X-L1NKoEi10)).
4) Create OAuth credentials and use the Desktop App type (see, e.g.,: [YouTube2](https://www.youtube.com/watch?v=X-L1NKoEi10)).
5) Download the JSON (see e.g.,: [YouTube2](https://www.youtube.com/watch?v=X-L1NKoEi10)).

### Python 
1) Create a venv and activate it.
2) Install the required modules:
```bash
pip install google-api-python-client google-auth google-auth-httplib2 google-auth-oauthlib
```

### Getting your tokens
1) Place the downloaded JSON file in this directory and rename it to `client_secret.json`.
2) Run the `get_refresh_token.py`. This opens your browser. Log into your account and accept everything.
3) Copy your Access token and Refresh token from the console.
4) Create a `access_tokens.json` file and input your tokens:
```json
{
  "access_token": "...",
  "refresh_token": "..."
}
```

## Usage
1) Follow the initial setup steps.
2Change the `SPREADSHEET_ID` and `RANGE_NAME` variables in the `main.py` file to your spreadsheet ID and desired range.
