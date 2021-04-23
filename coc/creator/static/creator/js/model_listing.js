export function list_model(res){
    //lists all records of the selected model on the sidebar
    for(let record of res.records_title){
        let detail_button  = $(`
        <button class="list-group-item" 
        data-bs-toggle="modal" 
        data-bs-target="#listingModal"
        value="${record[0]}">${record[1]}</button>`).appendTo('#mod-list')
        //creates a modal with the details of the clicked element
        detail_button.click(function(){
            $.ajaxSetup({ cache: false });
            $.ajax({
                url: "detail" + "/" + detail_button.val() + "/" + res.model_name,
                success: function (res) {
                    populate_detail_modal(res);
                },
                error: function (res) {
                    console.log(res);
                }
            })
        })
}}

function populate_detail_modal(detail_fields){
    //TODO: for now we are listing all record fields on the modal.But later we will need to prettify the modal so printing all fields will have to change.
    $('.modal-title').append(`${detail_fields.record[Object.keys(detail_fields.record)[0]]}`);
    for(let item in detail_fields.record){
        $('#listingModal .modal-body').append(`<div>${item}: ${detail_fields.record[item]}</div>`);
    }
}

$('#listingModal').on('hidden.bs.modal', function (e) {
   //empty the modal when closed
    $('.modal-title').empty();
    $('#listingModal .modal-body').empty()
  })


export function getListingData (url) {
    $.ajax({
        url: url,
        success: function (res) {
            list_model(res)
        },
        error: function (res) {
            console.log(res);
        }
    })
};


export function createOverlay(){
    //creates an overlay for the sidebar + disables buttons for listing
    $('.wrapper').append('<div class="overlay"></div>');
    $('.listing-btn').prop('disabled', true);
    $('.overlay').on('click', function(){
        //when the overlay is clicked it removes all appended elements of the sidebar and removes the overlay
        $('.overlay').remove();
        $('#mod-list').remove();
        $('#sidebar-header').remove()
        $('.listing-btn').prop('disabled', false);
    })
}
