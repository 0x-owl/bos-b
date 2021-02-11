export function skills(res) {
    let id_ = "#skills_1";;
    for (let inv_skill of res.skills) {
        let full_val = inv_skill[1] < 10 ? "0" + inv_skill[1] : inv_skill[1];
        let half_val = inv_skill[2] < 10 ? "0" + inv_skill[2] : inv_skill[2];
        let fifth_val = inv_skill[3] < 10 ? "0" + inv_skill[3] : inv_skill[3];
        let index_of = res.skills.indexOf(inv_skill);
        if (index_of === 0) {
            $("#inv-skills").append(
                `<div class="col" id="skills_1"></div>`
            );
        } else if (index_of === 35) {
            id_ = "#skills_2";
            $("#inv-skills").append(
                `<div class="col" id="skills_2"></div>`
            );
        }
        else if (index_of === 71) {
            id_ = "#skills_3";
            $("#inv-skills").append(
                `<div class="col" id="skills_3"></div>`
            );
        };
        $(id_).append(
            `
            <div class="row">
                <div class="col">
                    ${inv_skill[0]}:
                </div >
                <div style="text-align: right" class="col">
                    <b>${full_val}</b >|
                    <b>${half_val}</b > |
                    <b>${fifth_val}</b>
                </div >
            </div >`
        )
    }
}