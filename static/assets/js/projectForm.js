$(document).ready(function () {





    $("#form-wrapper").submit(function (event) {

        
        event.preventDefault();

        
        var formData = new FormData();
        formData.append('challenge', $('#challenge').val().trim());
        formData.append('dates', $('#dates').val().trim());
        formData.append('moreExplain', $('#moreExplain').val().trim());
        formData.append('results', $('#results').val().trim());
        formData.append('prjRequirements', $('#prjRequirements').val().trim());
        formData.append('wyLike', $('#wyLike').val().trim());
        formData.append('limits', $('#limits').val().trim());
        formData.append('goals', $('#goals').val().trim());
        formData.append('measurement', $('#measurement').val().trim());
        formData.append('audience', $('#audience').val().trim());
        formData.append('problems', $('#problems').val().trim());
        formData.append('introduction', $('#introduction').val().trim());
        formData.append('connection', $('#connection').val().trim());
        

        $.ajax({
            url: 'projectConfirm',
            headers: {
                "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
            },
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function (data) {
                console.log(data);
            },
            error: function (data){
                console.log("error");
            }
        }); // end ajax
    });
});





// function create_post() {
//     console.log("create post is working!"); // sanity checks

//     $.ajaxSetup({
//         headers: {
//             "X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()
//           },
//     });
//     $.ajax({
//         type : "POST", 
//         url: 'projectConfirm',
        
//         //data: $('#form-wrapper').serialize(),
//         data: {
//             challenge : $('#challenge').val(),
//             dates : $('#dates').val(),
//             moreExplain : $('#moreExplain').val(),
//             results : $('#results').val(),
//             prjRequirements : $('#prjRequirements').val(),
//             wyLike : $('#wyLike').val(),
//             limits : $('#limits').val(),
//             goals : $('#goals').val(),
//             measurement : $('#measurement').val(),
//             audience : $('#audience').val(),
//             problems : $('#problems').val(),
//             introduction : $('#introduction').val(),
//             connection : $('#introduction').val(),

//             //  csrfmiddlewaretoken: '{{ csrf_token }}',
//             //csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
//             //  dataType: "json",    
//         },
//         dataType: "json",
//         success : function(json) {
//             //$('#post-text').val(''); // remove the value from the input
//             console.log(json); // log the returned json to the console
//             console.log("success"); // another sanity check
//         },

//         // handle a non-successful response
//         error : function(xhr,errmsg,err) {
//             $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
//                 " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
//             console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//         }
//     });

//     console.log($('#challenge').val());
// };