import os
import random

def reference_solve(n: int) -> int:
    """Эталонное решение, полностью копирующее вашу формулу."""
    return n if n < 3 else n * (n - 1) * (n - 2)

def generate_tests(output_dir: str = "tests", num_random: int = 40):
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Граничные и типовые случаи
    manual_cases = [
        1, 2, 3, 4, 5, 10, 50, 100, 500, 1000, 5000, 10000
    ]

    # 2. Случайные числа в диапазоне 1 ≤ N ≤ 10^4
    random.seed(42)  # Фиксированный seed для воспроизводимости
    manual_cases.extend(random.randint(1, 10000) for _ in range(num_random))

    # Убираем дубликаты и сортируем
    test_cases = sorted(set(manual_cases))

    print(f"📦 Генерация {len(test_cases)} тестов в папке '{output_dir}/'...")
    
    for idx, n in enumerate(test_cases, start=1):
        name = f"{idx:02d}"
        in_path = os.path.join(output_dir, f"{name}.")
        out_path = os.path.join(output_dir, f"{name}.a")

        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{n}\n")
            
        ans = reference_solve(n)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"{ans}\n")
            
        if idx <= 5 or idx > len(test_cases) - 3:
            print(f"  ✅ Тест {name}: N={n:<5} → {ans}")

    print(f"\n🎉 Готово! Сгенерировано {len(test_cases)} пар файлов.")
    print(f"   📁 Путь: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    generate_tests()