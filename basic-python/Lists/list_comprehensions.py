even_numbers = [x for x in range(5) if x % 2 == 0]
squares = [x**2 for x in range(0:5)]
even_squares = [x**2 for x in range(5) if x % 2 == 0]

# turn lists into dictionaries or sets
square_dict = { x : x*x for x in range(5) }
square_set = {x * x for x in [-1, 1, 3, -3, -5, 5]}

zeroes = [0 for _ in even_numbers]  # same length as even_numbers

# list comprehensions can include more than one "for"
pairs = [(x, y)
         for x in range(10)
         for y in range(10)]   # 100 pairs (0,0), (0,1), ... (9,8), (9,9)

increasing_pairs = [(x, y)
                    for x in range(10)
                    for y in range(x + 1, 10)]
