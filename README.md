# Nano Tips
Nano Tips is a reddit tipping service to easily give nano (XNO) to your favorite redditors, posts and comments! [Nano](https://nano.org) is a fast and feeless cryptocurrency that can be traded at numerous exchanges. Before using Nano Tips, please take a look at the [Terms of Service](https://github.com/playnano/nano_tips#terms-of-service)

Nano Tips is a fork of [Nano Tipper](https://github.com/danhitchcock/nano_tipper_z), which [was discontinued](https://www.reddit.com/r/nanocurrency/comments/t5uotr/reddit_tipbot_to_shut_down/) on March 7th, 2022.
### To get started with Nano Tips, either:
A) **Create an account** by [sending a message](https://reddit.com/message/compose/?to=nano_tips&subject=hi&message=create) to /u/nano_tips with 'create' or 'register' in the message body. You will receive a nano address, to which you can add nano\*. You will receive a 0.001 XNO tip for registering! Also, try any of the faucets at [Nano Links](https://nanolinks.info/#faucets-free-nano)

-or-

B) **Receive a nano tip** from a fellow redditor, and you will automatically have an account made! be sure to activate it afterwards by [sending a message](https://reddit.com/message/compose/?to=nano_tips&subject=command&message=create) to /u/nano_tips.
Once you have funds in your account, you can tip other redditors, or send to nano address via PM to /u/nano_tips.

(\**Nano Tips is in early beta! Only send small amounts of XNO*)
# Comment Replies:
Nano Tips is intended for tipping on reddit posts and replies. On any [tracked subreddit](https://www.reddit.com/r/nano_tips/comments/tbt78y/nano_tips_subreddits_and_status/) you can tip and type a message like:

    !ntips 0.01 This is great!

This will tip a redditor 0.01 XNO. `!ntips AMOUNT` must be the first thing in your message OR the last thing. Such, this is also a valid tip:

    This is great! !ntips 0.01

Or from anywhere on reddit, you can tip a commenter by:

    /u/nano_tips 0.01 This is great!
   
or

    This is great! /u/nano_tips 0.01

Even specify a currency!

    !ntips 1USD Enjoy a dollar!

If the subreddit is a [friendly subreddit](https://www.reddit.com/r/nano_tips/comments/tbt78y/nano_tips_subreddits_and_status/) (which correlates to [tracked subreddit](https://www.reddit.com/r/nano_tips/comments/tbt78y/nano_tips_subreddits_and_status/)), the bot will respond with a message. If the subreddit is not tracked, there is a $1USD minimum and the bot will send PMs instead of responding. If the subreddit is marked as "silent", PMs will be sent.


    
# Private Messages

Nano Tips also works by PM (NOT CHAT). [Send a message](https://reddit.com/message/compose/?to=nano_tips&subject=hi&message=type_command_here) to /u/nano_tips for a variety of actions.

To send 0.1 XNO to redditor_username, include this text in the message body:

    send 0.1 /u/redditor_username
-or-

    send 0.1 redditor_username

To send 0.1 XNO to nano\_3pnanopr3d5g7o45zh3nmdkqpaqxhhp3mw14nzr41smjz8xsrfyhtf9xac77, include this text in the message body:

    send 0.1 nano_3pnanopr3d5g7o45zh3nmdkqpaqxhhp3mw14nzr41smjz8xsrfyhtf9xac77

or send all your balance:

    send all nano_3pnanopr3d5g7o45zh3nmdkqpaqxhhp3mw14nzr41smjz8xsrfyhtf9xac77

There are many other commands.

```
'balance' or 'address' - Retrieve your account balance. Includes both pocketed and unpocketed transactions
'create' - Create a new account if one does not exist
'help' - Get this help message
'history <optional: number of records>' - Retrieves tipbot commands. Default 10, maximum is 50.
'minimum <amount>' - (default 0.0001) Sets a minimum amount for receiving tips
'send <amount or all, optional: Currency> <user/address>' - Send nano to a reddit user or an address
'silence <yes/no>' - (default 'no') Prevents the bot from sending you tip notifications or tagging in posts
'percentage <percent>' - (default 10 percent) Sets a percentage of returned tips to donate to TipBot development
'subreddit <subreddit> <'activate'/'deactivate'> <option>' - Subreddit Moderator Controls - Enabled Tipping on Your Sub (`silent`, `minimal`, `full`)
'withdraw <amount or all> <user/address>' - Same as send
'convert <amountcurrency>' - Calculates the nano value of the specified curency. e.g. `convert 1USD`. Also works with "price" and "value".
'opt-out' - Disables your account and donates your remaining nano to the tipbot.
'opt-in' - Reenables your account. Your nano may or may not still be available. 
```
## Broccolish! 🥦
Nano Tips is broccolish! You can use 🥦 on your tips to send 0.133 XNO.

    !ntips 🥦
You can also specify different amounts to send more 🥦!

    !ntips 5🥦
    -or-
    !ntips 🥦🥦🥦🥦🥦
# Activate the TipBot on Your Subreddit
If you are a moderator of a subreddit, and would like to tipping to your sub, use the `subreddit` command. For example, for me to activate tipping on my /r/nano_tips subreddit, I send a PM to the bot saying:

`subreddit nano_tips activate`

This will allow the bot to look for !ntips commands and respond to posts. 
-or- If I don't want the bot to respond, but still want tips:

`subreddit nano_tips activate silent`

-or- for a cleaner tipbot response:

`subreddit nano_tips activate minimal`

To deactivate, simply PM:

`subreddit nano_tips deactivate`

To set a minimum, specify like so:

`subreddit nano_tips minimum 1`

### Here's a few other great links:
[Nano Tips Subreddit](https://reddit.com/r/nano_tips) -- Post any questions about Nano Tips
[Nano Tips GitHub](https://github.com/playnano/nano_tips) -- This software is open source!
[Nano Currency](https://nano.org) -- The Official Nano website
[Nano Links](https://nanolinks.info) -- has numerous useful links to get to using Nano!
[Nano Subreddit](https://www.reddit.com/r/nanocurrency) -- The official Nano Subreddit

# Terms of Service
* Don't keep a lot of nano in your Nano Tip Bot account
* You accept the risks of using this Tip Bot--While I have no intention of stealing your nanos, they might be lost at any point, and I'm under no obligation to replace them. Don't put in more than you're willing to lose.
* If your account is inactive for more than 3 years, and no meaningful attempt has been made to reach me, the nanos in your account will be forfeited and I am under no obligation to return them. Why did I write this? Because the tip bot is not a lifelong custodian service -- I don't want people reaching out to me after years for their nanos the left on the tip bot. I don't want to have to keep the database with me the rest of my life. That being said, if the bot is still running in 3 years, your nano is more than likely available.
* Don't submit more than 5 requests every 30 seconds. The bot will ignore any commands you issue until 30 seconds have passed.
* I can change the Terms of Service at any time.

# FAQ
## Why does the message have to start or end with !ntips?
This is to prevent unintentional tips! If the program simply scanned the entire comment, a user might accidentally quote someone else's tip command in a response. In the future I might change this, but for now it's the best way to ensure the program behaves as expected.

## Are my funds safe?
**NO! Unless you and you alone control your private keys, your funds are never safe!** Please don't keep more than a few nanos on the tipbot at any time! This program is a hobby project, not a battle tested exchange. Bad things can happen, including lost nano! **Use at your own risk!**

## I sent a tip to the wrong address. Can I get it back?
If the address isn't affiliated with a redditor, **No.** I only have private keys for redditors, not for addresses. If you send nano to Binance for example, I cannot retrieve it.

## I sent a tip to the wrong redditor. Can I get it back?
You basically gave a stranger a dollar, and I have no control over that. Yes, I technically control the private keys, but I really don't want to start manually making unauthorized transactions on people's accounts. If the stranger is a redditor and doesn't activate their account, you will get your tip back in 30 days. If they *do* activate their account, it's theirs. You can try asking them for it back.

## Have you implemented any spam prevention for your bot?
Users are allowed 5 requests every 30 seconds. If you do more than that, the bot ignores you until 30 seconds have passed.

## I tried to send a tip, but received no response. Did it go through?
Probably not. It's most likely the bot was temporarily disconnected. If a command is issued while the bot is offline, the command will not be seen. If no response is received from the bot after a few minutes, send a message to the bot with the text 'history'. If you get a response and the tip isn't in your history, that means it wasn't seen. If you don't get a response, the bot is probably still offline. Try again in a few minutes.

## I found a bug or I have a concern. Question Mark?
Send /u/playnano a PM on reddit, or post on https://reddit.com/r/nano_tips

# Error Codes
If a reddit tip is a reply to a reply, it's better to keep a short message with an error code.
* 100 - You do not have an account -- Create an account by typing 'create' or by receiving a tip from another redditor.
* 110 - You must specify an amount and a user, e.g. `send 1 nano_tips`.
* 120 - Could not read the tip amount -- use either a number or the word 'all'.
* 130 - Tip amount is below program minimum -- This is to prevent spamming other redditors.
* 140 - If using currency conversion, make sure there is no space. Example: `!ntips 0.5USD`.
* 150 - You are likely attempting to tip in an unfamiliar sub. The minimum is 1 XNO.
* 160 - You have insufficient funds.
* 180 - Tip amount is below recipients specified tip minimum.
* 190 - The recipient has disabled tipping for their account.
