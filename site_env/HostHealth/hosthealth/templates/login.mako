<%inherit file="layout.mako"/>

<%block name="page_content">
    <form method="GET">
        <label for="login">Login</label><input id="login" name="login" type="text">
        <label for="password">Password</label><input name="password" id="password" type="password">
        <input type="submit">
    </form>

</%block>
