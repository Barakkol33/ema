from setuptools import setup, find_packages

# Configuration for pypi upload

setup(name="ema",
      version=1.0,
      description="Hardware Control Library",
      author="EMA Team",
      keywords="ema",
      packages=find_packages("src"),
      package_dir={"": "src"},
      include_package_data=True,
      # These are the version numbers that worked.
      install_requires=["pyfirmata>=1.1.0", "pyserial>=3.5", "pyyaml>=5.4.1"],
      python_requires=">=3",
      zip_safe=False)