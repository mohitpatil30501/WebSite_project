$(function () {
    $('[data-mask]').inputmask()
})

// Scroll Down table
function scrollToBottom(box, table) {
   box.scrollTop(table.height());
}

// Variable
var publications_book_no = 0;
var publications_journal_no = 0;
var publications_paper_no = 0;
var sttps_no = 0;
var workshops_no = 0;
var oiis_no = 0;
var consultancys_no = 0;
var awards_no = 0;
var projects_no = 0;
var ecas_no = 0;

// Socket
var loc = window.location
var wsStart = 'ws://'
if(loc.protocol == 'https:'){
    wsStart = 'wss://'
}
var endpoint = wsStart + loc.host + '/activity/' + data.designation.id
ssbtSocket = new ReconnectingWebSocket(endpoint)


// Socket Functions
ssbtSocket.onopen = function(e) {
    $("#loading").text('').addClass('d-none');
    $("#activity-form").removeClass('d-none');

    $("#book-name").prop('readonly', false);
    $("#book-publication").prop('readonly', false);
    $("#book-year").prop('readonly', false);

    $("#journal-name").prop('readonly', false);
    $("#journal-title").prop('readonly', false);
    $("#journal-publication").prop('readonly', false);
    $("#journal-page").prop('readonly', false);
    $("#journal-year").prop('readonly', false);
    $("#journal-url").prop('readonly', false);
    $("#journal-level-national").prop('disabled', false);
    $("#journal-level-international").prop('disabled', false);

    $("#paper-name").prop('readonly', false);
    $("#paper-title").prop('readonly', false);
    $("#paper-publication").prop('readonly', false);
    $("#paper-year").prop('readonly', false);
    $("#paper-url").prop('readonly', false);
    $("#paper-level-state").prop('disabled', false);
    $("#paper-level-national").prop('disabled', false);
    $("#paper-level-international").prop('disabled', false);

    $("#sttp-name").prop('readonly', false);
    $("#sttp-organization").prop('readonly', false);
    $("#sttp-date_form").prop('readonly', false);
    $("#sttp-date_to").prop('readonly', false);
    $("#sttp-day").prop('readonly', false);

    $("#workshops-name").prop('readonly', false);
    $("#workshops-organization").prop('readonly', false);
    $("#workshops-date_form").prop('readonly', false);
    $("#workshops-date_to").prop('readonly', false);
    $("#workshops-days").prop('readonly', false);

    $("#oii-organization").prop('readonly', false);
    $("#oii-year").prop('readonly', false);
    $("#oii-invitee-visiting_faculty").prop('disabled', false);
    $("#oii-invitee-examiner").prop('disabled', false);
    $("#oii-invitee-supervisor").prop('disabled', false);
    $("#oii-invitee-expert").prop('disabled', false);

    $("#consultancy-organization").prop('readonly', false);
    $("#consultancy-year").prop('readonly', false);
    $("#consultancy-work_done").prop('readonly', false);
    $("#consultancy-cost").prop('readonly', false);

    $("#award-organization").prop('readonly', false);
    $("#award-year").prop('readonly', false);
    $("#award-title").prop('readonly', false);

    $("#project-name").prop('readonly', false);
    $("#project-year").prop('readonly', false);
    $("#project-level-ug").prop('disabled', false);
    $("#project-level-pg").prop('disabled', false);
    $("#project-level-phd").prop('disabled', false);

    $("#eca-name").prop('readonly', false);
    $("#eca-year").prop('readonly', false);

    // Startup
    if(publications_book_no == 0){
        for(book of data.publications_book){
            $("#book-id").val(book.id)

            $("#book-name").val(book.name)
            $("#book-publication").val(book.publication)
            $("#book-year").val(book.year)

            $("#book-add").click()
        }
    }

    if(publications_journal_no == 0){
        for(journal of data.publications_journal){
            $("#journal-id").val(journal.id)

            $("#journal-name").val(journal.name)
            $("#journal-title").val(journal.title)
            $("#journal-publication").val(journal.publication)
            $("#journal-page").val(journal.page)
            $("#journal-year").val(journal.year)
            $("#journal-url").val(journal.url)
            if($("#journal-level-national").val() === journal.level){
                $("#journal-level-national").prop('checked', true)
            }
            else if($("#journal-level-international").val() === journal.level){
                $("#journal-level-international").prop('checked', true)
            }
            else{
                $("#journal-level-national").prop('checked', true)
            }

            $("#journal-add").click()
        }
    }

    if(publications_paper_no == 0){
        for(paper of data.publications_paper){
            $("#paper-id").val(paper.id)

            $("#paper-name").val(paper.name)
            $("#paper-title").val(paper.title)
            $("#paper-publication").val(paper.publication)
            $("#paper-year").val(paper.year)
            $("#paper-url").val(paper.url)
            if($("#paper-level-state").val() === paper.level){
                $("#paper-level-state").prop('checked', true)
            }
            else if($("#paper-level-national").val() === paper.level){
                $("#paper-level-national").prop('checked', true)
            }
            else if($("#paper-level-international").val() === paper.level){
                $("#paper-level-international").prop('checked', true)
            }
            else{
                $("#paper-level-state").prop('checked', true)
            }

            $("#paper-add").click()
        }
    }

    if(sttps_no == 0){
        for(sttp of data.sttps){
            $("#sttp-id").val(sttp.id)

            $("#sttp-name").val(sttp.name)
            $("#sttp-organization").val(sttp.organization)
            $("#sttp-date_form").val(sttp.date_form)
            $("#sttp-date_to").val(sttp.date_to)
            $("#sttp-day").val(sttp.day)

            $("#sttp-add").click()
        }
    }

    if(workshops_no == 0){
        for(workshop of data.workshops){
            $("#workshops-id").val(workshop.id)

            $("#workshops-name").val(workshop.name)
            $("#workshops-organization").val(workshop.organization)
            $("#workshops-date_form").val(workshop.date_form)
            $("#workshops-date_to").val(workshop.date_to)
            $("#workshops-days").val(workshop.day)

            $("#workshops-add").click()
        }
    }

    if(oiis_no == 0){
        for(oii of data.oiis){
            $("#oii-id").val(oii.id)

            $("#oii-organization").val(oii.organization)
            $("#oii-year").val(oii.year)

            if($("#oii-invitee-visiting_faculty").val() === oii.invitee){
                $("#oii-invitee-visiting_faculty").prop('checked', true)
            }
            else if($("#oii-invitee-examiner").val() === oii.invitee){
                $("#oii-invitee-examiner").prop('checked', true)
            }
            else if($("#oii-invitee-supervisor").val() === oii.invitee){
                $("#oii-invitee-supervisor").prop('checked', true)
            }
            else if($("#oii-invitee-expert").val() === oii.invitee){
                $("#oii-invitee-expert").prop('checked', true)
            }
            else{
                $("#oii-invitee-visiting_faculty").prop('checked', true)
            }

            $("#oii-add").click()
        }
    }

    if(consultancys_no == 0){
        for(consultancy of data.consultancys){
            $("#consultancy-id").val(consultancy.id)

            $("#consultancy-organization").val(consultancy.organization)
            $("#consultancy-year").val(consultancy.year)
            $("#consultancy-work_done").val(consultancy.work_done)
            $("#consultancy-cost").val(consultancy.cost)

            $("#consultancy-add").click()
        }
    }

    if(awards_no == 0){
        for(award of data.awards){
            $("#award-id").val(award.id)

            $("#award-organization").val(award.organization)
            $("#award-year").val(award.year)
            $("#award-title").val(award.title)

            $("#award-add").click()
        }
    }

    if(projects_no == 0){
        for(project of data.projects){
            $("#project-id").val(project.id)

            $("#project-name").val(project.name)
            $("#project-year").val(project.year)
            if($("#project-level-ug").val() === project.level){
                $("#project-level-ug").prop('checked', true)
            }
            else if($("#project-level-pg").val() === project.level){
                $("#project-level-pg").prop('checked', true)
            }
            else if($("#project-level-phd").val() === project.level){
                $("#project-level-phd").prop('checked', true)
            }
            else{
                $("#project-level-state").prop('checked', true)
            }

            $("#project-add").click()
        }
    }

    if(ecas_no == 0){
        for(eca of data.ecas){
            $("#eca-id").val(eca.id)

            $("#eca-name").val(project.name)
            $("#eca-year").val(project.year)

            $("#eca-add").click()
        }
    }

};

