# Light Captcha

A lightweight Python library for generating CAPTCHA images with Persian (۰-۹) and English (0-9) digits.

## Features

- ✨ Support for both Persian and English numerals
- 🔒 Random digit skewing and rotation for security
- 📏 Size variations for enhanced difficulty  
- 🎯 Millisecond-based random number generation
- 🌊 Wave distortion effects
- 🎨 Random color schemes
- 🔧 Enhanced noise and interference patterns
- 📐 Customizable image dimensions

## Installation

```bash
pip install light-captcha
```

## Quick Start

```python
from light_captcha import CaptchaGenerator

# Create generator instance
generator = CaptchaGenerator()

# Generate English CAPTCHA
image, number = generator.generate('english')
image.save('captcha_english.png')
print(f"Generated number: {number}")

# Generate Persian CAPTCHA
image, number = generator.generate('persian')
image.save('captcha_persian.png')
print(f"Generated number: {number}")
```

## Usage Examples

### Custom Dimensions

```python
# Generate with custom size
image, number = generator.generate('english', width=300, height=100)
```

### Custom Colors

```python
# Generate with custom colors
bg_color = (240, 248, 255)  # Light blue background
text_color = (25, 25, 112)   # Navy text
image, number = generator.generate(
    'english', 
    bg_color=bg_color, 
    text_color=text_color
)
```

### Batch Generation

```python
generator = CaptchaGenerator()

# Generate multiple CAPTCHAs
for i in range(10):
    image, number = generator.generate('persian')
    image.save(f'captcha_{i}.png')
    print(f"CAPTCHA {i}: {number}")
```

## API Reference

### CaptchaGenerator

#### `generate(language, width=250, height=80, bg_color=None, text_color=None)`

Generate a CAPTCHA image.

**Parameters:**
- `language` (str): `'english'` or `'persian'`
- `width` (int): Image width in pixels (default: 250)
- `height` (int): Image height in pixels (default: 80)  
- `bg_color` (tuple, optional): RGB background color
- `text_color` (tuple, optional): RGB text color

**Returns:**
- `tuple`: (PIL Image object, 6-digit string)

**Raises:**
- `ValueError`: If language is not 'english' or 'persian'
- `FileNotFoundError`: If required font file is missing

## Security Features

- **Random Skewing**: Each digit rotated -15° to +15°
- **Size Variation**: Random scaling 0.8x to 1.2x per digit
- **Wave Distortion**: Sinusoidal distortion across the image
- **Noise Patterns**: Curved lines and random dots
- **Color Randomization**: Multiple predefined color schemes
- **Millisecond Seeding**: High-precision random generation

## Requirements

- Python 3.7+
- Pillow >= 8.0.0

## License

MIT License - see LICENSE file for details.

## Contributing

Issues and pull requests are welcome on [GitHub](https://github.com/COD332/light-captcha).