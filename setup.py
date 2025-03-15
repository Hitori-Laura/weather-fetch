from setuptools import setup, find_packages

setup(
    name="weather-fetch",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,  # Ensures non-Python files are included
    install_requires=[
        "geocoder",
        "requests",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "weather-fetch=weather.weather:main",
        ],
    },
)

