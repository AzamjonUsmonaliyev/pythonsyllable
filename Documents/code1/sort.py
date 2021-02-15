import syllables
import eng_to_ipa as ipa
f=open("words.txt","r")
ff=open("sybl1.html","w")
ffa=open("sybl2.html","w")
ffb=open("sybl3.html","w")
ffc=open("sybl4.html","w")
ffd=open("sybl5.html","w")

for word in f:
    words=ipa.convert(word)
    sylbcount=syllables.estimate(word)
    if sylbcount==1:
        ff.write("<table><tr><td>"+word+"<br>"+"["+words+"]"+"</td></tr></table>")
    if sylbcount==2:
        ffa.write("<table><tr><td>"+word+"<br>"+"["+words+"]"+"</td></tr></table>")
    if sylbcount==3:
        ffb.write("<table><tr><td>"+word+"<br>"+"["+words+"]"+"</td></tr></table>")
    if sylbcount==4:
        ffc.write("<table><tr><td>"+word+"<br>"+"["+words+"]"+"</td></tr></table>")
    if sylbcount==5:
        ffd.write("<table><tr><td>"+word+"<br>"+"["+words+"]"+"</td></tr></table>") 
f.close()
ff.close()
ffa.close()
ffb.close()
ffc.close()
ffd.close()

