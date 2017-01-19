from model.formfiller import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app



    def new_project(self, project):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("searchstring")) > 0:
            self.app.open_home_page()
        self.open_project_manage(wd)
        # add new project
        wd.find_element_by_xpath("//table[3]/tbody/tr[1]/td/form/input[2]").click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input.button").click()
        self.project_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def open_project_manage(self, wd):
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()


    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.project_cache = []
            self.open_project_manage(wd)
            table = wd.find_elements_by_tag_name("table")[2]
            for row in table.find_elements_by_css_selector('tr.row-1, tr.row-2'):
                cells = row.find_elements_by_tag_name("td")
                name = cells[0].text
                description = cells[1].text
                href = row.find_element_by_css_selector("a").get_attribute("href")
                id = href[href.rfind('=') + 1:]
                self.project_cache.append(Project(name=name, description=description,
                                                  id=id))
        return list(self.project_cache)



    def del_project(self, id):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("searchstring")) > 0:
            self.app.open_home_page()
        self.open_project_manage(wd)
        # open deletion
        wd.find_element_by_css_selector("a[href='manage_proj_edit_page.php?project_id=%s']" % id).click()
        # submit deletion
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input.button").click()
        self.app.open_home_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_css_selector("a"))