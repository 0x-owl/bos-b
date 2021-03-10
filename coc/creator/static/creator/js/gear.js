export function get_gear(res) {
    for (let item of res.gear) {
        $("#inv-gear").append(
            `<tr class="gear-row">
                <div class="input-group mb-3">
                    <td><input type="text" class="form-control" value=${item["title"]} readonly></td>
                    <td><input type="text" class="form-control" value=${item["price"]} readonly></td>
                    <td><input type="text" class="form-control" value=${item["stock"]} readonly></td>
                    <td><a href="" class="btn btn-outline-danger" id="item-inv-${item["uuid"]}">Remove</button></td>
                </div>
            </tr >`
        )
    }
}

