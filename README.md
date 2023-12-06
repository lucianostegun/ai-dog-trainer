# Dog Behavior Monitor

This Python application uses a Logitech webcam connected to a Raspberry Pi 4 to monitor your dog's behavior and identify instances of peeing in the wrong place. When detected, it emits a sound to train your dog to pee in the right place.

## Requirements

- Logitech webcam
- Raspberry Pi 4
- Python 3.x

## Installation

1. Clone the repository:

```bash
git clone https://github.com/lucianostegun/ai-dog-trainer.git
cd ai-dog-trainer
```

pip install -r requirements.txt

## Configuration

You can customize the behavior of the application by modifying the configuration in the config.py file.

- CAMERA_INDEX: Set the camera index for your Logitech webcam.
- SLEEP_DURATION: Adjust the sleep duration (in seconds) between image captures.
- MODEL_PATH: Specify the path to your pre-trained AI model for dog behavior recognition.
Add any additional configuration options as needed.

## Training the AI Model

Train your AI model using a dataset of images labeled with correct and incorrect dog behaviors. Refer to the documentation of your chosen machine learning library for guidance on model training.
Acknowledgements

This application uses OpenCV for webcam access.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.


## Author
Luciano Stegun

Feel free to contribute or report issues by opening a GitHub issue.
