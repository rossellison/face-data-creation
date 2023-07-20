# Face-Data-Creation
This repository provides the tools necessary to create face-data from videos and images. It can download videos from Youtube, extract facial images at a defined frame rate, and prepare images for StyleGAN applications.

![Project Workflow]([https://i.imgur.com/fjY6jFV.gif](https://imgur.com/fjY6jFV))

## Notebooks

1. **DownloadVideos.ipynb:** This notebook contains code to download videos from Youtube and extract facial images from them at a specified frame rate. 

    You can also use this Google Colab notebook for the same purpose: [DownloadVideos.ipynb](https://colab.research.google.com/drive/1NLgZPKEjmmntgujIl5TtMA_tFeQolBKl?usp=drive_link)
    
2. **Eye_Center_Images.ipynb:** This notebook provides code to extract faces images and prepare them for any future StyleGAN related work.

    Alternatively, use this Google Colab notebook: [Eye_Center_Images.ipynb](https://colab.research.google.com/drive/1t_8N1MT2Zt_hfrGCWJsX76caxhIDy1V_?usp=drive_link)

## Data
With these two notebooks and manual filtering, we have downloaded 4483 high-quality 1024x1024 Kpop Girl Group Idol face images which can be accessed here: [Kpop Idol Faces](https://www.kaggle.com/datasets/rossellison/kpop-idol-faces)

## Model
Using the [stylegan3-fun](https://github.com/PDillis/stylegan3-fun) repository, a model was trained on these faces to create more. You can download the .pkl file generated here: [Download .pkl file](https://drive.google.com/file/d/1Nd-0AFpDG_RMkfKC-uohVz9YpBsEj2QB/view?usp=sharing)

Here are examples of some non-existent Kpop faces: ![Kpop Faces](https://i.imgur.com/jBlfZtM.png)

Watch the process in this video: [YouTube video](https://www.youtube.com/watch?v=lNuxvZI3syM)

## Tutorial
A detailed tutorial on how to use these resources is in progress and will be linked here soon!

## Cool Results
- Combine faces of Blackpink members: ![Blackpink Faces](https://imgur.com/a/qTTGhLB)

- Project yourself into Kpop Girl Group Latent Space: ![Latent Space Projection](https://imgur.com/s5nZLEZ)

- Compare this model with the FFHQ model from NVIDIA: ![FFHQ vs kpopGG.pkl](https://imgur.com/xHFJ794)

## To-do
- Curate images better: remove low-quality or blurry images, very similar images, or duplicates, and retrain the model.
- Add new images from a wider variety of sources.
- Add Boy Group images.

## Acknowledgements
Special thanks to NVIDIA for releasing the FFHQ model and StyleGAN, to PDillis for his stylegan3-fun repository, and to jeffheaton for his insightful code and YouTube videos. These resources were invaluable in making this project possible.
