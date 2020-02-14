from cognite.client import CogniteClient

# Insert your API key here. Do NOT publicize this.
COGNITE_API_KEY = ""
# Insert your desired client name here, usually your username or real name.
COGNITE_CLIENT_NAME = ""
# Set the desired project here. Default is "publicdata".
COGNITE_PROJECT = "publicdata"

def client_instantiate():
    """ This method instantiates a Cognite client and returns the client object.\n
        It checks the login status before returning the client object.\n
        Before running, the API key, client name and project name must be defined.\n
        They are defined in COGNITE_API_KEY, COGNITE_CLIENT_NAME and COGNITE_PROJECT respectively, in the src/api_key.py file."""
    # Instantiate the client.
    client = CogniteClient(api_key=COGNITE_API_KEY, project=COGNITE_PROJECT, client_name=COGNITE_CLIENT_NAME)

    # Assert if the login was successful.
    if (client.login.status().logged_in == True):
        print("Logged in successfully!")
        return client
    else:
        print("Client login failed!")
        return 0