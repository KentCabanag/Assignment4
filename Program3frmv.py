def getAmmountAplprice():
    _amt = float(input("Enter the ammount of money you have: "))
    _aplprice = float(input("Enter the price of an apple: "))
    return _amt, _aplprice

def getNappleChange(Ammount, Aplprice):
    _napple = int(Ammount//Aplprice)
    _change = Ammount % Aplprice
    return _napple, _change

ammount, aplprice = getAmmountAplprice()
napple, change = getNappleChange(ammount, aplprice)

print(f"You can buy {napple} apples and your change is {change:.2f} pesos.")