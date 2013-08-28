<html>
    <head>
        <title>${page_title}</title>
        <link rel="stylesheet" type="text/css" href="/static/css/bootstrap.css">
        <link rel="stylesheet" type="text/css" href="/static/css/main.css">
        <script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
    </head>
    <body>
        <div class="global-wrapper">
            <div class="hh-page-header">
                <%include file="blocks/header.mako"/>
            </div>

            <div id="page-content">
                <%block name="page_content"/>
            </div>

            <div class="global-buffer"></div>
        </div>

        <div id="global-footer">
            <%include file="blocks/footer.mako"/>
        </div>
    </body>
    <!-- scripts here -->
    <script language="javascript">
        <%block name="js"/>
    </script>

</html>

