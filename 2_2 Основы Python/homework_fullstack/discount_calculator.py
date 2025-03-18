# расчет скидки

amount = float(input("Введите сумму покупки: "))
discount = float(input("Введите процент скидки: "))

saving = amount * (discount / 100)
final_amount = round(amount - saving)

print(f"Вы экономите: {saving:.2f}")
print(f"Сумма к оплате (округлено): {final_amount}")
