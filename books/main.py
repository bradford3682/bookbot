


def count_words(book):
    import string
    word_count=0
    book=book.split()
    word_count=len(book)
    
   
    
    return word_count

with open("frankenstien.txt") as f:
    file_contents = f.read()
    print(count_words(file_contents))
