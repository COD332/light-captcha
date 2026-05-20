# Light Captcha

A lightweight Python library for generating CAPTCHA images with Persian (۰-۹) and English (0-9) digits.

## Features

- Supports Persian and English numerals
- Random digit skewing and rotation
- Size variations per digit
- Millisecond-based random number generation
- Wave distortion effects
- Random color schemes
- Noise and interference patterns
- Customizable image dimensions
- Output as PIL Image or base64 string
- Reliable font loading across platforms (v0.0.3)

## Installation

```bash
pip install light-captcha
```

## Quickstart

```python
from light_captcha import CaptchaGenerator

generator = CaptchaGenerator()

# English CAPTCHA as PIL Image (default)
image, number = generator.generate("english")
image.save("captcha_english.png")
print(f"Generated number: {number}")

# Persian CAPTCHA as base64 string
base64_str, number = generator.generate("persian", output="base64")
print(f"Generated number: {number}")
print(f"Base64 data: {base64_str[:50]}...")
```

## API Reference

### CaptchaGenerator

#### generate(language, width=250, height=80, bg_color=None, text_color=None, output="image")

Generate a CAPTCHA image.

Parameters:
- language (str): "english" or "persian"
- width (int): image width in pixels (default: 250)
- height (int): image height in pixels (default: 80)
- bg_color (tuple, optional): RGB background color
- text_color (tuple, optional): RGB text color
- output (str): "image" for a PIL Image or "base64" for a base64 string (default: "image")

Returns:
- tuple: (PIL Image or base64 string, 6-digit string)

Raises:
- ValueError: invalid language or output
- FileNotFoundError: missing font file in the package

## Advanced Usage

### Output Formats

```python
image, number = generator.generate("english", output="image")
image.save("captcha.png")

base64_str, number = generator.generate("english", output="base64")
html_img = f'<img src="data:image/png;base64,{base64_str}" alt="CAPTCHA">'
```

### Custom Dimensions

```python
image, number = generator.generate("english", width=300, height=100)
```

### Custom Colors

```python
bg_color = (240, 248, 255)
text_color = (25, 25, 112)
image, number = generator.generate(
    "english",
    bg_color=bg_color,
    text_color=text_color,
    output="image"
)
```

### Web Integration

```python
base64_captcha, correct_answer = generator.generate(
    language="english",
    width=250,
    height=80,
    output="base64"
)

# Store correct_answer in session for validation
# Send base64_captcha to frontend
```

### Batch Generation

```python
for i in range(5):
    image, number = generator.generate("persian", output="image")
    image.save(f"captcha_img_{i}.png")

    base64_str, number = generator.generate("english", output="base64")
    with open(f"captcha_b64_{i}.txt", "w") as f:
        f.write(base64_str)

    print(f"CAPTCHA {i}: {number}")
```

## Error Handling

```python
try:
    generator.generate(language="invalid")
except ValueError as exc:
    print(f"Invalid language: {exc}")
```

## Security Notes

- Random rotation per digit: -15 to +15 degrees
- Random scaling: 0.8x to 1.2x
- Wave distortion with noise lines and dots
- Multiple predefined color palettes
- Millisecond-based seeding

## Compatibility

- Python 3.7+
- Pillow >= 8.0.0
- importlib_resources >= 1.3.0 (Python < 3.9)

## What's New in v0.0.3

- Font loading now reads font data into memory for reliable installs
- Resource loading fallback chain improved for cross-platform consistency

## License

MIT License - see LICENSE for details.

## Contributing

Issues and pull requests are welcome on GitHub:
https://github.com/COD332/light-captcha