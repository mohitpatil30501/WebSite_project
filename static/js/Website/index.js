// Loader
$(window).on("load",function(){
	$('.loader-wrapper, .page-wrapper').hide()
	$(".page-wrapper").removeClass("d-none");
	$('.loader-wrapper').fadeIn(500).fadeOut(1000);
	$('.page-wrapper').delay(500).fadeIn(2800)
});

// Socket
var loc = window.location
var wsStart = 'ws://'
if(loc.protocol == 'https:'){
    wsStart = 'wss://'
}
var endpoint = wsStart + loc.host + '/user/' + create_UUID()
chatSocket = new ReconnectingWebSocket(endpoint)

var signup_verify_process = 0
var signup_create_process = 0
var userdata = null

var username_status = false
var password_status = false

$(document).on('click', "#submit-create-form", function(e){
    e.preventDefault();
    if($("#first_name").val() === '' || $("#last_name").val() === '' || $("#set_email").val() === '' || $("#set_username").val() === '' || $("#set_password").val() === '' || $("#retype_password").val() === '' ){
        alert("All fields are Compulsory to Fill...!");
    }
    else{
        if(isEmail($("#set_email").val())){
            var password = $("#set_password").val()
            var retype_password = $("#retype_password").val()
            if(username_status){
                if(password_status){
                    if(password === retype_password){
                        $("#signup-create-form").submit();
                    }
                    else{
                        alert("Password and Retype password are Not Matching...!");
                    }
                }
                else{
                    alert("Choosen Password not Satisfying requirements...!");
                }
            }
            else{
                alert("Choosen Username not Satisfying requirements...!");
            }
        }
        else{
            alert("Wrong Email Format...!");
        }
    }
    return false;
})

$(document).on('input', "#retype_password", function(e){
    var password = $("#set_password").val()
    var retype_password = $("#retype_password").val()
    if(password === retype_password){
        $("#retype_password").removeClass('border border-danger');
        $("#set_password").removeClass('border border-danger');
        $("#retype_password").addClass('border border-success');
        $("#set_password").addClass('border border-success');
    }
    else if(retype_password === ''){
        $("#retype_password").removeClass('border border-danger');
        $("#set_password").removeClass('border border-danger');
        $("#retype_password").removeClass('border border-success');
        $("#set_password").removeClass('border border-success');
    }
    else{
        $("#retype_password").removeClass('border border-success');
        $("#set_password").removeClass('border border-success');
        $("#retype_password").addClass('border border-danger');
        $("#set_password").addClass('border border-danger');
    }
    return false;
})

$(document).on('input', "#set_password", function(e){
    var password = $("#set_password").val()
    var username = $("#set_username").val()
    if(password === '' || password.length <= 2){
        $("#set_password").val(password)
        $("#create-message-password").text('');
        $("#create-message-password").addClass('d-none');
        password_status = false;
    }
    else{
        chatSocket.send(JSON.stringify({
                    'process': 'password-availability',
                    'username': username,
                    'password': password
                }))
    }

    if($("#retype_password").val() !== '')
    {
        var retype_password = $("#retype_password").val()
        if(password === retype_password){
            $("#retype_password").removeClass('border border-danger');
            $("#set_password").removeClass('border border-danger');
            $("#retype_password").addClass('border border-success');
            $("#set_password").addClass('border border-success');
        }
        else{
            $("#retype_password").removeClass('border border-success');
            $("#set_password").removeClass('border border-success');
            $("#retype_password").addClass('border border-danger');
            $("#set_password").addClass('border border-danger');
        }
    }
    return false;
})

$(document).on('input', "#set_username", function(e){
    var username = $("#set_username").val()
    if(username === '' || username.length <= 3){
        $("#set_username").val(username)
        $("#create-message-username").text('');
        $("#create-message-username").addClass('d-none');
        username_status = false;
    }
    else{
        chatSocket.send(JSON.stringify({
                    'process': 'username-availability',
                    'username': username
                }))
    }
    return false;
})

