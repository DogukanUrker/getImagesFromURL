import typer
from getImagesFromURL import toFolder, toTXT


def getImagesFromURLCLI():
    url = typer.prompt("Enter URL 🌐")
    method = typer.confirm(
        """Save images to ...
         Y: Folder 📂
         N: File 📄
        """
    )
    match method:
        case True:
            foldername = typer.prompt("Folder name 📂")
            toFolder(url, foldername)
        case False:
            filename = typer.prompt("File name 📄")
            toTXT(url, filename)


if __name__ == "__main__":
    typer.run(getImagesFromURLCLI)
