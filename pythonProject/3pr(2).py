
def price(x):
	if((x > 0) and (x == 1)): # Условие при одной позиции
		return 10.95 #Возвращает стартовую цену
	elif(x > 0):
		return (x-1)*2.95+10.95 #Подсчет итоговой цены
	else:
		return 0
print('Магазин практических работ по бд')
print('В выбранной функции экспресс-доставка цена первого товара: 10.95$. А за каждый следующий - 2.95$.')
count = int(input('Введите количество товаров, которое вы хотите купить: '))
print(f'{price(count):,.2f}$ - цена за все практические работы')