
# INPI-MDP_Scrapper

<img src="https://github.com/user-attachments/assets/448a9786-8e03-4932-ab5f-754b64fe0588" width="700">

**INPI-MDP_Scrapper** is a desktop application developed in Python that allows users to search for specific terms in recent publications from the **Brazilian National Institute of Industrial Property (INPI)**.

The application uses **Selenium in headless mode** to automatically access and download PDFs from the following publication categories:

* **Industrial Designs**
* **Trademarks**
* **Patents**

After downloading the documents, the application automatically organizes them into a folder created on the user's desktop. It then scans the documents and identifies the pages where the searched term appears.

PDFs in which the term is not found are automatically deleted, leaving only the documents relevant to the search.

## Objective

The project was developed as an automation tool to simplify the process of monitoring new INPI publications, reducing the need to manually search through lengthy documents for specific terms.

## Technologies Used

* **Python**
* **PyQt5** — graphical user interface
* **Selenium** — browser automation and document downloads
* **pypdf** — PDF text extraction and search

## How It Works

In simplified terms, the application follows this workflow:

1. Accesses the INPI publication portal.
2. Identifies the most recent publication.
3. Downloads the Industrial Designs, Trademarks, and Patents PDFs.
4. Organizes the files into a dedicated folder on the user's desktop.
5. Searches each document for the term provided by the user.
6. Displays the pages where the term was found.
7. Deletes PDFs in which no occurrences were identified.

## Notes

This project is still in an early stage and may contain bugs or unexpected behavior.

The main areas that currently require improvement are **error handling and automation stability**, particularly in situations such as:

* INPI website unavailability or instability;
* Download failures or interruptions;
* Changes to the website's structure;
* Unavailable or corrupted PDFs;
* Changes to the format or content of publications;
* Files that already exist in the destination directory.

