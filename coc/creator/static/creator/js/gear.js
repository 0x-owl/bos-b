export function get_gear(res) {
    for (let item of res.gear) {
        $("#inv-gear").append(
            `<tr id='gear-row-${item["uuid"]}'>
                <div class="input-group mb-3">
                    <td><input type="text" class="form-control" id="item-inv-title-${item['uuid']}" value=${item["title"]} readonly></td>
                    <td><input type="text" class="form-control" id="item-inv-price-${item['uuid']}" value=${item["price"]} readonly></td>
                    <td><input type="text" class="form-control" id="item-inv-stock-${item['uuid']}" value=${item["stock"]} readonly></td>
                    <td>
                        <a class="btn btn-info" id="item-inv-edit-${item["uuid"]}">Edit</a>
                        <a class="btn btn-warning disabled" id="item-inv-save-${item["uuid"]}">Save</a>
                        <a class="btn btn-danger" id="item-inv-rem-${item["uuid"]}">Remove</a>
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
            // var object_id = "#gear-row-" + item_id;
            // var url_ = "/creator/inventory/" + item_id + "/remove";
            // $.ajax(
            //     {
            //         url: url_,
            //         type: "GET",
            //         success: function (res) {
            //             $(object_id).remove()
            //         },
            //         error: function (res) {
            //             console.log(res)
            //         }
            //     }
            // )
        }
    )
}

export function save_item_inventory_handler() {
    $("a[id^='item-inv-save-']").click(
        function (evt) {
            evt.preventDefault();
            var item_id = evt.target.id.replace("item-inv-save-", "");
            $("input[id*='" + item_id + "']").prop('readonly', true);
            $("#item-inv-save-" + item_id).addClass("disabled");
            $("#item-inv-rem-" + item_id).removeClass("disabled");
        }
    )
}