import markovify
# Get raw text as string.
with open("alice.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())
    print ('Sentence end')
# Print three randomly-generated sentences of no more than 140 characters
