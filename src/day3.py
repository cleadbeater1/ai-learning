hours = float(input("How many hours did you study?: "))

if hours >= 2:
    print("Excellent")
elif 1 <= hours < 2:
    print("Good")
elif 0 <= hours < 1:
    print("Needs Improvement")
elif hours < 0: 
    print("Invlaid input")

#Why does an AI system need:
# 1) inputs - to know what to process and use to make decisions 
# 2) Stored Values - to compare the inputs against the expectated solution to a decision
# 3) Conditional Logic - the engine of the AI system that compares the inputes to the stored values and makes a decision. 

