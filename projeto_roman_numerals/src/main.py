def int_to_roman(num):
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = []
    
    for value, symbol in roman_numerals:
        count = num // value
        result.append(symbol * count)
        num -= value * count
    
    return ''.join(result)

if __name__ == "__main__":
    while True:
        user_input = input("Digite um número inteiro (ou 'sair' para encerrar): ")
        if user_input.lower() == "sair":
            print("Encerrando o programa. Até mais!")
            break
        try:
            num = int(user_input)
            if num <= 0:
                print("Por favor, digite um número inteiro positivo maior que zero.")
            else:
                print(f"O número {num} em algarismos romanos é: {int_to_roman(num)}")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro válido.")
