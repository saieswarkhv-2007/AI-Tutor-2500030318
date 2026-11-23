# word level tokenizations 
text = input("Enter a sentence:") or "i love learning genai"
print("Text:",text)
tokens=text.split()
print("Tokens:",tokens)
print("Length of tokens:",len(tokens))
