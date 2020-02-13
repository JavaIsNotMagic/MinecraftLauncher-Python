import setuptools,os,platform,subprocess

path = str(os.getcwd())

def reqs():
    windows = open(str(os.getcwd()) + "/bin/req-windows.txt")
    other = open(str(os.getcwd()) + "/bin/req-other.txt")
    if platform.system() == 'Windows':
        return windows.readlines()
    else:
        return other.readlines()
#end

def installWindows():
    launchArgs = [f"{path}/build/install.cmd"]
    try:
        subprocess.run(launchArgs)
    except FileNotFoundError:
        pass
#end

# packages=setuptools.find_packages(),
setuptools.setup(
    name="mcpy",
    version="0.0.4.1",
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
#Now build mcpy for the host's operating system and arch
if platform.system() == 'Windows':
    installWindows()
else:
    pass
#end
launchArgs = [f"{path}/build/install.sh"]
subprocess.run(launchArgs)
