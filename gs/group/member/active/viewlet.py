# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from gs.group.member.viewlet import MemberViewlet
from queries import ActiveMemberQuery


class ActiveMembersViewlet(MemberViewlet):

    def __init__(self, group, request, view, manager):
        super(ActiveMembersViewlet, self).__init__(group, request, view,
                                                    manager)

    @Lazy
    def show(self):
        retval = self.isMember or self.groupVisibility.isPublic
        return retval

    @Lazy
    def query(self):
        retval = ActiveMemberQuery()
        return retval

    @Lazy
    def userPosts(self):
        retval = self.query.user_posts(self.siteInfo.id, self.groupInfo.id)
        return retval

    @property
    def activeMembers(self):
        for userPost in self.userPosts:
            a = createObject('groupserver.UserFromId', self.context,
                                userPost['user_id'])
            yield a
