# Wardrobe AI: AI-Powered Virtual Try-On

## Overview

Wardrobe AI is an innovative AI-driven tool that enables users to virtually try on clothing items using simple image uploads. By providing a photo of a person (e.g., "image1") and an image of the desired clothing (e.g., "image2"), the script generates a realistic composite image showing how the outfit would look on the individual. This bridges the gap between online shopping and real-world fitting, reducing purchase uncertainties and enhancing user experience.

Powered by advanced AI models like Google's Gemini series, the tool leverages computer vision and image generation to ensure natural fits, accurate proportions, lighting, and perspectives. Ideal for e-commerce integrations, personal styling apps, or fashion tech prototypes.

## Key Features

- **Image Upload and Processing**: Automatically detects, validates, and preprocesses input images.
- **AI-Driven Try-On Generation**: Uses prompts to overlay clothing realistically on the person's body.
- **Model Fallback System**: Tries multiple Gemini models (2.5-flash-image-preview, 1.5-flash, 1.5-pro) for reliable results.
- **Output Saving**: Generates and saves the result as "virtual_try_on_result.png".
- **Error Handling**: Robust retries and validation to manage API failures or invalid inputs.

## Requirements

- **Python Version**: 3.8 or higher.
- **Dependencies**:
  - `pillow` (PIL for image handling).
  - Google Gemini API client (via `google-generativeai` or similar).
  - Custom modules: `config.py` (for API client setup), `image_utils.py` (for image finding and validation), `api_utils.py` (for API requests with retries).
- **API Access**: A valid Google API key for Gemini models. Set this up in `config.py`.
- **Input Images**: Place "image1" (person photo) and "image2" (clothing item) in the working directory or a searchable path. Supported formats: JPEG, PNG, etc.

## Installation

1. **Clone the Repository** (if applicable):
   ```
   git clone https://github.com/yourusername/wardrobe-ai.git
   cd wardrobe-ai
   ```

2. **Set Up Virtual Environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```
   pip install pillow google-generativeai
   ```
   Note: Ensure custom modules (`config.py`, `image_utils.py`, `api_utils.py`) are present or implement them based on the script's imports.

4. **Configure API**:
   - In `config.py`, implement `get_client()` to return a Gemini API client instance (e.g., using `genai.GenerativeModel`).
   - Add your API key: `genai.configure(api_key="YOUR_API_KEY")`.

## Usage

1. **Prepare Images**:
   - Rename your person photo to "image1.jpg" (or similar) and clothing to "image2.jpg".
   - Place them in the script's directory.

2. **Run the Script**:
   ```
   python virtual_tryon.py
   ```
   - The script will load images, process them, and attempt generation using the specified models.
   - Output: A new file "virtual_try_on_result.png" in the current directory.

3. **Example Output**:
   - Console logs will show progress, model attempts, and success/failure messages.
   - If successful: "Virtual try-on result saved as 'virtual_try_on_result.png'".
   - If issues arise: Check for file not found errors or API failures.

## How It Works

The core logic is in the `run_virtual_tryon()` function:

- **Image Loading**: Searches for "image1" and "image2" using `find_image_file()`, then validates/preprocesses with `validate_and_preprocess_image()`.
- **API Prompt**: A fixed prompt instructs the AI to composite the clothing onto the person naturally.
- **Model Iteration**: Loops through Gemini models, calling `make_api_request_with_retry()` until success.
- **Response Handling**: Extracts the generated image from the API response and saves it using PIL.

For customization:
- Modify the `PROMPT` string for different try-on behaviors.
- Extend models in the `MODELS` list if more become available.

## Limitations and Troubleshooting

- **API Dependencies**: Requires internet and a valid Gemini API key. Rate limits may apply.
- **Image Quality**: Best results with clear, front-facing person photos and isolated clothing images.
- **Errors**:
  - "FileNotFoundError": Ensure images exist and are named correctly.
  - API failures: Check your key, network, or model availability.
  - No image generated: The response might contain text only; inspect the API output.
- **Scalability**: This is a script-based prototype. For web integration, wrap it in a Flask/Django app.

## Contributing

Contributions welcome! Fork the repo, add features (e.g., multi-clothing support, UI), and submit a pull request. Follow standard Python conventions.

## License

MIT License. See [LICENSE](LICENSE) for details.

