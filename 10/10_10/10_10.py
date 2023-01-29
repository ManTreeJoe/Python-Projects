filenames = 'World_of_chance.txt'

for filename in filenames:

    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
            print("\nReading " + contents)

    except FileNotFoundError:
        pass

    else:
        word = contents.split()
        num_word = word.count('the')

        print(f"The word the is seen {num_word} times in the book {filename}")


print('done')