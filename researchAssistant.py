sessionId = 1
tasktype = ""
start = ""
end = ""
duration = 0
reflection = ""
takeaways = ""
notes = ""
cont = ""

while True:
    sessionId = sessionId + 1

    tasktype = input("What task did you work on? ")
    start = input("What time did you begin? ")
    end = input("What time did you finish? ")
    duration = int(input("How many minutes did you spend on this task? "))
    reflection = input("Reflect on what you learned. Write it down here. ")
    takeaways = input("What is the biggest takeaway from this? Try to keep this to less than 3 sentences. ")
    notes = input("Include notes here: ")

    cont = input("Would you like to do another session? y/n ")


    if cont == "n":
        break
    else:
        print("Starting session", sessionId, "now.")
print("You have completed", sessionId - 1, "session(s).")