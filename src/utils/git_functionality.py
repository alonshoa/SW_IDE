import os


def push_to_git(folder):
    os.system("git add " + folder)
    os.system("git commit -m 'add " + folder + "'")
    os.system("git push origin master")


def pull_from_git(folder):
    os.system("git pull origin master")


def init_git(folder):
    os.system("git init")
    os.system("git remote add origin https://github.com/alonshoa/" + folder + ".git")


def open_gitgub_descktop(folder):
    os.system(f"C:\\Users\\arlla\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe {folder}")
