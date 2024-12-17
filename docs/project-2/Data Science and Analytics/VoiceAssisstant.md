---
sidebar_position: 8
---
# Voice Assistant feature for Elderly Care Wearable.

The goal of this sub-project is to develop and integrate voice assistant functionality into the Elderly care wearable device. 
This is done with the intention of offering a useful method of interacting with and receiving assisstance from the wearable and to bolster the devices accessibility.

This feature aims to be able to answer verbal queries relating to the user's daily scheduling and provide information relating to the user's health based on locally recorded data.

## Implementation
At present the voice assistant is able to repond to queries relating to local time, weather and basic assistance to reported symptoms.
Features in active development include mental health counselling / guidance, making calls, dictating messages and conducting health assessments. 

The project uses the following external sources as part of its design:
- [pygame](https://www.pygame.org/docs/): Python UI Library
- [speech_recognition](https://github.com/Uberi/speech_recognition): Library for parsing spoken word and transcribing to text
- [NeuralIntents](https://github.com/NeuralNine/neuralintents): Library created by python Youtuber / Blogger Florian Dedov aka NeuralNine for rudimentry Voice Assistants.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): The most popular library for parsing HTML and XML.
- [LocationTagger](https://github.com/kaushiksoni10/locationtagger): A Python library implementing location extraction from NLP
- [requests](https://github.com/psf/requests): A library for generating HTTP/1.1 requests

### Structure

#### Voice Assistant Runtime
**main.py**  
    Spins up the UI module `pygame_win` and `speech_to_text` modules and executes them in parallel,  
    Handles overall program execution and termination.

**pygame_win.py**  
    Module implementing UI classes and functions from pygame.

**speech_to_text.py**  
    Wrapper for the speech_recognition library functions that records user spoken queuries and attempts to use Google Speech recognition to convert it into text.

**generate_response.py**  
    Defines the logic for responding to user queries across a number of categories. 
    Creates an assisstant object based on the `intents.json` and supplied pre-trained voice assistant model.

**text_to_speech.py**  
    Calls the get_response function from the `generate_response.py` module,  
    Verbally outputs the generated response.

#### Training

**train_model.py**
Trains the model based on the neuralintents.assistants module and the `intents.json` file.  
Fits the model with `epoch=50`.
Outputs model to `./models/` as:  
- [model_name].keras - A zip file containing the config of the model, .h5 state with the weights and biases and a JSON metadata file
- [model_name]_intents.pkl - A serialized byte stream of the intents object structure.
- [model_name]_words.pkl - A serialized byte stream of the bag-of-words object structure the model was trained on.

## Future Plans
- Broaden scope of the voice assistants subject matter
- Support more languages / multilingualism
- Build compatability with emerging health care technologies
- Implementation into the wearable. 

## Local Development 
To run the project on a local machine, follow these steps:

1. Clone the repository from GitHub
2. Navigate to the Voice Assistant directory
3. Install the required dependencies using pip install -r docs/requirements.txt
4. Use the code in neural_intents_code/assistants.py to update the neuralintents library code. NOTE: This step is required as for this feature, parts of the neuralintents>assistants.py code are updated.
5. To retrain a model, run the train_model.py script
6. Run the main.py script to start the voice assistant feature

:::info
**Document Creation:** 5 September 2024. **Last Edited:** 5 September 2024. **Authors:** Lachlan Costigan
:::
