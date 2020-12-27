$(document).ready(function() {

    $('.shareButton').on('click', function(e) {
        $('#modal').fadeIn();
        e.preventDefault();
    });
    
    $('#closeModal').click((e) => {
        $('#modal').fadeOut();
        e.preventDefault();
    });

    $('#copyToClipBoardButton').click((e) => {
        let $inputValue = $('#shareLinkInput').select().val();
        document.execCommand("copy", false, $inputValue);
        
        e.preventDefault();
    });

});

