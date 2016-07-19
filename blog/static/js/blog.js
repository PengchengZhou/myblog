/*====================django ajax ======*/
jQuery(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});
/*===============================django ajax end===*/

function addPopStateListener()
{
    window.onpopstate = function(e){
        var state = window.history.state;
        if(state!=null)
        {
            if(state.url=='/blog/ajax_a_post')
            {
                get_a_post(state.id, true);
            }
            else if(state.url=='/blog/ajax_abstract')
            {
                get_abstract_by_page_num(state.page_num, true);
            }
            else if(state.url=='/blog/ajax_abstract_c')
            {
                get_abstract_by_cid_and_page_num(state.c_id, state.page_num, true);
            }
        }
    };
}

function get_a_post(post_id, flag)
{
    $.ajax({
        type: 'POST',
        url: '/blog/ajax_a_post',
        data: {'id': post_id},
        dataType: 'json',
        success: function(result){
            if(flag==false)
            {
                var url = '/blog/post/'+result['id'];
                var state = {
                    url: '/blog/ajax_a_post',
                    id: result['id'],
                };
                window.history.pushState(state, '', url);
            }

            var title = '<div id="post-title"><h2>'+result['title']+'</h2></div>';
            var content = '<div id="post-content">'+result['content']+'</div>';
            $('#body-right').html(title+content);
        }
    });
}

function get_abstract_by_page_num(page_num, flag)
{
    $.ajax({
        type: 'POST',
        url: '/blog/ajax_abstract',
        data: {'page_num': page_num},
        dataType: 'json',
        success: function(result){
            if(flag==false)
            {
                var url = '/blog/abstract/'+result['page_num'];
                var state = {
                    url: '/blog/ajax_abstract',
                    page_num: result['page_num'],
                };
                window.history.pushState(state, '', url);
            }

            var abstracts = result['abstracts'];
            var i = 0, len = abstracts.length;
            $('#body-right').html('');
            for(; i<len; i++)
            {
                var abstr = abstracts[i];
                abstr = JSON.parse(abstr);
                $('#body-right').append("<div class='post_abstract'>"
                +"<div class='post_abstract_title'><a href='javascript: get_a_post("
                +abstr.id+")'>"+abstr.title+"</a></div><div class='post_abstract_abstract'><p>"
                +abstr.abstract+"</p></div><div class='post_abstract_footer'><p>"
                +abstr.pub_date+"&nbsp;&nbsp;阅读("+abstr.visit_count+")</p></div></div>");
            }
        }
    });
}

function get_abstract_by_cid_and_page_num(c_id, page_num, flag)
{
    $.ajax({
        type: 'POST',
        url: '/blog/ajax_abstract_c',
        data: {'c_id': c_id, 'page_num': page_num},
        dataType: 'json',
        success: function(result){
            if(flag==false)
            {
                var url = '/blog/abstract_c/'+result['c_id']+'/'+result['page_num'];
                var state = {
                    url: '/blog/ajax_abstract_c',
                    c_id: result['c_id'],
                    page_num: result['page_num'],
                };
                window.history.pushState(state, '', url);
            }

            var abstracts = result['abstracts'];
            var i = 0, len = abstracts.length;
            $('#body-right').html('');
            for(; i<len; i++)
            {
                var abstr = abstracts[i];
                abstr = JSON.parse(abstr);
                $('#body-right').append("<div class='post_abstract'>"
                +"<div class='post_abstract_title'><a href='javascript: get_a_post("
                +abstr.id+")'>"+abstr.title+"</a></div><div class='post_abstract_abstract'><p>"
                +abstr.abstract+"</p></div><div class='post_abstract_footer'><p>"
                +abstr.pub_date+"&nbsp;&nbsp;阅读("+abstr.visit_count+")</p></div></div>");
            }
        }
    });
}
