from virtual_tryon import run_virtual_tryon

if __name__ == "__main__":
    try:
        run_virtual_tryon()
    except Exception as e:
        print(f"Error during virtual try-on: {str(e)}")
