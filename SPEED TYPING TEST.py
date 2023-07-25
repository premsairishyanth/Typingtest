import time
print("Welcome to the speed typing test.")
input("Press 'ENTER' to generate the sentence")
sentence='The quick brown fox jumps over the lazy dog'
print(sentence)
input("press 'ENTER' when you are ready to type")
start_time = time.time()
text=input("start typing here :- ")
end_time = time.time()
time_taken = end_time - start_time
words=len(text.split())
speed= (words/time_taken)*60
print("Time taken:-",time_taken,"Seconds")
print("Typing speed",speed,"Words per minute")


