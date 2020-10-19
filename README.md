# Greenland Ice Mapping Project
Example notebooks for working with data from the [Greenland Ice Sheet Mapping Project](https://nsidc.org/data/measures/gimp), which provides benchmark data sets for observing ice sheet change and stability.

These datasets cover the entire landmass of Greenland and consequently images can be quite large. Often researchers are just interested in data covering a specific glacier. *The goal of these notebooks is to illustrate how to efficiently work with data using modern Python libraries that can read imagery directly on a server without downloading entire files first.* 

We'll work with Sentinel-1 backscatter mosasics stored as [Cloud-Optimized Geotiffs (COG)](https://nsidc.org/data/nsidc-0723). This imagery is publically-available and hosted by NASA's [National Snow and Ice Data Center](https://nsidc.org/data/nsidc-0723).


## Run these notebooks on the Cloud:
Clicking the following button will transport you into a temporary server running on [mybinder.org](https://mybinder.org/)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/scottyhq/greenland-ice-mapping-project/master?urlpath=lab)


## Run these notebooks on your own computer:
This requires that you have [conda](https://docs.conda.io/en/latest/miniconda.html) installed.
```
git clone https://github.com/scottyhq/greenland-ice-mapping-project.git
cd greenland-ice-mapping-project
conda env create -f .binder/environment.yml
conda activate greenland-ice-mapping
jupyter lab
```
