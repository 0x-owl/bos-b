export function get_arcane(res) {
    for (let spell of res.spells) {
        $("#inv-spells").append(
            `
                <li>
                    <dl>
                        <dt><u>${spell.name}</u> (${spell.cost})</dt>
                        <dd>
                            <span><b>Casting Time:</b></span> ${spell.casting_time}<br>
                            <span><b>Desc.:</b></span> ${spell.description}<br>
                            <span><b>Deeper Magic:</b></span>${spell.deeper_magic}<br>
                            <span><b>Alt Names:</b></span> <i>${spell.alternative_names}</i>
                        </dd>

                    </dl>
                </li>
            `
        )
    }

    for (let artifact of res.artifacts) {
        $("#inv-artifacts").append(
            `<li>${artifact}</li>`
        )
    }
    $("#inv-encounters").after(
        `<p>${res.encounters}</p>`
    )
}