from random import choice
from plotly.graph_objs import*
from plotly import offline


class RandomWalk:
    '''Generate random walks'''


    def __init__(self,points=5000):

        self.points = points


      
        self.x_values =[0]
        self.y_values = [0]


    def fill_walk(self):

        '''calculating all of the points in the walk'''

        while len(self.x_values) < self.points:

            x_direction = choice([-1, 1])
            x_distance = choice([0, 3])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 3])
            y_step = y_direction * y_distance

            # reject all moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)




rw = RandomWalk()
rw.fill_walk()

xa = list(range(rw.points))

frequencies = []

for a_number in (range(1,rw.points)):
    frequency = rw.x_values.count(a_number)
    frequencies.append(frequency)

data = [Bar(x=xa,y=frequencies)]

my_layout = Layout(title="We'll see",xaxis={'title':'X'},yaxis={'title':'Y'})

offline.plot({'data': data,'layout':my_layout},filename='my.html')