export function get_backstory(res) {
    $("#inv-description-inp").val(
        res.description
    );
    $("#inv-ideologies-inp").val(
        res.ideologies
    )
    $("#inv-significant-people-inp").val(
        res.significant_people
    )
    $("#inv-meaningful-locations-inp").val(
        res.meaningful_locations
    )
    $("#inv-treasured-possessions-inp").val(
        res.treasured_possessions
    )
    $("#inv-traits-inp").val(
        res.traits
    )
    $("#inv-injuries-scars-inp").val(
        res.injuries_scars
    )
    $("#inv-encounters-with-strange-entities-inp").val(
        res.encounters_with_strange_entities
    )
}

export function update_backstory(evt) {
    evt.preventDefault();
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        url: evt.url,
        method: 'POST',
        data: {
            'description': $("#inv-description-inp").val(),
            'ideologies': $("#inv-ideologies-inp").val(),
            'significant_people': $("#inv-significant-people-inp").val(),
            'meaningful_locations': $("#inv-meaningful-locations-inp").val(),
            'treasured_possessions': $("#inv-treasured-posessions-inp").val(),
            'traits': $("#inv-traits-inp").val(),
            'injure_scars': $("#inv-injuries-scars-inp").val(),
            'encounters_with_strange_entities': $("#inv-encounters-with-strange-entities-inp").val()

        },
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function (res) {
            for (const key in res) {
                let id = key.replaceAll('_', '-');
                $("#inv-" + id + "-inp").val(res[key])
            }
        },
        error: function (res) {
            console.log(res);
        }
    })
}