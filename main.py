__author__ = 'evilkhaoskat'

import sys
import os
import GitHelper

# AA means Awesome-Awesomeness
AA_GIT_LINK = "https://github.com/bayandin/awesome-awesomeness.git"
AA_DIR_NAME = "awesome-awesomeness"
AA_MAIN_FILE = "README.md"

def get_dir_to_clone(argv):
    """

    :param argv: list of string
    :return: another dir to if specified

    :type argv: list of string
    :rtype: string
    """
    for arg in argv:
        if arg.startswith("-dir"):
            return arg.split("=")[-1]

    return None

class Main:
    def perform_backup(self, dir_to_clone=""):
        print("dir_to_clone:" + dir_to_clone)
        if dir_to_clone:
            if not os.path.exists(dir_to_clone):
                print("dir_to_clone is not exists. performing dir creation")
                os.makedirs(dir_to_clone)

            os.chdir(dir_to_clone)

        GitHelper.clone_rep(AA_GIT_LINK)
        aa_main_file = open(AA_DIR_NAME + "/" + AA_MAIN_FILE)

        reps = GitHelper.get_reps_list(aa_main_file)

        for rep in reps:
            print("Cloning {0}. Additional directory specified as:{1}".format(rep.rep_link, rep.rep_dir_name))
            GitHelper.clone_rep(rep.rep_link, dir_to=rep.rep_dir_name)

        print("all repos successfully synchronized")

if __name__ == "__main__":
    print("awesome-awesomeness backuper launched")
    print("by specifying -dir= dir for backup can be changed")
    dir_to_clone = get_dir_to_clone(sys.argv)
    Main().perform_backup(dir_to_clone=dir_to_clone)

# TODO parallel cloning
# TODO logging for actions - for instance list of repos