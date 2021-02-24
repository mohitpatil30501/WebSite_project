// Function
$(function () {
    $('[data-mask]').inputmask()
})
// Variable
var interest_no = 0;

// Socket
var loc = window.location
var wsStart = 'ws://'
if(loc.protocol == 'https:'){
    wsStart = 'wss://'
}
var endpoint = wsStart + loc.host + '/designation/' + data.designation.id
ssbtSocket = new ReconnectingWebSocket(endpoint)



// Socket Functions
ssbtSocket.onopen = function(e) {
    $("#loading").text('').addClass('d-none');
    $("#designation-div-form").removeClass('d-none');

    $("#designation").prop('readonly', false);
    $("#department").prop('readonly', false);
    $("#institute").prop('readonly', false);

    $("#subject_of_interest").prop('readonly', false);

    $("#degree").prop('readonly', false);
    $("#specialisation").prop('readonly', false);
    $("#university").prop('readonly', false);
    $("#academic-year").prop('readonly', false);
    $("#remarks").prop('readonly', false);

    $("#society").prop('readonly', false);
    $("#ist_no").prop('readonly', false);
    $("#date_of_membership").prop('readonly', false);

    $("#institute-name").prop('readonly', false);
    $("#institute-designation").prop('readonly', false);
    $("#institute-date_of_join").prop('readonly', false);
    $("#institute-date_of_leave").prop('readonly', false);

    $("#administrative-name").prop('readonly', false);
    $("#administrative-designation").prop('readonly', false);
    $("#administrative-date_of_join").prop('readonly', false);
    $("#administrative-date_of_leave").prop('readonly', false);

    $("#industry-name").prop('readonly', false);
    $("#industry-designation").prop('readonly', false);
    $("#industry-date_of_join").prop('readonly', false);
    $("#industry-date_of_leave").prop('readonly', false);

    $("#faculty-name").prop('readonly', false);
    $("#faculty-designation").prop('readonly', false);
    $("#faculty-date_of_approval").prop('readonly', false);

    // Startup
    if(interest_no == 0){
        for(subject of data.subject_of_interest){
            $("#subject_of_interest-id").val(subject.id)
            $("#subject_of_interest").val(subject.subject_of_interest)
            $("#subject_of_interest-add").click()
        }
    }
};

ssbtSocket.onclose = function(e) {
    $("#designation-div-form").addClass('d-none')
    $("#loading").text('Wait for connecting to Server').removeClass('d-none');

    $("#designation").prop('readonly', true);
    $("#department").prop('readonly', true);
    $("#institute").prop('readonly', true);

    $("#subject_of_interest").prop('readonly', true);

    $("#degree").prop('readonly', true);
    $("#specialisation").prop('readonly', true);
    $("#university").prop('readonly', true);
    $("#academic-year").prop('readonly', true);
    $("#remarks").prop('readonly', true);

    $("#society").prop('readonly', true);
    $("#ist_no").prop('readonly', true);
    $("#date_of_membership").prop('readonly', true);

    $("#institute-name").prop('readonly', true);
    $("#institute-designation").prop('readonly', true);
    $("#institute-date_of_join").prop('readonly', true);
    $("#institute-date_of_leave").prop('readonly', true);

    $("#administrative-name").prop('readonly', true);
    $("#administrative-designation").prop('readonly', true);
    $("#administrative-date_of_join").prop('readonly', true);
    $("#administrative-date_of_leave").prop('readonly', true);

    $("#industry-name").prop('readonly', true);
    $("#industry-designation").prop('readonly', true);
    $("#industry-date_of_join").prop('readonly', true);
    $("#industry-date_of_leave").prop('readonly', true);

    $("#faculty-name").prop('readonly', true);
    $("#faculty-designation").prop('readonly', true);
    $("#faculty-date_of_approval").prop('readonly', true);
};

ssbtSocket.onerror = function(e){
}