ssbtSocket.onclose = function(e) {
    $("#activity-form").addClass('d-none')
    $("#loading").text('Wait for connecting to Server').removeClass('d-none');

    $("#book-name").prop('readonly', true);
    $("#book-publication").prop('readonly', true);
    $("#book-year").prop('readonly', true);

    $("#journal-name").prop('readonly', true);
    $("#journal-title").prop('readonly', true);
    $("#journal-publication").prop('readonly', true);
    $("#journal-page").prop('readonly', true);
    $("#journal-year").prop('readonly', true);
    $("#journal-url").prop('readonly', true);
    $("#journal-level-national").prop('disabled', true);
    $("#journal-level-international").prop('disabled', true);

    $("#paper-name").prop('readonly', true);
    $("#paper-title").prop('readonly', true);
    $("#paper-publication").prop('readonly', true);
    $("#paper-year").prop('readonly', true);
    $("#paper-url").prop('readonly', true);
    $("#paper-level-state").prop('disabled', true);
    $("#paper-level-national").prop('disabled', true);
    $("#paper-level-international").prop('disabled', true);

    $("#sttp-name").prop('readonly', true);
    $("#sttp-organization").prop('readonly', true);
    $("#sttp-date_form").prop('readonly', true);
    $("#sttp-date_to").prop('readonly', true);
    $("#sttp-day").prop('readonly', true);

    $("#workshops-name").prop('readonly', true);
    $("#workshops-organization").prop('readonly', true);
    $("#workshops-date_form").prop('readonly', true);
    $("#workshops-date_to").prop('readonly', true);
    $("#workshops-days").prop('readonly', true);

    $("#oii-organization").prop('readonly', true);
    $("#oii-year").prop('readonly', true);
    $("#oii-invitee-visiting_faculty").prop('disabled', true);
    $("#oii-invitee-examiner").prop('disabled', true);
    $("#oii-invitee-supervisor").prop('disabled', true);
    $("#oii-invitee-expert").prop('disabled', true);

    $("#consultancy-organization").prop('readonly', true);
    $("#consultancy-year").prop('readonly', true);
    $("#consultancy-work_done").prop('readonly', true);
    $("#consultancy-cost").prop('readonly', true);

    $("#award-organization").prop('readonly', true);
    $("#award-year").prop('readonly', true);
    $("#award-title").prop('readonly', true);

    $("#project-name").prop('readonly', true);
    $("#project-year").prop('readonly', true);
    $("#project-level-ug").prop('disabled', true);
    $("#project-level-pg").prop('disabled', true);
    $("#project-level-phd").prop('disabled', true);

    $("#eca-name").prop('readonly', true);
    $("#eca-year").prop('readonly', true);
};

ssbtSocket.onerror = function(e){
}

