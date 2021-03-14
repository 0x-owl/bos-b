export function get_gear(res) {
    for (let item of res.gear) {
        $("#inv-gear").append(
            `<tr id='gear-row-${item["uuid"]}'>
                <div class="input-group mb-3">
                    <td><input type="text" class="form-control" id="item-inv-title-${item['uuid']}" value=${item["title"]} readonly></td>
                    <td><input type="text" class="form-control" id="item-inv-price-${item['uuid']}" value=${item["price"]} readonly></td>
                    <td><input type="text" class="form-control" id="item-inv-stock-${item['uuid']}" value=${item["stock"]} readonly></td>
                    <td>
                        <a class="btn btn-primary" id="item-inv-edit-${item["uuid"]}"><i class="bi bi-pencil"></i></a>
                        <a class="btn btn-success disabled" id="item-inv-save-${item["uuid"]}"><i class="bi bi-save"></i></a>
                        <a class="btn btn-danger" id="item-inv-rem-${item["uuid"]}"><i class="bi bi-x-circle"></i></a>
                    </td>
                </div>
            </tr >`
        )
    }
}

export function remove_item_inventory_handler() {
    $("a[id^='item-inv-rem-']").click(
        function (evt) {
            evt.preventDefault();
            var item_id = evt.target.id.replace("item-inv-rem-", "");
            var object_id = "#gear-row-" + item_id;
            var url_ = "/creator/inventory/" + item_id + "/remove";
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

export function edit_item_inventory_handler() {
    $("a[id^='item-inv-edit-']").click(
        function (evt) {
            evt.preventDefault();
            var item_id = evt.target.id.replace("item-inv-edit-", "");
            $("input[id*='" + item_id + "']").prop('readonly', false);
            $("#item-inv-save-" + item_id).removeClass("disabled");
            $("#item-inv-rem-" + item_id).addClass("disabled");
            $("#item-inv-edit-" + item_id).addClass("disabled");
        }
    )
}

export function save_item_inventory_handler() {
    $("a[id^='item-inv-save-']").click(
        function (evt) {
            var item_id = evt.currentTarget.id.replace("item-inv-save-", "");
            $("input[id*='" + item_id + "']").prop('readonly', true);
            $("#item-inv-save-" + item_id).addClass("disabled");
            $("#item-inv-rem-" + item_id).removeClass("disabled");
            $("#item-inv-edit-" + item_id).removeClass("disabled");
            var csrftoken = $("[name=csrfmiddlewaretoken]").val();
            $.ajax({
                url: '/creator/inventory/' + item_id + '/edit',
                method: 'POST',
                data: {
                    'title': $("#item-inv-title-" + item_id).val(),
                    'price': $("#item-inv-price-" + item_id).val(),
                    'stock': $("#item-inv-stock-" + item_id).val(),
                },
                beforeSend: function (xhr, settings) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                success: function (res) {
                    // update values
                    $("#item-inv-title-" + item_id).val(res.title);
                    $("#item-inv-price-" + item_id).val(res.price);
                    $("#item-inv-stock-" + item_id).val(res.stock);
                },
                error: function (res) {
                    console.log(res)
                }

            })
        }
    )
}