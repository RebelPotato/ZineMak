from typing import Tuple, List, NamedTuple
import fitz  # PyMuPDF
from PIL import Image
import sys


class Face(NamedTuple):
    id: int
    flipped: bool


def make_deck(n: int) -> List[Tuple[Face, Face]]:
    acc = []
    top = Face(2 * n - 1, False)
    bottom = Face(2 * n, False)
    for _ in range(2 * n):
        acc.append((top, bottom))
        top = Face(top.id - 1, not top.flipped)
        bottom = Face(bottom.id + 1, not bottom.flipped)

    return acc


def main():
    if len(sys.argv) != 3:
        print("Usage: python zine.py input.pdf output.pdf")
        return

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Open input PDF
    doc = fitz.open(input_path)
    total_pages = len(doc)

    # Handle empty PDF case
    if total_pages == 0:
        print("Input PDF is empty. Creating empty output.")
        fitz.open().save(output_path)
        return

    # Calculate number of sheets and pad pages
    n_sheets = (total_pages + 3) // 4  # Ceiling division for 4-page sheets
    first_page = doc[0]
    width, height = first_page.rect.width, first_page.rect.height

    # Process each page to images
    def get_page_image(page_idx: int) -> Image.Image:
        if page_idx < total_pages:
            page = doc[page_idx]
            pix = page.get_pixmap(colorspace="rgb", dpi=600)
            return Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        return Image.new("RGB", (int(width), int(height)), (255, 255, 255))

    # Generate zine pages using deck layout
    zine_pages = []
    for face1, face2 in make_deck(n_sheets):
        img1 = get_page_image(face1.id)
        img2 = get_page_image(face2.id)

        if face1.flipped:
            img1 = img1.rotate(180)
        if face2.flipped:
            img2 = img2.rotate(180)

        # Standardize widths
        w = max(img1.width, img2.width)
        if img1.width != w:
            img1 = img1.resize((w, img1.height))
        if img2.width != w:
            img2 = img2.resize((w, img2.height))

        # Create stacked page
        stacked = Image.new("RGB", (w, img1.height + img2.height))
        stacked.paste(img1, (0, 0))
        stacked.paste(img2, (0, img1.height))
        zine_pages.append(stacked)

    # Save output PDF
    assert zine_pages, "Zine pages should not be empty"
    zine_pages[0].save(
        output_path,
        save_all=True,
        append_images=zine_pages[1:],
        # resolution=288.0,
        dpi=(600, 600),
    )

    doc.close()


if __name__ == "__main__":
    main()
