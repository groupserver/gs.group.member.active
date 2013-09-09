jQuery.noConflict();

function gs_group_member_active_loaded (response, status, xhr) {
    var FADE_SPEED = 'slow', FADE_METHOD = 'swing';
    jQuery('#gs-group-member-active-loading').fadeOut(FADE_SPEED, FADE_METHOD);
    jQuery('#gs-group-member-active-ajax-hole').fadeIn(FADE_SPEED, FADE_METHOD);
}

jQuery(window).load(function () {
    var baseUrl = null, url = null, hole = null;
    baseUrl = jQuery('#gs-group-member-active-list-js').attr('data-group-url');
    url = baseUrl + '/gs-group-member-active-ajax.html';
    hole = jQuery('#gs-group-member-active-ajax-hole');
    hole.load(url, gs_group_member_active_loaded);
});
