import sys
import matplotlib
from cognite.client import CogniteClient
from cog_config import COGNITE_API_KEY, COGNITE_CLIENT_NAME, COGNITE_PROJECT

def setup():
    client = CogniteClient(api_key=COGNITE_API_KEY, project=COGNITE_PROJECT, client_name=COGNITE_CLIENT_NAME)

    return client

def time_series_find_all(client):
    time_series_list = client.time_series.list(include_metadata=False)
    for time_series in time_series_list:
        print(time_series)

    specific_time_series = client.time_series.retrieve(id=6496701131728076)
    specific_time_series.plot(start="365d-ago", end="now", aggregates=["average"], granularity="1d")

if __name__ == "__main__":
    client = setup()
    time_series_find_all(client)