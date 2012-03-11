This plugin provides 'decide' command. If you supply one argument, it randomly
responds yes or no. If you provide multiple choices separated by '--', it will
randomly pick one.

Shamelessly copied from anydot's (https://github.com/anydot) perl script.

 * The responses can be considered a function of question and current time.
   That means that the bot will use the same answer for some amount of time.
   By default, it "changes its mind" every 6 hours, this value can be set in
   variable 'supybot.plugins.Decide.interval' (in seconds).

 * Which multiple-choice separator is used can be set in
   'supybot.plugins.Decide.separator"
