$ ->
    $("#lets-fly").on "click", ->
        $("#lets-fly").attr "data-content", "<b>working...</b>"

        onError = (jqXHR, textStatus, errorThrown) ->
            if jqXHR.status == 403
                location.href = "/login/twitter"
            else
                alert "We could not access Twitter at this time. Please try again soon."

        request = $.ajax({
            url: '/twitter',
            type: 'get'
        })

        request.done (data, textStatus, jqXHR) ->
            users = data.users
            location.href = 'http://weflock.co/suggest'

        request.fail onError

        return request
