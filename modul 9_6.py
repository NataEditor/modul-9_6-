
def all_variants(text):
    pod_str=[]
    for i in range(len(text)):
        pod_str.append(text[i])
    n=0
    j=2
    while n < len(text)-1:
        pod_str.append(text[n:j])
        n+=1
        if j<len(text):
            j+=1
        else:
            pod_str.append(text[0:len(text)])
    
    yield ('\n'.join(pod_str))

    


a = all_variants("abc")
for i in a:
    print(i)
    
