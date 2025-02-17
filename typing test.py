import tkinter as tk
import random
import time
class TypingTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Test")
        self.master.geometry("500x400")
        self.master.resizable(True, True)
        # Define the text options
        self.text_options = [
           "Google was founded on September 4, 1998, by Larry Page and Sergey Brin while they were PhD students at Stanford University in California. Together they own about 14% of its publicly listed shares and control 56% of its stockholder voting power through super-voting stock.",
    
    "Its most common use so far is creating ChatGPT - a highly capable chatbot. To give you a little taste of its most basic ability, we asked GPT-3's chatbot to write its own description as you can see above. It’s a little bit boastful, but completely accurate and arguably very well written.",
    
    "Facebook is a social networking platform that allows users to connect with friends, family, and communities. It was founded in 2004 and has since become one of the largest social media websites in the world with over 2.8 billion monthly active users. Users can share photos, videos, updates, and messages, as well as join groups, attend events, and create pages." ,
    
"Nepal is a landlocked country located in South Asia, bordered by China and India. It is home to Mount Everest, the highest peak in the world, and is renowned for its stunning Himalayan mountain ranges and diverse cultural heritage. The Nepalese people are warm and friendly, with a rich cultural history that encompasses Hinduism and Buddhism. The country has a rich tradition of arts and crafts, including intricate wood carving, weaving, and metalwork. Despite the challenges of poverty and limited economic opportunities, Nepalese people are known for their resilience and determination. Nepal is a beautiful and fascinating country that offers a unique blend of natural beauty and cultural richness.",
    
"Programming languages are sets of instructions and syntax that allow developers to create software applications. They vary in terms of complexity, readability, and functionality, with popular examples including Java, Python, C++, and JavaScript. Choosing a programming language depends on the specific needs of a project, such as performance, readability, or compatibility with other tools. The ability to learn and use multiple programming languages is a valuable skill for software developers, allowing them to tackle different challenges and build a diverse range of applications.",
    
"Quantum Computing is a complex and rapidly developing field that aims to harness the strange behavior of matter and energy at the quantum level to perform computations. Unlike classical computers, which store information as binary digits (bits) that can be either 0 or 1, quantum computers use quantum bits (qubits) that can exist in multiple states simultaneously. This allows quantum computers to solve certain problems much faster than classical computers, making them ideal for certain applications in cryptography, optimization, and simulation. However, developing a practical and scalable quantum computer is challenging due to the delicate nature of qubits and the need for error correction and control. Despite these challenges, significant progress has been made in recent years, and quantum computing is poised to have a major impact on science and technology in the coming decades.",    
    
"Bitcoin is a decentralized digital currency that operates on a peer-to-peer network, allowing users to send and receive payments without the need for intermediaries such as banks. It was created in 2009 by an unknown person or group using the pseudonym Satoshi Nakamoto. Bitcoin transactions are recorded on a public ledger called the blockchain, which provides a secure and transparent way to track ownership and transfer of the currency. The supply of Bitcoin is limited to 21 million, which is expected to be reached around 2140. Bitcoin has been subject to significant price volatility, but has also been adopted by some businesses and individuals as a form of investment or alternative to traditional currencies. The future of Bitcoin and other cryptocurrencies remains uncertain, with some experts predicting widespread adoption and others warning of potential security and regulatory challenges.",  
    
"Drugs refer to any substance that can alter an individual's physical or mental state. They can be legal or illegal, and can be used for medical or recreational purposes. However, the misuse of drugs can have serious health and social consequences, including addiction, overdose, and increased risk of infectious diseases. Illegal drugs such as cocaine, heroin, and methamphetamine have destructive effects on individuals and communities, leading to increased crime and health problems. The use of prescription drugs, such as opioids, can also lead to abuse and addiction. It's important to be aware of the risks and dangers associated with drug use, and to seek help if you or someone you know is struggling with a substance use disorder. Governments, healthcare providers, and communities are working to reduce the harm caused by drugs through education, treatment, and law enforcement efforts.",
    
"Addaction is a UK-based charity that provides support for individuals struggling with drug and alcohol addiction. It was founded in 1971 and has since grown to become one of the largest addiction treatment organizations in the country, with a network of over 100 service centers. Addaction provides a range of services, including advice and information, detoxification and rehabilitation programs, and support for families and carers. The charity adopts a person-centered approach, working with individuals to develop a customized treatment plan that takes into account their unique needs and circumstances. Addaction also conducts research and campaigns to raise awareness of addiction and promote better understanding of the issues faced by those affected. Its work helps to improve the lives of thousands of people every year and contributes to a more equitable and supportive society."  ,
    
"लक्ष्मीप्रसाद देवकोटा एक नेपाली कवि तथा साहित्यकार थिए। उनको जन्म वि. सं. १९६६ कार्तिक २७ गते 'लक्ष्मीपुजा'को दिनमा काठमाडौँको डिल्लीबजारमा भएको थियो।[१] उनको निधन वि.सं. २०१६ भाद्र २९ मा भएको थियो। उनी नेपाली साहित्यका महाकविका रूपमा सुप्रसिद्ध छन्।[२] देवकोटा नेपाली साहित्यका कविता, आख्यान, नाटक र निबन्ध गरी साहित्यका चारवटै विधामा कलम चलाउने बहुमुखी प्रतिभाका धनी मानिन्छन्। उनले कविता र निबन्ध विधामा गरेका योगदानहरू उच्च कोटिको मानिन्छ। उनले मुनामदन, सुलोचना, शाकुन्तलजस्ता अद्वितीय कृतिहरू लेखेका छन्। विशेष गरी मुनामदन कृतिका लागि उनी सबैभन्दा प्रख्यात छन्।",   

"श्री ५ बडामहाराजाधिराज पृथ्वीनारायण शाह (वि.सं.१७७९-१८३१) शाहवंशीय राजा थिए। स-साना राज्यहरूमा बाँडिएका बाईसे तथा चौबिसे राज्यहरूलाई एकत्रित गरी एउटै देशको सृजना गर्ने यिनी आधुनिक नेपालको राष्ट्रनिर्माताको रूपमा चिनिन्छन्। उनको सम्झनामा पुष २७ गते नेपालमा राष्ट्रिय एकता दिवस मनाउने गरिन्छ। नेपालमा २००७ सम्म राणा शासन थियो भने सात सालको क्रान्ति पश्चात् नेपालमा आएको प्रजातन्त्र पश्चात् योगी नरहरीनाथले नेपालमा राष्ट्रपिता पृथ्वीनारायण शाहको जन्मोत्सव मनाउनु पर्छ भनेर प्रक्रिया सुरु गरेका थिए।",

"अभिलेखहरूमा गोपालहरू र महिषपालहरू काठमाडौं उपत्यकाको दक्षिण-पश्चिम कुनामा मातातीर्थमा राजधानी भएको प्रारम्भिक शासकहरू मानिन्छन्। सातौं वा आठौं शताब्दी ईसापूर्वदेखि किराँतीहरूले उपत्यकामा शासन गरेको भनिन्छ। तिनीहरूका प्रसिद्ध राजा यलुम्बरको पनि महाकाव्य ‘महाभारत’ मा उल्लेख छ। लगभग 300 ईस्वीमा लिच्छवीहरू उत्तरी भारतबाट आए र किराँतीहरूलाई पराजित गरे। लिच्छविहरूको विरासत मध्ये एक हो भक्तपुर नजिकै रहेको चाँगु नारायण मन्दिर, युनेस्कोको विश्व सम्पदा (संस्कृति) 5 औं शताब्दीको हो। सातौं शताब्दीको प्रारम्भमा, प्रथम ठकुरी राजा अम्शुवर्माले आफ्नो ससुरा लिच्छवीबाट राजगद्दी सम्हालेका थिए। उनले आफ्नी छोरी भृकुटीको विवाह प्रख्यात तिब्बती राजा सोङ त्सेन गाम्पोसँग गरे जसले गर्दा तिब्बतसँग राम्रो सम्बन्ध स्थापित भयो। लिच्छविहरूले उपत्यकामा कला र वास्तुकला ल्याए तर सृजनात्मकताको स्वर्ण युग १२०० ईस्वीमा मल्लहरूसँग आयो।"    

        ]
 
        # Create the GUI elements
        self.sentence_label = tk.Label(self.master,
                                       text="Type the sentence below:",
                                       font=("Helvetica", 12))
        self.sentence_text = tk.Label(self.master,
                                      text="",
                                      font=("Helvetica", 14, "bold"),
                                      fg="blue",
                                      wraplength=450)
        self.user_input_label = tk.Label(self.master,
                                         text="Your input:",
                                         font=("Helvetica", 12))
        self.user_input_text = tk.Entry(self.master,
                                        font=("Helvetica", 14),
                                        width=30)
        self.prompt_label = tk.Label(self.master,
                                     text="Click the Start button to begin the test.",
                                     font=("Helvetica", 12),
                                     fg="black")
        self.start_button = tk.Button(self.master,
                                      text="Start Test",
                                      font=("Helvetica", 12),
                                      command=self.start_test,
                                      bg="green",
                                      fg="white")
        self.submit_button = tk.Button(self.master,
                                        text="Submit",
                                        font=("Helvetica", 12),
                                        command=self.end_test,
                                        bg="blue",
                                        fg="white",
                                        state="disabled")
        # Configure the GUI elements
        self.sentence_label.pack(pady=(10,0))
        self.sentence_text.pack(pady=(0,20))
        self.user_input_label.pack()
        self.user_input_text.pack(pady=(0,20))
        self.prompt_label.pack()
        self.start_button.pack(pady=(0,10))
        self.submit_button.pack(pady=(0,10))
        
    def start_test(self):
        self.test_sentence = random.choice(self.text_options)
        self.sentence_text.configure(text=self.test_sentence)
        self.prompt_label.configure(
            text="Type the sentence as fast and as accurately as possible.",
            fg="blue")
        self.start_button.configure(state="disabled", bg="grey")
        self.submit_button.configure(state="normal")
        self.user_input_text.configure(state="normal")
        self.user_input_text.delete(0, "end")
        self.user_input_text.focus()
        self.master.bind("<Return>", self.end_test)
        self.start_time = time.time()
        
       
    def end_test(self):
        self.user_input = self.user_input_text.get()
        end_time = time.time()
        time_taken = end_time - self.start_time
        words_typed = len(self.user_input.split())
        accuracy = self.calculate_accuracy(self.user_input, self.test_sentence)
        result_text = f"You typed {words_typed} words in {time_taken:.2f} seconds.\nYour accuracy was {accuracy:.2f}%."
        self.prompt_label.configure(text=result_text, fg="green")
        self.start_button.configure(state="normal", bg="green")
        self.submit_button.configure(state="disabled")
        self.user_input_text.configure(state="disabled")
        self.master.unbind("<Return>")
        self.user_input = ""

    def calculate_accuracy(self, user_input, test_sentence):
        user_words = user_input.split()
        test_words = test_sentence.split()
        correct_words = [uw for uw, tw in zip(user_words, test_words) if uw == tw]
        accuracy = (len(correct_words) / len(test_words)) * 100
        return accuracy


root = tk.Tk()
typing_test = TypingTest(root)
root.mainloop()

