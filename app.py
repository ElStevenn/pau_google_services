from flask import Flask, render_template, request, redirect, url_for, session, flash
# from .services import gmail_acess
import google.oauth2.credentials
import google_auth_oauthlib.flow
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
SCOPES = ["https://mail.google.com/"]
CLIENT_SECRETS_FILE = "credentials/gmail/client_secret.json"


@app.route('/')
def index():
    return render_template('gmail_access.html')

@app.route('/authorize')
def authorize():
    # Create a flow instance to manage the OAuth 2.0 Authorization Grant Flow steps.
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES)

    # The URI created here must exactly match one of the authorized redirect URIs for the OAuth 2.0 client, which you configured in the API Console.
    flow.redirect_uri = url_for('oauth2callback', _external=True)

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true',
        prompt='consent')

    # Store the state so the callback can verify the auth server response.
    session['state'] = state

    return redirect(authorization_url)

@app.route('/oauth2callback')
def oauth2callback():
    state = session['state']

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
    flow.redirect_uri = url_for('oauth2callback', _external=True)

    # Use the authorization server's response to fetch the OAuth 2.0 tokens.
    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials
    session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

    flash("Thank you! Everything was ok!")
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
