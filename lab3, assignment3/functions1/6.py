def reverse(text):
    txt_elements=text.split()
    index=-1
    reverse=[]
    i=0
    while i < len(txt_elements):
        reverse.append(txt_elements[index])
        index=index-1
        i+=1
    final=' '.join(reverse)
    return final

sent = input()
print(reverse(sent))