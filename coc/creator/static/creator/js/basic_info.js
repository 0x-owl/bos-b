import { skills, flush_skills_columns, edit_skills_handler } from "/static/creator/js/skills.js";


export function post_basic_info(res) {
    let investigator = res.investigator;
    let occupations = res.occupations;
    $("#inv-name-inp").val(investigator['name']);
    $("#inv-sex-inp").val(investigator['sex']);
    $("#inv-age-inp").val(investigator['age']);
    $("#inv-birthplace-inp").val(investigator['birthplace']);
    $("#inv-residence-inp").val(investigator['residence']);
    $("#inv-player-inp").val(investigator['player']);
    flush_skills_columns();

    for (let occ of occupations) {
        if (occ[0] == investigator['occupation']) {
            $("#inv-occupation-inp").append(
                `<option value=${occ[0]} selected>${occ[1]}</option>`
            );
        } else {
            $("#inv-occupation-inp").append(
                `<option value=${occ[0]}>${occ[1]}</option>`
            );
        }
    }
    $.ajax({
        url: window.location.href + "/skills",
        success: function (res) {
            skills(res);
            edit_skills_handler();
        },
        error: function (res) {
            console.log(res);
        }
    })
};

export function get_basic_info(res) {
    let investigator = res.investigator;
    let occupations = res.occupations;
    let sexes = $("#inv-sex-inp option");
    $("#inv-name-inp").val(investigator['name']);
    $("#inv-age-inp").val(investigator['age']);
    $("#inv-birthplace-inp").val(investigator['birthplace']);
    $("#inv-residence-inp").val(investigator['residence']);
    $("#inv-player-inp").val(investigator['player']);
    for (let sex of sexes) {
        if (sex.value === investigator['sex']) {
            sex.selected = true;
        }
    }
    for (let occupation of occupations) {
        let occ_uuid = occupation[0];
        let occ_string = occupation[1];
        if (occ_uuid == investigator['occupation']) {
            $("#inv-occupation-inp").append(
                `<option value=${occ_uuid} selected>${occ_string}</option>`
            );
        } else {
            $("#inv-occupation-inp").append(
                `<option value=${occ_uuid}>${occ_string}</option>`
            );
        }
    }
}

export function get_portrait(res) {
    $("#inv-portrait").append(
        `<img class="rounded float-right img-thumbnail" src="${res.portrait}" alt="Investigator portrait">`
    )
}