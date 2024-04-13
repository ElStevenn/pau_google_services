import google.oauth2.credentials
import google_auth_oauthlib.flow

# Scopes 
SCOPES = ["https://mail.google.com/"]
CLIENT_SECRETS_FILE = "credentials/gmail/client_secret.json"

flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    'credentials/gmail/client_secret.json',
    scopes=SCOPES)

flow.redirect_uri = 'https://127.0.0.1/oauth2callback'

authorization_url, state = flow.authorization_url(
    access_type='offline',
    include_granted_scopes='true',
    state=sample_passthrough_value,
    prompt='consent')

def main():


if __name__ == "__main__":
  main()

