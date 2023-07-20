# face-data-creation

Create face-data from videos and images

![Project gif](https://imgur.com/fjY6jFV)

## Notebooks

The `DownloadVideos.ipynb` provides code to download videos from YouTube and then extract facial images from them at N number of frames. You can also use this Google Colab notebook [here](https://colab.research.google.com/drive/1NLgZPKEjmmntgujIl5TtMA_tFeQolBKl?usp=drive_link) to create facial image data on Google Colab.

The `Eye_Center_Images.ipynb` provides code to extract face images and prepare images for any StyleGAN future image work. You can also use this Google Colab notebook [here](https://colab.research.google.com/drive/1t_8N1MT2Zt_hfrGCWJsX76caxhIDy1V_?usp=drive_link).

Using these two notebooks and filtering images manually, 4483 high-quality 1024x1024 Kpop Girl Group Idol face images have been downloaded which you can access [here](https://www.kaggle.com/datasets/rossellison/kpop-idol-faces).

A model was trained on these faces using [this repository](https://github.com/PDillis/stylegan3-fun) to create more faces. The .pkl file generated can be downloaded [here](https://drive.google.com/file/d/1Nd-0AFpDG_RMkfKC-uohVz9YpBsEj2QB/view?usp=sharing).

Here is an example of some non-existent Kpop faces: ![Kpop faces](https://imgur.com/jBlfZtM)

And here is a video: https://www.youtube.com/watch?v=lNuxvZI3syM

And here is a tutorial on how to do all of this and more: (coming soon)

## Cool Things

Some cool things you can do:
- Combining Blackpink member faces: ![Blackpink faces](https://imgur.com/a/qTTGhLB)
- Project yourself into Kpop Girl Group Latent Space: ![Project](https://imgur.com/s5nZLEZ)
- Comparing this model with the FFHQ model from NVIDIA: ffhq vs kpopGG.pkl: ![Comparison](https://imgur.com/xHFJ794)

## Future Work

To do: 
- Curate images better, remove low quality or blurry images, very similar images or duplicates, and retrain model.
- Add new images from a more variety of sources
- Add Boy Group images

## Acknowledgements

Thank yous and acknowledgements:
Note I used the FFHQ model to transfer learn from originally so I am incredibly thankful for NVIDIA for releasing StyleGAN and the trained models as well as PDillis for his StyleGAN3-fun repo as well as jeffheaton for code and his YouTube videos which showed me about this technology.
