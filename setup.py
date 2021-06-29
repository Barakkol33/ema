from setuptools import setup, find_packages

setup(name="ema",
      version=1.2,
      description="Hardware Control Library",
      author="EMA Team",
      keywords="ema",
      packages=find_packages("src"),
      packages_dir={"": "src"},
      include_package_data=True,
      install_requires=["pyfirmata"],
      python_requires=">=3",
      zip_safe=False)