import typer
from getImagesFromURL import toFolder, toFile


def getImagesFromURLCLI():
    url = typer.prompt("Enter URL 🌐")
    method = typer.confirm(
        """Save images to ...
         Y: File 📄
         N: Folder 📂
        """
    )
    match method:
        case True:
            filename = typer.prompt("File name 📄")
            toFile(url, filename)
        case False:
            foldername = typer.prompt("Folder name 📂")
            toFolder(url, foldername)


if __name__ == "__main__":
    typer.run(getImagesFromURLCLI)
