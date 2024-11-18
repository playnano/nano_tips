import shared
from shared import from_raw

COMMENT_FOOTER = """

***

[*^(Nano Tips)*](https://github.com/playnano/nano_tips)*^( | )*
[*^(Nano)*](https://nano.org)*^( | )*
[*^(Earn Nano)*](https://playnano.online/?ref=nano_tips)*^( | )*
[*^(NanoLinks)*](https://nanolinks.org)*^( | )*
[*^(Opt Out)*](https://reddit.com/message/compose/?to=nano_tips&subject=opt-out&message=opt-out)
"""

HELP = """
Help from Nano Tips! This bot handles tips via the nano currency. Visit us on 
[GitHub](https://github.com/playnano/nano_tips) or /r/nano_tips for more information on its use and its status. 

By using this service, you agree to the [Terms of Service](https://github.com/playnano/nano_tips#terms-of-service). If 
you do not accept the Terms of Service, or do not wish to participate, please respond with the text `opt-out`.

Nano Tips works in two ways - either directly tip a user on a subreddit, or send a PM to /u/nano_tips with any command 
below.

***

To tip someone `0.01 XNO` on a
[tracked subreddit](https://www.reddit.com/r/nano_tips/comments/tbt78y/nano_tips_subreddits_and_status/), reply to 
their post or comment, starting or ending with:

    !ntips 0.01
    -or-
    !ntip 0.01
    -or-
    !nano_tips 0.01

To tip anywhere on reddit, start or end your comment by tagging the bot as such (it won't post on all the subreddits, 
but it will PM the users):

    /u/nano_tips 0.01

You can tip any amount above the program minimum of `0.0001 XNO`.

Also, you can specify a currency, like USD:

    !ntips 1USD

In untracked subreddits, the minimum tip is `1USD` in nano.

***

For PM commands, send u/nano_tips a message (not Chat!), or reply to this message, with any of the following 
commands:

    'create' - Create a new account if one does not exist
    'send <amount or all> <user/address>' - Send nano to a reddit user or an address
    'balance' or 'address' - Retrieves your account balance
    'minimum <amount>' - (default 0.0001) Sets a minimum amount for receiving tips
    'silence <yes/no>' - (default 'no') Prevents the bot from sending you tip notifications or tagging in posts
    'history <optional: number of records>' - Retrieves tipbot commands. Default 10, maximum is 50
    'percentage <percent>' - (default 10) Sets a percentage of returned tips to donate to the tipbot development
    'convert <amount><currency>' - Calculates the nano value of the specified currency. e.g. `convert 1USD`
    'opt-out' - Disables your account and donates your remaining nano to the tipbot
    'opt-in' - Re-enables your account. Your nano may or may not still be available
    'help' - Get this help message

E.g. if you wanted to send `0.01 XNO` to u/reddit_user, reply:

    send 0.01 reddit_user

If you have any questions or bug fixes, please post at /r/nano_tips or send a PM to u/playnano.
"""

WELCOME_CREATE = """
Welcome to Nano Tips, a reddit tipbot that allows you to tip and send nano (XNO) to your favorite redditors! Your 
account is **active** and your nano address is [{address}](https://blocklattice.io/account/{address}).

You will be receiving a tip of `0.001 XNO` as a welcome gift! To load more nano, you can deposit some nano to your 
address, receive a tip from a fellow redditor, or you can watch videos about nano and earn small amounts while learning at 
[PlayNANO](https://playnano.online/watch-and-learn?ref=nano_tips)!

By using this service, you agree to the [Terms of Service](https://github.com/playnano/nano_tips#terms-of-service). If 
you do not accept the Terms of Service, or do not wish to participate, please respond with the text `opt-out`.

Nano Tips works in two ways - either directly tip a user on a subreddit, or send a PM to /u/nano_tips with any command 
below.

***

To tip someone `0.01 XNO` on a 
[tracked subreddit](https://www.reddit.com/r/nano_tips/comments/tbt78y/nano_tips_subreddits_and_status/), reply to 
their post or comment starting or ending with:

    !ntips 0.01

To tip anywhere on reddit, start or end your comment by tagging the bot as such:

    /u/nano_tips 0.01

***

For PM commands, 
[send a message](https://reddit.com/message/compose/?to=nano_tips&subject=command&message=type_command_here) (not 
Chat!) to /u/nano_tips:

    'send <amount> <valid_nano_address>' - Withdraw your nano to your own wallet.
    'send <amount> <redditor username>' - Send to another redditor.
    'balance' - Check your account balance.
    'help' - Receive an in-depth help message.

View your account on the [block explorer](https://blocklattice.io/account/{address}).

If you have any questions or bug fixes, please post at /r/nano_tips or send a PM to u/playnano."""

