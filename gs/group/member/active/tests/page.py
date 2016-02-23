# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2016 OnlineGroups.net and Contributors.
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
from __future__ import absolute_import, unicode_literals, print_function
from functools import partial
from mock import (MagicMock, patch, PropertyMock)
from unittest import TestCase
from gs.group.member.active.page import (ActiveMembersAjax, )


class TestActiveMembersAjax(TestCase):
    'Test the ``ActiveMembersAjax`` "page".'

    @patch.object(ActiveMembersAjax, 'viewTopics', new_callable=PropertyMock)
    @patch.object(ActiveMembersAjax, 'query', new_callable=PropertyMock)
    @patch.object(ActiveMembersAjax, 'groupInfo', new_callable=PropertyMock)
    @patch.object(ActiveMembersAjax, 'siteInfo', new_callable=PropertyMock)
    def test_posts_view_topics(self, m_sI, m_gI, m_q, m_vT):
        m_gI.id = 'example_group'
        m_sI.id = 'example'
        m_vT.return_value = True
        m_q().user_posts.return_value = ['userId']
        group = MagicMock()
        request = MagicMock()
        a = ActiveMembersAjax(group, request)

        self.assertEqual(['userId'], a.userPosts)

    @patch.object(ActiveMembersAjax, 'viewTopics', new_callable=PropertyMock)
    @patch.object(ActiveMembersAjax, 'query', new_callable=PropertyMock)
    @patch.object(ActiveMembersAjax, 'groupInfo', new_callable=PropertyMock)
    @patch.object(ActiveMembersAjax, 'siteInfo', new_callable=PropertyMock)
    def test_posts_topics_hidden(self, m_sI, m_gI, m_q, m_vT):
        m_gI.id = 'example_group'
        m_sI.id = 'example'
        m_vT.return_value = False
        m_q().user_posts.return_value = ['userUd']
        group = MagicMock()
        request = MagicMock()
        a = ActiveMembersAjax(group, request)

        self.assertEqual([], a.userPosts)

    @staticmethod
    def create_user(factory, context, userId, anonymous):
        retval = MagicMock()
        retval.id = userId
        retval.anonymous = anonymous
        return retval

    @patch.object(ActiveMembersAjax, 'userPosts', new_callable=PropertyMock)
    @patch.object(ActiveMembersAjax, 'groupInfo', new_callable=PropertyMock)
    @patch.object(ActiveMembersAjax, 'siteInfo', new_callable=PropertyMock)
    @patch('gs.group.member.active.page.createObject')
    def test_active_members(self, m_cO, m_sI, m_gI, m_uP):
        m_gI.id = 'example_group'
        m_sI.id = 'example'
        m_uP.return_value = [{'user_id': u} for u in ['a', 'b', 'c', ]]
        m_cO.side_effect = partial(self.create_user, anonymous=False)

        group = MagicMock()
        request = MagicMock()
        a = ActiveMembersAjax(group, request)
        r = a.activeMembers

        activeMemberIds = [u.id for u in r]
        self.assertEqual(['a', 'b', 'c', ], activeMemberIds)
        self.assertEqual(3, m_cO.call_count)

    @patch.object(ActiveMembersAjax, 'userPosts', new_callable=PropertyMock)
    @patch.object(ActiveMembersAjax, 'groupInfo', new_callable=PropertyMock)
    @patch.object(ActiveMembersAjax, 'siteInfo', new_callable=PropertyMock)
    @patch('gs.group.member.active.page.createObject')
    def test_active_members_odd(self, m_cO, m_sI, m_gI, m_uP):
        '''Ensure people without a profile are skipped'''
        m_gI.id = 'example_group'
        m_sI.id = 'example'
        m_uP.return_value = [{'user_id': u} for u in ['a', 'b', 'c', ]]
        m_cO.side_effect = partial(self.create_user, anonymous=True)

        group = MagicMock()
        request = MagicMock()
        a = ActiveMembersAjax(group, request)
        r = a.activeMembers

        activeMemberIds = [u.id for u in r]
        self.assertEqual([], activeMemberIds)
        self.assertEqual(3, m_cO.call_count)
