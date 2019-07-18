def remove_tags(string):
    i=0
    j=0
    L=[]
    H=[]
    
    if "<" not in string or ">" not in string:
        return string.split()

    while i<len(string) and i!=(-1):
        L.append(string.find("<",i))
        i=string.find("<",string.find("<",i)+1)

    while j<len(string) and j!=(-1):
        H.append(string.find(">",j))
        j=string.find(">",string.find(">",j)+1)
    
    string_new=string[:L[0]]
    k=0
    while k<(len(L)-1):
        string_new=string_new+" "+string[H[k]+1:L[k+1]]
        k=k+1
    
    string_new=string_new+" "+string[H[-1]+1:]
    
    return string_new.split()


print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')

print remove_tags("<hello><goodbye>")

print remove_tags("This is plain text.")
