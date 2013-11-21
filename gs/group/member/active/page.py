# -*- coding: utf-8 -*-
##############################################################################
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
##############################################################################
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from AccessControl import getSecurityManager
from gs.group.base import GroupPage
from queries import ActiveMemberQuery


class ActiveMembersAjax(GroupPage):

    def __init__(self, group, request):
        super(ActiveMembersAjax, self).__init__(group, request)

    @Lazy
    def viewTopics(self):
        # TODO: Figure out I could do this better.
        msgs = self.context.messages
        user = getSecurityManager().getUser()
        retval = bool(user.has_permission('View', msgs))
        return retval

    @Lazy
    def query(self):
        retval = ActiveMemberQuery()
        return retval

    @Lazy
    def userPosts(self):
        retval = []
        if self.viewTopics:
            retval = self.query.user_posts(self.siteInfo.id, self.groupInfo.id)
        return retval

    @Lazy
    def length(self):
        # --=mpj17=-- Not actually the length (because of the anonymous
        # user check below) but close, and good enough for new groups.
        retval = len(self.userPosts)
        return retval

    @property
    def activeMembers(self):
        for userPost in self.userPosts:
            a = createObject('groupserver.UserFromId', self.context,
                                userPost['user_id'])
            if not a.anonymous:
                yield a
