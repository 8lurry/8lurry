# how to run a single test:
# $ python -m unittest tests.test_demo.Main.test_whitewall1

from lino.utils.pythontest import TestCase


class Main(TestCase):
    demo_projects_root = "whitewall/projects"

    def test_whitewall1(self):
        self.do_test_demo_project("whitewall1")
