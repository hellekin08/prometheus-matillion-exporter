
import requests

class MatillionClient:
    """
    Client to connect to matillion api
    """

    def __init__(self, matillion_api_user, matillion_api_password):
        self.matillion_instance_url = ""
        self.group_name = ""
        self.matillion_api_user = matillion_api_user
        self.matillion_api_password = matillion_api_password
        pass

    def get_all_projects(self):
        url = f"http:/{self.matillion_instance_url}/rest/v1/group/name/{self.group_name}/project"
        response = requests.get(url, auth=HTTPBasicAuth( self.matillion_api_user ,  self.matillion_api_password ))

        if response.status_code == 200:
            project_data = resp.json()
        else:
            print("Failed to fetch projects. Status code:", response.status_code)


    def get_tasks_per_project(self, project_name):
        url=f"http:/{self.matillion_instance_url}/rest/v1/group/name/{self.group_name}/project/name/{project_name}/task/<endpoint>"
        response = requests.get(url, auth=HTTPBasicAuth( self.matillion_api_user , self.matillion_api_password))

        if response.status_code == 200:
            task_data = resp.json()
        else:
            print(f"Failed to fetch tasks for project: {project_name}.")


        
