# Welcome to `mosely` 
> A tiny python package for simulating XRF spectra to better understand measurements 


The widespread use of point-and-shoot hand held x-ray fluorescence (XRF) instruments in cultural heritage research, would suggest that it is easy enough for anyone to find out the elemental composition of materials. Alas, due to myriads of emission energies, escape peaks and other nuisances, reliable interpretation of x-ray fluorescence spectra is actually hard. If you are not yet deterred, just read the [Handheld XRF in Cultural Heritage - A practical workbook for conservators](http://www.getty.edu/conservation/publications_resources/pdf_publications/pdf/handheld-xrf-cultural-heritage.pdf) with many, many examples of spectra that was recently made available on-line by the Getty Conservation Institute. 

My take on this as a physicist and a python programmer is that instead of learning from data directly (i.e. staring at measured spectra), a nicer route to insight exists. Due to huge efforts and advances of the open source scientific computing community it is nowadays possible to install readily available python packages and create physics simulations and visualizations with a few lines of computer code. Once you understand why certain patterns of peaks appear, it becomes much more easy to interpret XRF spectra reliably.  

## Moseley's law 

An x-ray fluorescence spectrum for a specific pure element contains a characteristic combination of peaks of different heights at different energies. It follows that for a material that contains a mixture of different elements a  spectrum with a complex pattern of peaks will arise. Inferring a material composition from a measured XRF spectrum amounts to attributing peaks to elements. 

In 1913-1914 the young British physicist [Henry Moseley](https://en.wikipedia.org/wiki/Moseley%27s_law) discovered a beautifully simple regular pattern that relates the energy of the (typically) strongest peak in a pure element spectrum (called the $K_{\alpha}$ line) to the atomic number ($Z$). 

{% raw %}
$$ E_{K_{\alpha}} = 10.2 \left( Z^2 - 1 \right) $$
{% endraw %}

Where the energy is expressed in units of electron volt $[eV]$. Suppose now that you observe a large peak in a spectrum at a given energy but it is unknown which element generated. It is useful now to invert this expression to calculate the atomic number of the prime suspect chemical element that possibly emitted the peak. 

{% raw %}
$$ Z = \sqrt{\frac{E_{K_{\alpha}}}{10.2}} + 1 $$
{% endraw %}

Note that that we have simple a square root function here. As a practical numerical example, suppose now we measure an XRF spectrum for a sample of a pure (for the sake of this exercise) unknown element (See figure x). The largest peak in this spectrum has an energy of 6.40 keV = 6400 eV. Rounding off one can calculate

{% raw %}
$$ Z = \sqrt{\frac{6400}{10.2}} + 1 = 26.05 \approx 26 $$
{% endraw %}

In the periodic table it is found that this atomic number corresponds to iron (Fe), which indeed is the element used for the measurement. 

## Playing with XRF physics - Creating a Moseley plot

In order to develop a further intuition of XRF physics beyond Moseley's law, I thought it would be a good thing to create a plot with an overview of theoretical pure element XRF spectra for the complete periodic system. As a tribute to Henry Moseley I would like to name this plot after him.    

I am not an expert in XRF physics whatsoever. And therefore I am not able to predict the complex spectral patterns by myself. However, thanks to the open source scientific community advanced python packages are readily available from the python package index to make generate spectra. An excellent resource for simulating XRF physics is `fisx`, the periodic table can be consulted using `mendeleev`, plotting and peak finding can be done with `scipy` and `matplotlib`. 

*A Moseley plot here soon* 

## Installation 

If you would like to adapt this plot to your own needs, for instance to to see what happens if you change beam energy, you can install this package yourself. 

    $ pip install moseley 
    
    

## Usage 

More info follows soon. 
