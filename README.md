---

# Image Editor

A Streamlit web application that allows users to upload an image and apply basic edits like resizing, rotation, and filters using the PIL (Pillow) library.

## Features

- Upload images in various formats (`.png`, `.jpg`, `.jpeg`, `.pjp`, `.svg`)
- View image metadata (size, mode, format)
- Resize the image by specifying new width and height
- Rotate the image by any degree
- Apply filters:
  - Blur
  - Contour
  - Detail
  - Emboss
  - Smooth

## Requirements

Install the required Python packages:

```bash
pip install streamlit pillow
```

## How to Run

Start the app by running:

```bash
streamlit run image_editor.py
```

## Usage

1. Upload an image.
2. View basic information about it.
3. Choose resizing dimensions, rotation angle, and filter type.
4. Click "Commit Changes" to apply edits.
5. View the processed image directly in the app.

---
