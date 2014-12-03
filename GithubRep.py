__author__ = 'evilkhaoskat'

#import re


class GithubRep:
    init_line = ""
    rep_link = ""
    rep_dir_name = ""

    def __init__(self, init_line):
        """

        :param init_line: line from file with format like '- [Algorithms](https://github.com/tayllan/awesome-algorithms)'

        :type init_line: string
        """
        self.init_line = init_line

        rep_link_start_num = init_line.find("https")
        if rep_link_start_num == -1:
            raise ValueError("input init line for GithubRep doesn't have https link to repository")

        self.rep_link = init_line[rep_link_start_num:-1].rstrip(")")

        author_start_sym = init_line.find("[by @")
        if author_start_sym != -1:
            author_end_num = init_line.find("]")
            author_string = init_line[author_start_sym:author_end_num]
            author_name = author_string.split("@")[-1]

            rep_name = self.rep_link.split("/")[-1]

            self.rep_dir_name = "{0}_{1}".format(rep_name, author_name)

