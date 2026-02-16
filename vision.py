import torch
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from PIL import Image

MODEL_ID = "Qwen/Qwen2-VL-2B-Instruct"

model = Qwen2VLForConditionalGeneration.from_pretrained(
    MODEL_ID,
    device_map={"": "cpu"},
    torch_dtype=torch.float32
)

processor = AutoProcessor.from_pretrained(MODEL_ID)

def analyze_screen(image_path, user_instruction):
    image = Image.open(image_path).convert("RGB")

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image"},
                {
                    "type": "text",
                    "text": (
                        f"{user_instruction}\n\n"
                    )
                }
            ]
        }
    ]

    prompt = processor.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=False
    )

    inputs = processor(
        text=prompt,
        images=image,
        return_tensors="pt"
    )

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=200
        )

    return processor.decode(output[0], skip_special_tokens=True)
