import pdfplumber
import re
import csv

arquivo_pdf = "bugueiros.pdf"            # Nome do seu arquivo PDF
arquivo_csv = "fornecedores.csv"       # Nome do CSV que será gerado

fornecedores = []
with pdfplumber.open(arquivo_pdf) as pdf:
    for pagina in pdf.pages:
        texto = pagina.extract_text()
        if texto:
            print(texto)
            print("=" * 560)
            for linha in texto.splitlines():
                print(linha) 
                print("-" * 40)
                if linha.startswith("FORNECEDOR:"):
                    linha_limpa = linha.replace("FORNECEDOR: ", "").split(" FANTASIA:")[0].strip()
                    match = re.match(r"(\d{4})-(.+)", linha_limpa)
                    if match:
                        codigo = match.group(1)
                        nome = match.group(2).strip()
                        
                        fornecedores.append((codigo, nome))

with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["codigo", "nome"])  # Cabeçalho
    escritor.writerows(fornecedores)

print(f"CSV salvo com sucesso como {arquivo_csv}")
