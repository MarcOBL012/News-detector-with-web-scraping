# News-detector-with-web-scraping

# 📰 News Detector based on Character Frequency

This project implements an automated system to identify the thematic section (**Politics, Economy, Sports**) of a digital news article. The approach is based on the **statistical analysis of the frequency of alphabetic characters** found in the texts.

## 📋 Description

The main objective is to associate a new news article with a specific category by comparing its "fingerprint" of letter frequencies against pre-established profiles.

The methodology follows these steps:
1.  **Web Scraping:** Extraction of news from portals such as *La República*, *Perú21*, *El País*, and *Clarín*.
2.  **Preprocessing:** Text cleaning (removal of special characters, normalization to uppercase).
3.  **Feature Extraction:** Counting of absolute and relative frequencies of letters (A-Z).
4.  **Classification:** Use of the **Chi-square ($\chi^2$)** statistical test to determine the similarity between the news article and the reference sections.

## 🛠️ Technologies and Libraries

The project was developed in **Python 3.12**. The main libraries used are:

* **[Newspaper3k](https://newspaper.readthedocs.io/):** For extracting and parsing web articles.
* **[Pandas](https://pandas.pydata.org/):** For data manipulation and DataFrame management.
* **[Matplotlib](https://matplotlib.org/):** For visualizing comparative histograms.
* **[SciPy](https://scipy.org/):** For statistical calculation (Chi-square).
* **Numpy:** For numerical calculations.

## 📦 Installation

To run this project, you need to install the dependencies. You can do this by executing:

```bash
pip install newspaper3k pandas matplotlib scipy numpy
```
## 🚀 Usage

1. **News Extraction**
To collect new news articles from the configured sources:

```Bash

python Noticias22.py
```
2. **Reference Visualization**
To view how letters are distributed across the base sections:

```Bash

python hist.py

```
3. **Classification and Comparison**
To execute the classification algorithm and view comparative charts between a news article and the sections:
```Bash
python barras1.py
```
## 📬 Contact
If you use or extend this project, please add a note in the README or contact:

Marco Obispo — marco.obispo.l@uni.pe
