from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("light_captcha/__init__.py", "r", encoding="utf-8") as fh:
    for line in fh:
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip('"')
            break

setup(
    name="light-captcha",
    version=version,
    author="Alireza",
    description="A lightweight CAPTCHA generator for Persian and English digits",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/COD332/light-captcha",
    packages=find_packages(),
    package_data={
        "light_captcha": ["fonts/*.ttf"],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security",
        "Topic :: Multimedia :: Graphics",
    ],
    python_requires=">=3.7",
    install_requires=[
        "Pillow>=8.0.0",
        "importlib_resources>=1.3.0; python_version<'3.9'"
    ],
    keywords=["captcha", "persian", "english", "security", "image", "generation"],
)
