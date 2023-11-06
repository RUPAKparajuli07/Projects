import pywhatkit as pw
txt=""" Python is a high-level, interpreted programming language that is widely used for a variety of purposes, including web development, 
scientific computing, data analysis, artificial intelligence, and more. It was first released in 1991 and has since become one of the most 
popular programming languages in the world. """

pw.text_to_handwriting(txt, " handwriting.png" , [0,0,130])
print("end")
