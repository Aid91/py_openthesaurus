from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as file:
    description = file.read()

setup(name="py_openthesaurus",
      version="1.0.4",
      description="Python wrapper for obtaining synonyms in the German language from OpenThesaurus",
      long_description=description,
      long_description_content_type="text/markdown",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Intended Audience :: Education",
          "Intended Audience :: Information Technology",
          "Intended Audience :: Science/Research",
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Topic :: Text Processing :: General"],
      url="https://github.com/Aid91/py_openthesaurus",
      keywords=["Natural Language Processing", "NLP", "German"],
      author="Aid Ahmetovic",
      author_email="aidahmetovic91@gmail.com",
      license="MIT",
      packages=find_packages(exclude=["tests*"]),
      install_requires=['mysqlclient==1.4.4'],
      entry_points={"console_scripts": ["py_openthesaurus=py_openthesaurus.main:main"]},
      python_requires=">=3.5")