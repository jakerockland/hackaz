$ ->
    $("#lets-fly").on "click", ->
        onError = (jqXHR, textStatus, errorThrown) ->
            if jqXHR.status == 403
                location.href = "/login/twitter"
            else
                alert "Your authentication with Twitter failed... Whoops."

        request = $.ajax({
            url: '/twitter',
            type: 'get'
        })

        request.done (data, textStatus, jqXHR) ->
            console.log "help"
            # names = data.names
            window.location = 'http://weflock.co/suggest'

        request.fail onError

        return request
