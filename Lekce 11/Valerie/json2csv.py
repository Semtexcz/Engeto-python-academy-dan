# Zapiš funkci pro upravení načteného obsahu
import os
import csv
import json


def write_to_csv(csv_name: str, json_contents: list) -> None:
    """
    Do zadaneho souboru (par. 'soubor') zapis filtrovane udaje (par. 'udaje').

    Z prvniho indexu par. 'udaje' zkus vzit jmena klicu a vytvorit z nich
    zahlavi souboru.
    """
    with open(csv_name, "w", encoding="utf-8", newline='') as f:
        try:
            col_names = json_contents[0].keys()
        except IndexError:
            print(f"Problem s indexem u {type(json_contents)}")
        except FileExistsError:
            print("Nemuzu prepsat existujici soubor")
        else:
            csv_writer = csv.DictWriter(f, fieldnames=col_names)
            csv_writer.writeheader()
            csv_writer.writerows(json_contents)
            print(f"Soubor {csv_name} zapsan na disk")


def find_all_json_files(files_dir: str) -> set:
    """
    V seznamu vsech souboru zadaneho adresare najdi jen soubory s priponou '.json'.
    """
    return {
        json_file
        for json_file in os.listdir(files_dir)
        if os.path.splitext(json_file)[1] == ".json"
    }

def filter_keys(keys_to_save: tuple, original_dict: dict) -> dict:
    """
    Zapis do noveho slovniku vsechny klice v par. 'zadouci' z puvodniho slovniku.
    """
    new_dict = dict()
    print(original_dict.keys())
    for key in original_dict.keys():
        if key not in keys_to_save:
            continue
        new_dict[key] = original_dict[key]
    return new_dict


def read_json(files_dir: str, json_name: str) -> list:
    with open(os.path.join(files_dir, json_name)) as f:
        return json.load(f)


def json_to_csv(files_dir: str, keys_to_save: tuple) -> None:
    """
    1. Nacist vsechny potrebne '.json' soubory (fce:'najdi_json_soubory()'),
    2. ^- nacist obsah vsech nalezenych '.json' (fce:'nacti_obsah_jsonu()'),
    3. ^- upravit nact. obs. podle naseho vyberu (fce:'filtruj_nepotrebne_klice()'),
    4. ^- ulozit upr. obs. do lokalniho souboru (fce:'zapis_upravene_do_csv()').
    """
    json_files = find_all_json_files(files_dir)
    json_contents = [
        filter_keys(keys_to_save, d)
        for json_file in json_files
        for d in read_json(files_dir, json_file)
    ]
    write_to_csv("output.csv", json_contents)


def main() -> None:
    files_dir = "data"
    keys_to_save = ("sepalLength", "sepalWidth", "species")
    json_to_csv(files_dir, keys_to_save)


if __name__ == "__main__":
    main()
