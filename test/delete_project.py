from model.formfiller import Project
import random

def test_del_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    old_projects=app.project.get_project_list()
    if len(old_projects) == 0:
        app.project.new_project()
        old_projects=app.project.get_project_list()
    Project = random.choice(old_projects)
    app.project.del_project(Project.id)
    new_projects=app.project.get_project_list()
    old_projects.append(Project)
    assert old_projects == new_projects