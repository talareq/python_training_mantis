def test_get_project_list(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    try:
        l = app.project.get_project_list()
        for item in l:
            print(item)

    finally:
        pass