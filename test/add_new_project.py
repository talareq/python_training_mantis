from model.formfiller import Project

def test_add_new_project(app, json_project):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    username="administrator"
    password="root"
    project=json_project
    if len(str(project.name)) == 0:
        print("Invalid project name specified. Project names cannot be blank.")

    else:
        old_projects=app.soap.get_project_list(username, password)
        if project in old_projects:
            print("A project with that name already exists. Please go back and enter a different name")
        else:
            app.project.new_project(project)
            new_projects=app.soap.get_project_list(username, password)
            old_projects.append(Project)
            assert old_projects == new_projects
