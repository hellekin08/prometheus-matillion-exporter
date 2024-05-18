
import requests

class MatillionClient:
    """
    Representation of Prometheus metrics and loop to fetch and transform
    application metrics into Prometheus metrics.
    """

    def __init__(self):
        self.matillion_instance_url = ""
        self.group_name = ""
        pass

    def get_all_projects(self):
        resp = requests.get(url=f"http:/{self.matillion_instance_url}/rest/v1/group/name/{self.group_name}/project")
        status_data = resp.json()

