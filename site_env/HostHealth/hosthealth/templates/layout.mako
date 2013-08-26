<html>
    <head>
        <title>${page_title}</title>
        <link rel="stylesheet" type="text/css" href="/static/css/main.css">
    </head>
    <body>
        <div class="global-wrapper">
            <div class="page-header">
                <%include file="blocks/header.mako"/>
            </div>

            <div class="page-content">
                <%block name="page_content"/>
            </div>

            <div class="global-buffer"></div>
        </div>

        <div class="global-footer">
            <%include file="blocks/footer.mako"/>
        </div>
    </body>
</html>

