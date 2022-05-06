function login() {
    $.ajax({
        type: "POST",
        url: "/signup",
        data: {
            insta_id_give: $('#user-id').val(),
            password_give: $('#user-pw').val()
        },
        success: function (response) {
            if (response['result'] == 'success') {
                $.cookie('mytoken', response['token']);

                alert('로그인 완료')
                window.location.href = '/'
            } else {
                alert(response['msg'])
            }
        }
    })
}

function signup() {
    $.ajax({
        type: 'POST',
        url: '/',
        data: {
            sign_email_give : $('#user-signup-id').val(),
            sign_password_give : $('#user-signup-pw').val()
        },
        success: function (response) {
            alert(response['msg'])
            window.location.reload();
        }
    });
}