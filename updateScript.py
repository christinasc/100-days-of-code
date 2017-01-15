from __future__ import print_function
from subprocess import call
import httplib2
import os, argparse, re, time

from sys import argv
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


def main():
    linebreak = "----------------------------"
    preamble = "# 100 Days Of Code - Log "
    dateline = "### Day "
    progressline = "**Today's Progress**:"

    call(["ls", "-l"])
    call(["git", "status"])
    call(["git", "checkout", "log.md"])
    print(linebreak)

    now = time.strftime("%c")
    dateline = dateline + ": " + now
    print(dateline)
    print(linebreak)

    ## prompt for entry
    var = input("Please enter Today's Log Entry: ")
    print("You Entered: ",  var)
    confirm = input("CONFIRM: y/n? ")
    if re.match( r"[Yy]", confirm):
        print("COMMITING to GITHUB")
        progressline = progressline + " "+var
    else: 
        print("aborting.....")

    entry = linebreak + "\n"+ preamble + " \n" + dateline + "\n" + progressline + "\n" + linebreak + "\n"
    print(entry)

    line_prepender("log.md", entry)
    call(["head", "log.md"])
    call(["git", "commit", "-m", "log entry on "+now])
    call(["git", "push"]) 

if __name__ == '__main__':
    main()

