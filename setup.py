from setuptools import setup, find_packages

setup(
    name='studentXX_flask_app',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['main'],  # Explicitly include main.py
    install_requires=[
        'Flask>=3.0.3',
        # Add other dependencies here
    ],
)

