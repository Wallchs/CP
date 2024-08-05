PI: float = 3.14159

def calc(a: float,b: float,c: float):
    
    print(f'TRIANGULO: {(a * c)/2:.3f}')
    print(f'CIRCULO: {PI * (c ** 2):.3f}')
    print(f'TRAPEZIO: {(a + b) * c / 2:.3f}')
    print(f'QUADRADO: {b ** 2:.3f}')
    print(f'RETANGULO: {a*b:.3f}')
    
    
    
a,b,c = map(float, input().split())
calc(a,b,c)
