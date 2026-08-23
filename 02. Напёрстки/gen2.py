import os
import random

def reference_solve(moves: str) -> int:
    """Эталонное решение (полностью повторяет вашу логику)"""
    l, c, r = 1, 0, 0
    for e in moves:
        if e == 'A':
            l, c = c, l
        elif e == 'B':
            r, c = c, r
        elif e == 'C':
            l, r = r, l
    if l: return 1
    if c: return 2
    return 3

def generate_tests(output_dir: str = "tests", num_random: int = 30):
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Граничные и типовые случаи
    manual_cases = [
        "A", "B", "C",
        "AA", "BB", "CC",
        "AB", "BC", "CA",
        "ABC", "CBA",
        "A" * 5, "B" * 10, "C" * 15,
        "ABC" * 16 + "AB",      # ~50 символов
        "CBA" * 15 + "C",       # ~46 символов
        "ABABAB", "ACACAC",     # Чередуемые ходы
    ]

    # 2. Случайные последовательности длиной от 1 до 50
    random.seed(42)  # Фиксированный seed для воспроизводимости
    for _ in range(num_random):
        length = random.randint(1, 50)
        case = "".join(random.choice("ABC") for _ in range(length))
        manual_cases.append(case)

    # Убираем дубликаты и сортируем для удобства проверки
    test_cases = sorted(set(manual_cases), key=lambda x: (len(x), x))

    print(f"📦 Генерация {len(test_cases)} тестов в папке '{output_dir}/'...")
    
    for idx, moves in enumerate(test_cases, start=1):
        name = f"{idx:02d}"
        in_path = os.path.join(output_dir, name)      # Вход: 01, 02, ...
        out_path = os.path.join(output_dir, f"{name}.a") # Выход: 01.a, 02.a, ...

        with open(in_path, "w", encoding="utf-8") as f:
            f.write(moves + "\n")
        
        ans = reference_solve(moves)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"{ans}\n")
            
        if idx <= 5 or idx > len(test_cases) - 3:
            print(f"  ✅ Тест {name}: \"{moves}\" → {ans}")

    print(f"\n🎉 Готово! Сгенерировано {len(test_cases)} пар файлов.")
    print(f"   📁 Путь: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    generate_tests(output_dir="tests", num_random=25)