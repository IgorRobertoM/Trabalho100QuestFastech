class DigitoDisplay:
    DIGITOS_5x3 = {
        '0': [
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1]
        ],
        '1': [
            [0, 1, 0],
            [1, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [1, 1, 1]
        ],
        '2': [
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1]
        ],
        '3': [
            [1, 1, 1],
            [0, 0, 1],
            [0, 1, 1],
            [0, 0, 1],
            [1, 1, 1]
        ],
        '4': [
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 0, 1],
            [0, 0, 1]
        ],
        '5': [
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1]
        ],
        '6': [
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ],
        '7': [
            [1, 1, 1],
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0],
            [1, 0, 0]
        ],
        '8': [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ],
        '9': [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1]
        ],
        'A': [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 1]
        ],
        'B': [
            [1, 1, 0],
            [1, 0, 1],
            [1, 1, 0],
            [1, 0, 1],
            [1, 1, 0]
        ],
        'C': [
            [1, 1, 1],
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
            [1, 1, 1]
        ],
        'D': [
            [1, 1, 0],
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 0]
        ],
        'E': [
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1]
        ],
        'F': [
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1],
            [1, 0, 0],
            [1, 0, 0]
        ]
    }

    def __init__(self, valor_decimal):
        self.valor_decimal = valor_decimal
        self.representacao_binaria = self.DIGITOS_5x3[self._para_caractere(valor_decimal)]

    def _para_caractere(self, valor):
        if 0 <= valor <= 9:
            return str(valor)
        else:
            return chr(ord('A') + valor - 10)

    def obter_representacao_binaria(self):
        return self.representacao_binaria


class DisplayDigital:
    def __init__(self, num_digitos):
        self.num_digitos = num_digitos
        self.altura_digito = 5
        self.largura_digito = 3
        self.digitos = [DigitoDisplay(0) for _ in range(num_digitos)]

    def exibir_numero(self, numero_str, base):
        try:
            numero_decimal = int(numero_str, base)
        except ValueError:
            print("Número inválido para a base fornecida.")
            return

        numero_convertido = self._converter_para_base(numero_decimal, base)

        if len(numero_convertido) > self.num_digitos:
            print("Número muito grande para o display.")
            return

        self.digitos = []
        for char in numero_convertido:
            if char.isdigit():
                valor = int(char)
            else:
                valor = ord(char.upper()) - ord('A') + 10
            self.digitos.append(DigitoDisplay(valor))

    def _converter_para_base(self, numero, base):
        if numero == 0:
            return '0'
        digitos = ''
        while numero > 0:
            resto = numero % base
            if resto < 10:
                digitos = str(resto) + digitos
            else:
                digitos = chr(ord('A') + resto - 10) + digitos
            numero //= base
        return digitos

    def renderizar_display(self):
        linhas_display = ['' for _ in range(self.altura_digito)]

        for idx, digito in enumerate(self.digitos):
            matriz = digito.obter_representacao_binaria()
            for i in range(self.altura_digito):
                linha = ''.join(['*' if bit else ' ' for bit in matriz[i]])
                linhas_display[i] += linha + ' ' 

        for linha in linhas_display:
            print(linha)


if __name__ == "__main__":
    num_digitos = 5
    display = DisplayDigital(num_digitos)

    numero = input("Digite o número: ")
    base = int(input("Digite a base do número (2 a 16): "))

    display.exibir_numero(numero, base)
    print("\nDisplay:")
    display.renderizar_display()