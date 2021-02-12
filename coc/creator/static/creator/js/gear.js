export function get_gear(res) {
    for (let item of res.gear) {
        $("#inv-gear").append(
            `<tr>
                <td>${item["title"]}</td>
                <td>${item["price"]}</td>
                <td>${item["stock"]}</td>
            </tr >`
        )
    }
}