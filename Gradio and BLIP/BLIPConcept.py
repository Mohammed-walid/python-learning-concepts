"""This module is for BLIP Training"""

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

print("downloading the processor...")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

print("Opening image...")
image = Image.open("RDR2.png")

print("Processing image...")
inputs = processor(image, return_tensors="pt")

print("Generating captions...")
outputs = model.generate(**inputs)
caption = processor.decode(outputs[0], skip_special_tokens=True)

print("Generated Caption:", caption)
