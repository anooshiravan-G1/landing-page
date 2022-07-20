$(document).ready(function () {





    $("#form-wrapper").submit(function (event) {

        
        event.preventDefault();

        
        var formData = new FormData();
        formData.append('pName', $('#pName').val().trim());
        formData.append('cName', $('#cName').val().trim());
        formData.append('bName', $('#bName').val().trim());
        formData.append('service', $('#service').val().trim());
        formData.append('wPhone', $('#wPhone').val().trim());
        formData.append('pPhone', $('#pPhone').val().trim());
        formData.append('email', $('#email').val().trim());
        formData.append('sAddress', $('#sAddress').val().trim());
        formData.append('bExplain', $('#bExplain').val().trim());
        formData.append('gExplain', $('#gExplain').val().trim());
        formData.append('nameInLogo', $('#nameInLogo').val().trim());
        formData.append('tags', $('#tags').val().trim());
        formData.append('isdExplain', $('#isdExplain').val().trim());
        formData.append('isd', $('#isd').val().trim());
        formData.append('usage', $('#usage').val().trim());
        formData.append('recommendation', $('#recommendation').val().trim());
        formData.append('logoType', $('#logoType').val().trim());
        formData.append('colorType', $('#colorType').val().trim());
        formData.append('example', $('#example').val().trim());
        formData.append('logomotion', $('#logomotion').val().trim());
        formData.append('budget', $('#budget').val().trim());
        

        $.ajax({
            url: 'logoConfirm',
            headers: {
                "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
            },
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function (data) {
                //console.log(data);
            },
            error: function (data){
                //console.log("error");
            }
        }); // end ajax
    });
});