WELCOME_TIP = """
Welcome to Nano Tips, a reddit tipbot that allows you to tip and send the nano currency (XNO) to your favorite 
redditors! You have just received a tip in the amount of `{amount:.4g} XNO` at your address 
[{address}](https://blocklattice.io/account/{address}).

Please activate your account by replying to this message, or any tips which are 30 days old will be returned to the 
sender.

To load more nano, you can deposit some nano to your address, receive a tip from a fellow redditor, or you can watch videos 
about nano and earn small amounts while learning at [PlayNANO](https://playnano.online/watch-and-learn?ref=nano_tips)!

By using this service, you agree to the [Terms of Service](https://github.com/playnano/nano_tips#terms-of-service). If 
you do not accept the Terms of Service, or do not wish to participate, please respond with the text `opt-out`.

Nano Tips works in two ways - either directly tip a user on a subreddit, or send a PM to /u/nano_tips with any command 
below.

***

To tip someone `0.01 XNO` on a 
[tracked subreddit](https://www.reddit.com/r/nano_tips/comments/tbt78y/nano_tips_subreddits_and_status/), reply to 
their post or comment starting or ending with:

    !ntips 0.01

To tip anywhere on reddit, start or end your comment by tagging the bot as such:

    /u/nano_tips 0.01

***

For PM commands, 
[send a message](https://reddit.com/message/compose/?to=nano_tips&subject=command&message=type_command_here) (not 
Chat!) to /u/nano_tips:

    'send <amount> <valid_nano_address>' - Withdraw your nano to your own wallet.
    'send <amount> <redditor username>' - Send to another redditor.
    'balance' - Check your account balance.
    'help' - Receive an in-depth help message.

View your account on the [block explorer](https://blocklattice.io/account/{address}).

If you have any questions or bug fixes, please post at /r/nano_tips or send a PM to u/playnano."""

NEW_TIP = """
Somebody just tipped you `{amount:.4g} XNO` at your address [{address}](https://blocklattice.io/account/{address}).

Your account balance is `{balance} XNO`.

[Transaction on explorer](https://blocklattice.io/block/{hash})

To turn off these notifications, reply with `silence yes`.
"""

RETURN_WARNING = """
Somebody tipped you at least 30 days ago, but your account hasn't been activated yet.

Please activate your account by replying any command to this bot. If you do not, any tips 35 days or older will be 
returned.

***

"""

COMMAND_NOT_RECOGNIZED = """
Beep boop, I'm a bot. Your command was not recognized.

Reply with `help` to receive an in-depth help message.

If you have any questions or bug fixes, please post at /r/nano_tips or send a PM to u/playnano.
"""


