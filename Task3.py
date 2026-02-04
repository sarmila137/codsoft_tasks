from PIL import Image
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch

# Load pre-trained image captioning model
model = VisionEncoderDecoderModel.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning"
)
processor = ViTImageProcessor.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning"
)
tokenizer = AutoTokenizer.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning"
)

# Load image
image = Image.open("image.jpg").convert("RGB")

# Preprocess image
pixel_values = processor(images=image, return_tensors="pt").pixel_values

# Generate caption
output_ids = model.generate(pixel_values, max_length=16)
caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)

print("Generated Caption:", caption)