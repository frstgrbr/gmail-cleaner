import os
import pickle
import time

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_gmail_service():
    """Get Gmail service."""
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def clean_inbox(service, query):
    """Clean up inbox."""
    messages = service.users().messages().list(userId='me', q=query).execute()
    if 'messages' in messages:
        for message in messages['messages']:
            service.users().messages().trash(userId='me', id=message['id']).execute()
            print(f"Message with id: {message['id']} trashed.")
        return True
    else:
        return False

def main():
    """Main function."""
    # Get Gmail service
    service = get_gmail_service()

    while True:
        # Example: Delete emails from a specific sender
        query = "example@google.com"
        if not clean_inbox(service, query):
            print("No more emails to delete using this query. Exiting")
            break

if __name__ == '__main__':
    main()
