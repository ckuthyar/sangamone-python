import statistics as st
def stats(sample):
    v1=st.mean(sample)
    v2=st.median(sample)
    v3=st.mode(sample)
    return(v1,v2,v3)
result=stats([90,95,98,100])
print(result)


