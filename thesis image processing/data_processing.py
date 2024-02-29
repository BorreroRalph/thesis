import os
import numpy as np
from PIL import Image

def load_data(data_dir):
  """
  Loads images, actual heights, and desired heights from a directory.

  Args:
    data_dir: Path to the directory containing data files.

  Returns:
    images: A list of preprocessed images (numpy arrays).
    actual_heights: A list of actual height labels.
    desired_heights: A list of desired height labels.
  """
  images = []
  actual_heights = []
  desired_heights = []
  for filename in os.listdir(data_dir):
    # Extract image name and labels
    name, ext = os.path.splitext(filename)
    if ext not in [".jpg", ".png"]:
      continue  # Skip non-image files
    actual_height_path = os.path.join(data_dir, name + "_actual_height.txt")
    desired_height_path = os.path.join(data_dir, name + "_desired_height.txt")

    # Load image and preprocess
    image = np.array(Image.open(os.path.join(data_dir, filename)))
    # Add your desired preprocessing steps here (e.g., resizing, normalization)

    # Load actual height
    with open(actual_height_path, "r") as f:
      actual_height = float(f.read())

    # Load desired height
    with open(desired_height_path, "r") as f:
      desired_height = float(f.read())

    images.append(image)
    actual_heights.append(actual_height)
    desired_heights.append(desired_height)

  return images, actual_heights, desired_heights

# ... other preprocessing functions as needed (e.g., preprocess_image)
