import os
import random

def reference_solve(a: int, b: int, c: int) -> str:
    """Эталонное решение, полностью копирующее вашу логику и формат вывода."""
    d = b ** 2 - 4 * a * c
    out = []
    
    if a == 0:
        if b == 0:
            out.append("-1" if c == 0 else "0")
        else:
            out.append("1")
            out.append(str(-c / b))
    elif d < 0:
        out.append("0")
    elif d == 0:
        out.append("1")
        out.append(str(-b / (2 * a)))
    else:
        out.append("2")
        x1 = (-b - d ** 0.5) / (2 * a)
        x2 = (-b + d ** 0.5) / (2 * a)
        out.append(str(x1))
        out.append(str(x2))
        
    return "\n".join(out)

def generate_tests(output_dir: str = "tests", num_random: int = 50):
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Ручные тесты, покрывающие все ветки условия
    manual_cases = [
        (0, 0, 0),   # -1
        (0, 0, 5),   # 0
        (0, 2, -4),  # 1 (линейное)
        (0, -3, 9),  # 1 (линейное, отриц. b)
        (1, 0, 1),   # 0 (D < 0)
        (1, 2, 1),   # 1 (D = 0)
        (1, -3, 2),  # 2 (D > 0, a>0)
        (-1, 0, 4),  # 2 (D > 0, a<0)
        (2, 4, 2),   # 1 (D = 0, a≠1)
        (1, 0, -1),  # 2 (корни целые: -1, 1)
        (1, 1, 0),   # 2 (корни: -1, 0)
        (30000, 30000, 30000), # Максимальные коэффициенты
    ]

    # 2. Случайные тесты
    random.seed(42)  # Фиксированный seed для повторяемости
    for _ in range(num_random):
        manual_cases.append((
            random.randint(-30000, 30000),
            random.randint(-30000, 30000),
            random.randint(-30000, 30000)
        ))

    # Убираем дубликаты
    seen = set()
    test_cases = []
    for case in manual_cases:
        if case not in seen:
            seen.add(case)
            test_cases.append(case)

    print(f"📦 Генерация {len(test_cases)} тестов в папке '{output_dir}/'...")
    
    for idx, (a, b, c) in enumerate(test_cases, start=1):
        name = f"{idx:02d}"
        in_path = os.path.join(output_dir, f"{name}")
        out_path = os.path.join(output_dir, f"{name}.a")

        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{a} {b} {c}\n")
            
        ans = reference_solve(a, b, c)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ans + "\n")
            
        if idx <= 5 or idx > len(test_cases) - 3:
            print(f"  ✅ Тест {name}: {a:>5} {b:>5} {c:>5} → {ans.replace(chr(10), ' | ')}")

    print(f"\n🎉 Готово! Сгенерировано {len(test_cases)} пар файлов.")
    print(f"   📁 Путь: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    generate_tests(output_dir="tests", num_random=40)