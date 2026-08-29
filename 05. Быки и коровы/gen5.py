import os
import random

def calc_bulls_cows(secret: str, guess: str) -> tuple:
    """Корректный расчёт быков и коров (работает за O(N), устойчив к дубликатам)"""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = len(set(secret) & set(guess)) - bulls
    return bulls, cows

def generate_valid_number() -> str:
    """Генерирует 4-значное натуральное число с различными цифрами"""
    first = random.choice('123456789')  # Первая цифра != 0 (натуральное число)
    others = random.sample([d for d in '0123456789' if d != first], 3)
    return first + ''.join(others)

def generate_tests(output_dir: str = "tests", num_random: int = 50):
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Ручные тесты, покрывающие ключевые сценарии
    manual_cases = [
        ("1234", "1234"),  # 4 быка, 0 коров
        ("1234", "4321"),  # 0 быков, 4 коров
        ("1234", "5678"),  # 0 быков, 0 коров
        ("1234", "1567"),  # 1 бык, 0 коров
        ("1234", "1324"),  # 2 быка, 2 коров (1,4 на месте; 2,3 переставлены)
        ("5671", "7251"),  # Пример из условия: 1 бык, 2 коровы
        ("9876", "6789"),  # 0 быков, 4 коров (полная инверсия)
        ("1023", "3201"),  # Тест с нулём внутри числа
    ]

    # 2. Случайные тесты
    random.seed(42)  # Фиксированный seed для повторяемости
    for _ in range(num_random):
        manual_cases.append((generate_valid_number(), generate_valid_number()))

    # Убираем дубликаты
    seen = set()
    test_cases = []
    for sec, guess in manual_cases:
        if (sec, guess) not in seen:
            seen.add((sec, guess))
            test_cases.append((sec, guess))

    print(f"📦 Генерация {len(test_cases)} тестов в папке '{output_dir}/'...")
    
    for idx, (secret, guess) in enumerate(test_cases, start=1):
        name = f"{idx:02d}"
        in_path = os.path.join(output_dir, f"{name}")
        out_path = os.path.join(output_dir, f"{name}.a")

        with open(in_path, "w", encoding="utf-8") as f:
            f.write(f"{secret} {guess}\n")
            
        bulls, cows = calc_bulls_cows(secret, guess)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"{bulls} {cows}\n")
            
        if idx <= 5 or idx > len(test_cases) - 3:
            print(f"  ✅ Тест {name}: {secret} {guess} → {bulls} {cows}")

    print(f"\n🎉 Готово! Сгенерировано {len(test_cases)} пар файлов.")
    print(f"   📁 Путь: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    generate_tests()