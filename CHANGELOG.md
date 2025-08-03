# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.2] - 2025-08-03

### Added
- **Output Format Options**: New `output` parameter in `generate()` method
  - `output='image'`: Returns PIL Image object (default, backward compatible)
  - `output='base64'`: Returns base64-encoded PNG string for web integration
- **Enhanced Font Loading**: Improved font resource loading for better cross-platform compatibility
  - Uses `importlib.resources` for Python 3.9+
  - Falls back to `pkg_resources` for older Python versions
  - Final fallback to relative path for development environments
- **Better Error Handling**: More descriptive error messages and validation
- **Web Integration Examples**: Added comprehensive examples for web application usage

### Fixed
- **Font Loading Issues**: Resolved PIL font format errors when package is installed system-wide
- **Cross-platform Compatibility**: Fixed font path issues across different operating systems
- **Resource Access**: Proper package resource loading that works in all installation scenarios

### Changed
- **Dependencies**: Added `importlib_resources>=1.3.0` for Python < 3.9
- **Documentation**: Updated README with new features and comprehensive examples
- **API**: Extended `generate()` method with `output` parameter (backward compatible)

### Technical Details
- Improved font resource loading mechanism using multiple fallback strategies
- Added base64 encoding functionality with proper PNG format
- Enhanced error handling for invalid parameters
- Maintained full backward compatibility with existing code

## [0.0.1] - 2025-08-02

### Added
- Initial release
- Persian and English digit CAPTCHA generation
- Random digit skewing and rotation
- Wave distortion effects
- Customizable colors and dimensions
- Noise and interference patterns
- Millisecond-based random number generation
