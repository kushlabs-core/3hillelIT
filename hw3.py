def get_input():
    return input("Введіть 12 чисел через пробіл: ")

def validate(raw_data):
    parts = raw_data.split()
    if len(parts) != 12:
        raise ValueError("Має бути рівно 12 чисел!")
    return [float(x) for x in parts]

def calculate(data):
    months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    
    total = sum(data)
    avg = total / 12
    
    max_val = max(data)
    min_val = min(data)
    
    max_info = (max_val, months[data.index(max_val)])
    min_info = (min_val, months[data.index(min_val)])
    
    return (total, avg, max_info, min_info)

def display(result):
    print(result)

def main():
    try:
        display(calculate(validate(get_input())))
    except ValueError as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()