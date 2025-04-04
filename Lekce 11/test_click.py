
import click

# Definice hlavní funkce
@click.command()
@click.argument("soubor")  # Povinný poziční argument
@click.option(
    "--vystup", "-o",
    default="output.txt",
    help="Cesta k výstupnímu souboru (výchozí: output.txt)"
)
@click.option(
    "--format", "-f",
    type=click.Choice(["text", "json", "csv"], case_sensitive=False),
    default="text",
    help="Formát výstupu: text, json nebo csv (výchozí: text)"
)
@click.option(
    "--verbose", "-v",
    is_flag=True,
    help="Zapne detailní výstup"
)
@click.option(
    "--filtry", "-fl",
    multiple=True,  # Umožňuje zadat více hodnot
    help="Seznam filtrů pro zpracování dat"
)
@click.option(
    "--iterace", "-i",
    default=1,
    type=int,
    show_default=True,
    help="Počet iterací zpracování"
)
def cli(soubor, vystup, format, verbose, filtry, iterace):
    """
    Ukázka klíčových funkcí knihovny Click.
    """
    # --- Použití argumentů ---
    click.echo(f"Vstupní soubor: {soubor}")
    click.echo(f"Výstupní soubor: {vystup}")
    click.echo(f"Formát výstupu: {format}")

    if verbose:
        click.echo("Detailní výstup je zapnut.")

    if filtry:
        click.echo(f"Aktivní filtry: {', '.join(filtry)}")
    else:
        click.echo("Žádné filtry nebyly zadány.")

    click.echo(f"Počet iterací: {iterace}")

    # Simulace iterací
    for i in range(iterace):
        click.echo(f"Iterace {i + 1}...")

# Spuštění programu
if __name__ == "__main__":
    cli()
