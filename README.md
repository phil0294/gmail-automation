# gmail-automation



A sample project to automate tasks with Gmail API.

I'll start by trying to search for emails in my inbox and print them in PDF.



# Initial setup steps:

1. Install python on your computer. Version 3.6 or higher is required.


2. Install google-auth-httplib2:
`pip install google-auth-httplib2`


3. Install python package for connection to Google OAuth 2.0:
`pip install google-auth-oauthlib`

4. Go to the [Google Cloud Console](https://console.cloud.google.com/)
4.1. Create a project → Enable Gmail API.
4.2. Configure OAuth consent screen and download OAuth 2.0 Client ID credentials as `credentials.json`.

