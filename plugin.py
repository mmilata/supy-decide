###
# Copyright (c) 2012, b42
# Published under WTFPL.
#
###

import random

import supybot.conf as conf
import supybot.utils as utils
from supybot.commands import *
import supybot.commands
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks


class Decide(callbacks.Plugin):
    """This plugin has only one command, 'decide'."""
    def __init__(self, irc):
        self.__parent = super(Decide, self)
        self.__parent.__init__(irc)

    def decide(self, irc, msg, args, timestamp, text):
        """(decide <question>) -- Either gives yes/no answer to a question, or
        if question is a list of items separated by '--', pick one item
        randomly."""

        # make it so that the answers stay the same in one interval
        time_quotient = timestamp / conf.supybot.plugins.Decide.interval()

        # seed the generator with the part of the time we care about and
        # the (normalized) question
        rg = random.Random(str(time_quotient)+text.replace(' ', ''))

        choices = text.split(conf.supybot.plugins.Decide.separator())
        choices = [s.strip() for s in choices]

        if len(choices) == 1:
            choices = ['Yes', 'No']

        irc.reply(rg.choice(choices))

    decide = wrap(decide, ['now', 'text'])



Class = Decide


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
