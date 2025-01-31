import re

def steg(image_path):
    with open(image_path, "rb") as file:
        data = file.read().decode(errors="ignore")  # Décoder en UTF-8 en ignorant les erreurs binaires
    # Expression régulière pour capturer le message PGP
    match = re.search(r"(-----BEGIN PGP PUBLIC KEY BLOCK-----.*?-----END PGP PUBLIC KEY BLOCK-----)", data, re.DOTALL)
    if match:
        print(match.group(1))
    else:
        print("Aucun message PGP trouvé.")
