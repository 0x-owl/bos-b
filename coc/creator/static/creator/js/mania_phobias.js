export function manias_phobias(res) {
    for (let phobia of res.phobias){
        append_html_phobia(phobia[0], phobia[1])
        remove_phobia_handler()
    }
    for (let mania of res.manias){
        append_html_mania(mania[0], mania[1])
        remove_mania_handler()
    }
}


export function add_mania(uuid){
    let inv = window.location.href.split('/').pop()
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        url: "add_mania",
        type: "POST",
        data: {
            'inv': inv,
            'mania': uuid
        },
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function (res, xhr, responseText) {
            if (responseText.status === 200){
                append_html_mania(uuid, res.title)
                remove_mania_handler()
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

export function add_phobia(uuid){
    let inv = window.location.href.split('/').pop()
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        url: "add_phobia",
        type: "POST",
        data: {
            'inv': inv,
            'phobia': uuid
        },
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function (res, xhr, responseText) {
            if (responseText.status === 200){
                append_html_phobia(uuid, res.title)
                remove_phobia_handler()
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

function append_html_mania(uuid, title){
    $("#inv-manias").append(`<li id=mania-inv-${uuid}>
        ${title}
        <a class="bi bi-x-circle-fill" id="mania-inv-rem-${uuid}">
        </a>
    </li>`)
}

function append_html_phobia(uuid, title){
    $("#inv-phobias").append(`<li id=phobia-inv-${uuid}>
        ${title}
        <a class="bi bi-x-circle-fill" id="phobia-inv-rem-${uuid}">
        </a>
    </li>`)
}

function remove_mania_handler() {
    $("a[id^='mania-inv-rem-']").off().click(
        function (evt) {
            evt.preventDefault();
            let inv = window.location.href.split('/').pop()
            let item_id = evt.target.id.replace("mania-inv-rem-", "");
            let object_id = "#mania-inv-" + item_id;
            let url_ = "mania/" + inv + "/" + item_id + "/remove";
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

function remove_phobia_handler() {
    $("a[id^='phobia-inv-rem-']").off().click(
        function (evt) {
            evt.preventDefault();
            let inv = window.location.href.split('/').pop()
            let item_id = evt.target.id.replace("phobia-inv-rem-", "");
            let object_id = "#phobia-inv-" + item_id;
            let url_ = "phobia/" + inv + "/" + item_id + "/remove";
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