export function get_weapons(res) {
    for (let weapon of res.weapons) {
        $("#inv-weapons").append(
            `<tr>
                <td>${weapon["title"]}</td>
                <td>${weapon["skill_value"][0]}</td>
                <td>${weapon["skill_value"][1]}</td>
                <td>${weapon["skill_value"][2]}</td>
                <td>${weapon.damage}</td>
                <td>${weapon.base_range}</td>
                <td>${weapon.uses_per_round}</td>
                <td>${weapon.bullets_in_gun_mag}</td>
                <td>${weapon.ammo}</td>
                <td>${weapon.malfunction}</td>
            </tr >`
        )
    }
}