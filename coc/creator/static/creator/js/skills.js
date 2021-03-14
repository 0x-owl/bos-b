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
                <input type="number" readonly max=90 style="width: 70px;"class="form-control" id="invsk-${inv_skill[0]}" value=${full_val}>
                <input type="text" readonly class="form-control" value=${half_val == 0 ? "01" : half_val}>
                <input type="text" readonly class="form-control" value=${fifth_val == 0 ? "01" : fifth_val}>
            </div>
            <br>`
        )
    }
    // updating skill value logic
    $("input[id^='invsk-']").change(
        function (evt) {
            let inp = $("#" + evt.target.id)[0];
            let val = inp.valueAsNumber;
            let skill_name = evt.target.id.replace('invsk-', '');
            if (inp.readOnly === false) {
                var csrftoken = $("[name=csrfmiddlewaretoken]").val();
                let data = {};
                data[skill_name] = val;
                let url_ = window.location.pathname + "/skill_update";
                $.ajax({
                    url: url_,
                    type: "POST",
                    data: data,
                    beforeSend: function (xhr, settings) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    },
                    success: function (res) {
                        let skill = Object.keys(res)[0];
                        let ids_ = "#invsk-" + skill;
                        $(ids_).val(res[skill][0])
                        let siblings = $(ids_).siblings("input");
                        siblings[0].value = res[skill][1];
                        siblings[1].value = res[skill][2];
                    },
                    error: function (res) {
                        console.log(res)
                    }
                })
            }
        }
    );
    // edit button logic for skills
    $("#inv-skills-edit").click(
        function (evt) {
            if ($("#inv-skills-edit")[0].innerHTML === `<i class="bi bi-unlock"></i>`) {
                $("input[id*='invsk-']").prop('readonly', false);
                $("#inv-skills-reset").removeClass('disabled');
                $("#inv-skills-shuffle").removeClass('disabled');
                $("#inv-skills-edit")[0].innerHTML = `<i class="bi bi-lock"></i>`
            } else {
                $("input[id*='invsk-']").prop('readonly', true);
                $("#inv-skills-reset").addClass('disabled');
                $("#inv-skills-shuffle").addClass('disabled');
                $("#inv-skills-edit")[0].innerHTML = `<i class="bi bi-unlock"></i>`
            }
        }
    )
}