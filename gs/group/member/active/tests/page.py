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
