import sys


def barra_de_progresso(it, prefix="", size=60, file=sys.stdout):
    cont = len(it)

    def show(j):
        x = int(size * j / cont)
        file.write("%s[%s%s] %i/%i\r" %
                   (prefix, "#" * x, "." * (size - x), j, cont))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    file.write("\n")
    file.flush()