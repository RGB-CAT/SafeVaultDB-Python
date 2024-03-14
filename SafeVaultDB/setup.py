from setuptools import setup, find_packages

VERSION = '1.0.2' 
DESCRIPTION = 'a free database library for python'
with open("./Description.md", "r") as f:
    LONG_DESCRIPTION = f.read()

# Setting up
setup(
        name="SafeVaultDB", 
        version=VERSION,
        author="RGB_CATT",
        author_email="<RGBCAT@duck.com>",  # Fill in your email address
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        entry_points={
            'console_scripts': [
                'SafeVaultDB = SafeVaultDB.cli:main',
            ],
        },
        url="https://github.com/RGB-CAT/SafeVaultDB-Python",
        packages=find_packages(),
        install_requires=["cryptography"],
        keywords=['python', 'database'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
