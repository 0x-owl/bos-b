export function get_gear(res) {
    for (let item of res.gear) {
        $("#inv-gear").append(
            `<tr id='gear-row-${item["uuid"]}'>
                <div class="input-group mb-3">
                    <td><input type="text" class="form-control" value=${item["title"]} readonly></td>
                    <td><input type="text" class="form-control" value=${item["price"]} readonly></td>
                    <td><input type="text" class="form-control" value=${item["stock"]} readonly></td>
                    <td><a class="btn btn-outline-danger" id="item-inv-${item["uuid"]}">Remove</a></td>
                </div>
            </tr >`
        )
    }
}

export function remove_item_inventory_handler() {
    $("a[id^='item-inv-']").click(
        function (evt) {
            evt.preventDefault();
            var item_id = evt.target.id.replace("item-inv-", "");
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
