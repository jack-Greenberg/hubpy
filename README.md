# hubpy

A command line tool to create Github repositories

## Install

### Requirements
* Python 3
* Click
```bash
pip install click
```
* PyGithub
```bash
pip install PyGithub
```

### hubpy
Download the hubpy file and make it executable:
```bash
chmod +x /path/to/hubpy
```

Add the path to your `~/.bash_profile`:
```
...
PATH=$PATH":path/to/directory_with_hubpy"
export PATH
```

Update your bash profile:
```bash
source ~/.bash_profile
```

## Usage

To store your Github username for future ease, run
```bash
hubpy init
```
and enter your username. This will store it in a file in your home directory called `.hubpyusername`

Then, while in any directory with a git repo (you've run `git init`), run
```bash
hubpy create
```
This will prompt you for a repository name and your Github password (only used for the PyGithub module)

If you didn't run `hubpy init`, it will also ask for a username.

## License
This is under the MIT license. If you have questions or critiques, let me know (email me or open an issue).


Made with :heart: by [Jack Greenberg](https://jacklgreenberg.com)
