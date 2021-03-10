export function flush_skills_columns() {
    $("#skills_1").remove();
    $("#skills_2").remove();
    $("#skills_3").remove();
    $("#inv-skills-submit").remove();
}

export function cleanse_skills() {
    let skills_inputs = $("input[id^='invsk-']");
    let data = {}
    for (let skill of skills_inputs) {
        data[skill.id.replace('invsk-', '')] = skill.value
    }
    return data
}



export function skills(res) {
    let id_ = "#skills_1";;
    flush_skills_columns();
    for (let inv_skill of res.skills) {
        let full_val = inv_skill[1] < 10 ? "0" + inv_skill[1] : inv_skill[1];
        let half_val = inv_skill[2] < 10 ? "0" + inv_skill[2] : inv_skill[2];
        let fifth_val = inv_skill[3] < 10 ? "0" + inv_skill[3] : inv_skill[3];
        let index_of = res.skills.indexOf(inv_skill);
        if (index_of === 0) {
            $("#inv-skills").append(
                `<div class="col" id="skills_1"></div>`
            );
        } else if (index_of === 36) {
            id_ = "#skills_2";
            $("#inv-skills").append(
                `<div class="col" id="skills_2"></div>`
            );
        }
        else if (index_of === 72) {
            id_ = "#skills_3";
            $("#inv-skills").append(
                `<div class="col" id="skills_3"></div>`
            );
        };
        $(id_).append(
            `
            <div style="text-align: right" class="input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text" style="width: 210px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" >${inv_skill[0]}:</span>
                </div>
                <input type="number" max=90 style="width: 70px;"class="form-control" id="invsk-${inv_skill[0]}" value=${full_val}>
                <input type="text" readonly class="form-control" value=${half_val == 0 ? "01" : half_val}>
                <input type="text" readonly class="form-control" value=${fifth_val == 0 ? "01" : fifth_val}>
            </div>
            <br>`
        )
    }
    $("#inv-skills").append(
        `<div id="inv-skills-submit" class="row">
            <input type="submit" class="btn btn-danger" value="Update">
        </div>`
    );
}