def build_a_sammy(*items):
    print("Welcome to Build-a-Sammy. \nLet me built you the best sandwich from thee ditch!")
    for item in items:
        print(f"  ...slappin on {item} to your sandwich.")
    print("Your sammy is ready!")

print('\n')
build_a_sammy('lettuce', 'mustard', 'ham', 'ham', 'ham', 'subaru wrx')
print('\n')
build_a_sammy('feta cheese', 'beef', 'tomato', 'peanutbutter')
print('\n')
build_a_sammy('fried chicken', 'maple syrup', 'waffles')