
import csv
import json
from pathlib import Path
import click


def najdi_soubory(adresar: str, pripona: str = ".json") -> None:
    directory = Path(adresar).resolve()
    if directory.exists() and directory.is_dir():
        return directory.rglob(f"*{pripona}")
    else:
        raise FileNotFoundError(f"Složka {adresar} neexistuje!")


def precti_json(cesta: str | Path) -> list:
    if isinstance(cesta, str):
        cesta = Path(cesta)
    with open(cesta, mode="r", encoding="UTF-8") as json_soubor:
        data = json.load(json_soubor)
        if isinstance(data, dict):
            return [data]
        return data


def flatten_dict(d, parent_key='', sep='.'):
    """
    Převede rozvětvený slovník, seznamy a n-tice na plochý slovník.

    :param d: Rozvětvený slovník, seznam nebo n-tice
    :param parent_key: Prefix pro klíče (pro interní použití)
    :param sep: Oddělovač klíčů
    :return: Plochý slovník
    """
    items = []
    if isinstance(d, dict):
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            items.extend(flatten_dict(v, new_key, sep=sep).items())
    elif isinstance(d, (list, tuple)):
        for i, v in enumerate(d):
            new_key = f"{parent_key}{sep}{i}" if parent_key else str(i)
            items.extend(flatten_dict(v, new_key, sep=sep).items())
    else:
        items.append((parent_key, d))
    return dict(items)


def uloz_dict_do_csv(adresar: str, jmeno_souboru: str, data: list):
    adresar: Path = Path(adresar).resolve()
    adresar.mkdir(exist_ok=True)
    soubor = adresar / Path(jmeno_souboru)
    with open(str(soubor), mode="w", encoding="UTF-8") as csv_soubor:
        writer = csv.DictWriter(csv_soubor, fieldnames=data[0].keys())
        writer.writeheader()
        for item in data:
            writer.writerow(item)


@click.command()
@click.argument("vstupni_adresar", type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True))
@click.argument("vystupni_adresar", type=click.Path(file_okay=False, dir_okay=True, writable=True))
@click.option("--pripona", default=".json", help="Přípona souborů k vyhledání (výchozí .json)")
def cli(vstupni_adresar, vystupni_adresar, pripona):
    """
    Konvertuje JSON soubory na CSV.

    VSTUPNI_ADRESAR je adresář obsahující JSON soubory.
    VYSTUPNI_ADRESAR je adresář, kam budou uloženy CSV soubory.
    """
    try:
        soubory = najdi_soubory(vstupni_adresar, pripona)
        for i, soubor in enumerate(soubory):
            data = precti_json(soubor)
            flatten_data = [flatten_dict(item) for item in data]
            uloz_dict_do_csv(vystupni_adresar, f"data_{i}.csv", flatten_data)
        click.echo(f"Konverze dokončena. CSV soubory byly uloženy do {vystupni_adresar}.")
    except Exception as e:
        click.echo(f"Chyba: {e}", err=True)


if __name__ == "__main__":
    cli()
