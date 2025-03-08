import requests
import base64
import time
from pathlib import Path

url = "http://127.0.0.1:7860"

output_dir = Path("generated_images")
output_dir.mkdir(exist_ok=True)

payload = {
    "prompt": "closeup portrait of a man in d&D setting, man in his 50's, older man, a sorcerer, dungeon setting, cinematic lighting, ((dlsr, dof, photorealistic, photoshoot, realistic)), torches on the wall, dark hair, dark short beart",
    "negative_prompt": "((cgi, cartoon, animation, painting)), hat, sweaty, candles, blurry, low quality",
    "steps": 30,
    "sampler_name": "DPM++ 2M SDE",
    "scheduler": "Karras",
    "cfg_scale": 4,
    "width": 512,
    "height": 512,
    "seed": -1,
    "denoising_strength": 0.5,    
    "enable_hr": True,
    "hr_scale": 2.0,
    "hr_upscaler": "ESRGAN_4x",
    "hr_steps": 15    
}

for i in range(1,10):
    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
    r = response.json()
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    with open(f"{output_dir}/img_{timestamp}.png", 'wb') as f:
        f.write(base64.b64decode(r['images'][0]))
    print(f'Generated image #{i}')
    