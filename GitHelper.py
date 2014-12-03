from GithubRep import GithubRep

__author__ = 'evilkhaoskat'

import os


def clone_rep(repository, dir_to=""):
    """
    clones repository and writes into stdout result of command execution using torsocks
    :param repository: link to github repository
    :param dir_to: another directory can be mentioned for cloning of repository

    :type repository: string
    :type dir_to: string
    """
    clone_command = "torsocks git clone {0} {1}".format(repository, dir_to)
    print("clone_command:" + clone_command + "|")
    os.system(clone_command)


def contains_rep_info(line):
    """
    Checks does that line contains link to the github repo (pretty simple 'algorithm' at the moment)
    :param line: string from aa readme file
    :return: true if it has link to the github repository

    :type line:string
    :rtype: boolean
    """
    return True if line.find("https://github.com/") != -1 else False  # looks awful


def get_reps_list(aa_readme_file):
    """
    Parses file and tries to find links to repositories in there

    :param aa_readme_file: iterable file to be checked
    :return: list of repositories

    :type aa_readme_file: Iterable
    :rtype: list of GithubRep
    """
    reps_list = []

    for line in aa_readme_file:
        if contains_rep_info(line):
            reps_list.append(GithubRep(line))

    return reps_list



