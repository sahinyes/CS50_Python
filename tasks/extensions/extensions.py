a = input("File name: ")

b = a.split(".")

match b[-1].lower().strip():
        case "gif":
                print("image/gif")
        case "jpg" | "jpeg":
                print("image/jpeg")
        case "png":
                print("image/png")
        case "pdf":
                print("application/pdf")
        case "txt":
                print("text/plain")
        case "zip":
                print("application/zip")
        case "txt":
                print("text/plain")
        case "bin" | _ :
                print("application/octet-stream")