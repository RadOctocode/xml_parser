from xml.dom import minidom
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import xml.etree.ElementTree as xml

tree = xml.parse("nexposeDiscovery.xml")

#parser = ET.XMLParser(encoding="utf-8")]
with open('nexposeDiscovery.xml','r') as f:
   content = f.readlines()

# from lxml import etree
# parser = etree.XMLParser(recover=True)
# etree.fromstring(xmlstring, parser=parser)

# import xml.dom.minidom
# import re

# # from http://boodebr.org/main/python/all-about-python-and-unicode#UNI_XML
# RE_XML_ILLEGAL = u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' + \
#                  u'|' + \
#                  u'([%s-%s][^%s-%s])|([^%s-%s][%s-%s])|([%s-%s]$)|(^[%s-%s])' % \
#                   (unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),
#                    unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),
#                    unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff))
# x = u"<foo>text\u001a</foo>"
# x = re.sub(RE_XML_ILLEGAL, "?", x)
# print x
# dom = xml.dom.minidom.parseString(x.encode("utf-8"))


# for i in content:
#    print i
#    parseString(i)


# Get all the movies in the collection
#paragraph_tags = collection.getElementsByTagName("TableRow")

# Print detail of each movie.
#for para in paragraph_tags:
#   print "*****Movie*****"
#   if para.hasAttribute("title"):
#      print "CellTable %s" % para.getAttribute("TableRowNumber")

   # type = movie.getElementsByTagName('type')[0]
   # print "Type: %s" % type.childNodes[0].data
   # format = movie.getElementsByTagName('format')[0]
   # print "Format: %s" % format.childNodes[0].data
   # rating = movie.getElementsByTagName('rating')[0]
   # print "Rating: %s" % rating.childNodes[0].data
   # description = movie.getElementsByTagName('description')[0]
   # print "Description: %s" % description.childNodes[0].data

#88 row number 
#1 row level
