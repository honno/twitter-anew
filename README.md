# Twitter Anew

If you follow so many people on twitter that your feed becomes an endless 24/7 deluge of depressing hot takes about why everything sucks, then *Twitter Anew* may just be for you.

Useful tools for your fresh start include:
* Creating a Twitter list that stores everyone you're following
* Generating a backup file that stores all users you currently follow
* Unfollowing everyone!
* God forbid you want to follow them all again, you can do that too

## Table of Contents

* [Installation](#installation)
* [Setup](#setup)
* [Usage](#usage)
* [TODO](#todo)
* [License](#todo)

## Installation

*Twitter Anew* is made in Python3, so [you'll need that first](https://www.python.org/downloads/).

The following Python packages are required: `docopt`, `tweepy` & `requests_oauthlib`. You can use pip to install them all.
```bash
pip install docopt tweepy requests_oauthlib
```

We can't forget to download this repository.
```bash
git clone https://github.com/Honno/twitter-anew.git
```

Enter the new directory created by the clone.
```bash
cd twitter-anew
```

And install the program like so.
```bash
python setup.py install --user
```

Now you can't quite run the `tanew` program yet—**you'll need to register a Twitter application first!**

## Setup

So Twitter requires all API requests, such as those used in *Twitter Anew*, to be handled by a "registered application". For security reasons and such I haven't distributed my own application's keys, but fortunately it's a really simple process.

Being signed in on twitter, go to [apps.twitter.com](https://apps.twitter.com/) and press the 'Create New App' button. Fill out the necessary details in the [form](/doc/scr/create_an_app.png) presented and proceed.
![who](/doc/scr/create_new_app.png)

Presented with the following window, first go to the 'Permissions' tab.
![reads](/doc/scr/app_details.png)

Change the permissions from 'Read only' to 'Read and Write'.
![these](/doc/scr/app_permissions.png)

Now go to 'Key and Acces tokens' tab and take note of the subsequent strings after the 'Consumer Key' and 'Consumer Secret' rows.
![things](/doc/scr/app_tokens.png)

This is the information you'll need to provide to the *Twitter Anew* client before it can be used. We're using a `json` file to store this (learn about how it works [here](https://www.w3schools.com/js/js_json_syntax.asp)). Create a file called `app.json` in the directory you installed this program (i.e. the same folder this README.md is in), and attribute the two strings mentioned above `key` and `secret` respectively. For the above example, `app.json` would read as follows:
```json
{
  "key": "ZyNhLthaYl7giOSEvr3k4tXZc",
  "secret": "J06jGiee9fYPQdeau9hlNXcnSypKJAs3us9R4f1EMuhtWQeqaE"
}
```
You would just replace the weird looking strings with the ones from your own application.

And now you're ready to run the `tanew` client! Test the application is linked properly with the `tanew status` command.

## Usage

```
Usage:
  tanew status
  tanew linkaccount
  tanew createlist [<file>] [-v] [--list-name=<name>] [--list-mode=<mode>]
  tanew addtolist <slug> [-v] [<file>]
  tanew backup [-v] [<file>] [--user-id=<id>]
  tanew unfollowall [-v]
  tanew followall <file> [-v]
  tanew -h | --help  
  tanew --version
```

### status
Check what account is linked to the application, if any.

### linkaccount
Generates an authorization request link for you to open. Upon accepting the request, twitter.com gives you a link which you can enter in the command line interface to register your account with the `tanew` application.

### createlist
Create a twitter list of all users followed by your linked account, or the users listed in the optional `file` parameter. The `--list-name` parameter dictates the list's name (default "Old"), and the `--list-mode` parameter determines whether the list generate is private or public (default private).

### addtolist
Add to an existing list (identified by the required `slug` parameter) all users followed by your linked account, or the users listed in the optional `file` parameter.

The slug is the shorthand name for the list that shows up in your browser, typically the full-name of the list (i.e. if my list "Old" has the url `twitter.com/lists/old`, then the slug is `old`).

### backup
Store all users followed by your linked account or the user specified in `--user-id` parameter to a backup file. By default this is `backup.txt`, but a different file to store the list can be specified in the `file` parameter.

### unfollowall
Unfollow every user your linked account follows.

### followall
Follow every user specified in the required `file` parameter.

### What is \[-v\]?
The optional `v` parameter stands for 'verbose'. When this option is used, detailed information on the current operations being executed by the application are displayed on the terminal.

## TODO

* Code review is probably necessary 'coz I imagine it's all a bit messy
* Document code that do weird specific things
* Have `addtolist` generate new lists if the `List_MAX` is exceeded
* Have a more detailed `setup.py`
* Use proper versioning
* Better handling of Twitter's silent throttling? Need to think how'd that work

The above would all be nice, but I'm probably done with this unless folk would ever want to use this heh. The utility was definitely important for my own personal use, but really this whole project was a learning experience.

## License

*Twitter Anew* is licensed under [MIT](/doc/MIT-LICENSE.txt) :)
