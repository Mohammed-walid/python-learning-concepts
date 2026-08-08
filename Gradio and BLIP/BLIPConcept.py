"""This module is for BLIP Training"""

from transformers import BlipProcessor, BlipForConditionalGeneration, BlipForQuestionAnswering
from PIL import Image

print("downloading the processor...")
processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-vqa-base")
model_two = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")
print("Opening image...")
image = Image.open("RDR2.png")

question = "whats the man riding and whats the colour of this horse?"

print("Processing image...")
inputs = processor(image,question , return_tensors="pt")


print("Generating captions...")
outputs = model_two.generate(**inputs, max_new_tokens=40)
caption = processor.decode(outputs[0], skip_special_tokens=True)

print("Generated Caption:", caption)
