# FlashLearnChain
Small undergraduate project for the course in **Statistical Methods for Machine Learning**, to practice with **Hugging Face** models and the **LangChain** library

## Brief description
<img width=200 src="https://github.com/Engrima18/FlashLearnChain/assets/93355495/863aaf30-a38f-4eaf-b925-eb49f1b6b806" width=10% height=10% align="left">

The main goal of the project is to create a prompt chain that can build a deck of flashcards from a pdf file given as input.\
Specifically, the purpose is to give learning support to students in STEM (and other) courses by automating the process of creating useful tools such as flashcards.

<br/>
<br/>

## Used LLM
We used `google/flan-t5-base` from HuggingFace.\
T5 is an encoder-decoder model pre-trained on a multi-task mixture of unsupervised and supervised tasks and for which each task is converted into a text-to-text format. T5 works well on a variety of tasks out-of-the-box by prepending a different prefix to the input corresponding to each task, (e.g., for translation: translate English to German: …, for summarization: summarize: ….).\
Flan is a pretraining methods that is based on prompting. The Flan-T5 are T5 models trained on the Flan collection of datasets which include: `taskmaster2`, `djaym7/wiki_dialog`, `deepmind/code_contests`, `lambada, gsm8k`, `aqua_rat`, `esnli`, `quasc` and `qed`.

[![Share to Community](https://huggingface.co/datasets/huggingface/badges/raw/main/powered-by-huggingface-dark.svg)](https://huggingface.co/google/flan-t5-large)

## Usage guide
If you want to test the code follow the following steps:

1. Use `colab` to run the notebook  <a target="_blank" href="https://colab.research.google.com/github/Engrima18/FlashLearnChain/blob/main/FlashLearn.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
2. Upload a PDF file in the `content` directory in colab
> <img width="262" alt="guide_image" src="https://github.com/Engrima18/FlashLeanrChain/assets/93355495/bfff446e-715f-43cb-941a-8ee175781c96">

3. Run all the cells in the notebook
4. Download the `flashcards.txt` file in the same `content` directory. This txt file contains one questione-asnwer pair per line.

## Definition of the chain
We build three blocks for our chain:
>- _summary block_ that takes as input the text chuck and writing style and then summarizes the chunk itself to meet the maximum number of tokens to be given as input to the model locally;
>- _question block_ which takes as input the text summary from the previous block and returns a plausible question about it;
>- _answer block_ that takes as input both the text summary and the question constructed in the previous blocks and formulates an ad hoc answer.

## Further improvements
We can define below a list of improvements to the project:

1. make a division of the text into blocks based on data mining algorithms in order to create summaries as clear and specific as possible;
2. grouping question-answer pairs into decks about the same topic using, for example, Latent Semantic Analysis or Clustering techniques;
3. use the Openai API and combine the three hand-defined blocks into a SequentialChain of langchain.

## Disclaimer

Our chain was defined on the basis of a free, open, runnable LLM without GPU, but that does not guarantee high quality of results.
In fact, the real power of langchain can really be harnessed in combination with the Openai model and API.
