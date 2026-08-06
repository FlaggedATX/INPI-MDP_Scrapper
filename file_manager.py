import os
import shutil
import time


def make_dir():
    path = os.path.join(os.path.expanduser("~"), "Desktop", "pdf_inpi")
    if not os.path.exists(path):
        os.makedirs(path)
        print("Pasta criada com sucesso!")
        return
    else:
        print("Pasta já existe")
        return

def move_pdf(numero):
    od_di = os.path.join(os.path.expanduser("~"), "Downloads", f"Desenhos_Industriais{numero}.pdf")
    od_m = os.path.join(os.path.expanduser("~"), "Downloads", f"Marcas{numero}.pdf")
    od_p = os.path.join(os.path.expanduser("~"), "Downloads", f"Patentes{numero}.pdf")
    nd_di = os.path.join(os.path.expanduser("~"), "Desktop", "pdf_inpi")
    try:
        shutil.move(od_di, nd_di)
        shutil.move(od_m, nd_di)
        shutil.move(od_p, nd_di)
        print("Movidos com sucesso!")
        return
    except Exception as e:
        print("Algo deu errado")
        print(e)
        return

def main():
    make_dir()


if __name__ == "__main__":
    main()