import xml.etree.ElementTree as ET

# Define the XML data as a string
xml_data = '''
<library>
    <book>
        <title>Book 1</title>
        <author>Author 1</author>
        <year>2003</year>
    </book>
    <book>
        <title>Book 2</title>
        <author>Author 2</author>
        <year>2005</year>
    </book>
    <book>
        <title>Book 3</title>
        <author>Author 3</author>
        <year>2005</year>
    </book>
</library>
'''

# Parse the XML data string
root = ET.fromstring(xml_data)

# Define a function to run queries on the XML data
def run_queries():
    # Query 1: Retrieve all book titles and authors
    for book in root.findall('book'):
        title = book.find('title').text
        author = book.find('author').text
        print(f"Title: {title}, Author: {author}")

    # Query 2: Retrieve books published in the year 2005
    for book in root.findall('book'):
        year = book.find('year').text
        if year.startswith('2005'):
            title = book.find('title').text
            author = book.find('author').text
            print(f"Title: {title}, Author: {author}, Year: {year}")

# Run the queries
run_queries()
