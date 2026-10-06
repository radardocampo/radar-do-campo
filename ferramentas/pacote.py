"""Leva a pasta de um video entre o PC e a nuvem pelo GitHub.

O GitHub recusa arquivos acima de 100 MB, entao arquivos grandes viram pedacos
"<arquivo>.parte000", ".parte001"... de 90 MB, e "juntar" os remonta byte a byte
(sem reencodar). Cada video anda num branch proprio: video/<nome-da-pasta>.

  python ferramentas/pacote.py partir  "Videos prontos/Shorts/<video>"
  python ferramentas/pacote.py juntar  "Videos prontos/Shorts/<video>"
"""
import os, sys

LIMITE = 90 * 1024 * 1024


def partir(pasta):
    for raiz, _, arquivos in os.walk(pasta):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if ".parte" in nome or os.path.getsize(caminho) <= LIMITE:
                continue
            with open(caminho, "rb") as f:
                i = 0
                while bloco := f.read(LIMITE):
                    with open(f"{caminho}.parte{i:03d}", "wb") as out:
                        out.write(bloco)
                    i += 1
            os.remove(caminho)
            print(f"partido em {i}: {caminho}")


def juntar(pasta):
    for raiz, _, arquivos in os.walk(pasta):
        for nome in sorted(arquivos):
            if not nome.endswith(".parte000"):
                continue
            base = os.path.join(raiz, nome[: -len(".parte000")])
            i = 0
            with open(base, "wb") as out:
                while os.path.exists(p := f"{base}.parte{i:03d}"):
                    with open(p, "rb") as f:
                        out.write(f.read())
                    os.remove(p)
                    i += 1
            print(f"juntado de {i}: {base}")


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("partir", "juntar"):
        sys.exit(__doc__)
    {"partir": partir, "juntar": juntar}[sys.argv[1]](sys.argv[2])
