
cities = {'orange':  {'fact':'doesnt have any orange orchirds as you would think', 'country':'U.S.', 'pop':'140,000'}, 'yekaterinburg':{'fact':'Largest city in Urals', 'country':'Russia', 'pop':'1.4 million'}, 'arad': {'fact':'Home of the neoclassical Ioan Slavici Theater', 'country':"Romania", 'pop':'160,000'}}




for city, city_info in cities.items():
    fact = city_info['fact'].title()
    country = city_info['country'].title()
    pop = city_info['pop']
    print(f"\n {city.title()}")
    print('  It is located in', country)
    print('  It has a population of about', str(pop))
    print('  Random Fact:', fact )    

print('\n')
