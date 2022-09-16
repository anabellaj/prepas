saldo = 3480
fecha = '2020/04/10'
print (f'El saldo inicial para {fecha} es de ${saldo}')

saldo -= 96
fecha = '2020/04/11'
print ('Se han retirado $96')
print (f'El saldo actual para {fecha} es de ${saldo}')

saldo += 1200
fecha = '2020/04/17'
print ('Se ha cobrado un salario de $1200')
print (f'El saldo actual para {fecha} es de ${saldo}')

saldo = saldo + saldo*0.03
fecha = '2020/04/30'
print ('Se ha cobrado un interes de 3%')
print (f'El saldo actual para {fecha} es de ${saldo}') 

saldo -= 51
fecha = '2020/05/02'
print ('Se han retirado $51')
print (f'El saldo final para {fecha} es de ${saldo}')