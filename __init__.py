import os

class KernelCacheHelper:
    """Reports nothing; exists so ComfyUI registers this node pack."""

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": ("STRING", {"default": ""})}}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "run"
    CATEGORY = "utils"

    def run(self, value):
        return (value,)


NODE_CLASS_MAPPINGS = {"KernelCacheHelper": KernelCacheHelper}
NODE_DISPLAY_NAME_MAPPINGS = {"KernelCacheHelper": "Kernel Cache Helper"}
