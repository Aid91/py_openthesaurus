from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as file:
    description = file.read()

setup(name='py_openthesaurus',
      version='1.0.0',
      description='Get synonyms of an input word (German language)',
      long_description=description,
      long_description_content_type="text/markdown",
      classifiers=[
          'Development Status :: 5 - Production/Stable'
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Machine Learning',
          'Intended Audience :: Science/Research',
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: MIT License',
          'Topic :: Natural Language Processing :: German'],
      url='https://github.com/Aid91/py_openthesaurus',
      author='Aid91',
      author_email='aidahmetovic91@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['tests*']),
      entry_points={"console_scripts": ['py_openthesaurus=py_openthesaurus.main:main']},
      zip_safe=False)
