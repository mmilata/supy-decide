###
# Copyright (c) 2012, b42
# Published under WTFPL.
#
###

from supybot.test import *

class DecideTestCase(PluginTestCase):
    plugins = ('Decide',)

    def test_one_choice(self):
        self.assertRegexp("decide something", "(Yes|No)")
        self.assertRegexp("decide something with multiple words", "(Yes|No)")

    def test_multichoice(self):
        self.assertRegexp("decide a -- b", "(a|b)")
        self.assertRegexp("decide a -- b -- c", "(a|b|c)")
        self.assertRegexp("decide a x -- b y -- c z -- d w", "(a x|b y|c z|d w)")

    def test_error(self):
        self.assertError("decide")


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
