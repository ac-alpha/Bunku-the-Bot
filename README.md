# Bunku the bot

This bot allows users to keep track of their attendance and remain updated with schedule of their classes.
To use
Bunku the bot, you can simply call it with `@Bunku` followed by a command,
like so:
```
@Bunku <command>
```

## Usage

This bot has following six commands.

1. `startrecording` : to start recording your leaves 
2. `left <course-code> class`: to record a leave for particular course code
3. `<course-code> class cancelled` : to report about a course class cancelled
4. `extra class <course-code>` : to report about an extra class
5. `attendancerecord` : to show your attendance record
6. `totalworkingdays` : to show total working days and 75% of it

## Setup
- clone the python-zulip-api repository `git clone https://github.com/zulip/python-zulip-api.git`
- navigate into your cloned repository `cd python-zulip-api`
- install `pip install virtualenv`
- install all requirements in a Python virtualenv `python3 ./tools/provision`
- Activate python3 virtual environment
- install `pip install zulip_bots`
- install `pip install graphqlclients`
- clone bunku the bot repository `https://github.com/ac-alpha/Bunku-the-Bot.git`
- Navigate into bot repository
- Run the bot using command `Zulip-terminal bunku`

### Usage examples

| Message | Response |
| ------- | ------ |
| `@Bunku startrecording` | aagarwal@cs.iitr.ac.in Started recording your attendance |
| `@Bunku attendancerecord` |aagarwal@cs.iitr.ac.in<br>---Stats---<br>csn221 : 42/42 100.0%<br>hss01 : 31/31 100.0%<br>ecn203 : 41/41 100.0%<br>csn291 : 51/51 100.0%<br>min106 : 61/61 100.0%<br>csn261 : 30/30 100.0%<br>----------- |



