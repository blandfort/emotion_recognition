# Emotion Recognition

_This package contains code for frame-based emotion recognition using deep learning._


## Installation

- Activate virtual environment
- cd to this directory
- `python3 setup.py install`
- Get the FERPlus dataset (used for training and validating models):
    - Get the FER-2013 dataset
    - Download additional annotations from https://github.com/microsoft/FERPlus
    - Use the script `generate_training_data.py` from FERPlus to compile the dataset based on the previous two resources
        (`<dataset base folder>` typically should be set to the directory `FERPlus/data`;
         see documentation of FERPlus repository for further details)


### Note on Requirements

For OpenCV on debian, version 4.4.0.44 causes issues, but 4.2.0.34 works.



## Usage

### Training your own Model

- Call `train(data_dir, model_path)` from `emotion_recognition.training.py` to train a model
- This will create a file with the trained model once the script finishes or is interrupted (e.g. by `CTRL-C`)


### Validating your Model

- Call `validate(data_dir, model_path)` from `emotion_recognition.validation.py` to validate a trained model


### Deployment

- For deployment, the class `EmotionRecognition` is used, so import this class first
- Instantiate a model, e.g. by `from emotion_recognition import EmotionRecognition` and then `er = EmotionRecognition(model_path=model_path, device='cpu')`
- Now you can recognize emotions in three different ways:
    - `er.run(frame)` takes a frame as open-cv image and returns a list (each entry corresponding to one detected face) of results in dict format
    - `er.run_on_face(face) takes an image of a face and returns a dict with results
    - `er.show(frame, return_type)` performs emotion recognition on a given frame and returns a modified frame that includes detection results (as bounding boxes around the faces and labels of detected emotions)


## Status

- Model trained on FERPlus seems reasonable already
    - Happiness is detected alright
    - For negative emotions it seems to be very conservative though
- Displaying certainty of the model as well:
    - Not that bad, the model does show uncertainty in some unusual cases
    - -> Still, model doesn't use softmax at the moment and thus becomes overconfident; perhaps this has to be adjusted
- To improve further, could try the following:
    - Not only consider majority class (to get also some more subtle expressions)
    - Use additional datasets (compile some samples of aff-wild2, taking few from each video, rescaling and saving in separate directories so it can be read easily)
    - Change model architecture (also consider adding dropout)
    - Augment dataset by introducing noise or changing colors
    - How about active learning with own webcam data?

Potential extensions:

- Consider audio data as well


## Acknowledgements

Some of the code (files `networks.py` and `emotion_recognition.py`) is based on PyPI package `facial-emotion-recognition` (0.3.4) by Rayyan Akhtar: [Go to PyPI page](https://pypi.org/project/facial-emotion-recognition/)

That repo from Rayyan was extended significantly, in particular by adding code for training and validating models and making deployment of the model more versatile.
