# Importing the required library: datetime, to record the execuetion time of the code

import datetime # Importing the datetime module to work with dates and times

# For DOM approach:
# 1. Importing the xml.dom.minidom module to work with XML files
# 2. Parsing the targeted file using the parse method
# 3. Gathering all the terms using the getElementsByTagName method
# 4. Initializing a dictionary to store the max_is_a values for namespaces
# 5. Iterating all the terms to get the id, name, namespace, and is_a elements
# 6. Checking if the namespace is in the max_is_a dictionary, and updating the values if meet the maximum is_a count condition
# 7. Iterating the max_is_a dictionary based on the namespace to output the results
# 8. Getting the current date and time to calculate the execution time of the DOM approach

start = datetime.datetime.now() # Getting the current date and time

import xml.dom.minidom # Importing this module to work with XML files using DOM approach
dom_tree = xml.dom.minidom.parse("go_obo.xml") # Parsing the targeted file and the file path should be passed as a string and enclosed in quotation marks
terms = dom_tree.getElementsByTagName("term") # Getting elemnents by tag name to gather all the terms, which are stored in a list
max_is_a = {
    "molecular_function":{"count":0, "id":"", "name":""},
    "biological_process":{"count":0, "id":"", "name":""},
    "cellular_component":{"count":0, "id":"", "name":""}
} # Initializing a dictionary to store the max_is_a values for namespaces, including count, id, and term name.
for term in terms: # Iterating all the terms
    id = term.getElementsByTagName("id")[0].firstChild.nodeValue # Getting the id of the term, and the first element is selected. FirstChild is used to get the text node and nodeValue is used to get the value 
    name = term.getElementsByTagName("name")[0].firstChild.nodeValue # Getting the name of the term
    namespace = term.getElementsByTagName("namespace")[0].firstChild.nodeValue # Getting the namespace of the term, used to identify the type of term
    is_a = term.getElementsByTagName("is_a") # Getting the is_a elements of the term, which are stored in a list
    if namespace in max_is_a: # Checking if the namespace is in the max_is_a dictionary
        if len(is_a) > max_is_a[namespace]["count"]: # Looking for the maximum is_a count
            max_is_a[namespace]["count"] = len(is_a) # Updating the count of the max_is_a dictionary
            max_is_a[namespace]["id"] = id # Updating the id of the max_is_a dictionary
            max_is_a[namespace]["name"] = name # Updating the name of the max_is_a dictionary

for namespace in max_is_a: # Iterating the max_is_a dictionary based on the namespace
    print(f"{namespace}: {namespace}, ID: {max_is_a[namespace]['id']}, Name: {max_is_a[namespace]['name']}, Count: {max_is_a[namespace]['count']}") # Outputting the results

end = datetime.datetime.now() # Getting the current date and time
print("Execution time of DOM:", end - start) # Printing the execution time of the DOM approach

print("--------------------")

# For SAX approach:
# 1. Importing the xml.sax module to work with XML files
# 2. Creating a class to handle the XML content
# 3. Initializing the class with empty strings and a dictionary to store the max_is_a values for namespaces
# 4. Defining the startElement method to set the current_data to the tag name and initialize the values
# 5. Defining the characters method to add the content to the id, name, and namespace
# 6. Defining the endElement method to increment the count and update the max_is_a dictionary if meet the maximum is_a count condition
# 7. Creating a parser object and setting the content handler to the parser
# 8. Parsing the targeted file using the parse method
# 9. Iterating the max_is_a dictionary based on the namespace to output the results
# 10. Getting the current date and time to calculate the execution time of the SAX approach

start = datetime.datetime.now() # Getting the current date and time

import xml.sax # Importing this module to work with XML files using SAX approach
class BioHandler(xml.sax.ContentHandler): # Creating a class to handle the XML content
    def __init__(self): # Initializing the class
        self.current_data = "" # Setting current_data to an empty string
        self.id = "" # Setting id to an empty string
        self.name = "" # Setting name to an empty string
        self.namespace = "" # Setting namespace to an empty string
        self.count = 0 # Setting count to 0
        self.max_is_a = {
            "molecular_function": {"count": 0, "id": "", "name": ""},
            "biological_process": {"count": 0, "id": "", "name": ""},
            "cellular_component": {"count": 0, "id": "", "name": ""}
        } # Initializing a dictionary to store the max_is_a values for namespaces, including count, id, and term name.
    
    def startElement(self, name, attr): # Defining the startElement method: self is the instance of the class, name is the name of the element, and attr is the attributes of the element
        self.current_data = name # Setting current_data to the tag name
        if name == "term": # Checking if the name is term and initializing the values
            self.id = "" # Setting id to an empty string
            self.name = "" # Setting name to an empty string
            self.namespace = "" # Setting namespace to an empty string
            self.count = 0 # Setting count to 0
    
    def characters(self, content): # Defining the characters method: self is the instance of the class and content is the text content of the element
        if self.current_data == "id": # Checking if the current_data is id
            self.id += content.strip() # Adding the content to the id
        elif self.current_data == "name": # Checking if the current_data is name
            self.name += content.strip() # Adding the content to the name
        elif self.current_data == "namespace": # Checking if the current_data is namespace
            self.namespace += content.strip() # Adding the content to the namespace
            
    def endElement(self, name): # Defining the endElement method: self is the instance of the class and name is the name of the element
        if name == "is_a": # Checking if the name is is_a
            self.count += 1 # Incrementing the count
        elif name == "term": # Checking if the name is term
            if self.namespace in self.max_is_a: # Checking if the namespace is in the max_is_a dictionary
                if self.count > self.max_is_a[self.namespace]["count"]: # Looking for the maximum is_a count
                    self.max_is_a[self.namespace]["count"] = self.count # Updating the count of the max_is_a dictionary
                    self.max_is_a[self.namespace]["id"] = self.id # Updating the id of the max_is_a dictionary
                    self.max_is_a[self.namespace]["name"] = self.name # Updating the name of the max_is_a dictionary

parser = xml.sax.make_parser() # Creating a parser object
handler = BioHandler() # Creating an instance of the BioHandler class
parser.setContentHandler(handler) # Setting the content handler to the parser
parser.parse("go_obo.xml") # The file path should be passed as a string and enclosed in quotation marks
for namespace in handler.max_is_a: # Iterating the max_is_a dictionary based on the namespace
    print(f"{namespace}: {namespace}, ID: {handler.max_is_a[namespace]['id']}, Name: {handler.max_is_a[namespace]['name']}, Count: {handler.max_is_a[namespace]['count']}") # Outputting the results


end = datetime.datetime.now() # Getting the current date and time
print("Execution time of SAX:", end - start) # Printing the execution time of the SAX approach

# Answer:
# SAX is faster than DOM.