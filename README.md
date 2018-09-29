# Bunku the bot

This bot allows users to keep track of their attendance and remain updated with rescheduling of their classes.
To use
Bunku the bot, you can simply call it with `@Bunku` followed by a command,
like so:
```
@Bunku <command>
```

## Usage

This bot has following five commands.

1. `startrecording` : to start recording your leaves 
2. `left <course-code> class`: to record a leave for particular course code
3. `<course-code> class cancelled` : to report about a course class cancelled
4. `extra class <course-code>` : to report about an extra class
5. `attendancerecord` : to show your attendance record

## Setup
First follow up the following instructions given on [chat.zulip.org](https://chat.zulip.org/api/writing-bots#writing-interactive-bots) :
1. `git clone https://github.com/zulip/python-zulip-api.git` - clone the [python-zulip-api](https://github.com/zulip/python-zulip-api) library.
2. `cd python-zulip-api` - navigate into your cloned repository.
3. `python3 ./tools/provision` - install all requirements in a Python virtualenv.
4. The output of `provision` will end with a command of the form `source .../activate`; run that command to enter the new virtualenv.
5. You should now see the name of your venv preceding your prompt, e.g. `(zulip-api-py3-venv)`.

## Links

### Usage examples

| Message | Response |
| ------- | ------ |
| `@Bunku startrecording` | aagarwal@cs.iitr.ac.in Started recording your attendance |
| `@Bunku attendancerecord` |aagarwal@cs.iitr.ac.in   ---Stats---<br>csn221 : 42/42 100.0%<br>hss01 : 31/31 100.0%<br>ecn203 : 41/41 100.0%<br>csn291 : 51/51 100.0%<br>min106 : 61/61 100.0%<br>csn261 : 30/30 100.0%<br>----------- |

## Notes

