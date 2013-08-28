<%inherit file="layout.mako"/>

<%block name="page_content">
    <div style="height:30%"></div>
    <form method="GET">
    <div id="loginbox">
        <table>
            <tr>
                <td><label for="login">Login</label></td>
                <td><input id="login" name="login" type="text"  style="width: 160px"></td>
            </tr>
            <tr>
                <td><label for="password">Password</label></td>
                <td><input name="password" id="password" type="password" style="width: 160px"></td>
            </tr>
            <tr>
                <td>&nbsp</td>
                <td><input style="float:right" type="submit"></td>
        </table>
    </div>
    </form>

</%block>
