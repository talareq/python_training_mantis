from model.formfiller import Project

def test_add_new_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    old_projects=app.project.get_project_list()
    app.project.new_project()
    new_projects=app.project.get_project_list()
    old_projects.append(Project)
    assert old_projects == new_projects
