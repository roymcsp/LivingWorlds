# -*- coding: utf-8 -*-
"""
Connection screen

Texts in this module will be shown to the user at login-time.

Evennia will look at global string variables (variables defined
at the "outermost" scope of this module and use it as the
connection screen. If there are more than one, Evennia will
randomize which one it displays.

The commands available to the user when the connection screen is shown
are defined in commands.default_cmdsets. UnloggedinCmdSet and the
screen is read and displayed by the unlogged-in "look" command.

"""

from django.conf import settings
from evennia import utils
quit
CONNECTION_SCREEN = """

    |_|_|_|_Welcome to |g{}|n, version {}!
    
    Warning!!! Logging in to this game expresses a commitment to
    follow all the rules.
    
    If you have problems you may contact the administration at:
    admin@lwmercadia.com.
    
    Enter your character name or enter quit to quit.
""" \
    .format(settings.SERVERNAME, utils.get_evennia_version())
