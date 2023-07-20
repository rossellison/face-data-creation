import torch
import dnnlib
import legacy
import PIL.Image
import numpy as np
import imageio
from tqdm import tqdm
import os


name = 'RossToSooyoung'  # Set the name variable here

#lvec1 = np.load('projection/00018-projection-w-wavgstart-sgan2/projected_wavg_final.npy')
#lvec2 = np.load('projection/00011-projection-w-wavgstart-sgan2/projected_wavg_final.npy')
lvec1 = np.load('out/projection/00002-projection-wplus-wavgstart-sgan2/projected_wplus_wavg_final.npy')
lvec2 = np.load('out/projection/00003-projection-wplus-wavgstart-sgan2/projected_wplus_wavg_final.npy')

network_pkl = "kpopGG.pkl"
device = torch.device('cuda')

with open(network_pkl, "rb") as fp:
    G = legacy.load_network_pkl(fp)['G_ema'].requires_grad_(False).to(device) # type: ignore

STEPS = 350
FPS = 30
FREEZE_STEPS = 15

diff = lvec2 - lvec1
step = diff / STEPS
current = lvec1.copy()

video = imageio.get_writer(f'movie/{name}.mp4', mode='I', fps=FPS, codec='libx264', bitrate='20M')

# Create the folder if it doesn't exist
folder_path = f'intermediate_latents/{name}'
os.makedirs(folder_path, exist_ok=True)

for j in tqdm(range(STEPS)):
  z = torch.from_numpy(current).to(device)
  synth_image = G.synthesis(z, noise_mode='const')
  synth_image = (synth_image + 1) * (255/2)
  synth_image = synth_image.permute(0, 2, 3, 1).clamp(0, 255).to(torch.uint8)[0].cpu().numpy()

  repeat = FREEZE_STEPS if j==0 or j==(STEPS-1) else 1
   
  for i in range(repeat):
    video.append_data(synth_image)
  
  # Save the current latent vector and its corresponding image every 200th step
  if j % 100 == 0:
    np.save(f'{folder_path}/{name}_latent_vector_{j:04d}.npy', current)
    imageio.imwrite(f'{folder_path}/{name}_image_{j:04d}.png', synth_image)

  current = current + step

video.close()
