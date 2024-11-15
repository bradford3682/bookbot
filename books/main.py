def main():
    book_location="frankenstien.txt"
    text = read_book(book_location)
    characters=count_characters(text)
    num_of_words=count_words(text)
    print("{} number of words in this file{}".format(num_of_words,book_location))
    print_character_count(characters)

def count_characters(book):
    import string
    character_count=0
    characters ={}
    book=str(book)
    lowered_string= book.lower()
    for word in lowered_string:
        if word in characters and word.isalpha():
            characters[word]+=1
        elif word.isalpha():
            characters[word]=1
    return characters
            
def print_character_count(characters):
    for key,value in characters.items():
        print("The {} character occurs {} times".format(key,value))


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