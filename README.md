# Face-Data-Creation
This repository provides the tools necessary to create face-data from videos and images. It can download videos from Youtube, extract facial images at a defined frame rate, and prepare images for various applications.

![Project Workflow](https://github.com/rossellison/face-data-creation/blob/main/Capturing%20Faces%20From%20Video%20480p.gif?raw=true)


## Notebooks

1. **DownloadVideos.ipynb:** This notebook contains code to download videos from Youtube and extract facial images from them at a specified frame rate. 

    You can also use this Google Colab notebook for the same purpose: [DownloadVideos.ipynb](https://colab.research.google.com/drive/1NLgZPKEjmmntgujIl5TtMA_tFeQolBKl?usp=drive_link)
    
2. **Eye_Center_Images.ipynb:** This notebook provides code to extract faces images and prepare them for any future StyleGAN related work.

    Alternatively, use this Google Colab notebook: [Eye_Center_Images.ipynb](https://colab.research.google.com/drive/1t_8N1MT2Zt_hfrGCWJsX76caxhIDy1V_?usp=drive_link)

## Data
With these two notebooks and manual filtering, we have made 4483 high-quality 1024x1024 Kpop Girl Group Idol face images which can be accessed here: [Kpop Idol Faces](https://www.kaggle.com/datasets/rossellison/kpop-idol-faces)

## Model
Using the [stylegan3-fun](https://github.com/PDillis/stylegan3-fun) repository, a model was trained on these faces to create more. You can download the .pkl file generated here: [Download .pkl file](https://huggingface.co/rossellison/kpop-face-generator/blob/main/kpopGG.pkl) 

Here are examples of some non-existent Kpop faces generated by the model: ![Kpop Faces](https://i.imgur.com/jBlfZtM.png)

Generate some faces for yourself using the model on HuggingFace: [HuggingFace](https://imgur.com/u8uS6PU)

Here are some upscaled from the 1024x1024 generated images: [Upscaled Generated Images](https://imgur.com/a/iPYLCYe)

Video smoothly transitioning through generated faces: [YouTube video](https://www.youtube.com/watch?v=lNuxvZI3syM)

The notebook used to train the stylegan model: [Google Collab](https://colab.research.google.com/drive/1YQJY-xx7kcmRgo9Rcre_a3gfnT9fpc2z?usp=sharing)

## Tutorial
A detailed tutorial on setup and code: [Youtube video](https://www.youtube.com/watch?v=3oqSJHWLuXs)

## Cool Results
- Combine faces of Blackpink members: [Blackpink Faces](https://imgur.com/Xho0rVt)
- Project yourself into Kpop Girl Group Latent Space: [Latent Space Projection](https://imgur.com/5Oa5W5Z)
- Compare this model with the FFHQ model from NVIDIA: [FFHQ vs kpopGG.pkl](https://imgur.com/1G6xkhJ)

## To-do
- Curate images better: remove low-quality or blurry images, very similar images, or duplicates, and retrain the model.
- Add new images from a wider variety of sources.
- Add Boy Group images.

Share any help or work you've done would love to see it!

## Acknowledgements
Special thanks to NVIDIA for releasing the FFHQ model and StyleGAN, to PDillis for his stylegan3-fun repository, and to jeffheaton for his insightful code and YouTube videos. These resources were invaluable in making this project possible.
