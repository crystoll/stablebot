# A simple demo repo of stable diffusion webui client scripts in Python

Grab stable diffusion webui from https://github.com/AUTOMATIC1111/stable-diffusion-webui - follow the instructions, get it running locally (or remotely, where-ever you prefer)

Grab a fun model, for the video I used https://civitai.com/models/4201/realistic-vision-v60-b1 - drop in in stable diffusion webui models/stable-diffusion folder

Run the webui with --api parameter, and any other optimizations you like, for example --medvram --xformers

Clone my repo, have Python installed. Stable diffusion webui is very picky about Python versions, but this client code only requires any Python 3 version with requests installed (pip install requests)

Some of the advanced scripts depend on having extensions installed, so start with the simple ones, and work your way onwards from there. Also remember, with the --api parameter you also get openapi documentation in the server, /docs folder.

Run the scripts, experiment with the parameters, have fun! This is just the starting place.

The img2img script requires pillow to be installed (pip install pillow)

