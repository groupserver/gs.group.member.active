# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2013 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from zope.cachedescriptors.property import Lazy
from gs.group.member.viewlet import MemberViewlet
from Products.GSGroupMember.groupMembersInfo import GSGroupMembersInfo


class ActiveMembersViewlet(MemberViewlet):

    def __init__(self, group, request, view, manager):
        super(ActiveMembersViewlet, self).__init__(group, request, view,
                                                    manager)

    @Lazy
    def show(self):
        retval = self.isMember or self.viewTopics
        return retval

    @Lazy
    def membersInfo(self):
        retval = GSGroupMembersInfo(self.groupInfo.groupObj)
        return retval
