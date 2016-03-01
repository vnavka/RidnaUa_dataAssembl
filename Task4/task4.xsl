<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <meta charset="UTF-8" />
                <style>

                    td:hover{

                        cursor:pointer;
                        background-color:yellow;
                    }
                </style>
            </head>
            <body>
                <table border="3" align="center" cellpadding="5" width = "70%" >
                    <tr>
                        <th>Title</th>
                        <th>Description</th>
                        <th>Price</th>
                        <th />
                    </tr>

                    <xsl:for-each select="items/item">
                        <tr>
                            <td><xsl:value-of select="title"/></td>
                            <td><xsl:value-of select="description"/></td>
                            <td><xsl:value-of select="price"/></td>
                            <td>

                                <img>
                                    <xsl:attribute name="src">
                                        <xsl:value-of select="img"/>
                                    </xsl:attribute>
                                </img>
                            </td>
                        </tr>
                    </xsl:for-each>

                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>