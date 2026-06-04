
import math

def decimal_to_binary(decimal_num):
    """Convierte un número decimal a binario y muestra el proceso."""
    print(f"\n--- Conversión de Decimal a Binario para {decimal_num} ---")
    if decimal_num == 0:
        print("0 en decimal es 0 en binario.")
        return "0"

    binary_digits = []
    current_num = decimal_num
    print(f"Comenzamos con el número decimal: {current_num}")

    while current_num > 0:
        remainder = current_num % 2
        current_num = current_num // 2
        binary_digits.append(str(remainder))
        print(f"{current_num * 2 + remainder} / 2 = {current_num} con residuo {remainder}")

    binary_result = "".join(binary_digits[::-1])
    print(f"Los residuos en orden inverso forman el número binario: {binary_result}")
    print(f"Resultado final: {decimal_num} (Decimal) = {binary_result} (Binario)")
    return binary_result

def decimal_to_octal(decimal_num):
    """Convierte un número decimal a octal y muestra el proceso."""
    print(f"\n--- Conversión de Decimal a Octal para {decimal_num} ---")
    if decimal_num == 0:
        print("0 en decimal es 0 en octal.")
        return "0"

    octal_digits = []
    current_num = decimal_num
    print(f"Comenzamos con el número decimal: {current_num}")

    while current_num > 0:
        remainder = current_num % 8
        current_num = current_num // 8
        octal_digits.append(str(remainder))
        print(f"{current_num * 8 + remainder} / 8 = {current_num} con residuo {remainder}")

    octal_result = "".join(octal_digits[::-1])
    print(f"Los residuos en orden inverso forman el número octal: {octal_result}")
    print(f"Resultado final: {decimal_num} (Decimal) = {octal_result} (Octal)")
    return octal_result

def decimal_to_hexadecimal(decimal_num):
    """Convierte un número decimal a hexadecimal y muestra el proceso."""
    print(f"\n--- Conversión de Decimal a Hexadecimal para {decimal_num} ---")
    if decimal_num == 0:
        print("0 en decimal es 0 en hexadecimal.")
        return "0"

    hex_digits = "0123456789ABCDEF"
    hexadecimal_digits = []
    current_num = decimal_num
    print(f"Comenzamos con el número decimal: {current_num}")

    while current_num > 0:
        remainder = current_num % 16
        current_num = current_num // 16
        hexadecimal_digits.append(hex_digits[remainder])
        print(f"{current_num * 16 + remainder} / 16 = {current_num} con residuo {hex_digits[remainder]}")

    hexadecimal_result = "".join(hexadecimal_digits[::-1])
    print(f"Los residuos en orden inverso forman el número hexadecimal: {hexadecimal_result}")
    print(f"Resultado final: {decimal_num} (Decimal) = {hexadecimal_result} (Hexadecimal)")
    return hexadecimal_result

def binary_to_decimal(binary_num):
    """Convierte un número binario a decimal y muestra el proceso."""
    print(f"\n--- Conversión de Binario a Decimal para {binary_num} ---")
    decimal_result = 0
    binary_num_str = str(binary_num)
    n = len(binary_num_str)
    print(f"Comenzamos con el número binario: {binary_num_str}")
    print("Cada dígito binario se multiplica por una potencia de 2, comenzando desde la derecha con 2^0.")

    for i in range(n):
        digit = int(binary_num_str[n - 1 - i])
        power_of_2 = 2**i
        term = digit * power_of_2
        decimal_result += term
        print(f"Dígito {digit} * 2^{i} ({power_of_2}) = {term}. Suma acumulada: {decimal_result}")

    print(f"Resultado final: {binary_num_str} (Binario) = {decimal_result} (Decimal)")
    return decimal_result

def octal_to_decimal(octal_num):
    """Convierte un número octal a decimal y muestra el proceso."""
    print(f"\n--- Conversión de Octal a Decimal para {octal_num} ---")
    decimal_result = 0
    octal_num_str = str(octal_num)
    n = len(octal_num_str)
    print(f"Comenzamos con el número octal: {octal_num_str}")
    print("Cada dígito octal se multiplica por una potencia de 8, comenzando desde la derecha con 8^0.")

    for i in range(n):
        digit = int(octal_num_str[n - 1 - i])
        power_of_8 = 8**i
        term = digit * power_of_8
        decimal_result += term
        print(f"Dígito {digit} * 8^{i} ({power_of_8}) = {term}. Suma acumulada: {decimal_result}")

    print(f"Resultado final: {octal_num_str} (Octal) = {decimal_result} (Decimal)")
    return decimal_result

def hexadecimal_to_decimal(hex_num):
    """Convierte un número hexadecimal a decimal y muestra el proceso."""
    print(f"\n--- Conversión de Hexadecimal a Decimal para {hex_num} ---")
    decimal_result = 0
    hex_num_str = str(hex_num).upper()
    n = len(hex_num_str)
    hex_values = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    print(f"Comenzamos con el número hexadecimal: {hex_num_str}")
    print("Cada dígito hexadecimal se multiplica por una potencia de 16, comenzando desde la derecha con 16^0.")

    for i in range(n):
        char = hex_num_str[n - 1 - i]
        digit_value = hex_values[char]
        power_of_16 = 16**i
        term = digit_value * power_of_16
        decimal_result += term
        print(f"Dígito {char} ({digit_value}) * 16^{i} ({power_of_16}) = {term}. Suma acumulada: {decimal_result}")

    print(f"Resultado final: {hex_num_str} (Hexadecimal) = {decimal_result} (Decimal)")
    return decimal_result

def convert_number(num_str, from_base, to_base):
    """Convierte un número de una base a otra, mostrando el proceso intermedio si es necesario."""
    print(f"\n--- Conversión de {from_base} a {to_base} para {num_str} ---")

    decimal_val = 0
    if from_base == 'binario':
        decimal_val = binary_to_decimal(num_str)
    elif from_base == 'octal':
        decimal_val = octal_to_decimal(num_str)
    elif from_base == 'decimal':
        decimal_val = int(num_str)
    elif from_base == 'hexadecimal':
        decimal_val = hexadecimal_to_decimal(num_str)
    else:
        print("Base de origen no válida.")
        return

    if to_base == 'binario':
        decimal_to_binary(decimal_val)
    elif to_base == 'octal':
        decimal_to_octal(decimal_val)
    elif to_base == 'decimal':
        print(f"El número ya está en decimal: {decimal_val}")
        print(f"Resultado final: {num_str} ({from_base}) = {decimal_val} (Decimal)")
    elif to_base == 'hexadecimal':
        decimal_to_hexadecimal(decimal_val)
    else:
        print("Base de destino no válida.")

def main():
    print("\n--- Convertidor de Sistemas Numéricos ---")
    print("Bases disponibles: binario, octal, decimal, hexadecimal")

    while True:
        num_str = input("\nIngrese el número a convertir: ")
        from_base = input("Ingrese la base de origen (binario, octal, decimal, hexadecimal): ").lower()
        to_base = input("Ingrese la base de destino (binario, octal, decimal, hexadecimal): ").lower()

        try:
            convert_number(num_str, from_base, to_base)
        except ValueError:
            print("Error: Entrada inválida. Asegúrese de que el número sea válido para la base de origen seleccionada.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

        another_conversion = input("\n¿Desea realizar otra conversión? (s/n): ").lower()
        if another_conversion != 's':
            break

    print("\n¡Gracias por usar el convertidor de sistemas numéricos!")

if __name__ == "__main__":
    main()
