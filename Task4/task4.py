import lxml.etree as et

xml = et.parse("../Task3/task3.xml")
xsl = et.parse("task4.xsl")
transform = et.XSLT(xsl)
xml = transform(xml)

fileToWrite = "task4.html"

et.ElementTree(xml.getroot()).write(fileToWrite,encoding="utf-8", pretty_print=True)