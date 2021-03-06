from suds.client import Client
from suds import WebFault
from model.formfiller import Project
from model.formfiller import SoapProject


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False



    def get_project_list(self, username, password):

            client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
            projects = client.service.mc_projects_get_user_accessible(username, password)
            items = []
            for project in projects:
                name=project.name
                description=project.description
                id=project.id
                items.append(Project(name=name, description=description,id=id))


            return items