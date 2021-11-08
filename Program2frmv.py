def getAppleOrange():
    n_apple = int(input("Number of Apples you want to buy: "))
    n_orange = int(input("Number of Oranges you want to buy: "))
    return n_apple, n_orange

def getPrice(apl_num, org_num):
    apl_price = apl_num * 20
    org_price = org_num * 25
    t_price = apl_price + org_price
    return t_price

apple, orange = getAppleOrange()
g_total = getPrice(apple, orange)

print(f"The total ammount is {g_total}.")