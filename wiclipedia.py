import wikipedia
import typer
from typing import Optional


def main(query=typer.Argument(...), search:Optional[bool]=typer.Option(False, "--search", "-S")):
    ws = wikipedia.search(query)

    if not search:
        page = ws[0]
    else:
        print("\n".join(ws))
        _S = int(input("Enter the Page Number"))
        if _S > len(ws)+1:
            main(query, True)
        page = ws[_S-1]

    pg = wikipedia.page(page)
    print(pg.title)
    print("-"*len(pg.title))
    print(pg.summary)
    print("-"*len(pg.title))
    print(pg.content)

    print("-"*len(pg.title))
    print("END")
    print("-"*len(pg.title))


if __name__ == "__main__":
    typer.run(main)
