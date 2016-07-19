__author__ = 'evilkhaoskat'

import unittest
import GitHelper


class GitHelperTests(unittest.TestCase):
    def test_contains_rep_info(self):
        self.assertTrue(GitHelper.contains_rep_info("   - [Algorithms](https://github.com/tayllan/awesome-algorithms)"))
        self.assertTrue(GitHelper.contains_rep_info("	- [Analytics](https://github.com/onurakpolat/awesome-analytics)"))
        self.assertFalse(GitHelper.contains_rep_info("some test useless string"))
        self.assertFalse(GitHelper.contains_rep_info(""))

    def test_get_reps_list(self):
        test_lines = ["	- Python",
                      "		- [by @kirang89](https://github.com/kirang89/pycrumbs)",
                      "		- [by @svaksha](https://github.com/svaksha/pythonidae)"]

        reps = GitHelper.get_reps_list(test_lines)

        self.assertEquals(2, len(reps))

if __name__ == '__main__':
    unittest.main()
