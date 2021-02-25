// Function
$(function () {
    $('[data-mask]').inputmask()
})
// Variable
var interest_no = 0;
var academics_no = 0;
var memberships_no = 0;
var institutes_no = 0;
var administratives_no = 0;
var industrys_no = 0;
var facultys_no = 0;

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
    $("#academics-year").prop('readonly', false);
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
    if(academics_no == 0){
        for(academic of data.academics){
            $("#academics-id").val(academic.id)

            $("#degree").val(academic.degree),
            $("#specialisation").val(academic.specialisation),
            $("#university").val(academic.university),
            $("#academics-year").val(academic.year),
            $("#remarks").val(academic.remarks),

            $("#academics-add").click()
        }
    }

    if(memberships_no == 0){
        for(membership of data.memberships){
            $("#membership-id").val(membership.id)

            $("#society").val(membership.society),
            $("#ist_no").val(membership.ist_no),
            $("#date_of_membership").val(membership.date_of_membership),

            $("#membership-add").click()
        }
    }

    if(institutes_no == 0){
        for(institute of data.institutes){
            $("#institute-id").val(institute.id)

            $("#institute-name").val(institute.name),
            $("#institute-designation").val(institute.designation),
            $("#institute-date_of_join").val(institute.date_of_join),
            $("#institute-date_of_leave").val(institute.date_of_leave),

            $("#institute-add").click()
        }
    }

    if(administratives_no == 0){
        for(administrative of data.administratives){
            $("#administrative-id").val(administrative.id)

            $("#administrative-name").val(administrative.name),
            $("#administrative-designation").val(administrative.designation),
            $("#administrative-date_of_join").val(administrative.date_of_join),
            $("#administrative-date_of_leave").val(administrative.date_of_leave),

            $("#administrative-add").click()
        }
    }

    if(industrys_no == 0){
        for(industry of data.industrys){
            $("#industry-id").val(industry.id)

            $("#industry-name").val(industry.name),
            $("#industry-designation").val(industry.designation),
            $("#industry-date_of_join").val(industry.date_of_join),
            $("#industry-date_of_leave").val(industry.date_of_leave),

            $("#industry-add").click()
        }
    }

    if(facultys_no == 0){
        for(faculty of data.facultys){
            $("#faculty-id").val(faculty.id)

            $("#faculty-name").val(faculty.name),
            $("#faculty-designation").val(faculty.designation),
            $("#faculty-date_of_approval").val(faculty.date_of_approval),

            $("#faculty-add").click()
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
    $("#academics-year").prop('readonly', true);
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
        $('#loading-animation-designation').addClass('d-none')
        $("#designation-form-submit").prop('disabled', false).text('Save');
    }
    else if(data_received['process'] === 'subject_of_interest-form-submission'){
        if(data_received['status']){
            data.subject_of_interest.subject_of_interest = data_received['data']['subject_of_interest']

            table_subject_of_interest(data_received['data']['id'], data_received['data']['subject_of_interest'])

            scrollToBottom($("#interest-table-box"), $("#interest-table-main"));

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-subject_of_interest').addClass('d-none')
            $("#subject_of_interest-add").prop('disabled', false).text('Add');
    }
    else if(data_received['process'] === 'academics-form-submission'){
        if(data_received['status']){
            data.academics.degree = data_received['data']['degree']
            data.academics.specialisation = data_received['data']['specialisation']
            data.academics.university = data_received['data']['university']
            data.academics.year = data_received['data']['year']
            data.academics.remarks = data_received['data']['remarks']

            table_academics(data_received['data']['id'], data_received['data']['degree'], data_received['data']['specialisation'], data_received['data']['university'], data_received['data']['year'], data_received['data']['remarks'])

            scrollToBottom($("#academics-table-box"), $("#academics-table-main"));

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-academics').addClass('d-none')
            $("#academics-add").prop('disabled', false).text('Add');
    }
    else if(data_received['process'] === 'membership-form-submission'){
        if(data_received['status']){
            data.memberships.society = data_received['data']['society']
            data.memberships.ist_no = data_received['data']['ist_no']
            data.memberships.date_of_membership = data_received['data']['date_of_membership']

            table_memberships(data_received['data']['id'], data_received['data']['society'], data_received['data']['ist_no'], data_received['data']['date_of_membership'])

            scrollToBottom($("#membership-table-box"), $("#membership-table-main"));

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-membership').addClass('d-none')
            $("#membership-add").prop('disabled', false).text('Add');
    }
    else if(data_received['process'] === 'institute-form-submission'){
        if(data_received['status']){
            data.institutes.name = data_received['data']['name']
            data.institutes.designation = data_received['data']['designation']
            data.institutes.date_of_join = data_received['data']['date_of_join']
            data.institutes.date_of_leave = data_received['data']['date_of_leave']

            table_institutes(data_received['data']['id'], data_received['data']['name'], data_received['data']['designation'], data_received['data']['date_of_join'], data_received['data']['date_of_leave'])

            scrollToBottom($("#institute-table-box"), $("#institute-table-main"));

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-institute').addClass('d-none')
            $("#institute-add").prop('disabled', false).text('Add');
    }
    else if(data_received['process'] === 'administrative-form-submission'){
        if(data_received['status']){
            data.administratives.name = data_received['data']['name']
            data.administratives.designation = data_received['data']['designation']
            data.administratives.date_of_join = data_received['data']['date_of_join']
            data.administratives.date_of_leave = data_received['data']['date_of_leave']

            table_administratives(data_received['data']['id'], data_received['data']['name'], data_received['data']['designation'], data_received['data']['date_of_join'], data_received['data']['date_of_leave'])

            scrollToBottom($("#administrative-table-box"), $("#administrative-table-main"));

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-administrative').addClass('d-none')
            $("#administrative-add").prop('disabled', false).text('Add');
    }
    else if(data_received['process'] === 'industry-form-submission'){
        if(data_received['status']){
            data.industrys.name = data_received['data']['name']
            data.industrys.designation = data_received['data']['designation']
            data.industrys.date_of_join = data_received['data']['date_of_join']
            data.industrys.date_of_leave = data_received['data']['date_of_leave']

            table_industrys(data_received['data']['id'], data_received['data']['name'], data_received['data']['designation'], data_received['data']['date_of_join'], data_received['data']['date_of_leave'])

            scrollToBottom($("#industry-table-box"), $("#industry-table-main"));

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-industry').addClass('d-none')
            $("#industry-add").prop('disabled', false).text('Add');
    }
    else if(data_received['process'] === 'faculty-form-submission'){
        if(data_received['status']){
            data.facultys.name = data_received['data']['name']
            data.facultys.designation = data_received['data']['designation']
            data.facultys.date_of_approval = data_received['data']['date_of_approval']

            table_facultys(data_received['data']['id'], data_received['data']['name'], data_received['data']['designation'], data_received['data']['date_of_approval'])

            scrollToBottom($("#faculty-table-box"), $("#faculty-table-main"));

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-faculty').addClass('d-none')
            $("#faculty-add").prop('disabled', false).text('Add');
    }

    else if(data_received['process'] === 'subject_of_interest-edit'){
        if(data_received['status']){
            var no = data_received['data']['row']
            $("#interest-row-id-" + no.toString()).val(data_received['data']['id']),
            $("#interest-row-subject_of_interest-" + no.toString()).val(data_received['data']['subject_of_interest']),

            data.subject_of_interest[no - 1].subject_of_interest = data_received['data']['subject_of_interest']

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $("#interest-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
    }
    else if(data_received['process'] === 'academics-edit'){
        if(data_received['status']){
            var no = data_received['data']['row']
            $("#academics-row-id-" + no.toString()).val(data_received['data']['id']),
            $("#academics-row-degree-" + no.toString()).val(data_received['data']['degree']),
            $("#academics-row-specialisation-" + no.toString()).val(data_received['data']['specialisation']),
            $("#academics-row-university-" + no.toString()).val(data_received['data']['university']),
            $("#academics-row-year-" + no.toString()).val(data_received['data']['year']),
            $("#academics-row-remarks-" + no.toString()).val(data_received['data']['remarks']),

            data.academics[no - 1].degree = data_received['data']['degree']
            data.academics[no - 1].specialisation = data_received['data']['specialisation']
            data.academics[no - 1].university = data_received['data']['university']
            data.academics[no - 1].year = data_received['data']['year']
            data.academics[no - 1].remarks = data_received['data']['remarks']

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $("#academics-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
    }
    else if(data_received['process'] === 'membership-edit'){
        if(data_received['status']){
            var no = data_received['data']['row']
            $("#membership-row-id-" + no.toString()).val(data_received['data']['id']),
            $("#membership-row-society-" + no.toString()).val(data_received['data']['degree']),
            $("#membership-row-ist_no-" + no.toString()).val(data_received['data']['specialisation']),
            $("#membership-row-date_of_membership-" + no.toString()).val(data_received['data']['university']),

            data.memberships[no - 1].society = data_received['data']['society']
            data.memberships[no - 1].ist_no = data_received['data']['ist_no']
            data.memberships[no - 1].date_of_membership = data_received['data']['date_of_membership']

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $("#membership-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
    }
    else if(data_received['process'] === 'institute-edit'){
        if(data_received['status']){
            var no = data_received['data']['row']
            $("#institute-row-id-" + no.toString()).val(data_received['data']['id']),
            $("#institute-row-name-" + no.toString()).val(data_received['data']['name']),
            $("#institute-row-designation-" + no.toString()).val(data_received['data']['designation']),
            $("#institute-row-date_of_join-" + no.toString()).val(data_received['data']['date_of_join']),
            $("#institute-row-date_of_leave-" + no.toString()).val(data_received['data']['date_of_leave']),

            data.institutes[no - 1].name = data_received['data']['name']
            data.institutes[no - 1].designation = data_received['data']['designation']
            data.institutes[no - 1].date_of_join = data_received['data']['date_of_join']
            data.institutes[no - 1].date_of_leave = data_received['data']['date_of_leave']

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $("#institute-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
    }
    else if(data_received['process'] === 'administrative-edit'){
        if(data_received['status']){
            var no = data_received['data']['row']
            $("#administrative-row-id-" + no.toString()).val(data_received['data']['id']),
            $("#administrative-row-name-" + no.toString()).val(data_received['data']['name']),
            $("#administrative-row-designation-" + no.toString()).val(data_received['data']['designation']),
            $("#administrative-row-date_of_join-" + no.toString()).val(data_received['data']['date_of_join']),
            $("#administrative-row-date_of_leave-" + no.toString()).val(data_received['data']['date_of_leave']),

            data.administratives[no - 1].name = data_received['data']['name']
            data.administratives[no - 1].designation = data_received['data']['designation']
            data.administratives[no - 1].date_of_join = data_received['data']['date_of_join']
            data.administratives[no - 1].date_of_leave = data_received['data']['date_of_leave']

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $("#administrative-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
    }
    else if(data_received['process'] === 'industry-edit'){
        if(data_received['status']){
            var no = data_received['data']['row']
            $("#industry-row-id-" + no.toString()).val(data_received['data']['id']),
            $("#industry-row-name-" + no.toString()).val(data_received['data']['name']),
            $("#industry-row-designation-" + no.toString()).val(data_received['data']['designation']),
            $("#industry-row-date_of_join-" + no.toString()).val(data_received['data']['date_of_join']),
            $("#industry-row-date_of_leave-" + no.toString()).val(data_received['data']['date_of_leave']),

            data.industrys[no - 1].name = data_received['data']['name']
            data.industrys[no - 1].designation = data_received['data']['designation']
            data.industrys[no - 1].date_of_join = data_received['data']['date_of_join']
            data.industrys[no - 1].date_of_leave = data_received['data']['date_of_leave']

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $("#industry-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
    }
    else if(data_received['process'] === 'faculty-edit'){
        if(data_received['status']){
            var no = data_received['data']['row']
            $("#faculty-row-id-" + no.toString()).val(data_received['data']['id']),
            $("#faculty-row-name-" + no.toString()).val(data_received['data']['name']),
            $("#faculty-row-designation-" + no.toString()).val(data_received['data']['designation']),
            $("#faculty-row-date_of_approval-" + no.toString()).val(data_received['data']['date_of_approval']),

            data.facultys[no - 1].name = data_received['data']['name']
            data.facultys[no - 1].designation = data_received['data']['designation']
            data.facultys[no - 1].date_of_approval = data_received['data']['date_of_approval']

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $("#faculty-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
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
            table_subject_of_interest($("#subject_of_interest-id").val(), $("#subject_of_interest").val())

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

$(document).on('click', '#academics-add', function(){
    $('#loading-animation-academics').removeClass('d-none')
    $("#academics-add").prop('disabled', true).text('Saving...');

    if($("#degree").val() !== '' && $("#specialisation").val() !== '' && $("#university").val() !== '' && $("#academics-year").val() !== '' && $("#remarks").val() !== ''){
        if($("#academics-id").val() === ''){
            ssbtSocket.send(JSON.stringify({
                'process': 'academics-form-submission',
                'data':{
                    'id': data.designation.id,
                    'teacher': data.designation.teacher,
                    'degree': $("#degree").val(),
                    'specialisation': $("#specialisation").val(),
                    'university': $("#university").val(),
                    'year': $("#academics-year").val(),
                    'remarks': $("#remarks").val(),
                }
            }))
        }
        else{
            table_academics($("#academics-id").val(), $("#degree").val(), $("#specialisation").val(), $("#university").val(), $("#academics-year").val(), $("#remarks").val())

            $('#loading-animation-academics').addClass('d-none')
            $("#academics-add").prop('disabled', false).text('Add');
        }
    }
    else{
        alert('Empty Field is not Allowed..!')
        $('#loading-animation-academics').addClass('d-none')
        $("#academics-add").prop('disabled', false).text('Add');
    }
})

$(document).on('click', '#membership-add', function(){
    $('#loading-animation-membership').removeClass('d-none')
    $("#membership-add").prop('disabled', true).text('Saving...');

    if($("#society").val() !== '' && $("#ist_no").val() !== '' && $("#date_of_membership").val() !== ''){
        if($("#membership-id").val() === ''){
            ssbtSocket.send(JSON.stringify({
                'process': 'membership-form-submission',
                'data':{
                    'id': data.designation.id,
                    'teacher': data.designation.teacher,
                    'society': $("#society").val(),
                    'ist_no': $("#ist_no").val(),
                    'date_of_membership': $("#date_of_membership").val(),
                }
            }))
        }
        else{
            table_memberships($("#membership-id").val(), $("#society").val(), $("#ist_no").val(), $("#date_of_membership").val())

            $('#loading-animation-membership').addClass('d-none')
            $("#membership-add").prop('disabled', false).text('Add');
        }
    }
    else{
        alert('Empty Field is not Allowed..!')
        $('#loading-animation-membership').addClass('d-none')
        $("#membership-add").prop('disabled', false).text('Add');
    }
})

$(document).on('click', '#institute-add', function(){
    $('#loading-animation-institute').removeClass('d-none')
    $("#institute-add").prop('disabled', true).text('Saving...');

    if($("#institute-name").val() !== '' && $("#institute-designation").val() !== '' && $("#institute-date_of_join").val() !== ''){
        if($("#institute-id").val() === ''){
            if($("#institute-date_of_leave").val() === ''){
                var date_of_leave = "Ongoing"
            }
            else{
                var date_of_leave = $("#institute-date_of_leave").val()
            }
            ssbtSocket.send(JSON.stringify({
                'process': 'institute-form-submission',
                'data':{
                    'id': data.designation.id,
                    'teacher': data.designation.teacher,
                    'name': $("#institute-name").val(),
                    'designation': $("#institute-designation").val(),
                    'date_of_join': $("#institute-date_of_join").val(),
                    'date_of_leave': date_of_leave,
                }
            }))
        }
        else{
            table_institutes($("#institute-id").val(), $("#institute-name").val(), $("#institute-designation").val(), $("#institute-date_of_join").val(), $("#institute-date_of_leave").val())

            $('#loading-animation-institute').addClass('d-none')
            $("#institute-add").prop('disabled', false).text('Add');
        }
    }
    else{
        alert('Empty Field is not Allowed..!')
        $('#loading-animation-institute').addClass('d-none')
        $("#institute-add").prop('disabled', false).text('Add');
    }
})

$(document).on('click', '#administrative-add', function(){
    $('#loading-animation-administrative').removeClass('d-none')
    $("#administrative-add").prop('disabled', true).text('Saving...');

    if($("#administrative-name").val() !== '' && $("#administrative-designation").val() !== '' && $("#administrative-date_of_join").val() !== ''){
        if($("#administrative-id").val() === ''){
            if($("#administrative-date_of_leave").val() === ''){
                var date_of_leave = "Ongoing"
            }
            else{
                var date_of_leave = $("#administrative-date_of_leave").val()
            }
            ssbtSocket.send(JSON.stringify({
                'process': 'administrative-form-submission',
                'data':{
                    'id': data.designation.id,
                    'teacher': data.designation.teacher,
                    'name': $("#administrative-name").val(),
                    'designation': $("#administrative-designation").val(),
                    'date_of_join': $("#administrative-date_of_join").val(),
                    'date_of_leave': date_of_leave,
                }
            }))
        }
        else{
            table_administratives($("#administrative-id").val(), $("#administrative-name").val(), $("#administrative-designation").val(), $("#administrative-date_of_join").val(), $("#administrative-date_of_leave").val())

            $('#loading-animation-administrative').addClass('d-none')
            $("#administrative-add").prop('disabled', false).text('Add');
        }
    }
    else{
        alert('Empty Field is not Allowed..!')
        $('#loading-animation-administrative').addClass('d-none')
        $("#administrative-add").prop('disabled', false).text('Add');
    }
})

$(document).on('click', '#industry-add', function(){
    $('#loading-animation-industry').removeClass('d-none')
    $("#industry-add").prop('disabled', true).text('Saving...');

    if($("#industry-name").val() !== '' && $("#industry-designation").val() !== '' && $("#industry-date_of_join").val() !== ''){
        if($("#industry-id").val() === ''){
            if($("#industry-date_of_leave").val() === ''){
                var date_of_leave = "Ongoing"
            }
            else{
                var date_of_leave = $("#industry-date_of_leave").val()
            }
            ssbtSocket.send(JSON.stringify({
                'process': 'industry-form-submission',
                'data':{
                    'id': data.designation.id,
                    'teacher': data.designation.teacher,
                    'name': $("#industry-name").val(),
                    'designation': $("#industry-designation").val(),
                    'date_of_join': $("#industry-date_of_join").val(),
                    'date_of_leave': date_of_leave,
                }
            }))
        }
        else{
            table_industrys($("#industry-id").val(), $("#industry-name").val(), $("#industry-designation").val(), $("#industry-date_of_join").val(), $("#industry-date_of_leave").val())

            $('#loading-animation-industry').addClass('d-none')
            $("#industry-add").prop('disabled', false).text('Add');
        }
    }
    else{
        alert('Empty Field is not Allowed..!')
        $('#loading-animation-industry').addClass('d-none')
        $("#industry-add").prop('disabled', false).text('Add');
    }
})

$(document).on('click', '#faculty-add', function(){
    $('#loading-animation-faculty').removeClass('d-none')
    $("#faculty-add").prop('disabled', true).text('Saving...');

    if($("#faculty-name").val() !== '' && $("#faculty-designation").val() !== '' && $("#faculty-date_of_approval").val() !== ''){
        if($("#faculty-id").val() === ''){
            ssbtSocket.send(JSON.stringify({
                'process': 'faculty-form-submission',
                'data':{
                    'id': data.designation.id,
                    'teacher': data.designation.teacher,
                    'name': $("#faculty-name").val(),
                    'designation': $("#faculty-designation").val(),
                    'date_of_approval': $("#faculty-date_of_approval").val(),
                }
            }))
        }
        else{
            table_facultys($("#faculty-id").val(), $("#faculty-name").val(), $("#faculty-designation").val(), $("#faculty-date_of_approval").val())

            $('#loading-animation-faculty').addClass('d-none')
            $("#faculty-add").prop('disabled', false).text('Add');
        }
    }
    else{
        alert('Empty Field is not Allowed..!')
        $('#loading-animation-faculty').addClass('d-none')
        $("#faculty-add").prop('disabled', false).text('Add');
    }
})


// Scroll Down table
function scrollToBottom(box, table) {
   box.scrollTop(table.height());
}

// Table fuction
function table_subject_of_interest(id, subject_of_interest){
    if($("#interest-table").hasClass('d-none')){
        $("#interest-table").removeClass('d-none');
    }
    interest_no++;

    markup = '<tr>'+
        '<td> <input type="text" class="border-0 w-100 d-none" value="' + id + '" id="interest-row-id-' + interest_no + '" readonly="true">'+
        '<input type="text" class="border-0 w-100 text-muted" value="' + subject_of_interest + '" id="interest-row-subject_of_interest-' + interest_no + '" readonly="true"> </td>'+
        '<td> <button type="button" class="btn btn-primary w-100" id="interest-row-button-' + interest_no + '" onclick="edit_subject_of_interest(' + interest_no + ')" value="Edit">Edit</button> </td>'+
        '</tr>';

    $("#interest-table-body").append(markup)
    $("#subject_of_interest-id").val('')
    $("#subject_of_interest").val('')
}

function table_academics(id, degree, specialisation, university, year, remarks){
    if($("#academics-table").hasClass('d-none')){
        $("#academics-table").removeClass('d-none');
    }
    academics_no++;

    markup = '<tr>'+
        '<td> <input type="text" class="border-0 w-100 d-none" value="' + id + '" id="academics-row-id-' + academics_no + '" readonly="true">'+
        '<input type="text" class="border-0 w-100 text-muted" value="' + degree + '" id="academics-row-degree-' + academics_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + specialisation + '" id="academics-row-specialisation-' + academics_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + university + '" id="academics-row-university-' + academics_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + year + '" id="academics-row-year-' + academics_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + remarks + '" id="academics-row-remarks-' + academics_no + '" readonly="true"> </td>'+
        '<td> <button type="button" class="btn btn-primary w-100" id="academics-row-button-' + academics_no + '" onclick="edit_academics(' + academics_no + ')" value="Edit">Edit</button> </td>'+
        '</tr>';

    $("#academics-table-body").append(markup)
    $("#academics-id").val('')
    $("#degree").val('')
    $("#specialisation").val('')
    $("#university").val('')
    $("#academics-year").val('')
    $("#remarks").val('')
}

function table_memberships(id, society, ist_no, date_of_membership){
    if($("#membership-table").hasClass('d-none')){
        $("#membership-table").removeClass('d-none');
    }
    memberships_no++;

    markup = '<tr>'+
        '<td> <input type="text" class="border-0 w-100 d-none" value="' + id + '" id="membership-row-id-' + memberships_no + '" readonly="true">'+
        '<input type="text" class="border-0 w-100 text-muted" value="' + society + '" id="membership-row-society-' + memberships_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + ist_no + '" id="membership-row-ist_no-' + memberships_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + date_of_membership + '" id="membership-row-date_of_membership-' + memberships_no + '" readonly="true"> </td>'+
        '<td> <button type="button" class="btn btn-primary w-100" id="membership-row-button-' + memberships_no + '" onclick="edit_membership(' + memberships_no + ')" value="Edit">Edit</button> </td>'+
        '</tr>';

    $("#membership-table-body").append(markup)
    $("#membership-id").val('')
    $("#society").val('')
    $("#ist_no").val('')
    $("#date_of_membership").val('')
}

function table_institutes(id, name, designation, date_of_join, date_of_leave){
    if(date_of_leave === ''){
        date_of_leave = "Ongoing"
    }

    if($("#institute-table").hasClass('d-none')){
        $("#institute-table").removeClass('d-none');
    }
    institutes_no++;

    markup = '<tr>'+
        '<td> <input type="text" class="border-0 w-100 d-none" value="' + id + '" id="institute-row-id-' + institutes_no + '" readonly="true">'+
        '<input type="text" class="border-0 w-100 text-muted" value="' + name + '" id="institute-row-name-' + institutes_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + designation + '" id="institute-row-designation-' + institutes_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + date_of_join + '" id="institute-row-date_of_join-' + institutes_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + date_of_leave + '" id="institute-row-date_of_leave-' + institutes_no + '" readonly="true"> </td>'+
        '<td> <button type="button" class="btn btn-primary w-100" id="institute-row-button-' + institutes_no + '" onclick="edit_institute(' + institutes_no + ')" value="Edit">Edit</button> </td>'+
        '</tr>';

    $("#institute-table-body").append(markup)
    $("#institute-id").val('')
    $("#institute-name").val('')
    $("#institute-designation").val('')
    $("#institute-date_of_join").val('')
    $("#institute-date_of_leave").val('')
}

function table_administratives(id, name, designation, date_of_join, date_of_leave){
    if(date_of_leave === ''){
        date_of_leave = "Ongoing"
    }

    if($("#administrative-table").hasClass('d-none')){
        $("#administrative-table").removeClass('d-none');
    }
    administratives_no++;

    markup = '<tr>'+
        '<td> <input type="text" class="border-0 w-100 d-none" value="' + id + '" id="administrative-row-id-' + administratives_no + '" readonly="true">'+
        '<input type="text" class="border-0 w-100 text-muted" value="' + name + '" id="administrative-row-name-' + administratives_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + designation + '" id="administrative-row-designation-' + administratives_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + date_of_join + '" id="administrative-row-date_of_join-' + administratives_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + date_of_leave + '" id="administrative-row-date_of_leave-' + administratives_no + '" readonly="true"> </td>'+
        '<td> <button type="button" class="btn btn-primary w-100" id="administrative-row-button-' + administratives_no + '" onclick="edit_administrative(' + administratives_no + ')" value="Edit">Edit</button> </td>'+
        '</tr>';

    $("#administrative-table-body").append(markup)
    $("#administrative-id").val('')
    $("#administrative-name").val('')
    $("#administrative-designation").val('')
    $("#administrative-date_of_join").val('')
    $("#administrative-date_of_leave").val('')
}

function table_industrys(id, name, designation, date_of_join, date_of_leave){
    if(date_of_leave === ''){
        date_of_leave = "Ongoing"
    }

    if($("#industry-table").hasClass('d-none')){
        $("#industry-table").removeClass('d-none');
    }
    industrys_no++;

    markup = '<tr>'+
        '<td> <input type="text" class="border-0 w-100 d-none" value="' + id + '" id="industry-row-id-' + industrys_no + '" readonly="true">'+
        '<input type="text" class="border-0 w-100 text-muted" value="' + name + '" id="industry-row-name-' + industrys_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + designation + '" id="industry-row-designation-' + industrys_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + date_of_join + '" id="industry-row-date_of_join-' + industrys_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + date_of_leave + '" id="industry-row-date_of_leave-' + industrys_no + '" readonly="true"> </td>'+
        '<td> <button type="button" class="btn btn-primary w-100" id="industry-row-button-' + industrys_no + '" onclick="edit_industry(' + industrys_no + ')" value="Edit">Edit</button> </td>'+
        '</tr>';

    $("#industry-table-body").append(markup)
    $("#industry-id").val('')
    $("#industry-name").val('')
    $("#industry-designation").val('')
    $("#industry-date_of_join").val('')
    $("#industry-date_of_leave").val('')
}

function table_facultys(id, name, designation, date_of_approval){
    if($("#faculty-table").hasClass('d-none')){
        $("#faculty-table").removeClass('d-none');
    }
    facultys_no++;

    markup = '<tr>'+
        '<td> <input type="text" class="border-0 w-100 d-none" value="' + id + '" id="faculty-row-id-' + facultys_no + '" readonly="true">'+
        '<input type="text" class="border-0 w-100 text-muted" value="' + name + '" id="faculty-row-name-' + facultys_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + designation + '" id="faculty-row-designation-' + facultys_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + date_of_approval + '" id="faculty-row-date_of_approval-' + facultys_no + '" readonly="true"> </td>'+
        '<td> <button type="button" class="btn btn-primary w-100" id="faculty-row-button-' + facultys_no + '" onclick="edit_faculty(' + facultys_no + ')" value="Edit">Edit</button> </td>'+
        '</tr>';

    $("#faculty-table-body").append(markup)
    $("#faculty-id").val('')
    $("#faculty-name").val('')
    $("#faculty-designation").val('')
    $("#faculty-date_of_approval").val('')
}

// Edit function
function edit_subject_of_interest(no){
    if($("#interest-row-button-" + no.toString()).val() === "Edit"){
        $("#interest-row-subject_of_interest-" + no.toString()).prop('readonly', false).removeClass('text-muted');

        $("#interest-row-button-" + no.toString()).text('Save').val('Save').removeClass('btn-primary').addClass('btn-success');
    }
    else if($("#interest-row-button-" + no.toString()).val() === "Save"){
        if($("#interest-row-subject_of_interest-" + no.toString()).val() !== ''){
            if($("#interest-row-subject_of_interest-" + no.toString()).val() !== data.subject_of_interest[no - 1].subject_of_interest){
                $("#interest-row-subject_of_interest-" + no.toString()).prop('readonly', true).addClass('text-muted');

                $("#interest-row-button-" + no.toString()).text('Saving...').prop('disabled', true);

                ssbtSocket.send(JSON.stringify({
                    'process': 'subject_of_interest-edit',
                    'data':{
                        'teacher': data.designation.teacher,
                        'id': $("#interest-row-id-" + no.toString()).val(),
                        'subject_of_interest': $("#interest-row-subject_of_interest-" + no.toString()).val(),
                        'row': no,
                    }
                }))
            }
            else{
                alert("Nothing is changed..!")
                $("#interest-row-subject_of_interest-" + no.toString()).prop('readonly', true).addClass('text-muted');
                $("#interest-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
            }
        }
        else{
            alert("Empty field Not Allowed..!")
        }
    }
}

function edit_academics(no){
    if($("#academics-row-button-" + no.toString()).val() === "Edit"){
        $("#academics-row-degree-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#academics-row-specialisation-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#academics-row-university-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#academics-row-year-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#academics-row-remarks-" + no.toString()).prop('readonly', false).removeClass('text-muted');

        $("#academics-row-button-" + no.toString()).text('Save').val('Save').removeClass('btn-primary').addClass('btn-success');
    }
    else if($("#academics-row-button-" + no.toString()).val() === "Save"){
        if($("#academics-row-degree-" + no.toString()).val() !== '' && $("#academics-row-specialisation-" + no.toString()).val() !== '' && $("#academics-row-university-" + no.toString()).val() !== '' && $("#academics-row-year-" + no.toString()).val() !== '' && $("#academics-row-remarks-" + no.toString()).val() !== ''){

            $("#academics-row-degree-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#academics-row-specialisation-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#academics-row-university-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#academics-row-year-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#academics-row-remarks-" + no.toString()).prop('readonly', true).addClass('text-muted');


            if($("#academics-row-degree-" + no.toString()).val() !== data.academics[no - 1].degree || $("#academics-row-specialisation-" + no.toString()).val() !== data.academics[no - 1].specialisation || $("#academics-row-university-" + no.toString()).val() !== data.academics[no - 1].university || $("#academics-row-year-" + no.toString()).val() !== data.academics[no - 1].year || $("#academics-row-remarks-" + no.toString()).val() !== data.academics[no - 1].remarks){
                $("#academics-row-button-" + no.toString()).text('Saving...').prop('disabled', true);

                ssbtSocket.send(JSON.stringify({
                    'process': 'academics-edit',
                    'data':{
                        'teacher': data.designation.teacher,
                        'id': $("#academics-row-id-" + no.toString()).val(),
                        'degree': $("#academics-row-degree-" + no.toString()).val(),
                        'specialisation': $("#academics-row-specialisation-" + no.toString()).val(),
                        'university': $("#academics-row-university-" + no.toString()).val(),
                        'year': $("#academics-row-year-" + no.toString()).val(),
                        'remarks': $("#academics-row-remarks-" + no.toString()).val(),
                        'row': no,
                    }
                }))
            }
            else{
                alert("Nothing is changed..!")
                $("#academics-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
            }
        }
        else{
            alert("Empty field Not Allowed..!")
        }
    }
}

function edit_membership(no){
    if($("#membership-row-button-" + no.toString()).val() === "Edit"){
        $("#membership-row-society-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#membership-row-ist_no-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#membership-row-date_of_membership-" + no.toString()).prop('readonly', false).removeClass('text-muted');

        $("#membership-row-button-" + no.toString()).text('Save').val('Save').removeClass('btn-primary').addClass('btn-success');
    }
    else if($("#membership-row-button-" + no.toString()).val() === "Save"){
        if($("#membership-row-society-" + no.toString()).val() !== '' && $("#membership-row-ist_no-" + no.toString()).val() !== '' && $("#membership-row-date_of_membership-" + no.toString()).val() !== ''){

            $("#membership-row-society-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#membership-row-ist_no-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#membership-row-date_of_membership-" + no.toString()).prop('readonly', true).addClass('text-muted');


            if($("#membership-row-society-" + no.toString()).val() !== data.memberships[no - 1].society || $("#membership-row-ist_no-" + no.toString()).val() !== data.memberships[no - 1].ist_no || $("#membership-row-date_of_membership-" + no.toString()).val() !== data.memberships[no - 1].date_of_membership){

                $("#membership-row-button-" + no.toString()).text('Saving...').prop('disabled', true);

                ssbtSocket.send(JSON.stringify({
                    'process': 'academics-edit',
                    'data':{
                        'teacher': data.designation.teacher,
                        'id': $("#membership-row-id-" + no.toString()).val(),
                        'society': $("#membership-row-society-" + no.toString()).val(),
                        'ist_no': $("#membership-row-ist_no-" + no.toString()).val(),
                        'date_of_membership': $("#membership-row-date_of_membership-" + no.toString()).val(),
                        'row': no,
                    }
                }))
            }
            else{
                alert("Nothing is changed..!")
                $("#membership-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
            }
        }
        else{
            alert("Empty field Not Allowed..!")
        }
    }
}

function edit_institute(no){
    if($("#institute-row-button-" + no.toString()).val() === "Edit"){
        $("#institute-row-name-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#institute-row-designation-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#institute-row-date_of_join-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#institute-row-date_of_leave-" + no.toString()).prop('readonly', false).removeClass('text-muted');

        $("#institute-row-button-" + no.toString()).text('Save').val('Save').removeClass('btn-primary').addClass('btn-success');
    }
    else if($("#institute-row-button-" + no.toString()).val() === "Save"){
        if($("#institute-row-name-" + no.toString()).val() !== '' && $("#institute-row-designation-" + no.toString()).val() !== '' && $("#institute-row-date_of_join-" + no.toString()).val() !== '' && $("#institute-row-date_of_leave-" + no.toString()).val() !== ''){

            $("#institute-row-name-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#institute-row-designation-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#institute-row-date_of_join-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#institute-row-date_of_leave-" + no.toString()).prop('readonly', true).addClass('text-muted');

            if($("#institute-row-name-" + no.toString()).val() !== data.institutes[no - 1].name || $("#academics-row-designation-" + no.toString()).val() !== data.institutes[no - 1].designation || $("#academics-row-date_of_join-" + no.toString()).val() !== data.institutes[no - 1].date_of_join || $("#academics-row-date_of_leave-" + no.toString()).val() !== data.institutes[no - 1].date_of_leave){
                $("#institute-row-button-" + no.toString()).text('Saving...').prop('disabled', true);

                ssbtSocket.send(JSON.stringify({
                    'process': 'institute-edit',
                    'data':{
                        'teacher': data.designation.teacher,
                        'id': $("#institute-row-id-" + no.toString()).val(),
                        'name': $("#institute-row-name-" + no.toString()).val(),
                        'designation': $("#institute-row-designation-" + no.toString()).val(),
                        'date_of_join': $("#institute-row-date_of_join-" + no.toString()).val(),
                        'date_of_leave': $("#institute-row-date_of_leave-" + no.toString()).val(),
                        'row': no,
                    }
                }))
            }
            else{
                alert("Nothing is changed..!")
                $("#institute-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
            }
        }
        else{
            alert("Empty field Not Allowed..!")
        }
    }
}

function edit_administrative(no){
    if($("#administrative-row-button-" + no.toString()).val() === "Edit"){
        $("#administrative-row-name-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#administrative-row-designation-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#administrative-row-date_of_join-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#administrative-row-date_of_leave-" + no.toString()).prop('readonly', false).removeClass('text-muted');

        $("#administrative-row-button-" + no.toString()).text('Save').val('Save').removeClass('btn-primary').addClass('btn-success');
    }
    else if($("#administrative-row-button-" + no.toString()).val() === "Save"){
        if($("#administrative-row-name-" + no.toString()).val() !== '' && $("#administrative-row-designation-" + no.toString()).val() !== '' && $("#administrative-row-date_of_join-" + no.toString()).val() !== '' && $("#administrative-row-date_of_leave-" + no.toString()).val() !== ''){

            $("#administrative-row-name-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#administrative-row-designation-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#administrative-row-date_of_join-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#administrative-row-date_of_leave-" + no.toString()).prop('readonly', true).addClass('text-muted');

            if($("#administrative-row-name-" + no.toString()).val() !== data.administratives[no - 1].name || $("#administrative-row-designation-" + no.toString()).val() !== data.administratives[no - 1].designation || $("#administrative-row-date_of_join-" + no.toString()).val() !== data.administratives[no - 1].date_of_join || $("#administrative-row-date_of_leave-" + no.toString()).val() !== data.administratives[no - 1].date_of_leave){
                $("#administrative-row-button-" + no.toString()).text('Saving...').prop('disabled', true);

                ssbtSocket.send(JSON.stringify({
                    'process': 'administrative-edit',
                    'data':{
                        'teacher': data.designation.teacher,
                        'id': $("#administrative-row-id-" + no.toString()).val(),
                        'name': $("#administrative-row-name-" + no.toString()).val(),
                        'designation': $("#administrative-row-designation-" + no.toString()).val(),
                        'date_of_join': $("#administrative-row-date_of_join-" + no.toString()).val(),
                        'date_of_leave': $("#administrative-row-date_of_leave-" + no.toString()).val(),
                        'row': no,
                    }
                }))
            }
            else{
                alert("Nothing is changed..!")
                $("#administrative-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
            }
        }
        else{
            alert("Empty field Not Allowed..!")
        }
    }
}

function edit_industry(no){
    if($("#industry-row-button-" + no.toString()).val() === "Edit"){
        $("#industry-row-name-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#industry-row-designation-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#industry-row-date_of_join-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#industry-row-date_of_leave-" + no.toString()).prop('readonly', false).removeClass('text-muted');

        $("#industry-row-button-" + no.toString()).text('Save').val('Save').removeClass('btn-primary').addClass('btn-success');
    }
    else if($("#industry-row-button-" + no.toString()).val() === "Save"){
        if($("#industry-row-name-" + no.toString()).val() !== '' && $("#industry-row-designation-" + no.toString()).val() !== '' && $("#industry-row-date_of_join-" + no.toString()).val() !== '' && $("#industry-row-date_of_leave-" + no.toString()).val() !== ''){

            $("#industry-row-name-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#industry-row-designation-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#industry-row-date_of_join-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#industry-row-date_of_leave-" + no.toString()).prop('readonly', true).addClass('text-muted');

            if($("#industry-row-name-" + no.toString()).val() !== data.industrys[no - 1].name || $("#industry-row-designation-" + no.toString()).val() !== data.industrys[no - 1].designation || $("#industry-row-date_of_join-" + no.toString()).val() !== data.industrys[no - 1].date_of_join || $("#industry-row-date_of_leave-" + no.toString()).val() !== data.industrys[no - 1].date_of_leave){
                $("#industry-row-button-" + no.toString()).text('Saving...').prop('disabled', true);

                ssbtSocket.send(JSON.stringify({
                    'process': 'industry-edit',
                    'data':{
                        'teacher': data.designation.teacher,
                        'id': $("#industry-row-id-" + no.toString()).val(),
                        'name': $("#industry-row-name-" + no.toString()).val(),
                        'designation': $("#industry-row-designation-" + no.toString()).val(),
                        'date_of_join': $("#industry-row-date_of_join-" + no.toString()).val(),
                        'date_of_leave': $("#industry-row-date_of_leave-" + no.toString()).val(),
                        'row': no,
                    }
                }))
            }
            else{
                alert("Nothing is changed..!")
                $("#industry-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
            }
        }
        else{
            alert("Empty field Not Allowed..!")
        }
    }
}

function edit_faculty(no){
    if($("#faculty-row-button-" + no.toString()).val() === "Edit"){
        $("#faculty-row-name-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#faculty-row-designation-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#faculty-row-date_of_approval-" + no.toString()).prop('readonly', false).removeClass('text-muted');

        $("#faculty-row-button-" + no.toString()).text('Save').val('Save').removeClass('btn-primary').addClass('btn-success');
    }
    else if($("#faculty-row-button-" + no.toString()).val() === "Save"){
        if($("#faculty-row-name-" + no.toString()).val() !== '' && $("#faculty-row-designation-" + no.toString()).val() !== '' && $("#faculty-row-date_of_approval-" + no.toString()).val() !== ''){

            $("#faculty-row-name-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#faculty-row-designation-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#faculty-row-date_of_approval-" + no.toString()).prop('readonly', true).addClass('text-muted');

            if($("#faculty-row-name-" + no.toString()).val() !== data.facultys[no - 1].name || $("#faculty-row-designation-" + no.toString()).val() !== data.facultys[no - 1].designation || $("#faculty-row-date_of_approval-" + no.toString()).val() !== data.facultys[no - 1].date_of_approval){
                $("#faculty-row-button-" + no.toString()).text('Saving...').prop('disabled', true);

                ssbtSocket.send(JSON.stringify({
                    'process': 'faculty-edit',
                    'data':{
                        'teacher': data.designation.teacher,
                        'id': $("#faculty-row-id-" + no.toString()).val(),
                        'name': $("#faculty-row-name-" + no.toString()).val(),
                        'designation': $("#faculty-row-designation-" + no.toString()).val(),
                        'date_of_approval': $("#faculty-row-date_of_approval-" + no.toString()).val(),
                        'row': no,
                    }
                }))
            }
            else{
                alert("Nothing is changed..!")
                $("#faculty-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
            }
        }
        else{
            alert("Empty field Not Allowed..!")
        }
    }
}
