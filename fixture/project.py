from model.formfiller import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app



    def new_project(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("searchstring")) > 0:
            self.app.open_home_page()
        self.open_project_manage(wd)
        # add new project
        wd.find_element_by_xpath("//table[3]/tbody/tr[1]/td/form/input[2]").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("swistu")
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys("gwizdu")
        wd.find_element_by_css_selector("input.button").click()
        self.project_cache = None


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
            row = wd.find_element_by_css_selector('tr[@class="row-1"]')
            cells = row.find_elements_by_tag_name("td")
            name = cells[0].text
            description = cells[1].text
            id = wd.find_element_by_css_selector("a href[manage_proj_edit_page.php?project_id='%s']" % id)
            self.project_cache.append(Project(name=name, description=description,
                                                  id=id))
            return list(self.project_cache)
