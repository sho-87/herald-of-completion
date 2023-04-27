# Herald of Completion

[![Version](https://img.shields.io/github/v/release/sho-87/herald-of-completion?include_prereleases&sort=semver)](https://pypi.org/project/herald-of-completion/)
[![pypi](https://img.shields.io/pypi/pyversions/herald-of-completion)](https://pypi.org/project/herald-of-completion/)
![CI](https://img.shields.io/github/actions/workflow/status/sho-87/herald-of-completion/lint_test.yml?branch=develop)
[![Issues](https://img.shields.io/github/issues/sho-87/herald-of-completion)](https://github.com/sho-87/herald-of-completion/issues)
[![Donate](https://img.shields.io/badge/Buy%20me%20a%20coffee-donate-blue "Donate")](https://www.buymeacoffee.com/simonho)

Hark! The herald of completion has arrived ... to let you know when your long-running tasks are done.

Decorate your functions with messengers, who will send a notification to you when your function has finished running.

The notification can contain a message and, optionally, the traceback if your function failed.

## Installation

```bash
pip install herald-of-completion
```

## Usage

Wrap the `@herald` decorator around the function you want to be notified about:

```python
from herald.decorators import Herald
from herald.messengers import DiscordMessenger

herald = Herald(".env")  # Specify location of your .env settings file
                         # herald is the name of your decorator

discord = DiscordMessenger()  # create a new messenger

@herald(discord)  # wrap decorator around the function, with the messenger you want to use
def my_function():
    a = [1, 2, 3]
    return a
```

You can send multiple messengers at the same time:

```python
from herald.decorators import Herald
from herald.messengers import DiscordMessenger, EmailMessenger

herald = Herald(".env")

discord = DiscordMessenger()
email = EmailMessenger("recipient@email.com")  # some messengers take arguments

@herald([discord, email])  # multiple messengers can be used at the same time
def my_function():
    a = [1, 2, 3]
    return a
```

Passing `send_result=True` to the decorator will send the return value of your function through the messenger. This also includes notifying you of any exceptions that were raised:

```python
from herald.decorators import Herald
from herald.messengers import DiscordMessenger

herald = Herald(".env")

discord = DiscordMessenger()

@herald(discord, send_result=True)
def my_function():
    a = [1, 2, 3]
    return a[100]  # if an exception is raised, `send_result=True` will also send the traceback
```

For more details, the full API documentation can be found here: [Documentation](https://sho-87.github.io/herald-of-completion/)

### .env settings

Some messengers require credentials and/or additional settings to work. These values are stored in a `.env` file.

Pass the location of this file to the `Herald` constructor, which will pass the values down to your messengers.

The `.env` file should look something like this. You only need settings for the messengers you want to use:

```text
# Discord settings
WEBHOOK_URL="https://discord.com/..."

# Email settings
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=587
SMTP_STARTTLS=True
SMTP_USER="user@gmail.com"
SMTP_PASSWORD="password"
```

Given the contents of this file, make sure you don't check it in to version control!

#### Explanation

| Name            | Value Type | Messenger | Description                                                                                                                     |
| --------------- | ---------- | --------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `WEBHOOK_URL`   | str        | Discord   | The webhook URL for your server. Instructions [here](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) |
| `SMTP_SERVER`   | str        | Email     | STMP server of the email address you want to send _from_                                                                        |
| `SMTP_PORT`     | int        | Email     | STMP port of the email address you want to send _from_                                                                          |
| `SMTP_STARTTLS` | bool       | Email     | Whether your server uses STARTTLS for authentication                                                                            |
| `SMTP_USER`     | str        | Email     | Your email username                                                                                                             |
| `SMTP_PASSWORD` | str        | Email     | Your email password                                                                                                             |

## Contribution

### Creating a new messenger

Creating a new messenger is straightforward and requires only 1 file:

1. Create a new module in `src/herald/messengers/`
2. Your class name should take the form `<Name>Messenger` and inherit the base `Messenger` abstract class. Example: `class DiscordMessenger(Messenger): ...`
3. Your class must implement the abstract methods defined in the base `Messenger` class [here](https://github.com/sho-87/herald-of-completion/blob/develop/src/herald/types.py)
4. Those methods define how your messenger sets it's secret values, and how it uses those settings to send a notification
5. Finally, import your messenger in the `__init__.py` file [here](https://github.com/sho-87/herald-of-completion/blob/develop/src/herald/messengers/__init__.py). This shortens the import path for users.

**Note**: Pull requests should be made to the `develop` branch.

### Tests

Unit and integration tests are located [here](https://github.com/sho-87/herald-of-completion/tree/develop/tests).

Tests should be run using `pytest`.

### Code style

The project is formatted using the `black` formatter.

Docstrings should follow the [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings). This will help with automatic generation of documentation.