$(document).on('submit', "#signup-verify-form", function(e){
    e.preventDefault();
    var prn = $("#prn").val()
    var mother_name = $("#mother_name").val()
    chatSocket.send(JSON.stringify({
                'process': 'signup-verify',
                'data':{'prn': prn,
                        'mother_name': mother_name}
            }))
    return false;
})

chatSocket.onopen = function(e) {
    console.log("open", e)
    if($("#loading_signup").length){
        $("#loading_signup").remove()
    }

    if($("#signup_verify").length == 0 && signup_verify_process == 0){
        var signup_verify_form = '<div id="signup_verify"><h3 class="py-3">Join As Student</h3><div class="container m-auto text-center" style="max-width:480px;"><form class="text-center" method="post" action="" id="signup-verify-form"><p class="montserrat-alt text-left text-danger py-1" id="verify-message"></p><div class="form-group"><input type="text" class="form-control righteous" name="prn" id="prn" placeholder="PRN" autocomplete="off" required></div><div class="form-group"><input type="text" class="form-control righteous" name="mother_name" id="mother_name" autocomplete="off" placeholder="Mother Name" required></div><div class="text-right my-3"><button type="submit" id="submit-verify" class="btn btn-primary righteous rounded-pill text-center" style="width:50%;font-weight:bold">Verify</button></div></form></div></div>'
        $("#student").append(signup_verify_form)
    }

    if($("#signup_create").length == 0 && signup_create_process == 0 && signup_verify_process == 1){
        if($("#signup_verify").length == 1){
            $("#signup_verify").remove()
        }
        var signup_create_form = '<div id="signup_create"><h3 class="py-3">Fill Form As Student</h3><div class="container m-auto text-center" style="max-width:480px;"><form class="text-center" method="post" action="account/signup/createuser" id="signup-create-form"><div class="form-group"><input type="text" class="form-control righteous" name="prn" id="prn" readonly required></div><div class="d-none form-group"><input type="text" class="form-control righteous" name="mother_name" id="mother_name" readonly required></div><div class="d-none form-group"><input type="text" class="form-control righteous" name="name" id="name" readonly required></div><div class="row"><div class="col-sm form-group"><input type="text" class="form-control righteous" name="first_name" id="first_name" placeholder="First Name" autocomplete="off" required></div><div class="col-sm form-group"><input type="text" class="form-control righteous" name="last_name" id="last_name" placeholder="Last Name" autocomplete="off" required></div></div><div class="form-group"><input type="email" class="form-control righteous" name="email" id="set_email" placeholder="Enter Email" autocomplete="off" required></div><div class="form-group"><input type="text" class="form-control righteous" name="username" id="set_username" placeholder="Set Username" autocomplete="off" required></div><div class="alert montserrat-alt d-none" role="alert" id="create-message-username" ></div><div class="form-group"><input type="password" class="form-control righteous" name="password" id="set_password" placeholder="Set Password" required></div><div class="alert montserrat-alt d-none" role="alert" id="create-message-password"></div><div class="form-group"><input type="password" class="form-control righteous" name="retype_password" id="retype_password" placeholder="Retype Password" required></div><div class="text-right my-3"><button type="button" class="btn btn-primary righteous rounded-pill text-center" id="submit-create-form" style="width:50%;font-weight:bold">Signup</button></div></form></div></div>'
        $("#student").append(signup_create_form)
        $("#prn").val(userdata['prn']);
        $("#name").val(userdata['name']);
        $("#first_name").val(userdata['first_name']);
        $("#last_name").val(userdata['last_name']);
        $("#mother_name").val(userdata['mother_name']);
    }
};

chatSocket.onclose = function(e) {
    console.log('close', e);
    if($("#signup_verify").length){
        $("#signup_verify").remove()
    }

    if($("#signup_create").length){
        $("#signup_create").remove()
    }

    if($("#loading_signup").length == 0){
        $("#student").append('<p class="text-danger text-center py-3" id="loading_signup">Wait for connecting to Server</p>')
    }
};

