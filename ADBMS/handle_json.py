import json

# Define the JSON data as a string
json_data = '''
{
    "library": [
        {
            "title": "Book 1",
            "author": "Author 1",
            "year": "2003"
        },
        {
            "title": "Book 2",
            "author": "Author 2",
            "year": "2005"
        },
        {
            "title": "Book 3",
            "author": "Author 3",
            "year": "2005"
        }
    ]
}
'''

# Parse the JSON data string
data = json.loads(json_data)

# Define a function to run queries on the JSON data
def run_queries():
    # Query 1: Retrieve all book titles and authors
    for book in data['library']:
        title = book['title']
        author = book['author']
        print(f"Title: {title}, Author: {author}")

    # Query 2: Retrieve books published in the year 2005
    for book in data['library']:
        year = book['year']
        if year.startswith('2005'):
            title = book['title']
            author = book['author']
            print(f"Title: {title}, Author: {author}, Year: {year}")

# Run the queries
run_queries()
