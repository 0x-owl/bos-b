export function get_weapons(res) {
    for (let weapon of res.weapons) {
        $("#inv-weapons").append(
            `<tr id="gear-row-${weapon['uuid']}">
                <td><input type="text" class="form-control" style="width:200px" id="item-inv-title-${weapon['uuid']}" value=${weapon["title"]} readonly></td>
                <td>${weapon["skill_value"][0]}</td>
                <td>${weapon["skill_value"][1]}</td>
                <td>${weapon["skill_value"][2]}</td>
                <td><input type="text" class="form-control" style="width:70px" id="item-inv-dmg-${weapon['uuid']}" value=${weapon.damage} readonly></td>
                <td><input type="text" class="form-control" style="width:70px" id="item-inv-base-range-${weapon['uuid']}" value=${weapon.base_range} readonly></td>
                <td><input type="text" class="form-control" style="width:70px" id="item-inv-uses-per-round-${weapon['uuid']}" value=${weapon.uses_per_round} readonly></td>
                <td><input type="text" class="form-control" style="width:70px" id="item-inv-bullets-in-gun-mag-${weapon['uuid']}" value=${weapon.bullets_in_gun_mag} readonly></td>
                <td><input type="text" class="form-control" style="width:70px" id="item-inv-ammo-${weapon['uuid']}" value=${weapon.ammo} readonly></td>
                <td><input type="text" class="form-control" style="width:50px" id="item-inv-malf-${weapon['uuid']}" value=${weapon.malfunction} readonly></td>
                <td>
                    <a class="btn btn-primary" id="item-inv-edit-${weapon["uuid"]}"><i class="bi bi-pencil"></i></a>
                    <a class="btn btn-success disabled" id="weapon-inv-save-${weapon["uuid"]}"><i class="bi bi-save"></i></a>
                    <a class="btn btn-danger" id="item-inv-rem-${weapon["uuid"]}"><i class="bi bi-x-circle"></i></a>
                </td>
            </tr >`
        )
    }
}

export function save_weapon_inventory_handler() {
    $("a[id^='weapon-inv-save-']").click(
        function (evt) {
            evt.preventDefault();
            var item_id = evt.currentTarget.id.replace("weapon-inv-save-", "");
            $("input[id*='" + item_id + "']").prop('readonly', true);
            $("#weapon-inv-save-" + item_id).addClass("disabled");
            $("#item-inv-rem-" + item_id).removeClass("disabled");
            $("#item-inv-edit-" + item_id).removeClass("disabled");
            var csrftoken = $("[name=csrfmiddlewaretoken]").val();
            $.ajax({
                url: '/creator/inventory/' + item_id + '/edit',
                method: 'POST',
                data: {
                    'title': $("#item-inv-title-" + item_id).val(),
                    'damage': $("#item-inv-dmg-" + item_id).val(),
                    'base_range': $("#item-inv-base-range-" + item_id).val(),
                    'uses_per_round': $("#item-inv-uses-per-round-" + item_id).val(),
                    'bullets_in_gun_mag': $("#item-inv-bullets-in-gun-mag-" + item_id).val(),
                    'ammo': $("#item-inv-ammo-" + item_id).val(),
                    'malfunction': $("#item-inv-malf-" + item_id).val()
                },
                beforeSend: function (xhr, settings) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                success: function (res) {
                    // update values
                    $("#item-inv-title-" + item_id).val(res.title);
                    $("#item-inv-dmg-" + item_id).val(res.damage);
                    $("#item-inv-base-range-" + item_id).val(res.base_range);
                    $("#item-inv-uses-per-round-" + item_id).val(res.uses_per_round);
                    $("#item-inv-bullets-in-gun-mag-" + item_id).val(res.bullets_in_gun_mag);
                    $("#item-inv-ammo-" + item_id).val(res.ammo);
                    $("#item-inv-malf-" + item_id).val(res.malfunction);
                },
                error: function (res) {
                    console.log(res)
                }

            })
        }
    )
}

export function edit_weapon_inventory_handler() {
    $("a[id^='item-inv-edit-']").click(
        function (evt) {
            evt.preventDefault();
            var item_id = evt.target.id.replace("item-inv-edit-", "");
            $("input[id$='" + item_id + "']").prop('readonly', false);
            $("#weapon-inv-save-" + item_id).removeClass("disabled");
            $("#item-inv-rem-" + item_id).addClass("disabled");
            $("#item-inv-edit-" + item_id).addClass("disabled");
        }
    )
}