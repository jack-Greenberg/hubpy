#!/usr/bin/env python3

import click
from github import Github
import os, sys

home = os.path.expanduser("~")

# Set up click group
@click.group()
def hubpy():
    """Set up Github repositories from the commandline."""

# Set up init command to set the username
@hubpy.command('init', short_help="Set a Github username")
@click.option('-u', '--username', help="Github username")
def init(username):
    """Set a Github username for future use"""
    if not username:
        username = click.prompt("Github username")
    # Create the file .hubpyuser in the home directory for future use
    f = open(home + "/.hubpyuser", "w+")
    f.write(username)
    f.close()

    click.secho("Initialized Github user %s" % username, fg='green')
    click.echo("Now, when your current directory has a local git repository, run `hubpy create` to create a repository on Github (you\'ll be prompted for your password).")

# `hubpy create` command
@hubpy.command('create', short_help="Create the Github repo")
@click.option('-n', '--repository_name', help="Name for repository")
@click.option('-u', '--username', help="Github username")
def create(repository_name, username, password):
    """Create a Github repository for the current project"""
    # If there is no git repository, throw an error
    if not os.path.exists(os.getcwd() + '/.git'):
        click.secho("There is no local git repository here!", fg='red')
        sys.exit()
    # If no repository name is provided in the command
    if not repository_name:
        reponame = click.prompt("Repository name")

    # If no username is provided in the command
    if not username:
        # If there is a .hubpyuser file, use that
        if (os.path.exists(home + '/.hubpyuser')):
            f = open(home + '/.hubpyuser', 'r')
            username = f.read()
        # Or else just prompt the user
        else:
            username = click.prompt("Github username")
            click.echo("To set the ")
    password = click.prompt("Github password for %s" % username, hide_input=True)
    gh = Github(username, password)
    user = gh.get_user()
    remote_repo = user.create_repo(reponame)
    remote_url = 'https://github.com/' + user.login + '/' + reponame + '.git'
    try:
        os.system('git remote add origin %s' % remote_url)
    except OSError as e:
        print(e)

if __name__ == '__main__':
    hubpy()
