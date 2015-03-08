$ ->
    $("#lets-fly").on "click", ->
        onError = (jqXHR, textStatus, errorThrown) ->
            if jqXHR.status == 403
                console.log "vip is a shit"
                location.href = "/login/twitter"
            else
                alert "Your authentication with Twitter failed... Whoops."
        request = $.ajax('/twitter', {type: 'GET', dataType: 'json', data: ''})
        request.done (data, textStatus, jqXHR) ->
            names = data.names
            tags = data.tags
            profs = data.profs
        request.fail onError
        return request
