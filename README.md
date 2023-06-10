# FlashLeanrChains
Small undergraduate project for the course in Statistical Methods for Machine Learning, to practice with Hugging Face models and the LangChain library

## Brief description
The main goal of the project is to create a prompt chain that can build a deck of flashcards from a pdf file given as input.\
Specifically, the purpose is to give learning support to students in STEM (and other) courses by automating the process of creating useful tools such as flashcards.

## Usage guide
If you want to test the code follow the following steps:

1. Use `colab` to run the notebook  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1rdpaBsDhvR9iMWct_-7ydEIxq9ZYCQHp#scrollTo=7M3fZZVPllhv)
2. Upload a PDF file in the `content` directory in colab
3. 
4. Run all the cells in the notebook
5. Download the `flashcards.txt` file in the same `content` directory. This txt file contains a questione-asnwer pair per line


## Further improvements
We can define below a list of improvements to the project:

1. make a division of the text into blocks based on data mining algorithms in order to create summaries as clear and specific as possible;
2. grouping question-answer pairs into decks about the same topic using, for example, Latent Semantic Analysis or Clustering techniques;
3. use the Openai API and combine the three hand-defined blocks into a SequentialChain of langchain.
