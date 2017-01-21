from model.formfiller import Project
import random

def test_del_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    username="administrator"
    password="root"
    if len(app.soap.get_project_list(username, password)) == 0:
        app.project.new_project(Project(name="test", description="test"))
    old_projects=app.soap.get_project_list(username, password)
    project = random.choice(old_projects)
    app.project.del_project(project.id)
    new_projects=app.soap.get_project_list(username, password)
    old_projects.remove(project)
    assert old_projects == new_projects