SUBJECTS = {
    "RETURN_WARNING": "Nano Tips - Please activate your Nano Tips account",
    "RETURN_MESSAGE": "Nano Tips - Returned tips",
    "first_tip": "Nano Tips - Congrats on receiving your first nano tip!",
    "new_tip": "Nano Tips - You just received a new nano tip!",
    "help": "Nano Tips - Help",
    "balance": "Nano Tips - Account balance",
    "minimum": "Nano Tips - Tip minimum",
    "percentage": "Nano Tips - Returned tip percentage for donation",
    "create": "Nano Tips - Create",
    "send": "Nano Tips - Send",
    "history": "Nano Tips - History",
    "silence": "Nano Tips - Silence",
    "subreddit": "Nano Tips - Subreddit",
    "opt-out": "Nano Tips - Opt Out",
    "opt-in": "Nano Tips - Opt In",
    "success": "Nano Tips - Your tip was successful",
    "failure": "Nano Tips - Your tip did not go through",
    "convert": "Nano Tips - Currency conversion",
    "not_recognized": "Nano Tips - Command not recognized"
}

MINIMUM = {
    "set_min": "Updating tip minimum to `{:.4g} XNO`",
    "below_program": "Did not update. The amount you specified is below the program minimum of `{:.4g} XNO`.",
    "parse_error": "I couldn't parse your command. I was expecting `minimum <amount>`. Be sure to check your spacing.",
}

NAN = "'{}' didn't look like a number to me. If it is blank, there might be extra spaces in the command."


# full responses
SEND_TEXT = {
    10: "Sent `{amount:.4g} XNO` to /u/{recipient} - [Transaction on explorer](https://blocklattice.io/block/{hash})",
    11: "Sent `{amount:.4g} XNO` to {recipient} - [Transaction on explorer](https://blocklattice.io/block/{hash})",
    20: "Creating a new account for /u/{recipient} and sending `{amount:.4g} XNO` - [Transaction on explorer](https://blocklattice.io/block/{hash})",
    30: "Sent `{amount:.4g} XNO` to address `{recipient}` - [Transaction on explorer](https://blocklattice.io/block/{hash})",

    100: "You don't have an account yet. Please "
         "[PM me](https://reddit.com/message/compose/?to=nano_tips&subject=create&message=create) with `create` in the "
         "body to make an account.",
    110: "You must specify an amount and a user, e.g. `send 1 nano_tips`",
    120: "I could not read the amount or the currency code. Is '{amount_text}' a number? This could also mean the "
         "currency converter is down.",
    130: "Program minimum is `{program_minimum:.4g} XNO`.",
    140: "It wasn't clear if you were trying to perform a currency conversion or not. If so, be sure there is no space "
         "between the amount and currency. Example: `!ntips 0.5USD`",
    150: "Your tip is below the minimum for this subreddit. In untracked subreddits, the minimum tip is `1USD` in "
         "nano.",
    160: "You have insufficient funds. Please (check your balance)(https://reddit.com/message/compose/?to=nano_tips&subject=balance&message=balance).",
    170: "'{recipient}' is neither a redditor nor a valid address.",
    180: "Sorry, the user has set a tip minimum of {user_minimum:.4g}. Your tip of `{amount:.4g} XNO` is below this "
         "amount.",
    190: "Sorry, the user has opted-out of using Nano Tips."
}

# for subreddits who like minimal response, or 2nd level responses
SEND_TEXT_MIN = {
    10: "^[Sent](https://blocklattice.io/block/{hash}) ^({amount:.4g} XNO to) [^(/u/{recipient})](/u/{recipient})",
    11: "^[Sent](https://blocklattice.io/block/{hash}) ^({amount:.4g} XNO to {recipient})",
    20: "^(Made a new account and )^[sent](https://blocklattice.io/block/{hash}) ^({amount:.4g} XNO to) "
        "[^(/u/{recipient})](/u/{recipient})",
    100: "^(Tip not sent. Error code )^[{status}](https://github.com/playnano/nano_tips#error-codes)"
}

OPT_IN = """Welcome back! You have opted back in. Your account will be restored with the same address, though any nano 
you had may have already been returned or donated already."""

OPT_OUT = """You have opted-out and I promise not to bother you anymore.

Returnable nano will be returned to the tippers, and the remaining balance will be donated to the tipbot fund.

If this was in error, please respond immediately with the text `opt-in`."""

