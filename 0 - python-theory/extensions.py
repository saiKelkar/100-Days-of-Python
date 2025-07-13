def main():
    file_name = input("File name: ")
    extensions(file_name)

def extensions(file_name):
    name, extension = file_name.split(".")
    if extension in ["gif", "jpg", "jpeg", "png"]:
        print(f"image/{extension}")
    elif extension in ["pdf", "zip"]:
        print(f"application/{extension}")
    elif extension in ["txt"]:
        print(f"text/{extension}")
    else:
        print("invalid input")

main()