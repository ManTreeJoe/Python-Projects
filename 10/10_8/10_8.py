filenames = ['cat.txt','dog.txt']

for filename in filenames:

    try:
        with open(filename) as f:
            names = f.read()
            print("\nReading " + filename)
            print(names)

    except FileNotFoundError:
        print(f"  File {filename} does not exist in this realm")

print('done')