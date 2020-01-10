from time import process_time
from playsound import playsound

print("Hello, Welcome to alarm clock.\n")
user_input = float(input("Enter the time at which you want the alarm to go off: "))
process_time()  # initiates the processing time from the instance the user gives input

while True:
    if user_input == process_time():
        print(
            process_time()
        )  # Verifying whether the process is in fact running when the user wanted it to

        # Playing the alarm/song: Enter the location of the song/alarm you want to play
        # press ctrl-c to exit from terminal while the song is playing
        # else wait for it to complete
        playsound(
            r"C:\Users\ashwi\Desktop\Python 3\Projects\For_What_It_s_Worth_Liam_Gallagher.mp3"
        )

        # Knowing the current process time after the alarm switches off
        print(process_time())
        break
