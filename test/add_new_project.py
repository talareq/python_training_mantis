from model.formfiller import Project

def test_add_new_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    username="administrator"
    password="root"
    old_projects=app.soap.get_project_list(username, password)
    app.project.new_project()
    new_projects=app.soap.get_project_list(username, password)
    old_projects.append(Project)
    assert old_projects == new_projects
