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
- 🖼️ **NEW in v0.0.2**: Output format options (PIL Image or base64)
- 🔧 **NEW in v0.0.2**: Improved font resource loading for better cross-platform compatibility

## Installation

```bash
pip install light-captcha
```

## Quick Start

```python
from light_captcha import CaptchaGenerator

# Create generator instance
generator = CaptchaGenerator()

# Generate English CAPTCHA as PIL Image (default)
image, number = generator.generate('english')
image.save('captcha_english.png')
print(f"Generated number: {number}")

# Generate Persian CAPTCHA as base64 string
base64_str, number = generator.generate('persian', output='base64')
print(f"Generated number: {number}")
print(f"Base64 data: {base64_str[:50]}...")
```

## Usage Examples

### Output Format Options (New in v0.0.2)

```python
# Generate as PIL Image object (default)
image, number = generator.generate('english', output='image')
image.save('captcha.png')

# Generate as base64 string for web applications
base64_str, number = generator.generate('english', output='base64')
html_img = f'<img src="data:image/png;base64,{base64_str}" alt="CAPTCHA">'
```

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
    text_color=text_color,
    output='image'
)
```

### Web Application Integration

```python
generator = CaptchaGenerator()

# For APIs and web frameworks
base64_captcha, correct_answer = generator.generate(
    language='english',
    width=250, 
    height=80,
    output='base64'
)

# Store correct_answer in session for validation
# Send base64_captcha to frontend
```

### Batch Generation

```python
generator = CaptchaGenerator()

# Generate multiple CAPTCHAs with different formats
for i in range(5):
    # Image format
    image, number = generator.generate('persian', output='image')
    image.save(f'captcha_img_{i}.png')
    
    # Base64 format  
    base64_str, number = generator.generate('english', output='base64')
    with open(f'captcha_b64_{i}.txt', 'w') as f:
        f.write(base64_str)
    
    print(f"CAPTCHA {i}: {number}")
```

## API Reference

### CaptchaGenerator

#### `generate(language, width=250, height=80, bg_color=None, text_color=None, output='image')`

Generate a CAPTCHA image.

**Parameters:**
- `language` (str): `'english'` or `'persian'`
- `width` (int): Image width in pixels (default: 250)
- `height` (int): Image height in pixels (default: 80)  
- `bg_color` (tuple, optional): RGB background color
- `text_color` (tuple, optional): RGB text color
- `output` (str): `'image'` for PIL Image object or `'base64'` for base64 string (default: 'image')

**Returns:**
- `tuple`: (PIL Image object or base64 string, 6-digit string)

**Raises:**
- `ValueError`: If language is not 'english' or 'persian'
- `ValueError`: If output is not 'image' or 'base64'  
- `FileNotFoundError`: If required font file is missing

## What's New in v0.0.2

### Enhanced Font Loading
- Improved font resource loading using `importlib.resources` for better cross-platform compatibility
- Automatic fallback mechanisms for different Python versions
- Resolves PIL font format errors when package is installed system-wide

### Output Format Options
- **Image Output**: Returns PIL Image object (default, backward compatible)
- **Base64 Output**: Returns base64-encoded PNG string for direct web integration

### Better Error Handling
- More descriptive error messages for font loading issues
- Validation for output format parameter
- Improved cross-platform compatibility

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
- importlib_resources >= 1.3.0 (for Python < 3.9)

## License

MIT License - see LICENSE file for details.

## Contributing

Issues and pull requests are welcome on [GitHub](https://github.com/COD332/light-captcha).