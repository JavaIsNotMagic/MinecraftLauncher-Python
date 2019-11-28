import setuptools,os,platform
def reqs():
    windows = open(str(os.getcwd()) + "/req-windows.txt")
    other = open(str(os.getcwd()) + "/req-other.txt")
    if platform.system() == 'Windows':
        return windows.readlines()
    else:
        return other.readlines()
#end

# packages=setuptools.find_packages(),
setuptools.setup(
    name="mcpy",
    version="0.0.1",
    author="Connor Tozer",
    author_email="connor.tozer2017@gmail.com",
    long_description="mc-python is a minecraft launcher written entirley in python. This launcher supports all vanilla versions.",
    description="A Minecraft Launcher written in Python",
    url="https://github.com/JavaIsNotMagic/MinecraftLauncher-Python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #In order to streamline the install, include the requirements.txt
    install_requires=reqs(),
    python_requires='>=3.6',
)
