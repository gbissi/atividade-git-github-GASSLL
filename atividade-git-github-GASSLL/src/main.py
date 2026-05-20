NOTA_MIN = 0.0
NOTA_MAX = 10.0
NOTA_APROVACAO = 7.0
NOTA_RECUPERACAO = 5.0

def validarNota(nota):
    if not (NOTA_MIN <= nota <= NOTA_MAX):
        raise ValueError(f"Nota invalida: {nota}.")


def calcularMedia(A, B, C, D):
    for n in (A, B, C, D):
        validarNota(n)
    return (A + B + C + D) / 4


def situacao(media):
    if media >= NOTA_APROVACAO:
        return "Aprovado"
    else:
        if media >= NOTA_RECUPERACAO:
            return "Recuperação"
        else:
            return "Reprovado"

def lerNota():
    while True:
        try:
            entrada = input(f" Digite a nota: ")
            valor = float(entrada)
            validarNota(valor)
            return valor
        except:
            print(f"Entrada invalida")


def main():
    print("Informe as 4 notas do aluno:\n")

    A = lerNota()
    B = lerNota()
    C = lerNota()
    D = lerNota()

    media = calcularMedia(A, B, C, D)
    resultado = situacao(media)
    
    print()
    print(f"  Notas    : {A}  {B:.1f}  {C:.1f}  {D:.1f}")
    print(f"  Média    : {media:.2f}")
    print(f"  Situação : {resultado}")