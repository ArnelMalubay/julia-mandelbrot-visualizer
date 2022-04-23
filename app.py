# This file contains the main application file for our web applet.

# Importing necessary libraries
import streamlit as st 
from funcs import plot_julia_set, plot_mandelbrot_set

if __name__ == '__main__':

    st.title('Julia and Mandelbrot Set Visualizer')
    st.write('This applet allows you to visualize the (filled) Julia sets of the form $f(z)=z^2+c$ where $c$ is a complex number of your choice. A vectorized implementation of the escape-time algorithm was used to plot the figures. To get sharper images, try to increase the pixel density and maximum number of iterations. You also have the option to enable color bands or tick marks and choose your desired colormaps in the resulting figures. Finally, you can also display the Mandelbrot set and see whether $c$ is inside it or not. Enjoy!')

    # Configuring the sidebar widgets
    with st.sidebar:
        with st.form(key = 'form'):
            st.write('Play around with the parameters below and click Generate Plot to plot the figure.')
            real = st.text_input('Real Part', value = '0')
            imag = st.text_input('Imaginary Part', value = '0')
            max_iter = st.slider('Specify the maximum number of iterations', min_value = 10, max_value = 2000, value = 500, step = 10)
            pixel_density = st.slider('Specify pixel density', min_value = 0.5, max_value = 2.5, value = 1.0, step = 0.1)
            colormap_choices = ['inferno', 'magma', 'cividis','viridis', 'plasma', 'binary', 'Pastel1', 'Pastel2', 'Paired', 'Accent', 'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern', 'rainbow', 'jet', 'turbo', 'gray', 'bone', 'pink', 'spring', 'summer', 'autumn', 'winter', 'cool', 'hot', 'copper']
            cmap = st.selectbox('Choose colormap', options = colormap_choices)
            banding = st.checkbox('Enable color bands', value = False)
            show_tick_marks = st.checkbox('Show tick marks', value = False)
            show_mandelbrot = st.checkbox('Show Mandelbrot set', value = False)
            submit = st.form_submit_button('Generate Plot') 
    
    # Configuring applet response to form submission
    if submit:
        with st.spinner('Please wait for your plot to be rendered...'):
            try:
                c = eval(f'{real} + {imag}j')
                julia = plot_julia_set(c = c, max_iter = max_iter, pixel_density = pixel_density, cmap = cmap, banding = banding, show_tick_marks = show_tick_marks)
                st.header('Julia Set')
                st.pyplot(julia)
                if show_mandelbrot:
                    mandelbrot = plot_mandelbrot_set(c, cmap = cmap, banding = banding, show_tick_marks = show_tick_marks)
                    st.header('Mandelbrot Set')
                    st.pyplot(mandelbrot)
            except:
                st.header(f'Make sure your inputs are valid. Please try again.')