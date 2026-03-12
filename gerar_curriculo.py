import os
from fpdf import FPDF
import language_tool_python

class CurriculoProcessor:
    def __init__(self):
        self.tool = language_tool_python.LanguageTool('pt-BR')

    def corrigir_texto(self, texto):
        """Corrige erros de português e inglês no texto."""
        return self.tool.correct(texto)

    def organizar_curriculo(self, texto):
        """Organiza o currículo em seções ATS-friendly."""
        secoes = {
            "Contato": "",
            "Objetivo": "",
            "Formação Acadêmica": "",
            "Competências Técnicas": "",
            "Projetos": "",
            "Experiência Profissional": "",
            "Certificações": "",
            "Outras Experiências": ""
        }

        linhas = texto.split("\n")
        secao_atual = None

        for linha in linhas:
            linha = linha.strip()
            if not linha:
                continue

            if linha in secoes:
                secao_atual = linha
            elif secao_atual:
                secoes[secao_atual] += linha + "\n"

        return secoes

    def gerar_pdf(self, secoes, output_path):
        """Gera um PDF com o currículo organizado."""
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for secao, conteudo in secoes.items():
            pdf.set_font("Arial", style="B", size=14)
            pdf.cell(200, 10, txt=secao, ln=True, align="L")
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, conteudo.strip())
            pdf.ln(5)

        pdf.output(output_path)

    def processar_curriculo(self, input_path, output_path):
        """Processa o currículo de entrada e gera um PDF corrigido."""
        with open(input_path, "r", encoding="utf-8") as file:
            texto = file.read()

        texto_corrigido = self.corrigir_texto(texto)
        secoes = self.organizar_curriculo(texto_corrigido)
        self.gerar_pdf(secoes, output_path)

if __name__ == "__main__":
    input_path = "curriculo_original.txt"  # Substitua pelo caminho do arquivo de entrada
    output_path = "curriculo_corrigido.pdf"

    if not os.path.exists(input_path):
        print(f"Arquivo de entrada '{input_path}' não encontrado.")
    else:
        processor = CurriculoProcessor()
        processor.processar_curriculo(input_path, output_path)
        print(f"Currículo corrigido gerado: {output_path}")