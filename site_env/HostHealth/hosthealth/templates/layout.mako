<html>
    <head>
        <title>${page_title}</title>
        <link rel="stylesheet" type="text/css" href="/static/css/main.css">
    </head>
    <body>
        <div class="global-wrapper">
            <div id="page-header">
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
</html>

