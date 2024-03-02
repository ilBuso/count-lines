<div align="center">

# Project Stats
##### A quick way to know your project stats
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

</div>

## ⇁ TOC

* [About](#about)
* [Installation](#installation)
* [Usage](#usage)
* [Future Implementations](#future-implementations)
* [License](#license)

## ⇁ About
Project Stats is a simple Python script to count the lines of code in a directory. It's useful for getting a quick overview of your project's size. The script recursively goes through all files in the specified directory and counts non-empty lines of code.

## ⇁ Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/ilBuso/project-stats.git
    ```

2. Change into the `project-stats` directory:
    ```sh
    cd project-stats
    ```

3. Run the script:
    ```sh
    python project-stats.py
    ```

## ⇁ Usage
When you run the script, it will prompt you to enter the path to the directory you want to analyze. It will then display the total lines of code in that directory.

```sh
python project-stats.py
Enter the path to the directory: /path/to/your/directory
```

## ⇁ Future Implementations
This project is open for further development. Here are some ideas for future implementations:
- [ ] Display breakdown of file types (e.g. C, C++, h, Makefile)
- [ ] Implement a feature to ignore certain file types or directories
- [ ] Provide an option to save results to a file

## ⇁ Licence
Distributed under the MIT License. See LICENSE for more information.
