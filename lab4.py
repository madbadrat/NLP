# находится, оказался
from transformers import BertTokenizer, BertForMaskedLM
from torch.nn import functional as F
import torch

name = "bert-base-multilingual-uncased"
tokenizer = BertTokenizer.from_pretrained(name)
model = BertForMaskedLM.from_pretrained(name, return_dict=True)

text = "Я " + tokenizer.mask_token + " в центре событий."
input = tokenizer.encode_plus(text, return_tensors="pt")
mask_index = torch.where(input["input_ids"][0] == tokenizer.mask_token_id)
output = model(**input)

logits = output.logits
softmax = F.softmax(logits, dim=-1)
mask_word = softmax[0, mask_index[0], :]
top = torch.topk(mask_word, 10)
for token in top[-1][0].data:
    print(tokenizer.decode([token]))
