amount = float(input("Inserire denaro speso: "))
voucher = 0

if amount > 210:
	voucher = amount * .14
elif amount > 150:
	voucher = amount * .12
elif amount > 60:
	voucher = amount * .10
elif amount > 10:
	voucher = amount * .8

if voucher > 0:
	print(f"Hai ricevuto un buono sconto da {voucher:.2f}$ !")
else:
	print("Non hai ricevuto buoni sconot.")