==========================
``gs.group.member.active``
==========================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The active member list for the group page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2014-03-02
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
`Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/


Introduction
============

This product provides a list of most recently active members of a
GroupServer_ group, where *active* is defined as posting
[#us]_. The idea is that a list of people makes group look
personable. The list is implemented by two viewlets_, that
conspire to load some JavaScript_ that in turn loads an `AJAX
page`_

Viewlets
========

The viewlet ``gs-group-member-active-list`` is shown in the
right-hand side of the group page (the *Secondary* area). It
provides a hole that is filled by the `AJAX page`_ and provides
links to the *Members* page, and the *Posting statistics* page.

The viewlet ``gs-group-member-active-list-js`` provides the code
to load the JavaScript_. Both the JavaScript viewlet and the main
viewlet are only shown if the person viewing the page can see the
``messages`` area.

JavaScript
==========

The JavaScript resource ``gs-group-member-active-20130909.js``
loads the `AJAX page`_.

AJAX Page
=========

The AJAX page ``gs-group-member-active-ajax.html``, in the Group
context, lists the members of the group, showing a square photo,
and name. The active members are listed in order of most-recent
to oldest.

Resources
=========

- Code repository:
  https://github.com/groupserver/gs.group.member.active
- Questions and comments to
  http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/

.. [#us] It is the replacement for the old *Us Bar*.
