from __future__ import print_function
import sys
sys.stdout.reconfigure(encoding="utf-8")
import base64
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText

# If modifying SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def authenticate_gmail():
    """Authenticate and return Gmail API service instance."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def list_messages(service, user_id='me', max_results=5):
    """List messages in the user's mailbox."""
    results = service.users().messages().list(userId=user_id, maxResults=max_results).execute()
    messages = results.get('messages', [])
    if not messages:
        print("No messages found.")
    else:
        print("Messages:")
        for msg in messages:
            msg_detail = service.users().messages().get(userId=user_id, id=msg['id']).execute()
            snippet = msg_detail.get('snippet')
            print(f"ID: {msg['id']} | Snippet: {snippet[:50]}...")

def send_message(service, to, subject, body_text, user_id='me'):
    """Send an email via Gmail API."""
    message = MIMEText(body_text)
    message['to'] = to
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    message = {'raw': raw}
    sent_msg = service.users().messages().send(userId=user_id, body=message).execute()
    print(f"Message sent! ID: {sent_msg['id']}")
    return sent_msg

if __name__ == '__main__':
    service = authenticate_gmail()

    # List the 5 latest messages
    list_messages(service)

    # Send a test email
    # send_message(service, "recipient@example.com", "Hello from Gmail API", "This is a test email sent via Gmail API.")

