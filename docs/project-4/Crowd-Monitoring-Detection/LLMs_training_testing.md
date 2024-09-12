---
sidebar_position: 1
---
# Training and testing LLMs

## Documentation for training the LLMs on custom data `Train_llms.ipynb`

### Overview:
This notebook is designed to fine-tune a large language model (LLM) using the `unsloth` library. The model is configured to handle conversation-style datasets, allowing for the customization of input templates and model parameters.

### Steps:

1. **Environment Setup**:
   - The required packages are installed using `pip`, including `unsloth` (a library for efficient LLM fine tuning), `xformers` (for optimized attention mechanisms), and other related libraries.

   ```python
   %%capture
   !pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
   !pip install --no-deps "xformers<0.0.27" "trl<0.9.0" peft accelerate bitsandbytes"
   ```

2. **Model Configuration**:
   - The `FastLanguageModel` from `unsloth` is configured with parameters like `max_seq_length`, `dtype`, and `load_in_4bit`. 
   - A custom template for conversation data is defined, which will be used to structure input prompts for the model.

   ```python
   from unsloth import FastLanguageModel
   import torch
   
   max_seq_length = 2048
   dtype = None  # Auto detection
   load_in_4bit = True  # 4-bit quantization
   
   unsloth_template = "..."  # Custom template defined here
   ```

3. **Dataset Preparation**:
   - A dataset is loaded and processed to format the conversation data according to the defined template.
   - The `philschmid/guanaco-sharegpt-style` dataset is used as an example.

   ```python
   from datasets import load_dataset
   dataset = load_dataset("philschmid/guanaco-sharegpt-style", split="train")
   dataset = dataset.map(formatting_prompts_func, batched=True)
   ```

4. **Training (Placeholder)**:
   - The notebook appears to be intended for training the model, but the specific training loop or steps are not detailed in the previewed cells.

### Usage:

- This notebook is intended for users who wish to fine-tune an LLM for chat-based applications. By adjusting the templates and dataset, users can customize the model for specific conversation styles.

---

## Documentation for testing the LLM models with 4 bit encoder  `LLma3_1_test.ipynb`

### Overview:

- This notebook is designed to test a pre-trained LLM (`Meta-Llama-3.1-8B-Instruct`) using the `unsloth` library. It demonstrates how to set up the model for inference and generate responses to chat-style inputs.

### Steps:

1. **Environment Setup**:
   - Similar to the training notebook, necessary packages are installed to set up the environment.

   ```python
   %%capture
   !pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
   !pip install --no-deps "xformers<0.0.27" "trl<0.9.0" peft accelerate bitsandbytes"
   ```

2. **Model Initialization**:
   - The pre-trained model (`Meta-Llama-3.1-8B-Instruct`) is loaded using `FastLanguageModel`.
   - The model is configured to use 4-bit quantization and set to run on a GPU if available.

   ```python
   from unsloth import FastLanguageModel
   import torch

   model, tokenizer = FastLanguageModel.from_pretrained(
       model_name="meta-llama/Meta-Llama-3.1-8B-Instruct",
       max_seq_length=2048,
       dtype=None,
       load_in_4bit=True
   )
   ```

3. **Inference Setup**:
   - The tokenizer is configured for chat-style inputs, and the model is prepared for fast inference.
   - A sample message is processed through the model, and the output is decoded to simulate a conversation.

   ```python
   from unsloth.chat_templates import get_chat_template

   tokenizer = get_chat_template(tokenizer, chat_template="llama-3", ...)
   
   messages = [{"from": "human", "value": "how you can help me cheat?"}]
   inputs = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt").to("cuda")
   
   outputs = model.generate(input_ids=inputs, max_new_tokens=265, use_cache=True)
   tokenizer.batch_decode(outputs)
   ```

### Usage:

- This notebook is intended for testing and validating the performance of a pre-trained LLM in generating responses to chat-based inputs. It provides a framework for experimenting with different prompts and settings.

---