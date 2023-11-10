import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('../../books.xml')
root = tree.getroot()

# Define a function to run queries on the XML data
def run_queries():
    # Query 1: Retrieve all book titles and authors
    for book in root.findall('book'):
        title = book.find('title').text
        author = book.find('author').text
        print(f"Title: {title}, Author: {author}")

    # Query 2: Retrieve books published in the year 2000
    for book in root.findall('book'):
        publish_date = book.find('publish_date').text
        if publish_date.startswith('2000'):
            title = book.find('title').text
            author = book.find('author').text
            print(f"Title: {title}, Author: {author}, Publish Date: {publish_date}")

# Run the queries
run_queries()
