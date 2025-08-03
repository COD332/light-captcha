import random
import math
import time
import os
import base64
import io
try:
    from importlib import resources
except ImportError:
    # Python < 3.9 fallback
    import importlib_resources as resources
from PIL import Image, ImageDraw, ImageFont


class CaptchaGenerator:
    """Generate CAPTCHA images with Persian or English digits."""
    
    # Persian-English digit mapping
    PERSIAN_DIGITS = {'0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', 
                     '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'}
    
    # Color palettes for backgrounds and text
    LIGHT_BACKGROUNDS = [
        (240, 240, 240), (245, 245, 220), (250, 240, 230), (230, 230, 250),
        (240, 248, 255), (245, 255, 250), (255, 240, 245), (248, 248, 255),
        (255, 250, 240), (250, 255, 250)
    ]
    
    DARK_TEXTS = [
        (50, 50, 50), (75, 50, 50), (50, 75, 50), (50, 50, 75),
        (100, 50, 50), (50, 100, 50), (50, 50, 100), (75, 75, 50),
        (75, 50, 75), (50, 75, 75)
    ]
    
    def __init__(self):
        """Initialize the CAPTCHA generator."""
        self.font_path = self._get_font_path()
        
    def _get_font_path(self):
        """Get the path to the Vazirmatn font using proper resource loading."""
        try:
            # Try using importlib.resources (Python 3.9+)
            try:
                font_ref = resources.files('light_captcha.fonts').joinpath('Vazirmatn-Regular.ttf')
                if hasattr(font_ref, '__enter__'):  # Context manager support
                    return font_ref
                else:
                    # For older versions, extract to temporary location
                    with resources.as_file(font_ref) as font_path:
                        return str(font_path)
            except AttributeError:
                # Fallback for older Python versions
                import pkg_resources
                font_path = pkg_resources.resource_filename('light_captcha', 'fonts/Vazirmatn-Regular.ttf')
                if os.path.exists(font_path):
                    return font_path
                raise FileNotFoundError(f"Font file not found via pkg_resources: {font_path}")
        except (ImportError, FileNotFoundError):
            # Final fallback to relative path
            current_dir = os.path.dirname(os.path.abspath(__file__))
            font_path = os.path.join(current_dir, 'fonts', 'Vazirmatn-Regular.ttf')
            
            if not os.path.exists(font_path):
                raise FileNotFoundError(f"Font file not found: {font_path}")
                
            return font_path
    
    def _load_font(self, size):
        """Load font with proper resource handling."""
        font_resource = self.font_path
        if hasattr(font_resource, '__enter__'):  # Context manager
            with font_resource as font_path:
                return ImageFont.truetype(str(font_path), size)
        else:
            return ImageFont.truetype(font_resource, size)
            
    def _generate_number(self):
        """Generate a 6-digit number using millisecond-based seed."""
        seed = int(time.time() * 1000) % 1000000
        random.seed(seed)
        return f"{random.randint(100000, 999999)}"
    
    def _convert_to_persian(self, number_str):
        """Convert English digits to Persian."""
        return ''.join(self.PERSIAN_DIGITS[digit] for digit in number_str)
    
    def _select_colors(self, bg_color=None, text_color=None):
        """Select background and text colors."""
        if bg_color is None:
            bg_color = random.choice(self.LIGHT_BACKGROUNDS)
        if text_color is None:
            text_color = random.choice(self.DARK_TEXTS)
        return bg_color, text_color
    
    def _apply_distortion(self, image):
        """Apply wave distortion to the image."""
        width, height = image.size
        distorted = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        
        for x in range(width):
            for y in range(height):
                # Wave distortion
                offset_x = int(3 * math.sin(2 * math.pi * y / 30))
                offset_y = int(2 * math.sin(2 * math.pi * x / 25))
                
                src_x = max(0, min(width - 1, x - offset_x))
                src_y = max(0, min(height - 1, y - offset_y))
                
                pixel = image.getpixel((src_x, src_y))
                distorted.putpixel((x, y), pixel)
                
        return distorted
    
    def _add_noise(self, draw, width, height, text_color):
        """Add noise and interference patterns."""
        noise_color = (
            min(255, text_color[0] + 50),
            min(255, text_color[1] + 50),
            min(255, text_color[2] + 50)
        )
        
        # Random curved lines (reduced by half)
        for _ in range(random.randint(1, 3)):
            points = []
            for i in range(4):
                x = random.randint(0, width)
                y = random.randint(0, height)
                points.extend([x, y])
            
            # Draw thick curved line using multiple thin lines
            for offset in range(-2, 3):
                offset_points = []
                for i in range(0, len(points), 2):
                    offset_points.extend([points[i] + offset, points[i+1]])
                
                try:
                    for i in range(0, len(offset_points) - 2, 2):
                        draw.line([offset_points[i], offset_points[i+1], 
                                 offset_points[i+2], offset_points[i+3]], 
                                fill=noise_color, width=1)
                except:
                    pass
        
        # Random dots (reduced by half)
        for _ in range(random.randint(10, 20)):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            draw.ellipse([x-1, y-1, x+1, y+1], fill=noise_color)
    
    def _draw_skewed_digits(self, image, digits, font_size, text_color):
        """Draw digits with random skewing and distortion."""
        width, height = image.size
        font = self._load_font(font_size)
        
        # Calculate total text width for centering
        total_width = 0
        digit_widths = []
        for digit in digits:
            bbox = font.getbbox(digit)
            digit_width = bbox[2] - bbox[0]
            digit_widths.append(digit_width)
            total_width += digit_width
        
        # Add spacing between digits
        spacing = max(5, font_size // 10)
        total_width += spacing * (len(digits) - 1)
        
        # Start position for centering
        current_x = (width - total_width) // 2
        
        for i, digit in enumerate(digits):
            # Create individual digit image
            digit_img = Image.new('RGBA', (digit_widths[i] + 20, height), (0, 0, 0, 0))
            digit_draw = ImageDraw.Draw(digit_img)
            
            # Random size variation
            size_factor = random.uniform(0.8, 1.2)
            digit_font = self._load_font(int(font_size * size_factor))
            
            # Draw digit with vertical centering
            bbox = digit_font.getbbox(digit)
            digit_height = bbox[3] - bbox[1]
            y_pos = (height - digit_height) // 2 - bbox[1]
            
            digit_draw.text((10, y_pos), digit, font=digit_font, fill=text_color)
            
            # Random rotation
            angle = random.uniform(-15, 15)
            digit_img = digit_img.rotate(angle, expand=False)
            
            # Apply distortion to individual digit
            digit_img = self._apply_distortion(digit_img)
            
            # Paste onto main image
            image.alpha_composite(digit_img.resize((digit_widths[i] + 20, height)), 
                                (current_x - 10, 0))
            
            current_x += digit_widths[i] + spacing
    
    def generate(self, language='english', width=250, height=80, 
                bg_color=None, text_color=None, output='image'):
        """
        Generate a CAPTCHA image.
        
        Args:
            language (str): 'english' or 'persian'
            width (int): Image width in pixels
            height (int): Image height in pixels  
            bg_color (tuple): RGB background color (optional)
            text_color (tuple): RGB text color (optional)
            output (str): 'image' for PIL Image object or 'base64' for base64 string
            
        Returns:
            tuple: (PIL Image object or base64 string, digit string)
        """
        if language not in ['english', 'persian']:
            raise ValueError("Language must be 'english' or 'persian'")
            
        if output not in ['image', 'base64']:
            raise ValueError("Output must be 'image' or 'base64'")
        
        # Generate number and convert if needed
        number = self._generate_number()
        display_number = self._convert_to_persian(number) if language == 'persian' else number
        
        # Select colors
        bg_color, text_color = self._select_colors(bg_color, text_color)
        
        # Create base image
        image = Image.new('RGBA', (width, height), bg_color + (255,))
        draw = ImageDraw.Draw(image)
        
        # Calculate font size
        font_size = min(width // 8, height - 20)
        
        # Draw digits with effects
        self._draw_skewed_digits(image, display_number, font_size, text_color)
        
        # Add noise
        self._add_noise(draw, width, height, text_color)
        
        # Convert to RGB for final output
        final_image = Image.new('RGB', (width, height), bg_color)
        final_image.paste(image, mask=image.split()[-1])
        
        # Return based on output format
        if output == 'base64':
            buffer = io.BytesIO()
            final_image.save(buffer, format='PNG')
            img_str = base64.b64encode(buffer.getvalue()).decode()
            return img_str, number
        else:
            return final_image, number
