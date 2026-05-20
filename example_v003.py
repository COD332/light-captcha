#!/usr/bin/env python3
"""
Example usage of light-captcha v0.0.3.
"""

from light_captcha import CaptchaGenerator
import base64
from io import BytesIO
from PIL import Image


def example_image_output():
    """Generate CAPTCHA as PIL Image object."""
    print("=== Image Output Example ===")
    generator = CaptchaGenerator()

    image, number = generator.generate(
        language="english",
        width=300,
        height=100,
        output="image"
    )

    print(f"Generated number: {number}")
    print(f"Image type: {type(image)}")
    print(f"Image size: {image.size}")

    image.save("captcha_english.png")
    print("Image saved as 'captcha_english.png'")

    image, number = generator.generate(
        language="persian",
        width=300,
        height=100,
        output="image"
    )

    print(f"Generated Persian number: {number}")
    image.save("captcha_persian.png")
    print("Persian image saved as 'captcha_persian.png'")


def example_base64_output():
    """Generate CAPTCHA as base64 string."""
    print("\n=== Base64 Output Example ===")
    generator = CaptchaGenerator()

    base64_str, number = generator.generate(
        language="english",
        width=250,
        height=80,
        output="base64"
    )

    print(f"Generated number: {number}")
    print(f"Base64 string length: {len(base64_str)}")
    print(f"Base64 preview: {base64_str[:100]}...")

    image_data = base64.b64decode(base64_str)
    image = Image.open(BytesIO(image_data))
    image.save("captcha_from_base64.png")
    print("Converted base64 to image and saved as 'captcha_from_base64.png'")

    html_data_uri = f"data:image/png;base64,{base64_str}"
    print(f"HTML data URI length: {len(html_data_uri)}")
    print("You can use this data URI directly in HTML img tags!")


def example_web_integration():
    """How to use in web applications."""
    print("\n=== Web Integration Example ===")
    generator = CaptchaGenerator()

    base64_captcha, correct_number = generator.generate(
        language="english",
        output="base64"
    )

    print("For web frameworks (Flask, Django, FastAPI):")
    print(f"Store in session: correct_number = '{correct_number}'")
    print(f"Send to frontend: base64_data = '{base64_captcha[:50]}...'")

    print("\nExample HTML:")
    print(f'<img src="data:image/png;base64,{base64_captcha[:30]}..." alt="CAPTCHA">')

    image_captcha, correct_number = generator.generate(
        language="persian",
        output="image"
    )
    print("\nFor file-based APIs:")
    print("Save image temporarily and return file path")
    print("Or convert to BytesIO for direct streaming")


def example_custom_styling():
    """Custom colors and sizes."""
    print("\n=== Custom Styling Example ===")
    generator = CaptchaGenerator()

    dark_captcha, number = generator.generate(
        language="english",
        width=400,
        height=120,
        bg_color=(30, 30, 30),
        text_color=(255, 255, 255),
        output="base64"
    )

    print(f"Dark theme CAPTCHA (base64): {number}")
    print(f"Base64 length: {len(dark_captcha)}")

    colorful_captcha, number = generator.generate(
        language="persian",
        width=350,
        height=90,
        bg_color=(255, 248, 220),
        text_color=(139, 69, 19),
        output="image"
    )

    print(f"Colorful theme CAPTCHA (image): {number}")
    colorful_captcha.save("captcha_colorful.png")


def example_error_handling():
    """Proper error handling examples."""
    print("\n=== Error Handling Example ===")
    generator = CaptchaGenerator()

    try:
        generator.generate(language="invalid")
    except ValueError as exc:
        print(f"Caught expected error for invalid language: {exc}")

    try:
        generator.generate(output="invalid")
    except ValueError as exc:
        print(f"Caught expected error for invalid output: {exc}")

    try:
        image, number = generator.generate()
        print(f"Font loading test passed: {number}")
    except Exception as exc:
        print(f"Font loading error: {exc}")


if __name__ == "__main__":
    example_image_output()
    example_base64_output()
    example_web_integration()
    example_custom_styling()
    example_error_handling()

    print("\n" + "=" * 50)
    print("All examples completed!")
    print("Check the generated image files:")
    print("- captcha_english.png")
    print("- captcha_persian.png")
    print("- captcha_from_base64.png")
    print("- captcha_colorful.png")