ssbtSocket.onmessage = function(e) {
    const data_received = JSON.parse(e.data);
    if(data_received['process'] === 'publications_book-form-submission'){
        if(data_received['status']){
            data.publications_book.push({
                'name' : data_received['data']['name'],
                'publication' : data_received['data']['publication'],
                'year' : data_received['data']['year']
            })

            table_publications_book(data_received['data']['id'], data_received['data']['name'], data_received['data']['publication'], data_received['data']['year'])

            scrollToBottom($("#book-table-box"), $("#book-table-main"));

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-book').addClass('d-none')
            $("#book-add").prop('disabled', false).text('Add');
    }
    else if(data_received['process'] === 'publications_journal-form-submission'){
        if(data_received['status']){
            data.publications_journal.push({
                    'name' : data_received['data']['name'],
                    'title' : data_received['data']['title'],
                    'publication' : data_received['data']['publication'],
                    'page' : data_received['data']['page'],
                    'year' : data_received['data']['year'],
                    'url' : data_received['data']['url'],
                    'level' : data_received['data']['level'],
                })

            table_publications_journal(data_received['data']['id'], data_received['data']['name'], data_received['data']['title'], data_received['data']['publication'], data_received['data']['page'], data_received['data']['year'], data_received['data']['url'], data_received['data']['level'],)

            scrollToBottom($("#journal-table-box"), $("#journal-table-main"));

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-journal').addClass('d-none')
            $("#journal-add").prop('disabled', false).text('Add');
    }
    else if(data_received['process'] === 'publications_paper-form-submission'){
        if(data_received['status']){
            data.publications_paper.push({
                    'name' : data_received['data']['name'],
                    'title' : data_received['data']['title'],
                    'publication' : data_received['data']['publication'],
                    'year' : data_received['data']['year'],
                    'url' : data_received['data']['url'],
                    'level' : data_received['data']['level'],
                })

            table_publications_paper(data_received['data']['id'], data_received['data']['name'], data_received['data']['title'], data_received['data']['publication'], data_received['data']['year'], data_received['data']['url'], data_received['data']['level'],)


            scrollToBottom($("#paper-table-box"), $("#paper-table-main"));

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-paper').addClass('d-none')
            $("#paper-add").prop('disabled', false).text('Add');
    }
    else if(data_received['process'] === 'sttps-form-submission'){
        if(data_received['status']){
            data.sttps.push({
                    'name' : data_received['data']['name'],
                    'organization' : data_received['data']['organization'],
                    'year' : data_received['data']['year'],
                    'date_form' : data_received['data']['date_form'],
                    'date_to' : data_received['data']['date_to'],
                    'day' : data_received['data']['day'],
                })

            table_sttps(data_received['data']['id'], data_received['data']['name'], data_received['data']['organization'], data_received['data']['year'], data_received['data']['date_form'], data_received['data']['date_to'], data_received['data']['day'],)

            scrollToBottom($("#sttp-table-box"), $("#sttp-table-main"));

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-sttp').addClass('d-none')
            $("#sttp-add").prop('disabled', false).text('Add');
    }
    else if(data_received['process'] === 'workshops-form-submission'){
        if(data_received['status']){
            data.workshops.push({
                    'name' : data_received['data']['name'],
                    'organization' : data_received['data']['organization'],
                    'year' : data_received['data']['year'],
                    'date_form' : data_received['data']['date_form'],
                    'date_to' : data_received['data']['date_to'],
                    'day' : data_received['data']['day'],
                })

            table_workshops(data_received['data']['id'], data_received['data']['name'], data_received['data']['organization'], data_received['data']['year'], data_received['data']['date_form'], data_received['data']['date_to'], data_received['data']['day'],)

            scrollToBottom($("#workshops-table-box"), $("#workshops-table-main"));

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-workshops').addClass('d-none')
            $("#workshops-add").prop('disabled', false).text('Add');
    }
    else if(data_received['process'] === 'oiis-form-submission'){
        if(data_received['status']){
            data.oiis.push({
                    'organization' : data_received['data']['organization'],
                    'year' : data_received['data']['year'],
                    'invitee' : data_received['data']['invitee'],
                })
            data.oiis.organization = data_received['data']['organization']
            data.oiis.year = data_received['data']['year']
            data.oiis.invitee = data_received['data']['invitee']

            table_oiis(data_received['data']['id'], data_received['data']['organization'], data_received['data']['year'], data_received['data']['invitee'],)

            scrollToBottom($("#oii-table-box"), $("#oii-table-main"));

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-oii').addClass('d-none')
            $("#oii-add").prop('disabled', false).text('Add');
    }
    else if(data_received['process'] === 'consultancys-form-submission'){
        if(data_received['status']){
            data.consultancys.push({
                    'organization' : data_received['data']['organization'],
                    'year' : data_received['data']['year'],
                    'work_done' : data_received['data']['work_done'],
                    'cost' : data_received['data']['cost'],
                })
            table_consultancys(data_received['data']['id'], data_received['data']['organization'], data_received['data']['year'], data_received['data']['work_done'], data_received['data']['cost'],)

            scrollToBottom($("#consultancy-table-box"), $("#consultancy-table-main"));

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-consultancy').addClass('d-none')
            $("#consultancy-add").prop('disabled', false).text('Add');
    }
    else if(data_received['process'] === 'awards-form-submission'){
        if(data_received['status']){
            data.awards.push({
                    'organization' : data_received['data']['organization'],
                    'year' : data_received['data']['year'],
                    'title' : data_received['data']['title'],
                })

            table_awards(data_received['data']['id'], data_received['data']['organization'], data_received['data']['year'], data_received['data']['title'],)

            scrollToBottom($("#award-table-box"), $("#award-table-main"));

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-award').addClass('d-none')
            $("#award-add").prop('disabled', false).text('Add');
    }
    else if(data_received['process'] === 'projects-form-submission'){
        if(data_received['status']){
            data.projects.push({
                    'name' : data_received['data']['name'],
                    'year' : data_received['data']['year'],
                    'level' : data_received['data']['level'],
                })

            table_projects(data_received['data']['id'], data_received['data']['name'], data_received['data']['year'], data_received['data']['level'],)

            scrollToBottom($("#project-table-box"), $("#project-table-main"));

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-project').addClass('d-none')
            $("#project-add").prop('disabled', false).text('Add');
    }
    else if(data_received['process'] === 'ecas-form-submission'){
        if(data_received['status']){
            data.ecas.push({
                    'name' : data_received['data']['name'],
                    'year' : data_received['data']['year'],
                })

            table_ecas(data_received['data']['id'], data_received['data']['name'], data_received['data']['year'],)

            scrollToBottom($("#eca-table-box"), $("#eca-table-main"));

            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $('#loading-animation-eca').addClass('d-none')
            $("#eca-add").prop('disabled', false).text('Add');
    }

    else if(data_received['process'] === 'publications_book-edit'){
        var no = data_received['data']['row']
        if(data_received['status']){
            $("#book-row-id-" + no.toString()).val(data_received['data']['id']),
            $("#book-row-name-" + no.toString()).val(data_received['data']['name']),
            $("#book-row-publication-" + no.toString()).val(data_received['data']['publication']),
            $("#book-row-year-" + no.toString()).val(data_received['data']['year'])

            data.publications_book[no - 1].name = data_received['data']['name']
            data.publications_book[no - 1].publication = data_received['data']['publication']
            data.publications_book[no - 1].year = data_received['data']['year']
            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $("#book-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
    }
    else if(data_received['process'] === 'publications_journal-edit'){
        var no = data_received['data']['row']
        if(data_received['status']){
            $("#journal-row-id-" + no.toString()).val(data_received['data']['id']),
            $("#journal-row-name-" + no.toString()).val(data_received['data']['name']),
            $("#journal-row-title-" + no.toString()).val(data_received['data']['title']),
            $("#journal-row-publication-" + no.toString()).val(data_received['data']['publication']),
            $("#journal-row-page-" + no.toString()).val(data_received['data']['page']),
            $("#journal-row-year-" + no.toString()).val(data_received['data']['year'])
            $("#journal-row-url-" + no.toString()).val(data_received['data']['url'])
            $("#journal-row-level-" + no.toString()).val(data_received['data']['level'])

            data.publications_journal[no - 1].name = data_received['data']['name']
            data.publications_journal[no - 1].title = data_received['data']['title']
            data.publications_journal[no - 1].publication = data_received['data']['publication']
            data.publications_journal[no - 1].page = data_received['data']['page']
            data.publications_journal[no - 1].year = data_received['data']['year']
            data.publications_journal[no - 1].url = data_received['data']['url']
            data.publications_journal[no - 1].level = data_received['data']['level']
            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $("#journal-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
    }
    else if(data_received['process'] === 'publications_paper-edit'){
        var no = data_received['data']['row']
        if(data_received['status']){
            $("#paper-row-id-" + no.toString()).val(data_received['data']['id']),
            $("#paper-row-name-" + no.toString()).val(data_received['data']['name']),
            $("#paper-row-title-" + no.toString()).val(data_received['data']['title']),
            $("#paper-row-publication-" + no.toString()).val(data_received['data']['publication']),
            $("#paper-row-year-" + no.toString()).val(data_received['data']['year'])
            $("#paper-row-url-" + no.toString()).val(data_received['data']['url'])
            $("#paper-row-level-" + no.toString()).val(data_received['data']['level'])

            data.publications_paper[no - 1].name = data_received['data']['name']
            data.publications_paper[no - 1].title = data_received['data']['title']
            data.publications_paper[no - 1].publication = data_received['data']['publication']
            data.publications_paper[no - 1].year = data_received['data']['year']
            data.publications_paper[no - 1].url = data_received['data']['url']
            data.publications_paper[no - 1].level = data_received['data']['level']
            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $("#paper-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
    }
    else if(data_received['process'] === 'sttps-edit'){
        var no = data_received['data']['row']
        if(data_received['status']){
            $("#sttp-row-id-" + no.toString()).val(data_received['data']['id']),
            $("#sttp-row-name-" + no.toString()).val(data_received['data']['name']),
            $("#sttp-row-organization-" + no.toString()).val(data_received['data']['organization']),
            $("#sttp-row-year-" + no.toString()).val(data_received['data']['year']),
            $("#sttp-row-date_form-" + no.toString()).val(data_received['data']['date_form'])
            $("#sttp-row-date_to-" + no.toString()).val(data_received['data']['date_to'])
            $("#sttp-row-day-" + no.toString()).val(data_received['data']['day'])

            data.sttps[no - 1].name = data_received['data']['name']
            data.sttps[no - 1].organization = data_received['data']['organization']
            data.sttps[no - 1].year = data_received['data']['year']
            data.sttps[no - 1].date_form = data_received['data']['date_form']
            data.sttps[no - 1].date_to = data_received['data']['date_to']
            data.sttps[no - 1].day = data_received['data']['day']
            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $("#sttp-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
    }
    else if(data_received['process'] === 'workshops-edit'){
        var no = data_received['data']['row']
        if(data_received['status']){
            $("#workshops-row-id-" + no.toString()).val(data_received['data']['id']),
            $("#workshops-row-name-" + no.toString()).val(data_received['data']['name']),
            $("#workshops-row-organization-" + no.toString()).val(data_received['data']['organization']),
            $("#workshops-row-year-" + no.toString()).val(data_received['data']['year']),
            $("#workshops-row-date_form-" + no.toString()).val(data_received['data']['date_form'])
            $("#workshops-row-date_to-" + no.toString()).val(data_received['data']['date_to'])
            $("#workshops-row-day-" + no.toString()).val(data_received['data']['day'])

            data.workshops[no - 1].name = data_received['data']['name']
            data.workshops[no - 1].organization = data_received['data']['organization']
            data.workshops[no - 1].year = data_received['data']['year']
            data.workshops[no - 1].date_form = data_received['data']['date_form']
            data.workshops[no - 1].date_to = data_received['data']['date_to']
            data.workshops[no - 1].day = data_received['data']['day']
            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $("#workshops-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
    }
    else if(data_received['process'] === 'oiis-edit'){
        var no = data_received['data']['row']
        if(data_received['status']){
            $("#oii-row-id-" + no.toString()).val(data_received['data']['id']),
            $("#oii-row-organization-" + no.toString()).val(data_received['data']['organization']),
            $("#oii-row-year-" + no.toString()).val(data_received['data']['year']),
            $("#oii-row-invitee-" + no.toString()).val(data_received['data']['invitee'])

            data.oiis[no - 1].organization = data_received['data']['organization']
            data.oiis[no - 1].year = data_received['data']['year']
            data.oiis[no - 1].invitee = data_received['data']['invitee']
            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $("#oii-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
    }
    else if(data_received['process'] === 'consultancys-edit'){
        var no = data_received['data']['row']
        if(data_received['status']){
            $("#consultancy-row-id-" + no.toString()).val(data_received['data']['id']),
            $("#consultancy-row-organization-" + no.toString()).val(data_received['data']['organization']),
            $("#consultancy-row-year-" + no.toString()).val(data_received['data']['year']),
            $("#consultancy-row-work_done-" + no.toString()).val(data_received['data']['work_done'])
            $("#consultancy-row-cost-" + no.toString()).val(data_received['data']['cost'])

            data.consultancys[no - 1].organization = data_received['data']['organization']
            data.consultancys[no - 1].year = data_received['data']['year']
            data.consultancys[no - 1].work_done = data_received['data']['work_done']
            data.consultancys[no - 1].cost = data_received['data']['cost']
            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $("#consultancy-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
    }
    else if(data_received['process'] === 'awards-edit'){
        var no = data_received['data']['row']
        if(data_received['status']){
            $("#award-row-id-" + no.toString()).val(data_received['data']['id']),
            $("#award-row-organization-" + no.toString()).val(data_received['data']['organization']),
            $("#award-row-year-" + no.toString()).val(data_received['data']['year']),
            $("#award-row-title-" + no.toString()).val(data_received['data']['title'])

            data.awards[no - 1].organization = data_received['data']['organization']
            data.awards[no - 1].year = data_received['data']['year']
            data.awards[no - 1].title = data_received['data']['title']
            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $("#award-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
    }
    else if(data_received['process'] === 'projects-edit'){
        var no = data_received['data']['row']
        if(data_received['status']){
            $("#project-row-id-" + no.toString()).val(data_received['data']['id']),
            $("#project-row-name-" + no.toString()).val(data_received['data']['name']),
            $("#project-row-year-" + no.toString()).val(data_received['data']['year']),
            $("#project-row-level-" + no.toString()).val(data_received['data']['level'])

            data.projects[no - 1].name = data_received['data']['name']
            data.projects[no - 1].year = data_received['data']['year']
            data.projects[no - 1].level = data_received['data']['level']
            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $("#project-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
    }
    else if(data_received['process'] === 'ecas-edit'){
        var no = data_received['data']['row']
        if(data_received['status']){
            $("#eca-row-id-" + no.toString()).val(data_received['data']['id']),
            $("#eca-row-name-" + no.toString()).val(data_received['data']['name']),
            $("#eca-row-year-" + no.toString()).val(data_received['data']['year'])

            data.ecas[no - 1].name = data_received['data']['name']
            data.ecas[no - 1].year = data_received['data']['year']
            alert('Saving Successful')
        }
        else{
            alert('Saving Failed, Try again..!', data_received['error'])
        }
        $("#eca-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
    }
};

// Button Clicked
$(document).on('click', '#book-add', function(){
    $('#loading-animation-book').removeClass('d-none')
    $("#book-add").prop('disabled', true).text('Saving...');

    if($("#book-name").val() !== '' && $("#book-publication").val() !== '' && $("#book-year").val() !== ''){
        if($("#book-id").val() === ''){
            ssbtSocket.send(JSON.stringify({
                'process': 'publications_book-form-submission',
                'data':{
                    'id': data.designation.id,
                    'teacher': data.designation.teacher,
                    'name': $("#book-name").val(),
                    'publication': $("#book-publication").val(),
                    'year': $("#book-year").val(),
                }
            }))
        }
        else{
            table_publications_book($("#book-id").val(), $("#book-name").val(), $("#book-publication").val(), $("#book-year").val())

            $('#loading-animation-book').addClass('d-none')
            $("#book-add").prop('disabled', false).text('Add');
        }
    }
    else{
        alert('Empty Field is not Allowed..!')
        $('#loading-animation-book').addClass('d-none')
        $("#book-add").prop('disabled', false).text('Add');
    }
})

$(document).on('click', '#journal-add', function(){
    $('#loading-animation-journal').removeClass('d-none')
    $("#journal-add").prop('disabled', true).text('Saving...');

    if($("#journal-name").val() !== '' && $("#journal-title").val() !== '' && $("#journal-publication").val() !== '' && $("#journal-page").val() !== '' && $("#journal-year").val() !== '' && $("#journal-url").val() !== '' && $("input[name='journal-level']:checked").val() !== ''){
        if($("#journal-id").val() === ''){
            ssbtSocket.send(JSON.stringify({
                'process': 'publications_journal-form-submission',
                'data':{
                    'id': data.designation.id,
                    'teacher': data.designation.teacher,
                    'name': $("#journal-name").val(),
                    'title': $("#journal-title").val(),
                    'publication': $("#journal-publication").val(),
                    'page': $("#journal-page").val(),
                    'year': $("#journal-year").val(),
                    'url': $("#journal-url").val(),
                    'level': $("input[name='journal-level']:checked").val(),
                }
            }))
        }
        else{
            table_publications_journal($("#journal-id").val(), $("#journal-name").val(), $("#journal-title").val(), $("#journal-publication").val(), $("#journal-page").val(), $("#journal-year").val(), $("#journal-url").val(), $("input[name='journal-level']:checked").val(),)

            $('#loading-animation-journal').addClass('d-none')
            $("#journal-add").prop('disabled', false).text('Add');
        }
    }
    else{
        alert('Empty Field is not Allowed..!')
        $('#loading-animation-journal').addClass('d-none')
        $("#journal-add").prop('disabled', false).text('Add');
    }
})

$(document).on('click', '#paper-add', function(){
    $('#loading-animation-paper').removeClass('d-none')
    $("#paper-add").prop('disabled', true).text('Saving...');

    if($("#paper-name").val() !== '' && $("#paper-title").val() !== '' && $("#paper-publication").val() !== '' && $("#paper-year").val() !== '' && $("#paper-url").val() !== '' && $("input[name='paper-level']:checked").val() !== ''){
        if($("#paper-id").val() === ''){
            ssbtSocket.send(JSON.stringify({
                'process': 'publications_paper-form-submission',
                'data':{
                    'id': data.designation.id,
                    'teacher': data.designation.teacher,
                    'name': $("#paper-name").val(),
                    'title': $("#paper-title").val(),
                    'publication': $("#paper-publication").val(),
                    'year': $("#paper-year").val(),
                    'url': $("#paper-url").val(),
                    'level': $("input[name='paper-level']:checked").val(),
                }
            }))
        }
        else{
            table_publications_paper($("#paper-id").val(), $("#paper-name").val(), $("#paper-title").val(), $("#paper-publication").val(), $("#paper-year").val(), $("#paper-url").val(), $("input[name='paper-level']:checked").val(),)

            $('#loading-animation-paper').addClass('d-none')
            $("#paper-add").prop('disabled', false).text('Add');
        }
    }
    else{
        alert('Empty Field is not Allowed..!')
        $('#loading-animation-paper').addClass('d-none')
        $("#paper-add").prop('disabled', false).text('Add');
    }
})

$(document).on('click', '#sttp-add', function(){
    $('#loading-animation-sttp').removeClass('d-none')
    $("#sttp-add").prop('disabled', true).text('Saving...');

    if($("#sttp-name").val() !== '' && $("#sttp-organization").val() !== '' && $("#sttp-date_to").val().substr(6, 9) !== '' && $("#sttp-date_form").val() !== '' && $("#sttp-date_to").val() !== '' && $("#sttp-day").val() !== ''){
        if($("#sttp-id").val() === ''){
            ssbtSocket.send(JSON.stringify({
                'process': 'sttps-form-submission',
                'data':{
                    'id': data.designation.id,
                    'teacher': data.designation.teacher,
                    'name': $("#sttp-name").val(),
                    'organization': $("#sttp-organization").val(),
                    'year': $("#sttp-date_to").val().substr(6, 9),
                    'date_form': $("#sttp-date_form").val(),
                    'date_to': $("#sttp-date_to").val(),
                    'day': $("#sttp-day").val(),
                }
            }))
        }
        else{
            table_sttps($("#sttp-id").val(), $("#sttp-name").val(), $("#sttp-organization").val(), $("#sttp-date_to").val().substr(6, 9), $("#sttp-date_form").val(), $("#sttp-date_to").val(), $("#sttp-day").val(),)

            $('#loading-animation-sttp').addClass('d-none')
            $("#sttp-add").prop('disabled', false).text('Add');
        }
    }
    else{
        alert('Empty Field is not Allowed..!')
        $('#loading-animation-sttp').addClass('d-none')
        $("#sttp-add").prop('disabled', false).text('Add');
    }
})

$(document).on('click', '#workshops-add', function(){
    $('#loading-animation-workshops').removeClass('d-none')
    $("#workshops-add").prop('disabled', true).text('Saving...');

    if($("#workshops-name").val() !== '' && $("#workshops-organization").val() !== '' && $("#workshops-date_to").val().substr(6, 9) !== '' && $("#workshops-date_form").val() !== '' && $("#workshops-date_to").val() !== '' && $("#workshops-days").val() !== ''){
        if($("#workshops-id").val() === ''){
            ssbtSocket.send(JSON.stringify({
                'process': 'workshops-form-submission',
                'data':{
                    'id': data.designation.id,
                    'teacher': data.designation.teacher,
                    'name': $("#workshops-name").val(),
                    'organization': $("#workshops-organization").val(),
                    'year': $("#workshops-date_to").val().substr(6, 9),
                    'date_form': $("#workshops-date_form").val(),
                    'date_to': $("#workshops-date_to").val(),
                    'day': $("#workshops-days").val(),
                }
            }))
        }
        else{
            table_workshops($("#workshops-id").val(), $("#workshops-name").val(), $("#workshops-organization").val(), $("#workshops-date_to").val().substr(6, 9), $("#workshops-date_form").val(), $("#workshops-date_to").val(), $("#workshops-days").val(),)

            $('#loading-animation-workshops').addClass('d-none')
            $("#workshops-add").prop('disabled', false).text('Add');
        }
    }
    else{
        alert('Empty Field is not Allowed..!')
        $('#loading-animation-workshops').addClass('d-none')
        $("#workshops-add").prop('disabled', false).text('Add');
    }
})

$(document).on('click', '#oii-add', function(){
    $('#loading-animation-oii').removeClass('d-none')
    $("#oii-add").prop('disabled', true).text('Saving...');

    if($("#oii-organization").val() !== '' && $("#oii-year").val() !== '' && $("input[name='oii-invitee']:checked").val() !== ''){
        if($("#oii-id").val() === ''){
            ssbtSocket.send(JSON.stringify({
                'process': 'oiis-form-submission',
                'data':{
                    'id': data.designation.id,
                    'teacher': data.designation.teacher,
                    'organization': $("#oii-organization").val(),
                    'year': $("#oii-year").val(),
                    'invitee': $("input[name='oii-invitee']:checked").val(),
                }
            }))
        }
        else{
            table_oiis($("#oii-id").val(), $("#oii-organization").val(), $("#oii-year").val(), $("input[name='oii-invitee']:checked").val())

            $('#loading-animation-oii').addClass('d-none')
            $("#oii-add").prop('disabled', false).text('Add');
        }
    }
    else{
        alert('Empty Field is not Allowed..!')
        $('#loading-animation-oii').addClass('d-none')
        $("#oii-add").prop('disabled', false).text('Add');
    }
})

$(document).on('click', '#consultancy-add', function(){
    $('#loading-animation-consultancy').removeClass('d-none')
    $("#consultancy-add").prop('disabled', true).text('Saving...');

    if($("#consultancy-organization").val() !== '' && $("#consultancy-year").val() !== '' && $("#consultancy-work_done").val() !== '' && $("#consultancy-cost").val() !== ''){
        if($("#consultancy-id").val() === ''){
            ssbtSocket.send(JSON.stringify({
                'process': 'consultancys-form-submission',
                'data':{
                    'id': data.designation.id,
                    'teacher': data.designation.teacher,
                    'organization': $("#consultancy-organization").val(),
                    'year': $("#consultancy-year").val(),
                    'work_done': $("#consultancy-work_done").val(),
                    'cost': $("#consultancy-cost").val(),
                }
            }))
        }
        else{
            table_consultancys($("#consultancy-id").val(), $("#consultancy-organization").val(), $("#consultancy-year").val(), $("#consultancy-work_done").val(), $("#consultancy-cost").val())

            $('#loading-animation-consultancy').addClass('d-none')
            $("#consultancy-add").prop('disabled', false).text('Add');
        }
    }
    else{
        alert('Empty Field is not Allowed..!')
        $('#loading-animation-consultancy').addClass('d-none')
        $("#consultancy-add").prop('disabled', false).text('Add');
    }
})

$(document).on('click', '#award-add', function(){
    $('#loading-animation-award').removeClass('d-none')
    $("#award-add").prop('disabled', true).text('Saving...');

    if($("#award-organization").val() !== '' && $("#award-year").val() !== '' && $("#award-title").val() !== ''){
        if($("#award-id").val() === ''){
            ssbtSocket.send(JSON.stringify({
                'process': 'awards-form-submission',
                'data':{
                    'id': data.designation.id,
                    'teacher': data.designation.teacher,
                    'organization': $("#award-organization").val(),
                    'year': $("#award-year").val(),
                    'title': $("#award-title").val(),
                }
            }))
        }
        else{
            table_awards($("#award-id").val(), $("#award-organization").val(), $("#award-year").val(), $("#award-title").val())

            $('#loading-animation-award').addClass('d-none')
            $("#award-add").prop('disabled', false).text('Add');
        }
    }
    else{
        alert('Empty Field is not Allowed..!')
        $('#loading-animation-award').addClass('d-none')
        $("#award-add").prop('disabled', false).text('Add');
    }
})

$(document).on('click', '#project-add', function(){
    $('#loading-animation-project').removeClass('d-none')
    $("#project-add").prop('disabled', true).text('Saving...');

    if($("#project-name").val() !== '' && $("#project-year").val() !== '' && $("input[name='project-level']:checked").val() !== ''){
        if($("#project-id").val() === ''){
            ssbtSocket.send(JSON.stringify({
                'process': 'projects-form-submission',
                'data':{
                    'id': data.designation.id,
                    'teacher': data.designation.teacher,
                    'name': $("#project-name").val(),
                    'year': $("#project-year").val(),
                    'level': $("input[name='project-level']:checked").val(),
                }
            }))
        }
        else{
            table_projects($("#project-id").val(), $("#project-name").val(), $("#project-year").val(), $("input[name='project-level']:checked").val())

            $('#loading-animation-project').addClass('d-none')
            $("#project-add").prop('disabled', false).text('Add');
        }
    }
    else{
        alert('Empty Field is not Allowed..!')
        $('#loading-animation-project').addClass('d-none')
        $("#project-add").prop('disabled', false).text('Add');
    }
})

$(document).on('click', '#eca-add', function(){
    $('#loading-animation-eca').removeClass('d-none')
    $("#eca-add").prop('disabled', true).text('Saving...');

    if($("#eca-name").val() !== '' && $("#eca-year").val() !== ''){
        if($("#eca-id").val() === ''){
            ssbtSocket.send(JSON.stringify({
                'process': 'ecas-form-submission',
                'data':{
                    'id': data.designation.id,
                    'teacher': data.designation.teacher,
                    'name': $("#eca-name").val(),
                    'year': $("#eca-year").val(),
                }
            }))
        }
        else{
            table_ecas($("#eca-id").val(), $("#eca-name").val(), $("#eca-year").val())

            $('#loading-animation-eca').addClass('d-none')
            $("#eca-add").prop('disabled', false).text('Add');
        }
    }
    else{
        alert('Empty Field is not Allowed..!')
        $('#loading-animation-eca').addClass('d-none')
        $("#eca-add").prop('disabled', false).text('Add');
    }
})


// Table Functions

function table_publications_book(id, name, publication, year){
    if($("#book-table").hasClass('d-none')){
        $("#book-table").removeClass('d-none');
    }
    publications_book_no++;

    markup = '<tr>'+
        '<td> <input type="text" class="border-0 w-100 d-none" value="' + id + '" id="book-row-id-' + publications_book_no + '" readonly="true">'+
        '<input type="text" class="border-0 w-100 text-muted" value="' + name + '" id="book-row-name-' + publications_book_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + publication + '" id="book-row-publication-' + publications_book_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + year + '" id="book-row-year-' + publications_book_no + '" readonly="true"> </td>'+
        '<td> <button type="button" class="btn btn-primary w-100" id="book-row-button-' + publications_book_no + '" onclick="edit_book(' + publications_book_no + ')" value="Edit">Edit</button> </td>'+
        '</tr>';

    $("#book-table-body").append(markup)
    $("#book-id").val('')
    $("#book-name").val('')
    $("#book-publication").val('')
    $("#book-year").val('')
}

function table_publications_journal(id, name, title, publication, page, year, url, level){
    if($("#journal-table").hasClass('d-none')){
        $("#journal-table").removeClass('d-none');
    }
    publications_journal_no++;

    markup = '<tr>'+
        '<td> <input type="text" class="border-0 w-100 d-none" value="' + id + '" id="journal-row-id-' + publications_journal_no + '" readonly="true">'+
        '<input type="text" class="border-0 w-100 text-muted" value="' + name + '" id="journal-row-name-' + publications_journal_no + '" readonly="true"> </td>'+

        '<td><input type="text" class="border-0 w-100 text-muted" value="' + title + '" id="journal-row-title-' + publications_journal_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + publication + '" id="journal-row-publication-' + publications_journal_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + page + '" id="journal-row-page-' + publications_journal_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + year + '" id="journal-row-year-' + publications_journal_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + url + '" id="journal-row-url-' + publications_journal_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + level + '" id="journal-row-level-' + publications_journal_no + '" readonly="true"> </td>'+

        '<td> <button type="button" class="btn btn-primary w-100" id="journal-row-button-' + publications_journal_no + '" onclick="edit_journal(' + publications_journal_no + ')" value="Edit">Edit</button> </td>'+
        '</tr>';

    $("#journal-table-body").append(markup)
    $("#journal-id").val('')
    $("#journal-name").val('')
    $("#journal-title").val('')
    $("#journal-publication").val('')
    $("#journal-page").val('')
    $("#journal-year").val('')
    $("#journal-url").val('')
}

function table_publications_paper(id, name, title, publication, year, url, level){
    if($("#paper-table").hasClass('d-none')){
        $("#paper-table").removeClass('d-none');
    }
    publications_paper_no++;

    markup = '<tr>'+
        '<td> <input type="text" class="border-0 w-100 d-none" value="' + id + '" id="paper-row-id-' + publications_paper_no + '" readonly="true">'+
        '<input type="text" class="border-0 w-100 text-muted" value="' + name + '" id="paper-row-name-' + publications_paper_no + '" readonly="true"> </td>'+

        '<td><input type="text" class="border-0 w-100 text-muted" value="' + title + '" id="paper-row-title-' + publications_paper_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + publication + '" id="paper-row-publication-' + publications_paper_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + year + '" id="paper-row-year-' + publications_paper_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + url + '" id="paper-row-url-' + publications_paper_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + level + '" id="paper-row-level-' + publications_paper_no + '" readonly="true"> </td>'+

        '<td> <button type="button" class="btn btn-primary w-100" id="paper-row-button-' + publications_paper_no + '" onclick="edit_paper(' + publications_paper_no + ')" value="Edit">Edit</button> </td>'+
        '</tr>';

    $("#paper-table-body").append(markup)
    $("#paper-id").val('')
    $("#paper-name").val('')
    $("#paper-title").val('')
    $("#paper-publication").val('')
    $("#paper-year").val('')
    $("#paper-url").val('')
}

function table_sttps(id, name, organization, year, date_form, date_to, day){
    if($("#sttp-table").hasClass('d-none')){
        $("#sttp-table").removeClass('d-none');
    }
    sttps_no++;

    markup = '<tr>'+
        '<td> <input type="text" class="border-0 w-100 d-none" value="' + id + '" id="sttp-row-id-' + sttps_no + '" readonly="true">'+
        '<input type="text" class="border-0 w-100 text-muted" value="' + name + '" id="sttp-row-name-' + sttps_no + '" readonly="true"> </td>'+

        '<td><input type="text" class="border-0 w-100 text-muted" value="' + organization + '" id="sttp-row-organization-' + sttps_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + year + '" id="sttp-row-year-' + sttps_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + date_form + '" id="sttp-row-date_form-' + sttps_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + date_to + '" id="sttp-row-date_to-' + sttps_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + day + '" id="sttp-row-day-' + sttps_no + '" readonly="true"> </td>'+

        '<td> <button type="button" class="btn btn-primary w-100" id="sttp-row-button-' + sttps_no + '" onclick="edit_sttp(' + sttps_no + ')" value="Edit">Edit</button> </td>'+
        '</tr>';

    $("#sttp-table-body").append(markup)
    $("#sttp-id").val('')
    $("#sttp-name").val('')
    $("#sttp-organization").val('')
    $("#sttp-year").val('')
    $("#sttp-date_form").val('')
    $("#sttp-date_to").val('')
    $("#sttp-day").val('')
}

function table_workshops(id, name, organization, year, date_form, date_to, day){
    if($("#workshops-table").hasClass('d-none')){
        $("#workshops-table").removeClass('d-none');
    }
    workshops_no++;

    markup = '<tr>'+
        '<td> <input type="text" class="border-0 w-100 d-none" value="' + id + '" id="workshops-row-id-' + workshops_no + '" readonly="true">'+
        '<input type="text" class="border-0 w-100 text-muted" value="' + name + '" id="workshops-row-name-' + workshops_no + '" readonly="true"> </td>'+

        '<td><input type="text" class="border-0 w-100 text-muted" value="' + organization + '" id="workshops-row-organization-' + workshops_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + year + '" id="workshops-row-year-' + workshops_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + date_form + '" id="workshops-row-date_form-' + workshops_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + date_to + '" id="workshops-row-date_to-' + workshops_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + day + '" id="workshops-row-day-' + workshops_no + '" readonly="true"> </td>'+

        '<td> <button type="button" class="btn btn-primary w-100" id="workshops-row-button-' + workshops_no + '" onclick="edit_workshops(' + workshops_no + ')" value="Edit">Edit</button> </td>'+
        '</tr>';

    $("#workshops-table-body").append(markup)
    $("#workshops-id").val('')
    $("#workshops-name").val('')
    $("#workshops-organization").val('')
    $("#workshops-year").val('')
    $("#workshops-date_form").val('')
    $("#workshops-date_to").val('')
    $("#workshops-days").val('')
}

function table_oiis(id, organization, year, invitee){
    if($("#oii-table").hasClass('d-none')){
        $("#oii-table").removeClass('d-none');
    }
    oiis_no++;

    markup = '<tr>'+
        '<td> <input type="text" class="border-0 w-100 d-none" value="' + id + '" id="oii-row-id-' + oiis_no + '" readonly="true">'+
        '<input type="text" class="border-0 w-100 text-muted" value="' + organization + '" id="oii-row-organization-' + oiis_no + '" readonly="true"> </td>'+

        '<td><input type="text" class="border-0 w-100 text-muted" value="' + year + '" id="oii-row-year-' + oiis_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + invitee + '" id="oii-row-invitee-' + oiis_no + '" readonly="true"> </td>'+

        '<td> <button type="button" class="btn btn-primary w-100" id="oii-row-button-' + oiis_no + '" onclick="edit_oii(' + oiis_no + ')" value="Edit">Edit</button> </td>'+
        '</tr>';

    $("#oii-table-body").append(markup)
    $("#oii-id").val('')
    $("#oii-organization").val('')
    $("#oii-year").val('')
}

function table_consultancys(id, organization, year, work_done, cost){
    if($("#consultancy-table").hasClass('d-none')){
        $("#consultancy-table").removeClass('d-none');
    }
    consultancys_no++;

    markup = '<tr>'+
        '<td> <input type="text" class="border-0 w-100 d-none" value="' + id + '" id="consultancy-row-id-' + consultancys_no + '" readonly="true">'+
        '<input type="text" class="border-0 w-100 text-muted" value="' + organization + '" id="consultancy-row-organization-' + consultancys_no + '" readonly="true"> </td>'+

        '<td><input type="text" class="border-0 w-100 text-muted" value="' + year + '" id="consultancy-row-year-' + consultancys_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + work_done + '" id="consultancy-row-work_done-' + consultancys_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + cost + '" id="consultancy-row-cost-' + consultancys_no + '" readonly="true"> </td>'+

        '<td> <button type="button" class="btn btn-primary w-100" id="consultancy-row-button-' + consultancys_no + '" onclick="edit_consultancy(' + consultancys_no + ')" value="Edit">Edit</button> </td>'+
        '</tr>';

    $("#consultancy-table-body").append(markup)
    $("#consultancy-id").val('')
    $("#consultancy-organization").val('')
    $("#consultancy-year").val('')
    $("#consultancy-work_done").val('')
    $("#consultancy-cost").val('')
}

function table_awards(id, organization, year, title){
    if($("#award-table").hasClass('d-none')){
        $("#award-table").removeClass('d-none');
    }
    awards_no++;

    markup = '<tr>'+
        '<td> <input type="text" class="border-0 w-100 d-none" value="' + id + '" id="award-row-id-' + awards_no + '" readonly="true">'+
        '<input type="text" class="border-0 w-100 text-muted" value="' + organization + '" id="award-row-organization-' + awards_no + '" readonly="true"> </td>'+

        '<td><input type="text" class="border-0 w-100 text-muted" value="' + year + '" id="award-row-year-' + awards_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + title + '" id="award-row-title-' + awards_no + '" readonly="true"> </td>'+

        '<td> <button type="button" class="btn btn-primary w-100" id="award-row-button-' + awards_no + '" onclick="edit_award(' + awards_no + ')" value="Edit">Edit</button> </td>'+
        '</tr>';

    $("#award-table-body").append(markup)
    $("#award-id").val('')
    $("#award-organization").val('')
    $("#award-year").val('')
    $("#award-title").val('')
}

function table_projects(id, name, year, level){
    if($("#project-table").hasClass('d-none')){
        $("#project-table").removeClass('d-none');
    }
    projects_no++;

    markup = '<tr>'+
        '<td> <input type="text" class="border-0 w-100 d-none" value="' + id + '" id="project-row-id-' + projects_no + '" readonly="true">'+
        '<input type="text" class="border-0 w-100 text-muted" value="' + name + '" id="project-row-name-' + projects_no + '" readonly="true"> </td>'+

        '<td><input type="text" class="border-0 w-100 text-muted" value="' + year + '" id="project-row-year-' + projects_no + '" readonly="true"> </td>'+
        '<td><input type="text" class="border-0 w-100 text-muted" value="' + level + '" id="project-row-level-' + projects_no + '" readonly="true"> </td>'+

        '<td> <button type="button" class="btn btn-primary w-100" id="project-row-button-' + projects_no + '" onclick="edit_project(' + projects_no + ')" value="Edit">Edit</button> </td>'+
        '</tr>';

    $("#project-table-body").append(markup)
    $("#project-id").val('')
    $("#project-name").val('')
    $("#project-year").val('')
}

function table_ecas(id, name, year){
    if($("#eca-table").hasClass('d-none')){
        $("#eca-table").removeClass('d-none');
    }
    ecas_no++;

    markup = '<tr>'+
        '<td> <input type="text" class="border-0 w-100 d-none" value="' + id + '" id="eca-row-id-' + ecas_no + '" readonly="true">'+
        '<input type="text" class="border-0 w-100 text-muted" value="' + name + '" id="eca-row-name-' + ecas_no + '" readonly="true"> </td>'+

        '<td><input type="text" class="border-0 w-100 text-muted" value="' + year + '" id="eca-row-year-' + ecas_no + '" readonly="true"> </td>'+

        '<td> <button type="button" class="btn btn-primary w-100" id="eca-row-button-' + ecas_no + '" onclick="edit_eca(' + ecas_no + ')" value="Edit">Edit</button> </td>'+
        '</tr>';

    $("#eca-table-body").append(markup)
    $("#eca-id").val('')
    $("#eca-name").val('')
    $("#eca-year").val('')
}

// Edit Functions
function edit_book(no){
    if($("#book-row-button-" + no.toString()).val() === "Edit"){
        $("#book-row-name-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#book-row-publication-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#book-row-year-" + no.toString()).prop('readonly', false).removeClass('text-muted');

        $("#book-row-button-" + no.toString()).text('Save').val('Save').removeClass('btn-primary').addClass('btn-success');
    }
    else if($("#book-row-button-" + no.toString()).val() === "Save"){
        if($("#book-row-name-" + no.toString()).val() !== '' && $("#book-row-publication-" + no.toString()).val() !== '' && $("#book-row-year-" + no.toString()).val() !== ''){

            $("#book-row-name-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#book-row-publication-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#book-row-year-" + no.toString()).prop('readonly', true).addClass('text-muted');


            if($("#book-row-name-" + no.toString()).val() !== data.publications_book[no - 1].name || $("#book-row-publication-" + no.toString()).val() !== data.publications_book[no - 1].publication || $("#book-row-year-" + no.toString()).val() !== data.publications_book[no - 1].year){

                $("#book-row-button-" + no.toString()).text('Saving...').prop('disabled', true);

                ssbtSocket.send(JSON.stringify({
                    'process': 'publications_book-edit',
                    'data':{
                        'teacher': data.designation.teacher,
                        'id': $("#book-row-id-" + no.toString()).val(),
                        'name': $("#book-row-name-" + no.toString()).val(),
                        'publication': $("#book-row-publication-" + no.toString()).val(),
                        'year': $("#book-row-year-" + no.toString()).val(),
                        'row': no,
                    }
                }))
            }
            else{
                alert("Nothing is changed..!")
                $("#book-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
            }
        }
        else{
            alert("Empty field Not Allowed..!")
        }
    }
}

function edit_journal(no){
    if($("#journal-row-button-" + no.toString()).val() === "Edit"){
        $("#journal-row-name-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#journal-row-title-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#journal-row-publication-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#journal-row-page-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#journal-row-year-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#journal-row-url-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#journal-row-level-" + no.toString()).prop('readonly', false).removeClass('text-muted');

        $("#journal-row-button-" + no.toString()).text('Save').val('Save').removeClass('btn-primary').addClass('btn-success');
    }
    else if($("#journal-row-button-" + no.toString()).val() === "Save"){
        if($("#journal-row-name-" + no.toString()).val() !== '' && $("#journal-row-title-" + no.toString()).val() !== '' && $("#journal-row-publication-" + no.toString()).val() !== '' && $("#journal-row-page-" + no.toString()).val() !== '' && $("#journal-row-year-" + no.toString()).val() !== '' && $("#journal-row-url-" + no.toString()).val() !== '' && $("#journal-row-level-" + no.toString()).val() !== ''){

            $("#journal-row-name-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#journal-row-title-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#journal-row-publication-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#journal-row-page-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#journal-row-year-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#journal-row-url-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#journal-row-level-" + no.toString()).prop('readonly', true).addClass('text-muted');


            if($("#journal-row-name-" + no.toString()).val() !== data.publications_journal[no - 1].name || $("#journal-row-title-" + no.toString()).val() !== data.publications_journal[no - 1].title || $("#journal-row-publication-" + no.toString()).val() !== data.publications_journal[no - 1].publication || $("#journal-row-page-" + no.toString()).val() !== data.publications_journal[no - 1].page || $("#journal-row-year-" + no.toString()).val() !== data.publications_journal[no - 1].year || $("#journal-row-url-" + no.toString()).val() !== data.publications_journal[no - 1].url || $("#journal-row-level-" + no.toString()).val() !== data.publications_journal[no - 1].level){

                $("#journal-row-button-" + no.toString()).text('Saving...').prop('disabled', true);

                ssbtSocket.send(JSON.stringify({
                    'process': 'publications_journal-edit',
                    'data':{
                        'teacher': data.designation.teacher,
                        'id': $("#journal-row-id-" + no.toString()).val(),
                        'name': $("#journal-row-name-" + no.toString()).val(),
                        'title': $("#journal-row-title-" + no.toString()).val(),
                        'publication': $("#journal-row-publication-" + no.toString()).val(),
                        'page': $("#journal-row-page-" + no.toString()).val(),
                        'year': $("#journal-row-year-" + no.toString()).val(),
                        'url': $("#journal-row-url-" + no.toString()).val(),
                        'level': $("#journal-row-level-" + no.toString()).val(),
                        'row': no,
                    }
                }))
            }
            else{
                alert("Nothing is changed..!")
                $("#journal-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
            }
        }
        else{
            alert("Empty field Not Allowed..!")
        }
    }
}

function edit_paper(no){
    if($("#paper-row-button-" + no.toString()).val() === "Edit"){
        $("#paper-row-name-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#paper-row-title-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#paper-row-publication-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#paper-row-year-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#paper-row-url-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#paper-row-level-" + no.toString()).prop('readonly', false).removeClass('text-muted');

        $("#paper-row-button-" + no.toString()).text('Save').val('Save').removeClass('btn-primary').addClass('btn-success');
    }
    else if($("#paper-row-button-" + no.toString()).val() === "Save"){
        if($("#paper-row-name-" + no.toString()).val() !== '' && $("#paper-row-title-" + no.toString()).val() !== '' && $("#paper-row-publication-" + no.toString()).val() !== '' && $("#paper-row-year-" + no.toString()).val() !== '' && $("#paper-row-url-" + no.toString()).val() !== '' && $("#paper-row-level-" + no.toString()).val() !== ''){

            $("#paper-row-name-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#paper-row-title-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#paper-row-publication-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#paper-row-year-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#paper-row-url-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#paper-row-level-" + no.toString()).prop('readonly', true).addClass('text-muted');


            if($("#paper-row-name-" + no.toString()).val() !== data.publications_paper[no - 1].name || $("#paper-row-title-" + no.toString()).val() !== data.publications_paper[no - 1].title || $("#paper-row-publication-" + no.toString()).val() !== data.publications_paper[no - 1].publication || $("#paper-row-year-" + no.toString()).val() !== data.publications_paper[no - 1].year || $("#paper-row-url-" + no.toString()).val() !== data.publications_paper[no - 1].url || $("#paper-row-level-" + no.toString()).val() !== data.publications_paper[no - 1].level){

                $("#paper-row-button-" + no.toString()).text('Saving...').prop('disabled', true);

                ssbtSocket.send(JSON.stringify({
                    'process': 'publications_paper-edit',
                    'data':{
                        'teacher': data.designation.teacher,
                        'id': $("#paper-row-id-" + no.toString()).val(),
                        'name': $("#paper-row-name-" + no.toString()).val(),
                        'title': $("#paper-row-title-" + no.toString()).val(),
                        'publication': $("#paper-row-publication-" + no.toString()).val(),
                        'year': $("#paper-row-year-" + no.toString()).val(),
                        'url': $("#paper-row-url-" + no.toString()).val(),
                        'level': $("#paper-row-level-" + no.toString()).val(),
                        'row': no,
                    }
                }))
            }
            else{
                alert("Nothing is changed..!")
                $("#paper-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
            }
        }
        else{
            alert("Empty field Not Allowed..!")
        }
    }
}

function edit_sttp(no){
    if($("#sttp-row-button-" + no.toString()).val() === "Edit"){
        $("#sttp-row-name-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#sttp-row-organization-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#sttp-row-year-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#sttp-row-date_form-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#sttp-row-date_to-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#sttp-row-day-" + no.toString()).prop('readonly', false).removeClass('text-muted');

        $("#sttp-row-button-" + no.toString()).text('Save').val('Save').removeClass('btn-primary').addClass('btn-success');
    }
    else if($("#sttp-row-button-" + no.toString()).val() === "Save"){
        if($("#sttp-row-name-" + no.toString()).val() !== '' && $("#sttp-row-organization-" + no.toString()).val() !== '' && $("#sttp-row-year-" + no.toString()).val() !== '' && $("#sttp-row-date_form-" + no.toString()).val() !== '' && $("#sttp-row-date_to-" + no.toString()).val() !== '' && $("#sttp-row-day-" + no.toString()).val() !== ''){

            $("#sttp-row-name-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#sttp-row-organization-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#sttp-row-year-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#sttp-row-date_form-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#sttp-row-date_to-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#sttp-row-day-" + no.toString()).prop('readonly', true).addClass('text-muted');


            if($("#sttp-row-name-" + no.toString()).val() !== data.sttps[no - 1].name || $("#sttp-row-organization-" + no.toString()).val() !== data.sttps[no - 1].organization || $("#sttp-row-year-" + no.toString()).val() !== data.sttps[no - 1].year || $("#sttp-row-date_form-" + no.toString()).val() !== data.sttps[no - 1].date_form || $("#sttp-row-date_to-" + no.toString()).val() !== data.sttps[no - 1].date_to || $("#sttp-row-day-" + no.toString()).val() !== data.sttps[no - 1].day){

                $("#sttp-row-button-" + no.toString()).text('Saving...').prop('disabled', true);

                ssbtSocket.send(JSON.stringify({
                    'process': 'sttps-edit',
                    'data':{
                        'teacher': data.designation.teacher,
                        'id': $("#sttp-row-id-" + no.toString()).val(),
                        'name': $("#sttp-row-name-" + no.toString()).val(),
                        'organization': $("#sttp-row-organization-" + no.toString()).val(),
                        'year': $("#sttp-row-year-" + no.toString()).val(),
                        'date_form': $("#sttp-row-date_form-" + no.toString()).val(),
                        'date_to': $("#sttp-row-date_to-" + no.toString()).val(),
                        'day': $("#sttp-row-day-" + no.toString()).val(),
                        'row': no,
                    }
                }))
            }
            else{
                alert("Nothing is changed..!")
                $("#sttp-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
            }
        }
        else{
            alert("Empty field Not Allowed..!")
        }
    }
}

function edit_workshops(no){
    if($("#workshops-row-button-" + no.toString()).val() === "Edit"){
        $("#workshops-row-name-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#workshops-row-organization-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#workshops-row-year-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#workshops-row-date_form-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#workshops-row-date_to-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#workshops-row-day-" + no.toString()).prop('readonly', false).removeClass('text-muted');

        $("#workshops-row-button-" + no.toString()).text('Save').val('Save').removeClass('btn-primary').addClass('btn-success');
    }
    else if($("#workshops-row-button-" + no.toString()).val() === "Save"){
        if($("#workshops-row-name-" + no.toString()).val() !== '' && $("#workshops-row-organization-" + no.toString()).val() !== '' && $("#workshops-row-year-" + no.toString()).val() !== '' && $("#workshops-row-date_form-" + no.toString()).val() !== '' && $("#workshops-row-date_to-" + no.toString()).val() !== '' && $("#workshops-row-day-" + no.toString()).val() !== ''){

            $("#workshops-row-name-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#workshops-row-organization-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#workshops-row-year-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#workshops-row-date_form-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#workshops-row-date_to-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#workshops-row-day-" + no.toString()).prop('readonly', true).addClass('text-muted');


            if($("#workshops-row-name-" + no.toString()).val() !== data.workshops[no - 1].name || $("#workshops-row-organization-" + no.toString()).val() !== data.workshops[no - 1].organization || $("#workshops-row-year-" + no.toString()).val() !== data.workshops[no - 1].year || $("#workshops-row-date_form-" + no.toString()).val() !== data.workshops[no - 1].date_form || $("#workshops-row-date_to-" + no.toString()).val() !== data.workshops[no - 1].date_to || $("#workshops-row-day-" + no.toString()).val() !== data.workshops[no - 1].day){

                $("#workshops-row-button-" + no.toString()).text('Saving...').prop('disabled', true);

                ssbtSocket.send(JSON.stringify({
                    'process': 'workshops-edit',
                    'data':{
                        'teacher': data.designation.teacher,
                        'id': $("#workshops-row-id-" + no.toString()).val(),
                        'name': $("#workshops-row-name-" + no.toString()).val(),
                        'organization': $("#workshops-row-organization-" + no.toString()).val(),
                        'year': $("#workshops-row-year-" + no.toString()).val(),
                        'date_form': $("#workshops-row-date_form-" + no.toString()).val(),
                        'date_to': $("#workshops-row-date_to-" + no.toString()).val(),
                        'day': $("#workshops-row-day-" + no.toString()).val(),
                        'row': no,
                    }
                }))
            }
            else{
                alert("Nothing is changed..!")
                $("#workshops-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
            }
        }
        else{
            alert("Empty field Not Allowed..!")
        }
    }
}

function edit_oii(no){
    if($("#oii-row-button-" + no.toString()).val() === "Edit"){
        $("#oii-row-organization-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#oii-row-year-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#oii-row-invitee-" + no.toString()).prop('readonly', false).removeClass('text-muted');

        $("#oii-row-button-" + no.toString()).text('Save').val('Save').removeClass('btn-primary').addClass('btn-success');
    }
    else if($("#oii-row-button-" + no.toString()).val() === "Save"){
        if($("#oii-row-organization-" + no.toString()).val() !== '' && $("#oii-row-year-" + no.toString()).val() !== '' && $("#oii-row-invitee-" + no.toString()).val() !== ''){

            $("#oii-row-organization-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#oii-row-year-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#oii-row-invitee-" + no.toString()).prop('readonly', true).addClass('text-muted');


            if($("#oii-row-organization-" + no.toString()).val() !== data.oiis[no - 1].organization || $("#oii-row-year-" + no.toString()).val() !== data.oiis[no - 1].year || $("#oii-row-invitee-" + no.toString()).val() !== data.oiis[no - 1].invitee){

                $("#oii-row-button-" + no.toString()).text('Saving...').prop('disabled', true);

                ssbtSocket.send(JSON.stringify({
                    'process': 'oiis-edit',
                    'data':{
                        'teacher': data.designation.teacher,
                        'id': $("#workshops-row-id-" + no.toString()).val(),
                        'organization': $("#workshops-row-organization-" + no.toString()).val(),
                        'year': $("#workshops-row-year-" + no.toString()).val(),
                        'invitee': $("#workshops-row-invitee-" + no.toString()).val(),
                        'row': no,
                    }
                }))
            }
            else{
                alert("Nothing is changed..!")
                $("#oii-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
            }
        }
        else{
            alert("Empty field Not Allowed..!")
        }
    }
}

function edit_consultancy(no){
    if($("#consultancy-row-button-" + no.toString()).val() === "Edit"){
        $("#consultancy-row-organization-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#consultancy-row-year-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#consultancy-row-work_done-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#consultancy-row-cost-" + no.toString()).prop('readonly', false).removeClass('text-muted');

        $("#consultancy-row-button-" + no.toString()).text('Save').val('Save').removeClass('btn-primary').addClass('btn-success');
    }
    else if($("#consultancy-row-button-" + no.toString()).val() === "Save"){
        if($("#consultancy-row-organization-" + no.toString()).val() !== '' && $("#consultancy-row-year-" + no.toString()).val() !== '' && $("#consultancy-row-work_done-" + no.toString()).val() !== '' && $("#consultancy-row-cost-" + no.toString()).val() !== ''){

            $("#consultancy-row-organization-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#consultancy-row-year-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#consultancy-row-work_done-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#consultancy-row-cost-" + no.toString()).prop('readonly', true).addClass('text-muted');


            if($("#consultancy-row-organization-" + no.toString()).val() !== data.consultancys[no - 1].organization || $("#consultancy-row-year-" + no.toString()).val() !== data.consultancys[no - 1].year || $("#consultancy-row-work_done-" + no.toString()).val() !== data.consultancys[no - 1].work_done || $("#consultancy-row-cost-" + no.toString()).val() !== data.consultancys[no - 1].cost){

                $("#consultancy-row-button-" + no.toString()).text('Saving...').prop('disabled', true);

                ssbtSocket.send(JSON.stringify({
                    'process': 'consultancys-edit',
                    'data':{
                        'teacher': data.designation.teacher,
                        'id': $("#consultancy-row-id-" + no.toString()).val(),
                        'organization': $("#consultancy-row-organization-" + no.toString()).val(),
                        'year': $("#consultancy-row-year-" + no.toString()).val(),
                        'work_done': $("#consultancy-row-work_done-" + no.toString()).val(),
                        'cost': $("#consultancy-row-cost-" + no.toString()).val(),
                        'row': no,
                    }
                }))
            }
            else{
                alert("Nothing is changed..!")
                $("#consultancy-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
            }
        }
        else{
            alert("Empty field Not Allowed..!")
        }
    }
}

function edit_award(no){
    if($("#award-row-button-" + no.toString()).val() === "Edit"){
        $("#award-row-organization-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#award-row-year-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#award-row-title-" + no.toString()).prop('readonly', false).removeClass('text-muted');

        $("#award-row-button-" + no.toString()).text('Save').val('Save').removeClass('btn-primary').addClass('btn-success');
    }
    else if($("#award-row-button-" + no.toString()).val() === "Save"){
        if($("#award-row-organization-" + no.toString()).val() !== '' && $("#award-row-year-" + no.toString()).val() !== '' && $("#award-row-title-" + no.toString()).val() !== ''){

            $("#award-row-organization-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#award-row-year-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#award-row-title-" + no.toString()).prop('readonly', true).addClass('text-muted');


            if($("#award-row-organization-" + no.toString()).val() !== data.awards[no - 1].organization || $("#award-row-year-" + no.toString()).val() !== data.awards[no - 1].year || $("#award-row-title-" + no.toString()).val() !== data.awards[no - 1].title){

                $("#award-row-button-" + no.toString()).text('Saving...').prop('disabled', true);

                ssbtSocket.send(JSON.stringify({
                    'process': 'awards-edit',
                    'data':{
                        'teacher': data.designation.teacher,
                        'id': $("#award-row-id-" + no.toString()).val(),
                        'organization': $("#award-row-organization-" + no.toString()).val(),
                        'year': $("#award-row-year-" + no.toString()).val(),
                        'title': $("#award-row-title-" + no.toString()).val(),
                        'row': no,
                    }
                }))
            }
            else{
                alert("Nothing is changed..!")
                $("#award-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
            }
        }
        else{
            alert("Empty field Not Allowed..!")
        }
    }
}

function edit_project(no){
    if($("#project-row-button-" + no.toString()).val() === "Edit"){
        $("#project-row-name-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#project-row-year-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#project-row-level-" + no.toString()).prop('readonly', false).removeClass('text-muted');

        $("#project-row-button-" + no.toString()).text('Save').val('Save').removeClass('btn-primary').addClass('btn-success');
    }
    else if($("#project-row-button-" + no.toString()).val() === "Save"){
        if($("#project-row-name-" + no.toString()).val() !== '' && $("#project-row-year-" + no.toString()).val() !== '' && $("#project-row-level-" + no.toString()).val() !== ''){

            $("#project-row-name-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#project-row-year-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#project-row-title-" + no.toString()).prop('readonly', true).addClass('text-muted');


            if($("#project-row-name-" + no.toString()).val() !== data.projects[no - 1].name || $("#project-row-year-" + no.toString()).val() !== data.projects[no - 1].year || $("#project-row-level-" + no.toString()).val() !== data.projects[no - 1].level){

                $("#project-row-button-" + no.toString()).text('Saving...').prop('disabled', true);

                ssbtSocket.send(JSON.stringify({
                    'process': 'projects-edit',
                    'data':{
                        'teacher': data.designation.teacher,
                        'id': $("#project-row-id-" + no.toString()).val(),
                        'name': $("#project-row-name-" + no.toString()).val(),
                        'year': $("#project-row-year-" + no.toString()).val(),
                        'level': $("#project-row-level-" + no.toString()).val(),
                        'row': no,
                    }
                }))
            }
            else{
                alert("Nothing is changed..!")
                $("#project-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
            }
        }
        else{
            alert("Empty field Not Allowed..!")
        }
    }
}

function edit_eca(no){
    if($("#eca-row-button-" + no.toString()).val() === "Edit"){
        $("#eca-row-name-" + no.toString()).prop('readonly', false).removeClass('text-muted');
        $("#eca-row-year-" + no.toString()).prop('readonly', false).removeClass('text-muted');

        $("#eca-row-button-" + no.toString()).text('Save').val('Save').removeClass('btn-primary').addClass('btn-success');
    }
    else if($("#eca-row-button-" + no.toString()).val() === "Save"){
        if($("#eca-row-name-" + no.toString()).val() !== '' && $("#eca-row-year-" + no.toString()).val() !== ''){

            $("#eca-row-name-" + no.toString()).prop('readonly', true).addClass('text-muted');
            $("#eca-row-year-" + no.toString()).prop('readonly', true).addClass('text-muted');


            if($("#eca-row-name-" + no.toString()).val() !== data.ecas[no - 1].name || $("#eca-row-year-" + no.toString()).val() !== data.ecas[no - 1].year){

                $("#eca-row-button-" + no.toString()).text('Saving...').prop('disabled', true);

                ssbtSocket.send(JSON.stringify({
                    'process': 'ecas-edit',
                    'data':{
                        'teacher': data.designation.teacher,
                        'id': $("#eca-row-id-" + no.toString()).val(),
                        'name': $("#eca-row-name-" + no.toString()).val(),
                        'year': $("#eca-row-year-" + no.toString()).val(),
                        'row': no,
                    }
                }))
            }
            else{
                alert("Nothing is changed..!")
                $("#eca-row-button-" + no.toString()).text('Edit').val('Edit').removeClass('btn-success').addClass('btn-primary').prop('disabled', false);
            }
        }
        else{
            alert("Empty field Not Allowed..!")
        }
    }
}



