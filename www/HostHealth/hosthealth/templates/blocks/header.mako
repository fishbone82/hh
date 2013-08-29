<a href='/' id="hh-logo">
    <img src="/static/img/logo.png" width="80" height="80">HostHealth
</a>
<span style="float: right; margin-right: 15px; margin-top: 35px;">
    %if 'user_id' in session:
        Hi user # ${session['user_id']} &nbsp<a href='/logout'>Logout</a>
    %else:
        <a href='/login'>Login</a> or <a href='/register'>Create Account</a>
    %endif

</span>