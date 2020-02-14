import sys
from cognite.client import CogniteClient
from cog_config import COGNITE_API_KEY, COGNITE_CLIENT_NAME, COGNITE_PROJECT

def setup():
    client = CogniteClient(api_key=COGNITE_API_KEY, project=COGNITE_PROJECT, client_name=COGNITE_CLIENT_NAME)