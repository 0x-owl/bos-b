export function parse_deriv_attrs(res) {
    let investigator = res.investigator;
    $("#inv-health-inp").val(investigator['health']);
    $("#inv-mp-inp").val(investigator['magic_points']);
    $("#inv-sanity-inp").val(investigator['sanity']);
    $("#inv-luck-inp").val(investigator['luck']);
}