ssbtSocket.onmessage = function(e) {
    const data_received = JSON.parse(e.data);
    if(data_received['process'] === 'designation-form-submission'){
        if(data_received['status']){
            data.designation.designation = data_received['data']['designation']
            data.designation.department = data_received['data']['department']
            data.designation.institute = data_received['data']['institute']

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!')
        }
        $('#loading-animation').addClass('d-none')
        $("#designation-form-submit").prop('disabled', false).text('Save');
    }
    else if(data_received['process'] === 'subject_of_interest-form-submission'){
        if(data_received['status']){
            data.subject_of_interest.subject_of_interest = data_received['data']['subject_of_interest']

            if($("#interest-table").hasClass('d-none')){
                $("#interest-table").removeClass('d-none');
            }
            interest_no++;

            markup = '<tr>'+
                '<td> <input type="text" class="border-0 w-100 d-none" value="' + data_received['data']['id'] + '" id="interest-row-id-' + interest_no + '" readonly="true"> <input type="text" class="border-0 w-100 text-muted" value="' + data_received['data']['subject_of_interest'] + '" id="interest-row-subject_of_interest-' + interest_no + '" readonly="true"> </td>'+
                '<td>  <button type="button" class="btn btn-primary w-100" onclick="edit_subject_of_interest(' + interest_no + ')">Edit</button> </td>'+
                '</tr>';

            $("#interest-table-body").append(markup);
            $("#subject_of_interest-id").val('')
            $("#subject_of_interest").val('')
            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-subject_of_interest').addClass('d-none')
            $("#subject_of_interest-add").prop('disabled', false).text('Add');
    }
};

// Function
$(document).on('click', '#designation-form-submit', function(){
    $('#loading-animation-designation').removeClass('d-none')
    $("#designation-form-submit").prop('disabled', true).text('Saving...');

    if($("#designation").val() !== data.designation.designation || $("#department").val() !== data.designation.department || $("#institute").val() !== data.designation.institute){
        ssbtSocket.send(JSON.stringify({
            'process': 'designation-form-submission',
            'data':{
                'id': data.designation.id,
                'teacher': data.designation.teacher,
                'designation': $("#designation").val(),
                'department': $("#department").val(),
                'institute': $("#institute").val(),
            }
        }))
    }
    else{
        alert('Nothing is Changed to Save..!')
        $('#loading-animation-designation').addClass('d-none')
        $("#designation-form-submit").prop('disabled', false).text('Save');
    }
})

$(document).on('click', '#subject_of_interest-add', function(){
    $('#loading-animation-subject_of_interest').removeClass('d-none')
    $("#subject_of_interest-add").prop('disabled', true).text('Saving...');

    if($("#subject_of_interest").val() !== ''){
        if($("#subject_of_interest-id").val() === ''){
            ssbtSocket.send(JSON.stringify({
                'process': 'subject_of_interest-form-submission',
                'data':{
                    'id': data.designation.id,
                    'teacher': data.designation.teacher,
                    'subject_of_interest': $("#subject_of_interest").val(),
                }
            }))
        }
        else{
            if($("#interest-table").hasClass('d-none')){
                $("#interest-table").removeClass('d-none');
            }
            interest_no++;

            markup = '<tr>'+
                '<td> <input type="text" class="border-0 w-100 d-none" value="' + $("#subject_of_interest-id").val() + '" id="interest-row-id-' + interest_no + '" readonly="true"> <input type="text" class="border-0 w-100 text-muted" value="' + $("#subject_of_interest").val() + '" id="interest-row-subject_of_interest-' + interest_no + '" readonly="true"> </td>'+
                '<td> <button type="button" class="btn btn-primary w-100" onclick="edit_subject_of_interest(' + interest_no + ')">Edit</button> </td>'+
                '</tr>';

            $("#interest-table-body").append(markup);
            $("#subject_of_interest-id").val('')
            $("#subject_of_interest").val('')

            $('#loading-animation-subject_of_interest').addClass('d-none')
            $("#subject_of_interest-add").prop('disabled', false).text('Add');
        }
    }
    else{
        alert('Empty Field is not Allowed..!')
        $('#loading-animation-subject_of_interest').addClass('d-none')
        $("#subject_of_interest-add").prop('disabled', false).text('Add');
    }
})