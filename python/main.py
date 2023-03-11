# Nome: William Rodrigues Spada
# RM : 98177

# Nome: Vinicius Prates Silva Cruz
# RM: 550285

# Nome: Yohana Bispo Menezes
# RM: 551430

# Nome: Samuel Giron Marciliano
# RM: 98693

# The exercise has requested to consider 30 days as a month 

daysInMonth=30;
monthsInYear=12;

yearsSmoking = float(input("Insira a quantidade de anos fumando: "));
priceCigarretePackage = float(input("Insira o preço médio do maço de cigarro, R$: "));
quantityCigarretePackagePerDay = float(input("Insira a quantidade média de maços consumidas por dia: "));

totalDaysSmoking = yearsSmoking*monthsInYear*daysInMonth;

totalPriceSpent = totalDaysSmoking*priceCigarretePackage*quantityCigarretePackagePerDay;

if totalPriceSpent < 20000:
    print("Com o valor R${:.2f}, você poderia ter dado entrada em um carro".format(totalPriceSpent));
elif totalPriceSpent >= 20000 and totalPriceSpent <= 50000:
    print("Com o valor R${:.2f}, você poderia ter comprado um carro popular usado".format(totalPriceSpent));
else:
    print("Com o valor R${:.2f}, você poderia ter comprado um carro zero".format(totalPriceSpent));
