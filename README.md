## Python wrapper for obtaining synonyms in German language from openthesaurus.de

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2a302faa81aa41ed8647d917c268f5cd)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Aid91/py_openthesaurus&amp;utm_campaign=Badge_Grade)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

When working in Natural Language Processing (NLP) area, synonyms can be an important part of data augmentation process. The task of obtaining synonyms for German language is currently limited, since there are no easily accessible German lexical databases. Compared to WordNet
lexical database for English which is available as an **nltk** package,  [GermaNet](http://www.sfs.uni-tuebingen.de/GermaNet/) represents only one German lexical database alternative. However, to use **GermaNet** for further research purposes, it is necessary to 
manually obtain the licence. 

This repository represents a Python wrapper implementation for obtaining synonyms in faster and easier way, using the German synonym database and API from [OpenThesaurus](www.penthesaurus.de).

### Installation

Library can be installed from PyPI:

```pip install py_openthesaurus```

### Usage

As an Python library:

As an command line tool:

### Acknowledgments
Thanks to:

* [OpenThesaurus](www.penthesaurus.de) for developing a German synonym database with API from which synonyms for the German language can be obtained