import time as tm

tm.time()

antes = tm.time()

list = []

for i in range(0,1000):
  list.append(i)

depois = tm.time()

print(depois - antes)



print('Finalizando...')
tm.sleep(2)
print('...')
tm.sleep(2)
print('Finalizado')