# Emotion Recognition

_This package contains code for frame-based emotion recognition using deep learning._


## Installation

- Activate virtual environment
- cd to this directory
- `python3 setup.py install`

Usage:

- `train(data_dir, model_path)` from `emotion_recognition.training.py` can be used to train a model
- `validate(data_dir, model_path)` from `emotion_recognition.validation.py` can be used to validate
- Use EmotionRecognition class (give model path to init) for using the model in other ways

TODO update following, and make stuff pretty

- Get the FERPlus dataset:
    - Get the FER-2013 dataset
    - Download additional annotations from https://github.com/microsoft/FERPlus
    - Use the script `generate_training_data.py` from FERPlus to compile the dataset based on the previous two resources
        (`<dataset base folder>` typically should be set to the directory `FERPlus/data`;
         see documentation of FERPlus repository for further details)


### Note on Requirements

For OpenCV on debian, version 4.4.0.44 causes issues, but 4.2.0.34 works.



## Usage

### Training your own Model

- For training a new model, call `python training.py` (might need to adjust `MODEL_PATH` and `DATA_DIR`)
- This will create a file with the trained model once the script finishes or is interrupted (e.g. by `CTRL-C`)


### Validating your Model

- Call `python validate.py`


### Deployment

- For deployment, the class `EmotionRecognition` is used, so import this class first
- Instantiate a model, e.g. by `er = EmotionRecognition(device='cpu')`
- Now you can recognize emotions in three different ways:
    - `er.run(frame)` takes a frame as open-cv image and returns a list (each entry corresponding to one detected face) of results in dict format
    - `er.run_on_face(face) takes an image of a face and returns a dict with results
    - `er.show(frame, return_type)` performs emotion recognition on a given frame and returns a modified frame that includes detection results (as bounding boxes around the faces and labels of detected emotions)


## Status

- Model trained on FERPlus seems reasonable already (SOTA on that dataset is not even that high)
    - Happiness is detected alright
    - For negative emotions it seems to be very conservative though
- Results of displaying certainty of the model as well
    - Not that bad, the model shows uncertainty in some unusual cases
    - -> Still, model doesn't use softmax at the moment and thus becomes overconfident in stuff; perhaps this has to be adjusted
- To improve further, could try the following:
    - Not only consider majority class (to get also some more subtle expressions)
    - Use additional datasets (compile some samples of aff-wild2, taking few from each video, rescaling and saving in separate directories so it can be read easily)
    - Change model architecture (also consider adding dropout)
    - Augment dataset by introducing noise or changing colors
    - How about active learning with my own webcam data?

Potential extensions:

- Consider audio data as well


## Acknowledgements

Some of the code (files `networks.py` and `emotion_recognition.py`) is based on PyPI package `facial-emotion-recognition` (0.3.4) by Rayyan Akhtar: [Go to PyPI page](https://pypi.org/project/facial-emotion-recognition/)
