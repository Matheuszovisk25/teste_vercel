import requests
from bs4 import BeautifulSoup
import pandas as pd



def scrape(url):
        site = requests.get(url)
        soup = BeautifulSoup(site.content, "html.parser")
        tabela = soup.find("table", class_="tb_base tb_dados")

        headers = ["Produto", "Quantidade"]

        data = []

        for linha in tabela.find_all("tr"):
            linha2 = linha.find_all("td")
            if linha2:
                valores = [col.get_text(strip=True) for col in linha2]
                data.append(valores)

        df = pd.DataFrame(data, columns=headers)
        return df.to_dict(orient="records")

def scrape2(url):
        site = requests.get(url)
        soup = BeautifulSoup(site.content, "html.parser")
        tabela = soup.find("table", class_="tb_base tb_dados")

        headers = ["Produto", "Quantidade","Valor"]

        data = []

        for linha in tabela.find_all("tr"):
            linha2 = linha.find_all("td")
            if linha2:
                valores = [col.get_text(strip=True) for col in linha2]
                data.append(valores)

        df = pd.DataFrame(data, columns=headers)
        return df.to_dict(orient="records")


class Embrapa():
    def producao(self):
        dados =  scrape("http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02")
        return dados
       
    def comercializacao(self):
        dados =  scrape("http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04")
        return dados

    def processamento_viniferas(self):
        dados = scrape("http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03")
        return dados
    
    def processamento_americanas_e_hibridas(self):
        dados = scrape("http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_03")
        return dados
    
    def processamento_uvas_de_mesa(self):
       dados =  scrape("http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_03")
       return dados

    def importacao_vinhos_de_mesa(self):
        dados =  scrape2("http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05")
        return dados
    
    def importacao_espumantes(self):
        dados =  scrape2("http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_05")
        return dados
    
    def importacao_uvas_frescas(self):
        dados =  scrape2("http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_05")
        return dados
    
    def importacao_uvas_passas(self):
        dados =  scrape2("http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_05")
        return dados
    
    def importacao_suco_de_uva(self):
        dados =  scrape2("http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_05&opcao=opt_05")
        return dados
    
    def exportacao_vinho_de_mesa(self):
        dados =  scrape2("http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06")
        return dados
    
    def exportacao_espumantes(self):
        dados =  scrape2("http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_06")
        return dados
    
    def exportacao_uvas_frescas(self):
        dados =  scrape2("http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_06")
        return dados
    
    def exportacao_suco_de_uva(self):
        dados =  scrape2("http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_06")
        return dados






