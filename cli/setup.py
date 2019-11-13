import setuptools
setuptools.setup(
    name="mcpython", # Replace with your own username
    version="0.0.2a",
    author="Connor Tozer",
    author_email="connor.tozer2017@gmail.com",
    long_description="mc-python is a minecraft launcher written entirley in python. This launcher supports all vanilla versions.",
    description="A minecraft launcher written entirely in Python3",
    url="https://github.com/JavaIsNotMagic/MinecraftLauncher-Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
