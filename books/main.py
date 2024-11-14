def main():
    
    book_location="frankenstien.txt"
    text = read_book(book_location)
    num_of_words=count_words(text)
    print("{} number of words in this file{}".format(num_of_words,book_location))

def count_words(book):
    import string
    word_count=0
    book=book.split()
    word_count=len(book)
    return word_count

def read_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
main()