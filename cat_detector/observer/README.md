# observer

A module built with `python` and ran originally on a [Raspberry Pi 4](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/?resellerType=home) that produces a stream of photos and uploads them in the cloud in base64 format. 

The photos can be either captured using an attached [camera module](https://www.raspberrypi.org/products/camera-module-v2/?resellerType=home) (**live**) or read from a directory (**disk**)

#
## Structure
- `samples` - contains a collection of photos used in the **disk** mode
- `config.py` - a file containing credentials used to authenticate with the `collector` module and its address
- `main.py` - the source code
- `requirements.txt` - a file containing dependencies declaration

#
## Deployment
1. Install [python 3+](https://www.python.org/downloads/)
    - `pip` and `virtualenv` should also be installed - on Windows they should be installed by default, on Linux-based systems you may have to install them separately

2. Create a virtual environment to avoid polluting the global packages
    - `python3 -m venv sandbox --clear`

3. Activate the virtual environment
    - Windows: `sandbox/Scripts/activate`
    - Linux: `source sandbox/bin/activate`

4. Install the dependencies
    - `pip install -r requirements.txt`
    - if you deploy on Windows, replace `opencv-contrib-python==3.4.3.18` with `opencv-python==4.4.0.46` in [requirements.txt](./requirements.txt) (some errors might arise though)

5. Fill the `config.py` file with adequate inputs

6. Run the application in one of the available modes
    - `python3 main.py live` - capture images using the camera module and send them, one by one, to the `collector` module

    - `python3 main.py disk` - cycle through the photos present in the `samples` directory and send them, one by one, to the `collector` module
    
    - `python3 main.py debug` - test the camera module