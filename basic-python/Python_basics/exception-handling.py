def suggest(product_idea):
    if len(product_idea) < 3:
        raise ValueError("<<TYPE HERE THE REASON FOR THE ERROR>>")
    try:
        return product_idea + "inator"
    except ValueError as err:
        print(err)

z = suggest('spam')
print(z)
