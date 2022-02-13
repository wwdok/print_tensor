from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="printensor",
        version="0.0.2",
        description="Print shape of pytorch tensor inside list, tuple, dict, generator",
        long_description=open("README.md", "r").read(),
        long_description_content_type="text/markdown",
        url="https://github.com/wwdok/print_tensor",
        author="Weida Wang",
        author_email="wade.wang96@outlook.com",
        keywords="deep learning",
        platforms=["all"],
        packages=find_packages(),
        install_requires=[],
        classifiers=[
            "Development Status :: 3 - Alpha",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        license='MIT License',
        zip_safe=False,
    )