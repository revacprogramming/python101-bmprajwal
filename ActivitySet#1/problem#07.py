# Strings

text = "X-DSPAM-Confidence:    0.8475"

index = text.find('0.8475')

print(float(text[index:]))
