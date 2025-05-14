from setuptools import setup, find_packages

setup(
    name="cyclegan",
    version="0.1.0",
    description="CycleGAN and pix2pix in PyTorch",
    author="Jun-Yan Zhu",
    url="https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix",
    packages=find_packages(),
    install_requires=[
        "torch>=1.4.0",
        "torchvision>=0.5.0",
        "dominate>=2.4.0",
        "visdom>=0.1.8.8",
        "wandb"
    ],
    python_requires=">=3.6",
)