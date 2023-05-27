try:
    d = 'ai'
    a = 2 
    int(d)
    b = 0
    c = a/d
except ZeroDivisionError:
    print('Dividiu por zero')
except (TypeError, ValueError) as error:
    print('Msg:', error)
    print('Nome:', error.__class__.__name__)