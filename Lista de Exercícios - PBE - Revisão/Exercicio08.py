# EXERCÍCIO 08 - CONVERSOR DE TEMPERATURA

print(f"{"="*5} EXERCÍCIO 08 - CELSIUS --> FAHRENHEIT {"="*5}")
print("Bem vindo ao conversor de temperatura, segue a baixo as temperaturas que foram convertidas: ")
grausCelsius = ("   30.0", "  100.0", "    0.0")

print("ºCELSIUS ----> ºFAHRENHEIT")
for celsius in grausCelsius:
    fahreheit = (float(celsius)* (9/5)) + 32
    print(f" {celsius}º ----> {fahreheit:.1f}º")