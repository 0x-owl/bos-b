export function manias_phobias(res) {
    $("#inv-phobias").append(
        function () {
            for (let phobia in res.phobias) {
                `<li>${phobia[1]}</li>`
            }
        }
    )
    $("#inv-manias").append(
        function () {
            for (let mania in res.manias) {
                `<li>${mania[1]}</li>`
            }
        }
    )
}