## Python wrapper for obtaining synonyms in German language from OpenThesaurus

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2a302faa81aa41ed8647d917c268f5cd)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Aid91/py_openthesaurus&amp;utm_campaign=Badge_Grade)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

When working in Natural Language Processing (NLP) area, synonyms can be an essential part of the data augmentation process. The task of obtaining synonyms for the German language is currently limited since there are no easily accessible lexical databases for the German language. Compared to the WordNet
lexical database for the English language, which is available as an **nltk** package,  [GermaNet](http://www.sfs.uni-tuebingen.de/GermaNet/) represents only one German lexical database alternative. However, to use **GermaNet** for further research purposes, it is necessary to obtain the license manually. 

This repository represents a Python wrapper implementation for obtaining synonyms in a faster and easier way, using the German synonym database and API from [OpenThesaurus](https://www.openthesaurus.de/).

### Installation

The library can be installed from PyPI:

```pip install py_openthesaurus```

### Usage

As a Python library:

```python
from py_openthesaurus import OpenThesaurus

open_thesaurus = OpenThesaurus(word="München")

# to get the short version of synonyms as a list
synonyms = open_thesaurus.get_synonyms()

# to get the long version of synonyms as a list
synonyms_long = open_thesaurus.get_synonyms(form='long')
```

As a command-line tool:

```console
usage: py_openthesaurus [-h] [--form {long,short}] --word WORD

Get synonyms of German words from www.openthesaurus.de

optional arguments:
  -h, --help           show this help message and exit
  --form {long,short}  Defaults to form=short which means that short versions
                       of synonyms will be returned, without nach/zu
                       prefixes/suffixes.On the other hand, form=long returns
                       the full versions of synonyms including nach/zu, sich
                       prefixes/suffixes

required arguments:
  --word WORD          A word from which synonyms will be obtained

```

### Acknowledgments

* [OpenThesaurus](https://www.openthesaurus.de/) for developing a German synonym database with API from which synonyms for the German language can be obtained

### Licence

Even though this project is under MIT license, please check information about **OpenThesaurus** licensing and API limitations from the following link: [API](https://www.openthesaurus.de/about/api), in the case your software will need an exhaustive amount of synonym requests in a short period of time. 