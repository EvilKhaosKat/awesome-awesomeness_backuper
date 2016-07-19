from GithubRep import GithubRep
import unittest


class GithubRepTests(unittest.TestCase):
    def test_constructor_usual(self):
        init_line = "	- [Algorithms](https://github.com/tayllan/awesome-algorithms)"

        github_rep = GithubRep(init_line)

        self.assertEquals("https://github.com/tayllan/awesome-algorithms", github_rep.rep_link)
        self.assertEquals("", github_rep.rep_dir_name)

    def test_constructor_authored(self):
        init_line = "		- [by @vinta](https://github.com/vinta/awesome-python)"

        github_rep = GithubRep(init_line)

        self.assertEquals("https://github.com/vinta/awesome-python", github_rep.rep_link)
        self.assertEquals("awesome-python_vinta", github_rep.rep_dir_name)

    def test_constructure_input_incorrect(self):
        with self.assertRaises(ValueError):
            GithubRep("pew pew")