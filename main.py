from langchain.llms import HuggingFacePipeline
import torch
from transformers import AutoTokenizer, pipeline, AutoModelForSeq2SeqLM
from pdfminer.high_level import extract_text
from glob import glob
from functions import build_flashcards

model_id = 'google/flan-t5-base'
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id) # , load_in_8bit=True not working

pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=300
)

local_llm = HuggingFacePipeline(pipeline=pipe)


# script execution
if __name__ == "__main__":

    # find the path of the PDF file 
    pdf_file = glob("/content/**/*.pdf", recursive=True)
    # extrect text from the file at the path 
    pdf_text = extract_text(pdf_file[0])

    build_flashcards(pdf_text, local_llm)

