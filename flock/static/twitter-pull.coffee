$ ->
    $("#lets-fly").on "click", ->
        onError = (jqXHR, textStatus, errorThrown) ->
            if jqXHR.status == 403
                location.href = "/login/twitter"
            else
                alert "Your authentication with Twitter failed... Whoops."
        request = $.ajax('/twitter', {type: 'GET', dataType: 'json', data: ''}).fail onError
        request.done (data, textStatus, jqXHR) ->
            names = data.names
            tags = data.tags
            profs = data.profs
        return request
