class minha_classe:
    greeting = ''
    def __init__(self,name='There'):
        self.greeting = name + '!'
    def say_hello(self):
        print(f'Hello {self.greeting}')


my_instance = minha_classe()

my_instance.say_hello()

my_instance1 = minha_classe('Zomito')

my_instance1.say_hello()
my_instance.greeting = 'Harry!'

my_instance.say_hello()

# print(my_instance.var)

# print(my_instance.__class__)

# print(dir(my_instance))