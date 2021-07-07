import { append_html_gear, append_html_weapon, append_html_magic_item, remove_magic_item_handler } from "/static/creator/js/items_append_html.js";

let items_category = {
    '1' : append_html_magic_item,
    '2' : append_html_gear,
    '3' : append_html_weapon,
    '4' : append_html_gear,
    '5' : append_html_gear,
    '6' : append_html_gear
}

export function add_items(uuid){
    let inv = window.location.href.split('/').pop()
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        url: "inventory/add_item",
        type: "POST",
        data: {
            'inv': inv,
            'item': uuid
        },
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function (res, xhr, responseText) {
            if (responseText.status === 201){
                let category = res.category.toString();
                let func = items_category[category];
                func(res.item);
                remove_magic_item_handler()
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