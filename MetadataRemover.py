__author__ = "Quach"
__version__ = "1.0"
__status__ = "development"
__email__ = "quach.vrc@gmail.com"
__github__ = "https://github.com/QuachRTX"

import sys
from PIL import Image

def remove_metadata(input_path):
    output_path = input_path.rsplit('.', 1)[0] + '_no_metadata.' + input_path.rsplit('.', 1)[1]

    with Image.open(input_path) as img:
        img.save(output_path, quality=95, optimize=True)

if __name__ == "__main__":
    for input_path in sys.argv[1:]:
        remove_metadata(input_path)
