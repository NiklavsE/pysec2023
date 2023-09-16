# Order list of string by `a` char occurance
books = [
    "The Great Gatsby",
    "Emily Brontë, 'Wuthering Heights'",
    "Margaret Atwood, 'The Handmaid's Tale'",
    "Chinua Achebe, 'Things Fall Apart'",
]

def byACharOccurance(value):
    if value.count('a') > 0:
        return value.count('a')
    # If there are no `a` chars in list, set it to default -1, so that it is end of the list
    return -1

books.sort(key=byACharOccurance, reverse=True)

print(books)
