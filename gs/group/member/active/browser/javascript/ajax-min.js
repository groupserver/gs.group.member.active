// Copyright © 2013 OnlineGroups.net and Contributors.
// All Rights Reserved.
//
// This software is subject to the provisions of the Zope Public License,
// Version 2.1 (ZPL). http://groupserver.org/downloads/license/
jQuery.noConflict();function gs_group_member_active_loaded(b,a,e){var d="slow",c="swing";
jQuery("#gs-group-member-active-loading").fadeOut(d,c);jQuery("#gs-group-member-active-ajax-hole").fadeIn(d,c)
}jQuery(window).load(function(){var b=null,a=null,c=null;b=jQuery("#gs-group-member-active-list-js").attr("data-group-url");
a=b+"/gs-group-member-active-ajax.html";c=jQuery("#gs-group-member-active-ajax-hole");
c.load(a,gs_group_member_active_loaded)});