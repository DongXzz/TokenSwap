import math
import re
import string

IMAGE_TOKEN = re.compile(r"(<image \d+>)")


def doc_to_text(doc: dict, lmms_eval_specific_kwargs=None) -> str:
    prompt = f"The following are multiple choice questions about {' '.join(doc['subject'].split('_'))}.\nAnswer the question by replying A, B, C or D.\nQuestion: {doc['question']}\n"
    for i in range(len(doc["choices"])):
        prompt += f"{string.ascii_uppercase[i]}. {doc['choices'][i]}\n"
    prompt += "Answer: "
    return prompt


def doc_to_visual(doc, lmms_eval_specific_kwargs=None):
    prompt = doc_to_text(doc)
    image_tokens = re.findall(r"<image \d+>", prompt)
    image_tokens = sorted(
        list(set(t.strip("<>").replace(" ", "_") for t in image_tokens)),
        key=lambda x: int(x.split("_")[-1])
    )
    return [doc[t].convert("RGB") for t in image_tokens]


def _resize(image, pixels, factor):
    """Resize to about `pixels` pixels with sides divisible by `factor` (Qwen-VL smart_resize with min = max = pixels)."""
    w, h = image.size
    if h * w > pixels:
        beta = math.sqrt(h * w / pixels)
        h_new, w_new = max(factor, math.floor(h / beta / factor) * factor), max(factor, math.floor(w / beta / factor) * factor)
    else:
        beta = math.sqrt(pixels / (h * w))
        h_new, w_new = math.ceil(h * beta / factor) * factor, math.ceil(w * beta / factor) * factor
    return image.resize((w_new, h_new), resample=3)  # bicubic


def doc_to_messages(doc, lmms_eval_specific_kwargs=None):
    """Interleave each image at its <image N> position in the prompt."""
    kwargs = lmms_eval_specific_kwargs or {}
    content = []
    for part in IMAGE_TOKEN.split(doc_to_text(doc)):
        if IMAGE_TOKEN.fullmatch(part):
            image = doc[part.strip("<>").replace(" ", "_")].convert("RGB")
            if kwargs.get("image_pixels"):
                image = _resize(image, kwargs["image_pixels"], kwargs["image_factor"])
            content.append({"type": "image", "url": image})
        elif part:
            content.append({"type": "text", "text": part})
    return [{"role": "user", "content": content}]
