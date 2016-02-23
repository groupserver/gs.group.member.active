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
from gs.group.member.active.viewlet import (ActiveMembersViewlet, )


class TestActiveMembersViewlet(TestCase):
    'Test the ``ActiveMembersViewlet``'

    @patch.object(ActiveMembersViewlet, 'isMember', new_callable=PropertyMock)
    @patch.object(ActiveMembersViewlet, 'viewTopics', new_callable=PropertyMock)
    def test_show(self, m_vT, m_iM):
        m_vT.return_value = True
        m_iM.return_value = True
        group = MagicMock()
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        a = ActiveMembersViewlet(group, request, view, manager)

        self.assertTrue(a.show)

    @patch.object(ActiveMembersViewlet, 'isMember', new_callable=PropertyMock)
    @patch.object(ActiveMembersViewlet, 'viewTopics', new_callable=PropertyMock)
    def test_show_non_member(self, m_vT, m_iM):
        m_vT.return_value = True
        m_iM.return_value = False
        group = MagicMock()
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        a = ActiveMembersViewlet(group, request, view, manager)

        self.assertTrue(a.show)

    @patch.object(ActiveMembersViewlet, 'isMember', new_callable=PropertyMock)
    @patch.object(ActiveMembersViewlet, 'viewTopics', new_callable=PropertyMock)
    def test_show_blocked_topics(self, m_vT, m_iM):
        m_vT.return_value = False
        m_iM.return_value = True
        group = MagicMock()
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        a = ActiveMembersViewlet(group, request, view, manager)

        self.assertTrue(a.show)

    @patch.object(ActiveMembersViewlet, 'isMember', new_callable=PropertyMock)
    @patch.object(ActiveMembersViewlet, 'viewTopics', new_callable=PropertyMock)
    def test_show_not(self, m_vT, m_iM):
        m_vT.return_value = False
        m_iM.return_value = False
        group = MagicMock()
        request = MagicMock()
        view = MagicMock()
        manager = MagicMock()
        a = ActiveMembersViewlet(group, request, view, manager)

        self.assertFalse(a.show)
