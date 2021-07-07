import {remove_item_inventory_handler, edit_item_inventory_handler, save_item_inventory_handler} from "/static/creator/js/gear.js"
import {save_weapon_inventory_handler, edit_weapon_inventory_handler} from "/static/creator/js/weapons.js"

const ITEM_SUBCATEGORIES={
    'artifacts': 'Artifacts',
    'tomes': 'Tomes of Eldritch Lore',
    'occult_books': 'Occult Books'
}

export function append_html_gear(item){
    let item_title = JSON.stringify(item.properties['title']);
    $("#inv-gear").append(
        `<tr id='gear-row-${item.uuid}'>
            <div class="input-group mb-3">
                <td><input type="text" class="form-control" id="item-inv-title-${item.uuid}" value=${item_title} readonly></td>
                <td><input type="text" class="form-control" id="item-inv-price-${item.uuid}" value=${item.properties["price"]} readonly></td>
                <td><input type="text" class="form-control" id="item-inv-stock-${item.uuid}" value=${item.stock} readonly></td>
                <td>
                    <a class="btn btn-primary" id="item-inv-edit-${item.uuid}"><i class="bi bi-pencil"></i></a>
                    <a class="btn btn-success disabled" id="item-inv-save-${item.uuid}"><i class="bi bi-save"></i></a>
                    <a class="btn btn-danger" id="item-inv-rem-${item.uuid}"><i class="bi bi-x-circle"></i></a>
                </td>
            </div>
        </tr >`
    )
    remove_item_inventory_handler()
    edit_item_inventory_handler()
    save_item_inventory_handler()
}


export function append_html_weapon(weapon){
    let weapon_title = JSON.stringify(weapon.properties['title']);
    $("#inv-weapons").append(
        `<tr id="gear-row-${weapon.uuid}">
            <td><input type="text" class="form-control" style="width:200px" id="item-inv-title-${weapon.uuid}" value=${weapon_title} readonly></td>
            <td>${weapon.properties["skill_value"][0]}</td>
            <td>${weapon.properties["skill_value"][1]}</td>
            <td>${weapon.properties["skill_value"][2]}</td>
            <td><input type="text" class="form-control" style="width:70px" id="item-inv-dmg-${weapon.uuid}" value=${weapon.properties['damage']} readonly></td>
            <td><input type="text" class="form-control" style="width:70px" id="item-inv-base-range-${weapon.uuid}" value=${weapon.properties['base_range']} readonly></td>
            <td><input type="text" class="form-control" style="width:70px" id="item-inv-uses-per-round-${weapon.uuid}" value=${weapon.properties['uses_per_round']} readonly></td>
            <td><input type="text" class="form-control" style="width:70px" id="item-inv-bullets-in-gun-mag-${weapon.uuid}" value=${weapon.properties['bullets_in_gun_mag']} readonly></td>
            <td><input type="text" class="form-control" style="width:70px" id="item-inv-ammo-${weapon.uuid}" value=${weapon.properties['ammo']} readonly></td>
            <td><input type="text" class="form-control" style="width:50px" id="item-inv-malf-${weapon.uuid}" value=${weapon.properties['malfunction']} readonly></td>
            <td>
                <a class="btn btn-primary" id="item-inv-edit-${weapon.uuid}"><i class="bi bi-pencil"></i></a>
                <a class="btn btn-success disabled" id="weapon-inv-save-${weapon.uuid}"><i class="bi bi-save"></i></a>
                <a class="btn btn-danger" id="item-inv-rem-${weapon.uuid}"><i class="bi bi-x-circle"></i></a>
            </td>
        </tr >`
    )
    save_weapon_inventory_handler()
    edit_weapon_inventory_handler()
    remove_item_inventory_handler()
}


export function append_html_magic_item(magic_item){
    if (magic_item.properties['subcategory'] == ITEM_SUBCATEGORIES['artifacts']){
        append_html_artifact(magic_item)
    }
    else if (magic_item.properties['subcategory'] == ITEM_SUBCATEGORIES['tomes']){
        append_html_tome(magic_item)
    }
    else{
        append_html_occult_book(magic_item)
    }
    remove_magic_item_handler()
}


export function append_html_artifact(magic_item){
    $("#inv-artifacts").append(
        `
            <li  id=magic-item-inv-${magic_item.uuid}>
                <dl>
                    <dt><u>${magic_item.properties['title']}</u> <a class="bi bi-x-circle-fill" id="magic-item-inv-rem-${magic_item.uuid}"></a></dt>
                    <dd>
                        <span><b>Description:</b></span> ${magic_item.properties['description']}<br>
                        <span><b>Used By:</b></span> <i>${magic_item.properties['used_by']}</i>
                    </dd>

                </dl>
            </li>
        `
    )
}


export function append_html_tome(magic_item){
    $("#inv-tomes").append(
        `
            <li  id=magic-item-inv-${magic_item.uuid}>
                <dl>
                    <dt><u>${magic_item.properties['title']} - ${magic_item.properties['author']}</u> <a class="bi bi-x-circle-fill" id="magic-item-inv-rem-${magic_item.uuid}"></a></dt>
                    <i>${magic_item.properties['subheading']}</i><br>
                    <dd>
                        <span><b>Mythos Rating:</b></span> ${magic_item.properties['mythos_rating']}<br>
                        <span><b>Cthulhu Mythos:</b></span> ${magic_item.properties['cthulhu_mythos_initial']} - ${magic_item.properties['cthulhu_mythos_full']}<br>
                        <span><b>Language:</b></span> ${magic_item.properties['language']}<br>
                        <span><b>Sanity:</b></span> <i>${magic_item.properties['sanity']}</i>
                    </dd>

                </dl>
            </li>
        `
    )
}

export function append_html_occult_book(magic_item){
    $("#inv-tomes").append(
        `
            <li  id=magic-item-inv-${magic_item.uuid}>
                <dl>
                    <dt><u>${magic_item.properties['title']}</u> <a class="bi bi-x-circle-fill" id="magic-item-inv-rem-${magic_item.uuid}"></a></dt>
                    <i>${magic_item.properties['subheading']}</i><br>
                    <dd>
                        <span><b>Description:</b></span> ${magic_item.properties['description']}<br>
                        <span><b>Occult:</b></span> ${magic_item.properties['occult']}<br>
                        <span><b>Sanity:</b></span> <i>${magic_item.properties['sanity']}</i>
                    </dd>

                </dl>
            </li>
        `
    )
}

export function remove_magic_item_handler() {
    $("a[id^='magic-item-inv-rem-']").off().click(
        function (evt) {
            evt.preventDefault();
            let item_id = evt.target.id.replace("magic-item-inv-rem-", "");
            let object_id = "#magic-item-inv-" + item_id;
            let url_ = "inventory/" + item_id + "/remove";
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