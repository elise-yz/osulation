
<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="osulogoblue.png" alt="Logo" height="240">

  <h1 align="center">osulation!</h1>

  <p align="center">
    hand-driven osu!
    <br />
    <a href="https://devpost.com/software/osulation"><strong>Devpost »</strong></a>
    <br />
    <br />
    <a href="https://www.linkedin.com/in/cindy-li-569a30187/">Cindy Li</a>
    ·
    <a href="https://www.linkedin.com/in/2023cyang/">Cindy Yang</a>
    ·
    <a href="https://www.linkedin.com/in/elise-yz/">Elise Zhu</a>
    ·
    <a href="https://www.linkedin.com/in/selina-sun-550301227/">Selina Sun</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#technologies">Technologies</a>
      <ul>
        <li><a href="#roboflow">Roboflow</a></li>
        <li><a href="#streamlit">Streamlit</a></li>
        <li><a href="#matlab">Matlab</a></li>
        <li><a href="#optimizations">Optimizations</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img src="x7L2VSNEiyAB5Ux7nxKmLo6yLyEJT6Jt5yhNCUpGN9GDGT4URPYeuQtGvaPcpwHHCNppCsFFoQSxJqT.gif" alt="Logo" height="240">

If the Wii taught us anything, it’s that flailing your arms around is fun. So, we’ve built a pipeline that tracks your hand and arm movements in real-time, converting your moving limbs into precise game controls!

This project is not only a fun way to play games, but it also has a wide range of applications in various fields:

- 🎨 Gesture-controlled digital painting or air-drawing.

- 🧠 Gamifying controlled arm and hand movements are great for physical therapy exercises, especially in patients recovering from injuries.

- 🤖 Control robots or drones with the flick of a wrist!

**Why Osu! though?**

Because if our algorithm can handle tracking hyper-precise arm movements at ridiculous speeds, it can handle pretty much anything. Also, Osu! is a fun game that we're all abysmal at, so we figured we'd make it a little easier for ourselves.

### Built With

[![Roboflow][Roboflow]][Roboflow-url]
[![Mediapipe][Mediapipe]][Mediapipe-url]
[![Python][Python]][Python-url]
[![Streamlit][Streamlit]][Streamlit-url]<br/>
[![Wolfram][Wolfram]][Wolfram-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Technologies

### Roboflow

To train our model, we used Roboflow, a platform that allows us to easily train models on custom datasets. We combined two datasets hosted on Roboflow, the [Palm Detection Dataset](https://universe.roboflow.com/dasfsahfas/palm-detection-c3si5) and a [Hand Pose Dataset](https://universe.roboflow.com/vision-no7cd/vision-ni0je), to create a dataset that could be used to train a model to detect hands and their poses, specifically fists and open palms. We then used Roboflow to train a model on this dataset, achieving an mAP of 0.995 over 200 epochs.

We used this model to construct a custom workflow that could be used to detect hands and their poses in real-time. This workflow was then integrated into a Streamlit web app that could be used to play osu! with hand gestures.

![alt text](<Screenshot 2024-09-29 090645.png>)

### Streamlit

We used Streamlit to provide users with an easy way to launch and interact with our application, offering a clear and elegant showcase of our project. Streamlit enabled us to seamlessly present key features, our team, tech stack, gameplay instructions, and data visualizations that were critical in selecting the best model version. Its simplicity allowed us to create a clean and intuitive UI, ensuring a smooth user experience while maintaining a professional and polished look.

![alt text](image-2.png)

### Matlab

To determine the best version of our model, we conducted a comprehensive data collection process and leveraged Matlab for in-depth analysis. This allowed us to rigorously compare performance metrics across different iterations, ensuring that we selected the optimal model with confidence while minimizing lag. Our use of Matlab's powerful analytical tools enabled us to gain precise insights, driving the accuracy and reliability of our final choice.

![alt text](image.png)![alt text](image-1.png)

### Optimizations

To optimize code performance while ensuring high model confidence, we developed and tested various attributes across multiple models. These optimizations included frame splitting, which allowed us to evaluate specific intervals for more efficient resource usage, and smoothing techniques to gradually adjust movements, minimizing abrupt or jittery transitions. We also incorporated calibration to fine-tune sensitivity, enhancing user experience and reducing the need for excessive movement. Additionally, we implemented threading to process frames concurrently, significantly improving both performance and responsiveness.

<!-- CONTACT -->
## Contact

Cindy Li (autoclicker, model analytics, optimizations) - cl2674@cornell.edu

Cindy Yang (Roboflow workflow, model integration, tuning) - cwyang@umich.edu

Elise Zhu (CV pipeline, Streamlit app, design) - eyz7@georgetown.edu

Selina Sun (data generation, model training, Streamlit app) - selinas@umich.edu


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Roboflow]: https://img.shields.io/badge/roboflow-6706CE?style=for-the-badge&logo=roboflow&logoColor=white
[Roboflow-url]: https://roboflow.com/
[Mediapipe]: https://img.shields.io/badge/mediapipe-0097A7?style=for-the-badge&logo=mediapipe&logoColor=white
[Mediapipe-url]: https://github.com/google-ai-edge/mediapipe
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Streamlit]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[Streamlit-url]: https://streamlit.io/
[Wolfram]: https://img.shields.io/badge/MATLAB-0769AD?style=for-the-badge&logo=wolfram&logoColor=white
[Wolfram-url]: https://www.mathworks.com/products/matlab.html
