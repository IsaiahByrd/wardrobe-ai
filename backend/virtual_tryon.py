from io import BytesIO
from PIL import Image
from config import get_client
from image_utils import find_image_file, validate_and_preprocess_image
from api_utils import make_api_request_with_retry

PROMPT = (
    "Take the clothing items from the second image and put them on the person in the first image." 
    "Generate ONE single, realistic composite image of the person wearing ONLY the clothing from the second image." 
    "Do NOT include multiple versions of the person, do NOT show the original outfit, and do NOT create before-and-after comparisons." 
    "The result must contain exactly one person, wearing the new clothes naturally, with proper proportions, lighting, and perspective."
)

MODELS = [
    "gemini-2.5-flash-image-preview",
    "gemini-1.5-flash",
    "gemini-1.5-pro"
]

def run_virtual_tryon():
    client = get_client()
    print("Loading and validating images...")

    person_image_file = find_image_file("image1")
    clothing_image_file = find_image_file("image2")

    if not person_image_file:
        raise FileNotFoundError("Error: image1 not found.")
    if not clothing_image_file:
        raise FileNotFoundError("Error: image2 not found.")

    print(f"Found person image: {person_image_file}")
    print(f"Found clothing image: {clothing_image_file}")

    person_image = validate_and_preprocess_image(person_image_file)
    clothing_image = validate_and_preprocess_image(clothing_image_file)

    if not person_image or not clothing_image:
        raise ValueError("Error: Failed to process one or both images")

    print("Generating virtual try-on...")
    response = None
    last_error = None

    for model in MODELS:
        try:
            print(f"Trying model: {model}")
            response = make_api_request_with_retry(
                client, model, [PROMPT, person_image, clothing_image]
            )
            print(f"Success with model: {model}")
            break
        except Exception as e:
            last_error = e
            print(f"Model {model} failed: {str(e)}")
            continue

    if not response:
        raise Exception(f"All models failed. Last error: {str(last_error)}")

    image_generated = False
    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print("Response:", part.text)
        elif part.inline_data is not None:
            try_on_image = Image.open(BytesIO(part.inline_data.data))
            try_on_image.save("virtual_try_on_result.png")
            print("Virtual try-on result saved as 'virtual_try_on_result.png'")
            image_generated = True

    if not image_generated:
        print("Warning: No image was generated in the response")
