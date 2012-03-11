###
# Copyright (c) 2012, b42
# Published under WTFPL.
#
###

import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Decide', True)


Decide = conf.registerPlugin('Decide')
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(Decide, 'someConfigVariableName',
#     registry.Boolean(False, """Help for someConfigVariableName."""))
conf.registerGlobalValue(Decide, 'separator',
    registry.String('--', """String that separates multiple choices."""))

conf.registerGlobalValue(Decide, 'interval',
    registry.PositiveInteger(6*60*60, """How often can the plugin change it's
        mind (in seconds). Default is six hours. Change to 1 if you want to get
        random answer every time"""))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
