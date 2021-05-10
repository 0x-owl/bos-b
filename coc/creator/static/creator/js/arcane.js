export function get_arcane(res) {
    for (let spell of res.spells) {
        append_html_spell(spell.uuid, spell)
        remove_spell_handler()
    }

    for (let artifact of res.artifacts) {
        $("#inv-artifacts").append(
            `<li>${artifact}</li>`
        )
    }
    $("#inv-encounters").after(
        `<p>${res.encounters}</p>`
    )
}


export function add_spells(uuid){
    let inv = window.location.href.split('/').pop()
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        url: "add_spell",
        type: "POST",
        data: {
            'inv': inv,
            'spell': uuid
        },
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function (res, xhr, responseText) {
            if (responseText.status === 200){
                append_html_spell(uuid, res.spell)
                remove_spell_handler()
            }
            else{
                console.log(xhr)
            }
        },
        error: function (res) {
            console.log(res);
        }
    })
}


function append_html_spell(uuid, spell){
    $("#inv-spells").append(
        `
            <li  id=spell-inv-${uuid}>
                <dl>
                    <dt><u>${spell.name}</u> (${spell.cost}) <a class="bi bi-x-circle-fill" id="spell-inv-rem-${uuid}"></a></dt>
                    <dd>
                        <span><b>Casting Time:</b></span> ${spell.casting_time}<br>
                        <span><b>Desc.:</b></span> ${spell.description}<br>
                        <span><b>Deeper Magic:</b></span>${spell.deeper_magic}<br>
                        <span><b>Alt Names:</b></span> <i>${spell.alternative_names}</i>
                    </dd>

                </dl>
            </li>
        `
    )
}


function remove_spell_handler() {
    $("a[id^='spell-inv-rem-']").off().click(
        function (evt) {
            evt.preventDefault();
            let inv = window.location.href.split('/').pop()
            let item_id = evt.target.id.replace("spell-inv-rem-", "");
            let object_id = "#spell-inv-" + item_id;
            let url_ = "spell/" + inv + "/" + item_id + "/remove";
            $.ajax(
                {
                    url: url_,
                    type: "GET",
                    success: function (res) {
                        $(object_id).remove()
                    },
                    error: function (res) {
                        console.log(res)
                    }
                }
            )
        }
    )
}