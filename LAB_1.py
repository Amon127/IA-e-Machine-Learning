class CuradorEstilo:
    def __init__(self):
        self.regras = {}

    def fit(self):
        self.regras = {'frio': {'chuvoso': ['Casaco impermeável', 'Botas impermeáveis', 'Calça impermeável'], 'nublado': ['Casaco de lã', 'Calça jeans', 'Gorro'], 'ensolarado': ['Casaco', 'Calça jeans', 'Gorro']}, 'ameno': {'chuvoso': ['Jaqueta impermeável', 'Calça jeans', 'Guarda-chuva'], 'nublado': ['Jaqueta', 'Calça jeans', 'Tênis'], 'ensolarado': ['Camiseta', 'Calça jeans', 'Tênis']}, 'calor': {'chuvoso': ['Shorts', 'Camiseta leve', 'Guarda-chuva'], 'nublado': ['Shorts', 'Camiseta leve', 'Boné'], 'ensolarado': ['Shorts', 'Camiseta leve', 'Óculos de sol']}}

    def _classificar_temperatura(self, temp):
        return 'frio' if temp < 15 else 'ameno' if temp < 25 else 'calor'
    
    def predict(self, temp, clima):
        if clima.lower() not in ['ensolarado', 'nublado', 'chuvoso']:
            raise ValueError("Clima inválido!")
        return self.regras[self._classificar_temperatura(temp)][clima.lower()]
    
curador = CuradorEstilo()

curador.fit()

print("=" * 60 + "\nSISTEMA DE RECOMENDAÇÃO DE ROUPAS\n" + "=" * 60)
print("Faixas: Frio(<15°C) | Ameno(15-25°C) | Calor(>25°C)\nClimas: ensolarado, nublado, chuvoso")
print("-" * 60)

while True:
    try:
        temperatura = float(input("Temperatura (°C): "))
        break
    except ValueError:
        print("Inválido!")

while True:
    clima = input("Clima (ensolarado/nublado/chuvoso): ").lower()
    if clima in ['ensolarado', 'nublado', 'chuvoso']:
        break
    print("Inválido!")
print("-" * 60 + f"\nResultado: {temperatura}°C - {clima.capitalize()}\n" + "-" * 60)

try:
    rec = curador.predict(temperatura, clima)
    print("Roupas recomendadas:")
    for i, r in enumerate(rec, 1):
        print(f"  {i}. {r}")
except ValueError as e:
    print(f"Erro: {e}")
print("\n" + "=" * 60)