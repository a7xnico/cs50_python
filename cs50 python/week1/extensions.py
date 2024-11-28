file_check = input("File name: ").strip().lower()  # lowercase and strip for possible errors
# prints looking at the suffix
if file_check.endswith(".gif"):
    print("image/gif")
elif file_check.endswith(".jpg") or file_check.endswith(".jpeg"):
    print("image/jpeg")
elif file_check.endswith(".png"):
    print("image/png")
elif file_check.endswith(".pdf"):
    print("application/pdf")
elif file_check.endswith(".txt"):
    print("text/plain")
elif file_check.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
