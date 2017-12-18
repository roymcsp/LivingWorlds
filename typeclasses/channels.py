"""
Channel

The channel class represents the out-of-character chat-room usable by
Accounts in-game. It is mostly overloaded to change its appearance, but
channels can be used to implement many different forms of message
distribution systems.

Note that sending data to channels are handled via the CMD_CHANNEL
syscommand (see evennia.syscmds). The sending should normally not need
to be modified.

"""

from evennia import DefaultChannel

CHANNEL_COLORS = {'OOC': '|YOOC|n',
                  'Chat': '|MChat|n',
                  'Question': '|GQuestion|n',
                  'Caliphate': '|BCaliphate|n',
                  'Empire': '|BEmpire|n',
                  'Kingdom': '|BKingdom|n',
                  'World': '|RWorld|n',
                  'Fighter': '|CFighter|n',
                  'Mage': '|CMage|n',
                  'Thief': '|CThief|n',
                  'Merchant': '|CMerchant|n',
                  'Helotyr': '|cHelotyr|n',
                  'Templar': '|CTemplar|n',
                  'Helotyrim': '|CCleric|n',
                  'Warrior': '|CWarrior|n',
                  'Sorcerer': '|CSorcerer|n',
                  'Assassin': '|CAssassin|n',
                  'Trader': '|CTrader|n',
                  'Sarthoaran': '|CCleric|n',
                  'Harbinger': '|CHarbinger|n',
                  'Sarthoar': '|cSarthoar|n',
                  'Samurai': '|CSamurai|n',
                  'Shaman': '|CShaman|n',
                  'Monk': '|CMonk|n',
                  'Artisan': '|CArtisan|n',
                  'Druid': '|CDruid|n',
                  'Ranger': '|CRanger|n',
                  'Aphrea': '|cAphrea|n',
                  'News': '|bNews|n',
                  'Judicial': '|gJudicial|n',
                  'Tribune': '|gTribune|n',
                  'Magistrate': '|gMagistrate|n',
                  'Garrison': '|rGarrison|n',
                  'Medjai': '|rMedjai|n',
                  'Legion': '|rLegion|n',
                  'Sheriff': '|RSheriff|n',
                  'Warden': '|RWarden|n',
                  'Gumi': '|RGumi|n',
                  }

class Channel(DefaultChannel):
    """
    Working methods:
        at_channel_creation() - called once, when the channel is created
        has_connection(account) - check if the given account listens to this channel
        connect(account) - connect account to this channel
        disconnect(account) - disconnect account from channel
        access(access_obj, access_type='listen', default=False) - check the
                    access on this channel (default access_type is listen)
        delete() - delete this channel
        message_transform(msg, emit=False, prefix=True,
                          sender_strings=None, external=False) - called by
                          the comm system and triggers the hooks below
        msg(msgobj, header=None, senders=None, sender_strings=None,
            persistent=None, online=False, emit=False, external=False) - main
                send method, builds and sends a new message to channel.
        tempmsg(msg, header=None, senders=None) - wrapper for sending non-persistent
                messages.
        distribute_message(msg, online=False) - send a message to all
                connected accounts on channel, optionally sending only
                to accounts that are currently online (optimized for very large sends)

    Useful hooks:
        channel_prefix(msg, emit=False) - how the channel should be
                  prefixed when returning to user. Returns a string
        format_senders(senders) - should return how to display multiple
                senders to a channel
        pose_transform(msg, sender_string) - should detect if the
                sender is posing, and if so, modify the string
        format_external(msg, senders, emit=False) - format messages sent
                from outside the game, like from IRC
        format_message(msg, emit=False) - format the message body before
                displaying it to the user. 'emit' generally means that the
                message should not be displayed with the sender's name.

        pre_join_channel(joiner) - if returning False, abort join
        post_join_channel(joiner) - called right after successful join
        pre_leave_channel(leaver) - if returning False, abort leave
        post_leave_channel(leaver) - called right after successful leave
        pre_send_message(msg) - runs just before a message is sent to channel
        post_send_message(msg) - called just after message was sent to channel

    """

    def channel_prefix(self, msg, emit=False):
        prefix_string = ""
        if self.key in CHANNEL_COLORS:
            prefix_string = "[%s] " % CHANNEL_COLORS.get(self.key.lower())
        else:
            prefix_string = "[%s] " % self.key.capitalize()
        return prefix_string
