import torch
import time

class ImageHoldLast:
    _cache = {}

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {"image": ("IMAGE",)}
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "hold"
    CATEGORY = "utils"

    @classmethod
    def IS_CHANGED(cls, image=None):
        return time.time()

    def hold(self, image=None):
        if image is not None:
            ImageHoldLast._cache["last"] = image
        if "last" in ImageHoldLast._cache:
            return (ImageHoldLast._cache["last"],)
        return (torch.zeros(1, 1, 1, 3),)

NODE_CLASS_MAPPINGS = {"ImageHoldLast": ImageHoldLast}
NODE_DISPLAY_NAME_MAPPINGS = {"ImageHoldLast": "Image Hold Last"}