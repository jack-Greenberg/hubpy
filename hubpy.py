#!/usr/bin/env python3

import click
from github import Github
import os, sys

home = os.path.expanduser("~")

@click.group()
def hubpy():
    """Set up Github repositories from the commandline."""

@hubpy.command('init')
@click.option('-u', '--username', help="Github username")
def init(username):
    if not username:
        username = click.prompt("Github username")
    f = open(home + "/.hubpyuser", "w+")
    f.write(username)
    f.close()
    click.secho("Initialized Github user %s" % username, fg='green')
    click.echo("Now, when your current directory has a local git repository, run `hubpy` to create a repository on Github (you\'ll be prompted for your password).")

@hubpy.command('create')
def create():
    f = open(home + '/.hubpyuser', 'r')
    username = f.read()
    print(username)
    print(os.getcwd())
    if not os.path.exists(os.getcwd() + '/.git'):
        click.secho("There is no local git repository here!", fg='red')
        sys.exit()
    else:
        reponame = click.prompt("Repository Name")
        password = click.prompt("Github password for %s" % username, hide_input=True)
        gh = Github(username, password)
        user = gh.get_user()
        try:
            remote_repo = user.create_repo(reponame)
        except e:
            print(e)
            sys.exit()
        remote_url = 'https://github.com/' + user.login + '/' + projectname + '.git'
        try:
            os.system('git remote add origin %s' % remote_url)
        except OSError as e:
            print(e)



if __name__ == '__main__':
    hubpy()
