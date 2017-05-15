# Hello, You

`hello_you.py` is a simple Python script that read logs in real-time; extract
IPs of visitors; asks [ipinfo.io](https://ipinfo.io/) for their location; and
tell you where they’re from.

## Usage

Tail your logs in some way and pass them to the script, e.g.:

    $ ssh -t user@host 'tail -f /var/logs/something.log' | python3 hello_you.py

The original intend was to spell out loud the cities using macOS’ `say`
program. You can get this behavior by passing `--say` to the script.

Example output:

    $ ... | python3 hello_you.py
    Hello from Straoane!
    Hello from Shenyang!
    Hello from Hanoi!
    Hello from Straoane!
    Hello from Les Abymes!
    Hello from Les Abymes!
    Hello from Beijing!
    Hello from Hanoi!
    Hello from Straoane!

Those are bots hitting the port `23` on one of my servers.

## Install

The script’s only dependency, besides Python 3, is `requests`:

    pip install requests

Note that ipinfo.io’s free plan limits you to 1000 requests per day.
