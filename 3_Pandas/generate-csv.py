import pandas as pd

data = {
    'tienda': ['CompraGamer', 'Mercado Libre', 'FullH4rd', 'Venex', 'Gezatek'] * 20,
    'producto': [
        'GeForce RTX 4060 Ti', 'Ryzen 7 5700X', 'Monitor Samsung Odyssey G4 240Hz', 'Teclado Logitech G Pro KDA', 'Gabinete Corsair 4000D Airflow',
        'Radeon RX 7800 XT', 'Intel Core i5-13600K', 'SSD WD Black 1TB NVMe', 'Fuente EVGA 750W Gold', 'Mouse Razer DeathAdder V3',
        'GeForce RTX 4070 Super', 'Ryzen 5 7600', 'Motherboard ASUS B650-PLUS', 'RAM Kingston Fury 32GB (2x16)', 'Watercooling Cooler Master 240mm',
        'Radeon RX 7600', 'Intel Core i9-14900K', 'Monitor LG UltraGear 27"', 'Teclado Redragon Kumara K552', 'Gabinete Lian Li O11 Dynamic'
    ] * 5,
    'categoria': [
        'Placas de Video', 'Procesador', 'Monitores', 'Periféricos', 'Gabinete',
        'Placas de Video', 'Procesador', 'Almacenamiento', 'Fuentes', 'Periféricos',
        'Placas de Video', 'Procesador', 'Motherboard', 'Memorias', 'Refrigeración',
        'Placas de Video', 'Procesador', 'Monitores', 'Periféricos', 'Gabinete'
    ] * 5,
    'marca': [
        'NVIDIA', 'AMD', 'Samsung', 'Logitech', 'Corsair',
        'AMD', 'Intel', 'Western Digital', 'EVGA', 'Razer',
        'NVIDIA', 'AMD', 'ASUS', 'Kingston', 'Cooler Master',
        'AMD', 'Intel', 'LG', 'Redragon', 'Lian Li'
    ] * 5,
    'estado': ['nuevo', 'nuevo', 'nuevo', 'nuevo', 'usado'] * 20,
    'precio': [
        620000.0, 310000.0, 580000.0, 115000.0, 145000.0,
        980000.0, 420000.0, 135000.0, 185000.0, 95000.0,
        1250000.0, 340000.0, 290000.0, 180000.0, 155000.0,
        490000.0, 950000.0, 440000.0, 45000.0, 220000.0
    ] * 5,
    'stock': [12, 8, 4, 25, 3, 15, 6, 40, 18, 50, 5, 9, 11, 30, 7, 20, 2, 8, 100, 4] * 5,
    'descuento_porcentaje': [10, 0, 15, 5, 0] * 20,
    'puntuacion_usuarios': [4.8, 4.9, 4.5, 4.7, 4.2, 4.6, 4.9, 4.8, 4.4, 4.7, 4.8, 4.5, 4.3, 4.8, 4.5, 4.4, 5.0, 4.6, 4.2, 4.9] * 5
}

df = pd.DataFrame(data)

# Guardar como CSV
df.to_csv('productos_gamer_argentina.csv', index=False)

print("¡Archivo 'productos_gamer_argentina.csv' creado con éxito!")