SUBREDDIT = {
    "missing": "Your command seems to be missing something. Make sure it follow the format `subreddit <subreddit> "
    "<command> <option>`.",
    "not_mod": "You are not a moderator of /r/{subreddit}.",
    "minimum": "Successfully set your /r/{subreddit} minimum to {minimum}, active immediately.",
    "deactivate": "Within 5 minutes, tipping will be deactivated in /r/{subreddit}.",
    "activate": "Within 5 minutes, the Nano Tips response in /r/{subreddit} will be set to '{status}'.",
    "error": "There was something wrong with your activate or minimum command.",
    "all": "Here is a list of every subreddit and its status:\n\nName, Status, Minimum\n\n",
    "one": "Here are the settings for subreddit /r/{subreddit}:\n\nName, Status, Minimum\n\n",
}

SILENCE = {
    "yes_no": "I did not see 'no' or 'yes' after 'silence'. If you did type that, check your spacing.",
    "no": "Silence set to 'no'. You will receive tip notifications and be tagged by the bot in replies.",
    "yes": "Silence set to 'yes'. You will no longer receive tip notifications or be tagged by the bot.",
    "parse_error": "I couldn't parse your command. I was expecting 'silence <yes/no>'. Be sure to check your spacing.",
}

NOT_OPEN = """You do not currently have an account open. To create one, respond with the text 'create' in the message 
body."""

ALREADY_EXISTS = """It looks like you already have an account. In any case it is now **active**. Your nano address is 
[{address}](https://blocklattice.io/account/{address}).

View your account on the [block explorer](https://blocklattice.io/account/{address})."""

BALANCE = """Your account balance is `{balance} XNO`.

To load more nano, you can deposit some nano to your address, receive a tip from a fellow redditor, or you can watch videos 
about nano and earn small amounts while learning at [PlayNANO](https://playnano.online/watch-and-learn?ref=nano_tips)!

View your account on the [block explorer](https://blocklattice.io/account/{address})."""

CONVERT = {
    "no_amount_specified": "You must specify an amount, for example `convert 2.50USD`.",
    "success": "{} converts to {:.6g} XNO.",
}


def make_response_text(message, response):

    # make a minimal response if (subreddit is tracked) AND (level 2+ or minimal)
    if ("subreddit_status" in response.keys()) and (
        response["subreddit_status"] == "minimal"
        or (str(message.parent_id)[:3] != "t3_")
    ):
        if response["status"] < 100:
            return SEND_TEXT_MIN[response["status"]].format(
                hash=response["hash"],
                amount=from_raw(response["amount"]),
                recipient=response["recipient"],
            )
        else:
            return SEND_TEXT_MIN[100].format(status=response["status"])

    # otherwise, it will be a full response. Even if hostile/silent (we'll send PMs)
    if response["status"] in SEND_TEXT.keys():
        return SEND_TEXT[response["status"]].format(
            recipient=response.get("recipient"),
            amount=from_raw(response.get("amount", 0)),
            hash=response.get("hash"),
            amount_text=response.get("amount", ""),
            program_minimum=shared.PROGRAM_MINIMUM,
            user_minimum=response.get("minimum", shared.PROGRAM_MINIMUM)
        )

    return None


PERCENTAGE = {
    "parse_error": "I couldn't parse your command. I was expecting 'percentage <amount>'. "
    "Be sure to check your spacing.",
    "neg": "Did not update. Your percentage cannot be negative.",
    "100": "Did not update. Your percentage must be 100 or lower.",
    "updating": "Updating donation percentage to %s.",
}


def make_return_message(user):
    return_message = (
        "The following tips have been returned and %s percent of each tip has been "
        "donated to the tipbot development fund:\n\n "
        "(Redditor, Total Tip Amount, Returned Amount, Donation Amount)\n\n "
    )
    message = return_message % user["percent"]
    for transaction in user["transactions"]:
        message += "%s | %s | %s | %s\n\n " % (
            transaction[0],
            transaction[1],
            transaction[2],
            transaction[3],
        )
    return message

