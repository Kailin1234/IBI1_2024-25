import datetime
start = datetime.datetime.now()
import xml.dom.minidom
dom_tree = xml.dom.minidom.parse("go_obo.xml") # The file path should be passed as a string and enclosed in quotation marks
terms = dom_tree.getElementsByTagName("term")
max_is_a = {
    "molecular_function":{"count":0, "id":"", "name":""},
    "biological_process":{"count":0, "id":"", "name":""},
    "cellular_component":{"count":0, "id":"", "name":""}
}
for term in terms:
    id = term.getElementsByTagName("id")[0].firstChild.nodeValue
    name = term.getElementsByTagName("name")[0].firstChild.nodeValue
    namespace = term.getElementsByTagName("namespace")[0].firstChild.nodeValue
    is_a = term.getElementsByTagName("is_a")
    if namespace in max_is_a:
        if len(is_a) > max_is_a[namespace]["count"]:
            max_is_a[namespace]["count"] = len(is_a)
            max_is_a[namespace]["id"] = id
            max_is_a[namespace]["name"] = name

for namespace in max_is_a:
    print(f"{namespace}: {namespace}, ID: {max_is_a[namespace]['id']}, Name: {max_is_a[namespace]['name']}, Count: {max_is_a[namespace]['count']}")

end = datetime.datetime.now()
print("Execution time of DOM:", end - start)

print("--------------------")

start = datetime.datetime.now()
import xml.sax
class BioHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.id = ""
        self.name = ""
        self.namespace = ""
        self.count = 0
        self.max_is_a = {
            "molecular_function": {"count": 0, "id": "", "name": ""},
            "biological_process": {"count": 0, "id": "", "name": ""},
            "cellular_component": {"count": 0, "id": "", "name": ""}
        }
    
    def startElement(self, name, attr):
        self.current_data = name # set current_data to the tag name
        if name == "term":
            self.id = ""
            self.name = ""
            self.namespace = ""
            self.count = 0
    
    def characters(self, content):
        if self.current_data == "id":
            self.id += content.strip()
        elif self.current_data == "name":
            self.name += content.strip()
        elif self.current_data == "namespace":
            self.namespace += content.strip()
            
    def endElement(self, name):
        if name == "is_a":
            self.count += 1
        elif name == "term":
            if self.namespace in self.max_is_a:
                if self.count > self.max_is_a[self.namespace]["count"]:
                    self.max_is_a[self.namespace]["count"] = self.count
                    self.max_is_a[self.namespace]["id"] = self.id
                    self.max_is_a[self.namespace]["name"] = self.name

parser = xml.sax.make_parser()
handler = BioHandler()
parser.setContentHandler(handler)
parser.parse("go_obo.xml") # The file path should be passed as a string and enclosed in quotation marks
for namespace in handler.max_is_a:
    print(f"{namespace}: {namespace}, ID: {handler.max_is_a[namespace]['id']}, Name: {handler.max_is_a[namespace]['name']}, Count: {handler.max_is_a[namespace]['count']}")


end = datetime.datetime.now()
print("Execution time of SAX:", end - start)

# SAX is faster than DOM.