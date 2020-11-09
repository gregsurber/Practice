def count_words(filename):
    """ Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
    

filenames = ['alice.txt', 'moby_dick.txt', 'little_women.txt', 'art_of_war.txt']
for filename in filenames:
    count_words(filename)