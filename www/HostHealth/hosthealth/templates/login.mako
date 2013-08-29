<%! page_title = 'HostHealth::Login' %>

<%inherit file="layout.mako"/>

<%block name="page_content">
    <div style="height:100px"></div>
    <div class="dialog" style="width: 220px;">
        <form class="form-horizontal" style="margin-bottom:0" method="POST">
            <div class="control-group">
                <input type="text" id="email" name="email" placeholder="Email">
            </div>
            <div class="control-group">
                <input type="password" id="password" name="password" placeholder="Password">
            </div>
            <button type="submit" class="btn">Sign in</button>
            %if error:
                <span class="label label-important" style="margin-top:10px;">${error}</span>
            %endif
        </form>
    </div>
</%block>

<%block name="js">
    $(document).ready(function(){
        $("#email").focus();
    });
</%block>
