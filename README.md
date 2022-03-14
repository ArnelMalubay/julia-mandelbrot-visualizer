# Julia and Mandelbrot Set Visualizer

This is a simple web app that allows the user to visualize Julia sets and the Mandelbrot set. A vectorized implementation of the escape-time algorithm is used to plot the figures. This app was used in my report in my Complex Analysis class.

<p align="center"><img src="sample_images/samp1.png" width="300"/></p>
<p align="center"><strong>Julia set for c = -0.11564378757515037 + 0.8690819138276553i</strong></p>

<p align="center"><img src="sample_images/samp3.png" width="300"/></p>
<p align="center"><strong>Julia set for c = -0.512511498387847167 + 0.521295573094847167i</strong></p>

<p align="center"><img src="sample_images/samp6.png" width="300"/></p>
<p align="center"><strong>Julia set for c = -0.5012149298597195 - 0.5637838176352705i</strong></p>

<p align="center"><img src="sample_images/samp7.png" width="300"/></p>
<p align="center"><strong>Julia set for c = -0.8 + 0.156i</strong></p>

Accessing the App
=================

To access this app, you can either

1. Clone the repository. Then, run 

`pip install -r requirements.txt`

on the terminal. It is ideal to create a virtual environment first before proceeding to the installation of the required libraries. Once done, you can then run

`streamlit run app.py`

on the terminal and use the app on your local server.

OR

2. Access the app via Streamlit Sharing through this [link](https://share.streamlit.io/arnelmalubay/julia-mandelbrot-visualizer/main/app.py).