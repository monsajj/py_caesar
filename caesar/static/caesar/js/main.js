$(document).ready(function(){

    $(".btn-decrypt").click(function(){
        $.ajax({
            url: urlDecryptText,
            type: 'get',
            data: {
                decryption_text: $('#decryption_text').val()
            },
            success: function(response) {
                $("#decrypted_text").text(response.decrypted_text)
            }
        })
    })

})
