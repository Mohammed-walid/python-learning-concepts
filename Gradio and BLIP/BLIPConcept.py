"""This module is for BLIP Training"""

from transformers import BlipProcessor, BlipForConditionalGeneration, BlipForQuestionAnswering
from PIL import Image

print("downloading the processor...")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

print("Opening image...")
image = Image.open("RDR2.png")

question = "Whats this image?"

print("Processing image...")
inputs = processor(image,question , return_tensors="pt")


print("Generating captions...")
outputs = model.generate(**inputs, max_new_tokens=40)
caption = processor.decode(outputs[0], skip_special_tokens=True)

print("Generated Caption:", caption)
