jQuery.noConflict();

jQuery(window).load(function () {
    var baseUrl = null, url = null;
    baseUrl = jQuery('#gs-group-member-active-list-js').attr('data-group-url');
    url = baseUrl + '/gs-group-member-active-ajax.html';    
    jQuery('#gs-group-member-active-ajax-hole').load(url);
});
