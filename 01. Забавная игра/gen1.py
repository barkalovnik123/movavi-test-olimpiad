import os
import random

def reference_solve(m: int) -> int:
    """Эталонное решение (полностью повторяет вашу логику)"""
    s = bin(m)[2:]
    n = len(s)
    max_val = 0
    for i in range(n):
        rotated = s[i:] + s[:i]
        val = int(rotated, 2)
        if val > max_val:
            max_val = val
    return max_val

def generate_tests(output_dir: str = "tests", num_random: int = 20, max_m: int = 10**18):
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Граничные и типовые случаи
    manual_cases = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        15, 16, 17, 31, 32, 33, 63, 64, 65,
        127, 128, 255, 256,
        10**5, 10**9, 10**12, 10**15, 10**18,
        (1 << 60) - 1,          # Все единицы (60 бит)
        (1 << 59),              # Степень двойки
        (1 << 59) + 1,          # Степень двойки + 1
        int("101010101010101010101010101010", 2),  # Чередующиеся биты
        int("1100110011001100", 2),                # Блоки битов
    ]

    # 2. Случайные числа с равномерным распределением длин двоичной записи
    random.seed(42)  # Фиксированный seed для воспроизводимости
    for _ in range(num_random):
        bits = random.randint(1, 60)  # Длина от 1 до 60 бит
        # Гарантируем, что старший бит = 1 (число положительное и корректной длины)
        val = (1 << (bits - 1)) | random.getrandbits(bits - 1)
        manual_cases.append(val)

    # Убираем дубликаты и сортируем для удобства
    test_cases = sorted(set(manual_cases))

    print(f"📦 Генерация {len(test_cases)} тестов в папке '{output_dir}/'...")
    
    for idx, m in enumerate(test_cases, start=1):
        name = f"{idx:02d}"
        in_path = os.path.join(output_dir, f"{name}")
        out_path = os.path.join(output_dir, f"{name}.a")

        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{m}\n")
        
        ans = reference_solve(m)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"{ans}\n")
            
        if idx <= 5 or idx > len(test_cases) - 3:  # Выводим первые и последние
            print(f"  ✅ Тест {name}: m={m:<15} → {ans}")

    print(f"\n🎉 Готово! Сгенерировано {len(test_cases)} пар файлов.")
    print(f"   📁 Путь: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    # Параметры можно менять здесь
    generate_tests(output_dir="tests", num_random=25, max_m=10**18)