""" Extract module """
import pandas as pd
import requests
import io

from pathlib import Path

sources = [
        "https://portaldeinformacoes.conab.gov.br/downloads/arquivos/CustoProducao.txt", 
        "https://portaldeinformacoes.conab.gov.br/downloads/arquivos/SerieHistoricaGraos.txt",
        "https://portaldeinformacoes.conab.gov.br/downloads/arquivos/LevantamentoCafe.txt",
    ]

raw_path = (Path(__file__).parent.parent.parent / "data").resolve()
raw_path.mkdir(parents=True, exist_ok=True)

for url in sources:
    file_name = url.split("/")[-1].split(".")[0]
    response = requests.get(url)
    data = response.content

    df = pd.read_csv(io.StringIO(data.decode("latin1")), sep=";")

    df.to_csv(f"{raw_path}/{file_name}.csv", index=False, encoding="utf-8")