from langchain.prompts import ChatPromptTemplate
from langchain import LLMChain
# from langchain.chains import SequentialChain
from tqdm.auto import tqdm


def my_chain(text, llm):

  # define the correct style the AI should assume for our task
  style = """American English \
  you are a very helpful assistant and help a professor of statistics and machine learning in creating material to help pupils in learning
  """

  # define the chain for the summary of our text
  summary_template = """Summarize the following text using this style: {style}\
  Text: {text}"""

  summary_prompt = ChatPromptTemplate.from_template(summary_template)

  summary_chain = LLMChain(prompt=summary_prompt,
              llm=llm,
              output_key="summary"
              )

  summary = summary_chain.run({"text": text, "style": style})

  # define the chain to formulate the question form the previous summary
  question_template = """From the the text formulate a proper question using this style: {style}\
  Text: {summary}"""

  question_prompt = ChatPromptTemplate.from_template(question_template)

  question_chain = LLMChain(prompt=question_prompt,
                      llm=llm, 
                      output_key="question"
                      )
  question = question_chain.run({"summary": summary, "style": style})

  # define the chain for aswering the above question given the summary from the first block
  answer_template = """Try to asnwer this question using the information provided in the following text\
  Text: {summary}\
  Question: {question}"""

  answer_prompt = ChatPromptTemplate.from_template(answer_template)

  answer_chain = LLMChain(prompt=answer_prompt,
                      llm=llm, 
                      output_key="answer"
                      )
  answer = answer_chain.run({"question": question, "summary": summary, "style": style})

  return (question, answer)


# divide text into smaller chunks:
def divide_text(text, section_size):
    sections = []
    start = 0
    end = section_size
    while start < len(text):
        section = text[start:end]
        sections.append(section)
        start = end
        end += section_size
    return sections

# build the flash cards
def build_flashcards(pdf_text,llm):

    SECTION_SIZE = 4000
    divided_sections = divide_text(pdf_text, SECTION_SIZE)
    generated_flashcards = []
    for i, text in tqdm(enumerate(divided_sections)):
    
        QA_pair = my_chain(text)
        generated_flashcards.append(" -> ".join(QA_pair))

    # # Save the cards to a text file
    with open("flashcards.txt", "w") as f:
        f.write("\n".join(generated_flashcards))