from setuptools import setup
setup(
    name="wikinet",
    version="0.1",
    packages=["wikinet"],
    install_requires=["numpy", "h5py", "tqdm"],
    python_requires="~=3.4",
    author="Joseph Kleinhenz",
    description="tool for extracting link network from wiki xml dumps",
    license="MIT"
)
