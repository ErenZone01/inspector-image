# 🚀 INSPECTOR-IMAGE
# English
    Inspector-Image is a program that helps you extract metadata from an image and detect any hidden PGP data within it.

    WHAT IS STEGANOGRAPHY?

    Steganography is the practice of concealing information within a medium (such as images, videos, or documents) in a way that prevents its detection. Unlike encryption, which scrambles data to make it unreadable, steganography hides the very existence of the information.

    There are various techniques used in steganography, such as:

        LSB (Least Significant Bit) substitution: This method replaces the least significant bits of an image’s pixel values with bits from the hidden message.
        Masking and Filtering: Similar to watermarking, this method modifies an image in a way that is less noticeable to the human eye.
        Algorithms based on transforms (DCT, DWT, etc.): These techniques embed data in the frequency domain rather than directly modifying pixel values.

    WHAT IS METADATA?

    Metadata is structured information that describes, explains, or gives details about a file (image, video, audio, document, etc.) without being part of its main content.

    For example:

        Image metadata (EXIF, IPTC, XMP) may include camera settings, GPS location, and timestamps.
        Video metadata can contain codec details, resolution, duration, and subtitles.
        Audio metadata may store information about the artist, album, and track details.
        Document metadata can include author names, modification dates, and software version.

    In steganography, metadata can sometimes be manipulated or used to store hidden messages.

# francais
    Inspector-Image est un programme qui vous aide à extraire les métadonnées d'une image et à détecter toute donnée PGP cachée à l'intérieur.
    QU’EST-CE QUE LA STÉGANOGRAPHIE ?

    La stéganographie est la pratique qui consiste à dissimuler des informations dans un support (comme des images, des vidéos ou des documents) de manière à empêcher leur détection. Contrairement au chiffrement, qui rend les données illisibles, la stéganographie cache l’existence même de l’information.

    Il existe plusieurs techniques utilisées en stéganographie, notamment :

        Substitution du bit de poids faible (LSB - Least Significant Bit) : Cette méthode remplace les bits les moins significatifs des pixels d’une image par des bits du message caché.
        Masquage et filtrage : Similaire au filigrane numérique, cette technique modifie une image de manière subtile pour y intégrer une information cachée.
        Algorithmes basés sur les transformations (DCT, DWT, etc.) : Ces techniques intègrent des données dans le domaine fréquentiel plutôt que de modifier directement les pixels.

    QU’EST-CE QUE LES MÉTADONNÉES ?

    Les métadonnées sont des informations structurées qui décrivent, expliquent ou donnent des détails sur un fichier (image, vidéo, audio, document, etc.) sans faire partie de son contenu principal.

    Par exemple :

        Les métadonnées d’image (EXIF, IPTC, XMP) peuvent inclure les paramètres de l’appareil photo, la localisation GPS et l’horodatage.
        Les métadonnées vidéo peuvent contenir des informations sur le codec, la résolution, la durée et les sous-titres.
        Les métadonnées audio peuvent enregistrer des informations sur l’artiste, l’album et les détails des pistes.
        Les métadonnées de documents peuvent inclure le nom de l’auteur, la date de modification et la version du logiciel utilisé.

    En stéganographie, les métadonnées peuvent parfois être manipulées ou utilisées pour stocker des messages cachés.

## 📌 TABLE OF CONTENTS
1. [Installation](#installation)
2. [Utilisation](#utilisation)
3. [Examples](#examples)



### Installation
# Clone this project and Move in this directory:
    ```bash
    git clone https://learn.zone01dakar.sn/git/mandaw/inspector-image.git 
    cd inspector-image
    ```


#### Utilisation
# Start the program :

- help option[--help]/[-h]:
    ``` python3 image.py --help```
- map option:
    ``` python3 image.py -map "ressources/image.jpeg" ```
- steg option:
    ``` python3 image.py -steg "ressources/image.jpeg" ```




##### Examples
usage :
```bash
$>  image -map image.jpeg
Lat/Lon:	(32) / (34)

$> image -steg image.jpeg
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: 01

mQENBGIwpy4BCACFayWXCgHH2QqXkicbqD1ZlMUALpyGxDFiWh1SErFUPJOO/CgU
2688bAd26kxDSGShiL9YUOQJ6MS+zJ0KlBkeKPoQlPHRBVpH7vjcRbZNgDxd82uE
7mhM6AH+W3fAim/PhU3lm661UGMCHM3YLupa/N0Dhhmfimtg+0AimCoXk6Q6WJxg
ao8XY1Wqacd2L0ssASY5EkMahNgtX0Ri8snbTlImd5Jq/sC4buZq96IlxyhtX0ew
zD/md0U++8SxG9+gi+uuImqV8Wq1YHvJH5BtIbfcNG9V00+03ikEX9tppKxCkhzx
9rSqvyH6Uirs3FVhFtoXUSg8IeYgSH6p5tsVABEBAAG0CDAxQDAxLjAxiQEcBBAB
AgAGBQJiMKcuAAoJEAJuInmYDhhbO3gIAITZhEtLBj524y1oeBKI5fZDwgCQum6B
D9ZaUq1+dI98HsiRAiUqw1YbuJQgeUVGCmqXeC3E7VTPCPZsaCLfWWZVeosRIqB8
PwGxcY6vXHYR4S6T8rHwsNASw+Vo2pmQIGn4tABmtyappqJbwSz+5yg73DjYXiX/
e/f6i9nrFFsfMjjKd71cAyHjV8u0z7fGDXpR22vo7CdloXMxsZRyHjd/4ofUgvu0
6hWYG2zBWTXpwaYRU9u1NCr1gfKnukm8gbILSSgjr8pQ3OLWHleJXc0sCEJFKSbg
+I0KJP7Ccrxy0MaKYk0T0tYbBrvqQCzXqzAqcjn+1GoDDS1J8WBJopM=
=N8hc
-----END PGP PUBLIC KEY BLOCK-----
$>
```