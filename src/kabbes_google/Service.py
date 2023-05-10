from parent_class import ParentClass
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class Service( ParentClass ):

    def __init__( self ):

        ParentClass.__init__( self )
        creds = None
        if self.cfg['token.Path'].exists() and not self.cfg['regenerate_token']:
            creds = Credentials.from_authorized_user_file( self.cfg['token.Path'].path, self.cfg['SCOPES'])

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:

            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file( self.cfg['client_secrets.Path'].path, self.cfg['SCOPES'])
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            self.cfg['token.Path'].write( string = creds.to_json() )

        self.service = build( self.cfg['service_name'], self.cfg['version'], credentials=creds)
        