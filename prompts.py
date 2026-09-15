import pyautogui
import time
import subprocess

one_to_print = input("which prompt u want: ")
time.sleep(5)

if one_to_print == "1":
    pyautogui.typewrite("If you're just running one: Username: sware@marsdenparkanglicancollege Password: 37hear website:https://au.ixl.com/dashboard. From this website, log in, then once logged in, click learning in the top menu. From that menu, press English, then pick a random lesson that hasn't been starred or has a medal. Make it completely random, from any letter unit, Don't just click the first one, make it entirely random. Once in the quiz, reason your way through the quiz, until the quiz is complete.")
elif one_to_print == "2": 
    pyautogui.typewrite("If you're running multiple in parallel, make sure to check which units haven't been completed and specify by typed A1 at the end:Username: sware@marsdenparkanglicancollege Password: 37hear website:https://au.ixl.com/dashboard  From this website, log in, then once logged in, click learning in the top menu. From that menu, press English, then pick the unit that will be stated later. Once in the quiz, reason your way through the quiz, until the quiz is complete. The unit is")
elif one_to_print == "3":
    pyautogui.typewrite("To clean up unfinished ones - this was more of an issue before until I optimised the prompt, since now it actually finishes most of them, but it does occasionally not finish, so sometimes it's good to run one of these while the rest of your things are running the second prompt: Username: sware@marsdenparkanglicancollege Password: 37hear website:https://au.ixl.com/dashboard. From this website, log in, then once logged in, go to recent skills, and pick one of those skills, then reason your way through the quiz, until the quiz is complete.")
while True:
    subprocess.run(["osascript", "-e", 'tell application "Terminal" to do script ""'])
