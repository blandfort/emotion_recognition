import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="emotion-recognition-blandfort",
    version="0.0.1",
    author="Philipp Blandfort",
    #author_email="author@example.com",
    license='MIT',
    description="Frame-based emotion recognition using deep learning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blandfort/emotion_recognition",
    packages=setuptools.find_packages(include=['emotion_recognition', 'emotion_recognition.*']),
    install_requires=[
        'opencv-python==4.2.0.34',
        'torch',
        'facenet-pytorch',
        'torchvision',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        #"Operating System :: OS Independent",
        "Operating System :: Linux",
    ],
    python_requires='>=3.6',
)
