from light_captcha import CaptchaGenerator

generator = CaptchaGenerator()
image, number = generator.generate('persian')  # or 'english'
print(f"Generated captcha number: {number}")
image.show()  # Display the generated captcha image
image.save('captcha.png')  # Save the captcha image to a file
image.close()  # Close the image to free resources