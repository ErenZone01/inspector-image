from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def extract_metadata(image_path):
    # Charger l'image
    img = Image.open(image_path)
    exif_data = img._getexif()

    # Parcourir les métadonnées
    if exif_data:
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == "GPSInfo":
                lat_values = value.get(2)  # Latitude
                lon_values = value.get(4)  # Longitude
                # Vérifier que les valeurs existent et ont une taille suffisante
                if lat_values is not None and len(lat_values) >= 1 and lon_values is not None and len(lon_values) >= 1:
                    print(f"Lat / Lon: ({int(lat_values[0])}) / ({int(lon_values[0])})")
                else:
                    print("⚠️ Données GPS incomplètes ou absentes.")
    else:
        print("⚠️ Pas de metadonnée")               