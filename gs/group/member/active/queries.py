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
import sqlalchemy as sa
from gs.database import getSession, getTable


class ActiveMemberQuery(object):

    def __init__(self):
        self.postTable = getTable('post')

    def user_posts(self, siteId, groupId, limit=5):
        pt = self.postTable
        cols = [pt.c.user_id, sa.func.max(pt.c.date).label('max_date')]
        s = sa.select(cols, group_by=pt.c.user_id,
                        order_by=(sa.desc('max_date')), limit=limit)
        s.append_whereclause(pt.c.group_id == groupId)
        s.append_whereclause(pt.c.site_id == siteId)
        s.append_whereclause(pt.c.hidden == None)  # lint:ok

        session = getSession()
        r = session.execute(s)
        retval = []
        if r.rowcount:
            retval = [{'user_id': row['user_id'],
                        'max_date': row['max_date']} for row in r]
        return retval
