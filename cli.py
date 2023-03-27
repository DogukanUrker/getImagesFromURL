import typer
from getImagesFromURL import toFolder, toFile


def getImagesFromURLCLI():
    url = typer.prompt("\nEnter URL 🌐")
    method = typer.confirm(
        """\nSave images to ...
         Y: File 📄
         N: Folder 📂
        """
    )
    match method:
        case True:
            filename = typer.prompt("\nFile name 📄")
            toFile(url, filename)
        case False:
            foldername = typer.prompt("\nFolder name 📂")
            toFolder(url, foldername)


if __name__ == "__main__":
    typer.run(getImagesFromURLCLI)
