# Real-VS-A.I.-Generated-Image-Classification-Web-App-using-Flask

## Introduction
In today's world, where AI has become a boon to society, it also poses significant threats, such as identity theft through deepfakes and privacy breaches. This project aims to take a small yet crucial step in accurately distinguishing between AI-generated images and real-life photographs.

<h2>Data</h2>
<br>
<image src="../Real-VS-A.I.-Generated-Image-Classification-Web-App-using-Flask/static/img.png" width="600" height="350" class="center">
<br>
The source of data is a dataset from <b>Kaggle</b> called [AI vs. Human-Generated Images](https://www.kaggle.com/datasets/alessandrasala79/ai-vs-human-generated-dataset). The dataset consists of authentic images sampled from the Shutterstock platform. This structured pairing enables a direct comparison between real and AI-generated content, providing a robust foundation for developing and evaluating image authenticity detection systems.
<br>

The flow of the project goes as follows:
<ul><br>
<li><u><b>Modeling:</b></u>: Creating a CNN architecture with a validation accuracy of <b>98.75 %</b>.</li>
<li><b><u>Python app Backend:</u></b>: Using <b>Flask</b> to create URL endpoints for the GUI.</li>
<li><b><u>Front-end Development:</u></b> Creating a GUI Web-Page to Upload manual Images to Predict AI/Real Images Using <b>HTML and CSS</b></li>
</ul>
<br>

<h2>Getting Started</h2>

<li>Clone the repo and cd into it. </li>
<li>Create your Python environment in terminal using:</li>

```
python -m venv myenv
myenv\Scripts\activate
```

<li>Then run:</li>

`pip install tensorflow matplotlib sklearn opencv-python`

<li>Then Run the application using:</li>

`python app.py`

<br>

<h2>Demo</h2>

<image src="../Real-VS-A.I.-Generated-Image-Classification-Web-App-using-Flask/static/demo.gif" alt="Demo web-app" width="700" height="390" class="center">
