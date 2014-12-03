import unittest
from main import get_dir_to_clone


class MainTests(unittest.TestCase):
    def test_get_dir_to_clone(self):
        meaningless_argv = ["-pew=pew", "something anything"]
        self.assertEquals(None, get_dir_to_clone(meaningless_argv))

        norm_argv = ["-test=test", "-dir=/ultra/dir"]
        self.assertEqual("/ultra/dir", get_dir_to_clone(norm_argv))

