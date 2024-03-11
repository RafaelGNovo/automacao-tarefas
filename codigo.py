import pyautogui
import time
import pandas


pyautogui.PAUSE = 2


# Aperta a tecla windows
pyautogui.press("win")

# Digita o nome do programa
pyautogui.write("chrome")

# Aperta a tecla enterrafa123
pyautogui.press("enter")

# Digita o link da pagina
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

# Aperta a tecla enter
pyautogui.press("enter")


# Pausa para começar a inserir as informações de login no site
time.sleep(3)

# Clicar o campo para inserir o e-mail
pyautogui.click(x=631, y=410)


# Passo 2 - fazer o login
email = "rafaelgnovo@gmail.com"
senha = "rafa123"

pyautogui.write(email)
pyautogui.press("tab")

pyautogui.write(senha)
pyautogui.press("tab")

pyautogui.press("enter")

# Passo 3 - Importar a base de dados

tabela = pandas.read_csv("produtos.csv")
print(tabela)

time.sleep(1)

# Passo 4 - Cadastrar as informações
for linha in tabela.index:
    pyautogui.click(x=431, y=291)

    # Codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    # Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # Preco Unitario
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # Observacao
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)

    pyautogui.press("tab")

    # Enviar o produto
    pyautogui.press("enter")

    # Rolar a pagina para cima
    pyautogui.scroll(5000)
