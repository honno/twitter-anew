# Twitter Anew

If you follow so many people on twitter that your feed becomes an endless 24/7 deluge of depressing hot takes about why everything sucks, then *Twitter Anew* may just be for you.

Useful tools for your fresh start include:
* Creating a Twitter list that stores everyone you're following
* Generating a backup file that stores all users you currently follow
* Unfollowing everyone!
* And god forbid you want to follow them all again, you can just use that backup file

## Installation

*Twitter Anew* is made in Python3, so [you'll need that first](https://www.python.org/downloads/).

The following Python packages are required: `docopt`, `tweepy` & `requests_oauthlib`. You can use pip to install them all as follows.
```bash
pip install docopt tweepy requests_oauthlib
```

We can't forget to download this repository.
```bash
git clone https://github.com/Honno/twitter-anew.git
```

Enter the new directory created by the clone... 
```bash
cd twitter-anew
```

And install the program like so.
```bash
python setup.py install --user
```

Now just run any command you like with `tanew <command>`, but be aware you **need to register a Twitter application** first!

## Setup

So Twitter requires all API requests, such as those used in this application, be handled by a registered application. For security reasons I haven't distributed my own application's keys and such, but have no fear for it's a really simple process.

Being signed in on twitter, go to [apps.twitter.com](https://apps.twitter.com/) and press the 'Create New App' button. Fill out the necessary details in the [form](/doc/scr/create_an_app.png) presented and proceed.
![who](/doc/scr/create_new_app.png)

Presented with the following window, first go to the 'Permissions' tab.
![reads](/doc/scr/app_details.png)

Change the permissions from 'Read only' to 'Read and Write'.
![these](/doc/scr/app_permissions.png)

Now go to 'Key and Acces tokens' and take note of the subsequent strings after the 'Consumer Key' and 'Consumer Secret' rows.
![things](/doc/scr/app_tokens.png)

This is the information you'll need to provide to the *Twitter Anew* client. Create a file called `app.json` in the directory you installed this program (i.e. the same folder this README.md is in), and attribute the two strings mentioned above `key` and `secret` respectively. For the above example, `app.json` would read as follows:
```json
{
  "key": "das",
  "secret": "sadas"
}
```

And now you're ready to run the `tanew` client! Test the application is linked properly with the `tanew status` command.

## Usage

```
Usage:
  tanew status
    Check what account is linked to application, if any.
  tanew linkaccount
    Link a twitter account to application.
  tanew createlist [<file>] [-v] [--list-name=<name>] [--list-mode=<mode>]
    Create a twitter list of all users specified.
  tanew addtolist <slug> [-v] [<file>]
    Add to an existing list specified members.
  tanew backup [-v] [<file>] [--user-id=<id>]
    Store all users the specified account follows.
  tanew unfollowall [-v]
    Unfollow every user the linked account follows.
  tanew followall <file> [-v]
    Follow every user specified in the file parameter.
  tanew -h | --help  
  tanew --version
```
