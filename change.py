def change():
    expense = 23.75
    money = 100
    print(f"{"Ingresar gasto: "}"+ " " + f"\n{expense}")
    print(f"{"Dinero recibido: "}"+ " " + f"\n{money}")
    print(f"{"Vuelto: "}"+ " " + f"\n{""}")
    print(f"{"Pesos: "}"+ " " + f"\n{int(money - expense)}")
    print(f"{"Centavos: "}"+ " " + f"\n{(money - expense) - int(money - expense)}")
    