chatSocket.onerror = function(e){
    console.error("error", e)
}

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log('message', data)
    if(data['process'] === 'signup-verify'){
        if(data['status'] == false){
            $("#verify-message").text(data['error']);
        }
        else{
            signup_verify_process = 1

            if($("#signup_verify").length){
                $("#signup_verify").remove()
            }

            var signup_create_form = '<div id="signup_create"><h3 class="py-3">Fill Form As Student</h3><div class="container m-auto text-center" style="max-width:480px;"><form class="text-center" method="post" action="account/signup/createuser" id="signup-create-form"><div class="form-group"><input type="text" class="form-control righteous" name="prn" id="prn" readonly required></div><div class="d-none form-group"><input type="text" class="form-control righteous" name="mother_name" id="mother_name" readonly required></div><div class="d-none form-group"><input type="text" class="form-control righteous" name="name" id="name" readonly required></div><div class="row"><div class="col-sm form-group"><input type="text" class="form-control righteous" name="first_name" id="first_name" placeholder="First Name" autocomplete="off" required></div><div class="col-sm form-group"><input type="text" class="form-control righteous" name="last_name" id="last_name" placeholder="Last Name" autocomplete="off" required></div></div><div class="form-group"><input type="email" class="form-control righteous" name="email" id="set_email" placeholder="Enter Email" autocomplete="off" required></div><div class="form-group"><input type="text" class="form-control righteous" name="username" id="set_username" placeholder="Set Username" autocomplete="off" required></div><div class="alert montserrat-alt d-none" role="alert" id="create-message-username" ></div><div class="form-group"><input type="password" class="form-control righteous" name="password" id="set_password" placeholder="Set Password" required></div><div class="alert montserrat-alt d-none" role="alert" id="create-message-password"></div><div class="form-group"><input type="password" class="form-control righteous" name="retype_password" id="retype_password" placeholder="Retype Password" required></div><div class="text-right my-3"><button type="button" class="btn btn-primary righteous rounded-pill text-center" id="submit-create-form" style="width:50%;font-weight:bold">Signup</button></div></form></div></div>'
            $("#student").append(signup_create_form)
            userdata = data['data']
            $("#prn").val(userdata['prn']);
            $("#name").val(userdata['name']);
            $("#first_name").val(userdata['first_name']);
            $("#last_name").val(userdata['last_name']);
            $("#mother_name").val(userdata['mother_name']);
        }
    }
    else if(data['process'] === 'username-availability'){
        $("#create-message-username").removeClass('d-none');
        if(data['status'] == false){
            $("#create-message-username").text('Username Not Available');
            $("#create-message-username").removeClass('alert-success');
            $("#create-message-username").addClass('alert-danger');
            $("#set_username").removeClass('border border-success');
            $("#set_username").addClass('border border-danger');
            username_status = false;
        }
        else{
            $("#create-message-username").text('');
            $("#create-message-username").removeClass('alert-danger');
            $("#create-message-username").addClass('d-none');
            $("#set_username").removeClass('border border-danger');
            $("#set_username").addClass('border border-success');
            username_status = true;
        }
    }
    else if(data['process'] === 'password-availability'){
        $("#create-message-password").removeClass('d-none');
        if(data['status'] == false){
            $("#create-message-password").text(data['error']);
            $("#create-message-password").removeClass('alert-success');
            $("#create-message-password").addClass('alert-danger');
            password_status = false;
        }
        else{
            $("#create-message-password").text(data['data']);
            $("#create-message-password").removeClass('alert-danger');
            $("#create-message-password").addClass('d-none');
            password_status = true;
        }
    }
};

function create_UUID(){
    var dt = new Date().getTime();
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (dt + Math.random()*16)%16 | 0;
        dt = Math.floor(dt/16);
        return (c=='x' ? r :(r&0x3|0x8)).toString(16);
    });
    return uuid;
}

function isEmail(email) {
  var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
}
