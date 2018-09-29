# Bunku the bot

This bot allows users to keep track of their attendance and remain updated with schedule of their classes.
To use
Bunku the bot, you can simply call it with `@Bunku` followed by a command,
like so:
```
@Bunku <command>
```

## Setup
- Clone the python-zulip-api repository `git clone https://github.com/zulip/python-zulip-api.git`
- Navigate into your cloned repository `cd python-zulip-api`
- Install `pip install virtualenv`
- Install all requirements in a Python virtualenv `python3 ./tools/provision`
- Activate python3 virtual environment
- Install `pip install zulip_bots`
- Install `pip install graphqlclients`
- Clone Bunku-the-Bot repository `https://github.com/ac-alpha/Bunku-the-Bot.git`
- Navigate into bot repository
- Run the bot using command `zulip-terminal bunku`
- Add the bot to zulip workspace and download the zuliprc file for your bot.
- Move the `zuliprc` file to the `bunku` repository
- Start the bot using command `zulip-run-bot bunku --config zuliprc`
- You are good to interact with the bot

## Usage

This bot has following six commands.

1. `startrecording` : to start recording your leaves 
2. `left <course-code> class`: to record a leave for particular course code
3. `<course-code> class cancelled` : to report about a course class cancelled
4. `extra class <course-code> <date> <time>` : to report about an extra class
5. `attendancerecord` : to show your attendance record
6. `totalworkingdays` : to show total working days and 75% of it
7. `myextraclasses` : to show details of latest added extra classes

### Usage examples

| Message | Response |
| ------- | ------ |
| `@Bunku startrecording` | aagarwal@cs.iitr.ac.in Started recording your attendance |
| `@Bunku attendancerecord` |aagarwal@cs.iitr.ac.in<br>---Stats---<br>csn221 : 42/42 100.0%<br>hss01 : 31/31 100.0%<br>ecn203 : 41/41 100.0%<br>csn291 : 51/51 100.0%<br>min106 : 61/61 100.0%<br>csn261 : 30/30 100.0%<br>----------- |



