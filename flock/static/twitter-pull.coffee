$ ->
    $("#lets-fly").on "click", ->
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
            names = data.names
            location.href = 'http://weflock.co/suggest'

        request.fail onError

        return request
