# FlashLeanrChains
Small undergraduate project for the course in Statistical Methods for Machine Learning, to practice with Hugging Face models and the LangChain library

## Brief description
The main goal of the project is to create a prompt chain that can build a deck of flashcards from a pdf file given as input.\
Specifically, the purpose is to give learning support to students in STEM (and other) courses by automating the process of creating useful tools such as flashcards.

### Used LLM
We used `google/flan-t5-base` from HuggingFace.\
T5 is an encoder-decoder model pre-trained on a multi-task mixture of unsupervised and supervised tasks and for which each task is converted into a text-to-text format. T5 works well on a variety of tasks out-of-the-box by prepending a different prefix to the input corresponding to each task, (e.g., for translation: translate English to German: …, for summarization: summarize: ….).\
Flan is a pretraining methods that is based on prompting. The Flan-T5 are T5 models trained on the Flan collection of datasets which include: taskmaster2, djaym7/wiki_dialog, deepmind/code_contests, lambada, gsm8k, aqua_rat, esnli, quasc and qed.

[![Share to Community](https://huggingface.co/datasets/huggingface/badges/raw/main/powered-by-huggingface-dark.svg)](https://huggingface.co)

## Usage guide
If you want to test the code follow the following steps:

1. Use `colab` to run the notebook  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1rdpaBsDhvR9iMWct_-7ydEIxq9ZYCQHp#scrollTo=7M3fZZVPllhv)
2. Upload a PDF file in the `content` directory in colab
3. Run all the cells in the notebook
4. Download the `flashcards.txt` file in the same `content` directory. This txt file contains a questione-asnwer pair per line

## Definition of the chain
We build three blocks for our chain:
>- **summary block** that takes as input the text chuck and writing style and then summarizes the chunk itself to meet the maximum number of tokens to be given as input to the model locally;
>- **question block** which takes as input the text summary from the previous block and returns a plausible question about it;
>- **answer block** that takes as input both the text summary and the question constructed in the previous blocks and formulates an ad hoc answer.

## Further improvements
We can define below a list of improvements to the project:

1. make a division of the text into blocks based on data mining algorithms in order to create summaries as clear and specific as possible;
2. grouping question-answer pairs into decks about the same topic using, for example, Latent Semantic Analysis or Clustering techniques;
3. use the Openai API and combine the three hand-defined blocks into a SequentialChain of langchain.
