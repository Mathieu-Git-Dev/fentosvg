import chess
import chess.svg
import os


def fen_to_image(fen, folder="echiquiers", filename="echiquier.svg"):
    """
    Génère une image SVG à partir d'une notation FEN d'échecs et la sauvegarde dans un fichier.

    Args:
        fen (str): La notation FEN qui représente la position des pièces sur l'échiquier.
        folder (str, optional): Le dossier où l'image SVG sera sauvegardée. Par défaut à 'echiquiers'.
        filename (str, optional): Le nom du fichier sous lequel l'image sera sauvegardée. Par défaut à 'echiquier.svg'.

    Returns:
        None: La fonction ne retourne rien mais sauvegarde une image SVG dans le chemin spécifié.

    """
    board = chess.Board(fen)
    svg = chess.svg.board(board=board)
    if not os.path.exists(folder):
        os.makedirs(folder)
    filepath = os.path.join(folder, filename)
    with open(filepath, "w") as file:
        file.write(svg)


def main():
    fens = [
        "q2rN3/1p4Qk/4p1p1/1p6/3P3P/8/2P2PP1/4R1K1 b - - 1 30",
        "8/2p5/4p1pk/5p2/2P3P1/1P6/P4P2/6K1 w - - 0 1",
    ] # ici, tu mets tes fens dans une liste, séparées par des virgules
    for index, fen in enumerate(fens, start=1): # la boucle va séparer les fens et les numéroter à partir de 1
        file_name = f"echiquier_{index}.svg" # ici, tu crées un nom de fichier pour chaque image en fonction de l'index de la boucle
        fen_to_image(fen, filename=file_name)
        print(f"Image SVG sauvegardée sous : {os.path.join('echiquiers', file_name)}")

if __name__ == "__main__":
    main()
