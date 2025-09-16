
def convert_currency(dollars):
  
    peso = dollars * 57.17
    yen = dollars * 146.67
    return peso, yen 


user_input = input("Enter currency in ($): ")


dollar_amounts = [int(x.strip()) for x in user_input.split(",")]


print("\nDollar($)\tPeso(P)\t\tYen(Y)")


for d in dollar_amounts:
    peso, yen = convert_currency(d) 
    print(f"{d}\t\t{peso:,.2f}\t{yen:,.2f}")
