def conjuga_presente(verbo):
    appendix = verbo[-2:]
    if appendix == 'ar':
        endings_ar_presente = ['o', 'as', 'a', 'amos', 'áis', 'an']
        verbo_trimmed = verbo[:-2]
        for ending in endings_ar_presente:
            verbo_conjugado = verbo_trimmed + ending
            print(verbo_conjugado)

    if appendix == 'er':
        endings_er_presente = ['o', 'es', 'e', 'emos', 'éis', 'en']
        verbo_trimmed = verbo[:-2]
        for ending in endings_er_presente:
            verbo_conjugado = verbo_trimmed + ending
            print(verbo_conjugado)

    if appendix == 'ir':
        endings_ir_presente = ['o', 'es', 'e', 'imos', 'ís', 'en']
        verbo_trimmed = verbo[:-2]
        for ending in endings_ir_presente:
            verbo_conjugado = verbo_trimmed + ending
            print(verbo_conjugado)


def conjuga_indefinido(verbo):
    appendix = verbo[-2:]
    if appendix == 'ar':
        endings_ar_presente = ['é', 'aste', 'ó', 'amos', 'asteis', 'aron']
        verbo_trimmed = verbo[:-2]
        for ending in endings_ar_presente:
            verbo_conjugado = verbo_trimmed + ending
            print(verbo_conjugado)

    if appendix is 'er' or 'ir':
        endings_er_presente = ['í', 'iste', 'ió', 'imos', 'isteis', 'ieron']
        verbo_trimmed = verbo[:-2]
        for ending in endings_er_presente:
            verbo_conjugado = verbo_trimmed + ending
            print(verbo_conjugado)


def conjuga_futuro(verbo):
    endings_er_presente = ['é', 'ás', 'á', 'emos', 'éis', 'án']
    for ending in endings_er_presente:
        verbo_conjugado = verbo + ending
        print(verbo_conjugado)


def conjuga_verbo(verbo, tiempo):
    if tiempo == 'presente':
        conjuga_presente(verbo)

    if tiempo == 'indefinido':
        conjuga_indefinido(verbo)

    if tiempo == 'futuro':
        conjuga_futuro(verbo)
