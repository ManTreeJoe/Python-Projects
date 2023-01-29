filenames = ['cat1.txt','dog.txt']

for filename in filenames:

    try:
        with open(filename) as f:
            names = f.read()
            print("\nReading " + filename)
            print(names)

    except FileNotFoundError:
        pass

print('done')