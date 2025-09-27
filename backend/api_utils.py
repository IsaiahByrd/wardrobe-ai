import time

def make_api_request_with_retry(client, model, contents, max_retries=3, base_delay=1):
    """Make API request with retry logic and exponential backoff"""
    for attempt in range(max_retries):
        try:
            print(f"API request attempt {attempt + 1}/{max_retries}")
            response = client.models.generate_content(
                model=model,
                contents=contents,
            )
            if response and response.candidates:
                return response
            else:
                print("Warning: Empty or invalid response received")
        except Exception as e:
            error_str = str(e)
            print(f"Attempt {attempt + 1} failed: {error_str}")
            if "500" in error_str or "INTERNAL" in error_str or "timeout" in error_str.lower():
                if attempt < max_retries - 1:
                    delay = base_delay * (2 ** attempt)
                    print(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                    continue
            raise e
    raise Exception(f"All {max_retries} attempts failed")
