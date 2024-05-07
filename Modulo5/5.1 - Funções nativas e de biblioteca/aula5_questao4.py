from datetime import datetime

data_formatada = datetime.now().strftime("%d/%m/%Y")
hora_formatada = datetime.now().strftime("%H:%M")

print("Data:", data_formatada)
print("Hora:", hora_formatada)
