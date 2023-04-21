# About 👨‍💻
***This repository is about my Python learning and projects I have created***

______________________

## Things I have added here so far 💻
- ### [Flight Club and Flight Deal Finder (Day 39 and 40)](https://replit.com/@damsithbrosl/Flight-Club?v=1)
   - In this completed version, users can enter their details in a replit and the program updates the details into a google sheet

   - Summary - The program checks for flights (In the period of tomorrow to next 6 months) to specific locations in a google sheet,
                                        if the actual price of a flight is cheaper than the price in google sheet then
                                         send a email with relevent information to the emails that are in a google sheet
   - Note - The departure location of the flights is, Colombo (IATA Code - CMB) and the default value for maximum stop-overs is 1
   
- ### Workout Tracker with Google Sheets 💪 (Day 38)
   - In this program, user can input the exercises they did along with durations
     and then those data is sent to a API through POST method, the API returns some data (eg - How much calories spent).
     After that, the program asks the user the date and time they did those exercises
     Finally, the program updates a google sheet via another API with the following data:
                 1. Date
                 2. Time
                 3. Exercise (eg :- Push-up)
                 4. Duration
                 5. Calories
   - Note - Don't assume the calory count to be 100% accurate because defining the calory count may differ from person to person

- ### [Habit Tracker](https://pixe.la/v1/users/damsithbrosl/graphs/graph1.html) 🧘 (Day 37)
   - Via this program, I'm going to update my meditation time periods
     You can see those in https://pixe.la/v1/users/damsithbrosl/graphs/graph1.html

- ### Stock Trading Alert Program 📈 (Day 36)
   - Summary - The program checks the percentage between yesterday's closing value and day before yesterday's closing value of TSLA (Tesla Inc) company.
          If the percantage is greater than 5% or if it is smaller than -5%, program gets data from news API.
          And then it sends the top 3 news pieces to the desired email via smtplib
   - Problems - The stock updates seem to be quite late. And I assume they are updated in evening (I'm in Colombo Time Zone)

- ### Rain Alert Program ☔ (Day 35)
   - Summary - In this program, it checks if it will rain in next 12 hours via openweathermap API
          and if it predicts that it will rain in next 12 hours an e-mail is sent saying 'Bring An Umbrella'

- ### Quizzler App ⁉️ (Day 34)
   - This is a upgraded version of day 17 quiz game
   - Uses a GUI instead of text inputs
   - Uses questions from random topics via Trivia API

- ### Day 33 (Learn about API and create a **ISS Overhead Notifier** and a **Kanye Quote Program**)
  - In this program, an e-mail is sent if the International Space Station near me and if it is currently dark
  - In this commit, I created two functions 'is_iss_above_me()' and 'it_is_dark_now()', so that the code is more readable and easy to understand
  - Note: I think there is a minor problem with the sunrise-sunset API used in this program


- ### Day 32 📧 (Learn e-mail sending with **Smtplib** and do monday-motivation sender and *automated-birthday-wisher*)

- ### Flash Card App 📑 (Day 31)
  - This is a simple flash card app that allows the user to test their French words memory. The user can interact with the program using the buttons.
  - In this program the user can select whether they already know the current word or not by simply clicking the right button or the wrong button.
  - If the user clicks the right button, the row containing that word and it's translation will be deleted from the words_to_learn.csv.
  - So after that the program would only show the words in words_to_learn.csv and it wouldn't show the words that the user already knows.
  - If the user runs the program for the first time or the words_to_learn.csv file is deleted, the program would consider all the words are unknown.

- ### Day 30 work (in **features** branch) (Add json and search feature in password manager)
- ### Password Manager GUI 🔑 (Day 29)
- ### Pomodora Timer⏰ (Day 28)
- ### Day 27 work (Tkinter, optional arguments, *args, **kwargs)
- ### Day 26 work (List, dict comprehension and the **NATO phonetic alphabet challenge**)
- ### Day 25 work (Reading CSV, Pandas and the US states game)
- ### Mail Merge Challenge ✉(Day 24) ***~~BTW There is a small typo in the commit b7f9b53507e4c2a2f774372bacd9fbea67d83c92~~***
- ### Turtle Crossing 🚸 (Day 23)
- ### The Pong Game 🕹️ (Day 22)
- ### The Snake Game 🐍 (Day 20 and 21)
- ### Day 19 work (Including turtle race)
- ### Day 18 work (Including hirst challenge)
- ### Day 17 work (Quiz Game)
- ### Day 16 work 
- ### Coffee Machine ☕
- ### Higherlower Game
- ### Blackjack Game 🃏

______

## Pictures of my projects 🖼️


- Day 39 and 40

![image](https://user-images.githubusercontent.com/113516635/233313934-d2fed658-267e-42e3-a590-abc5be28190c.png)
![image](https://user-images.githubusercontent.com/113516635/233312932-2d31cf01-fa7f-4e6d-8dc8-6c00f7521ef1.png)
![image](https://user-images.githubusercontent.com/113516635/233313423-8460e0dd-2235-424f-bdd6-461be63a76e9.png)
![image](https://user-images.githubusercontent.com/113516635/233313545-04a4b544-2035-495c-a1b0-cbe707c4fe28.png)



- Day 38

![image](https://user-images.githubusercontent.com/113516635/230778117-21d0a18f-5274-407b-8258-a2bdc0c17939.png)
![image](https://user-images.githubusercontent.com/113516635/230778119-5e92a879-1a7c-4dd8-8437-a2216702b90a.png)


- Day 37

![image](https://user-images.githubusercontent.com/113516635/230722417-9bc51e7d-1d92-4da9-beb4-22052ee82231.png)



- Day 35

![image](https://user-images.githubusercontent.com/113516635/230299535-f6e68580-8f62-4879-bd45-753151441640.png)



- Day 34

![image](https://user-images.githubusercontent.com/113516635/229693687-3cd4d556-a115-48e3-90cd-14bb65207673.png)



- Day 33

![image](https://user-images.githubusercontent.com/113516635/229336765-63d34578-1601-4409-9b36-4e8285b8b976.png)



- Day 32

![image](https://user-images.githubusercontent.com/113516635/229268878-22b71095-3557-40d7-bdca-9a83781cc2b7.png)



- Day 31

![image](https://user-images.githubusercontent.com/113516635/228523604-13a356af-5ee5-4bba-b370-cd982ebf9fc6.png)



- Day 30 (in **features** branch)

![image](https://user-images.githubusercontent.com/113516635/227779088-e541c17b-c800-4fe9-84a3-d54eae5baae7.png)



- Day 29

![image](https://user-images.githubusercontent.com/113516635/227715023-af6f4d0e-6aa2-4034-83ab-fe75c0a55746.png)



- Day 28

![image](https://user-images.githubusercontent.com/113516635/227702427-202d080b-d521-4de8-8821-9df405684534.png)



- Day 27

![image](https://user-images.githubusercontent.com/113516635/226864274-bc39530d-5a41-4f7a-be8a-857630718af5.png)



- Day 25

![image](https://user-images.githubusercontent.com/113516635/225914547-cf4d9ba1-d45b-461f-9520-fdbb80294c87.png)



- Day 23

![image](https://user-images.githubusercontent.com/113516635/223456016-47040ef5-7275-449b-851f-0fe5963c75fc.png)


- Day 22

![image](https://user-images.githubusercontent.com/113516635/218700102-67c896ea-4eac-40f1-8818-10d24da960e6.png)


- Day 20 and 21

![image](https://user-images.githubusercontent.com/113516635/218411318-1942455d-c36d-44aa-8394-8a77f9077bf3.png)


- Day 19

![image](https://user-images.githubusercontent.com/113516635/218295623-cb4ce6bd-b119-431e-8142-5b1154101d34.png)


- Day 18

![image](https://user-images.githubusercontent.com/113516635/218295586-0e7c7ce8-def5-4142-80bd-c5ed016886a5.png)


- Day 17

![image](https://user-images.githubusercontent.com/113516635/218295449-f0d7269e-8155-4382-af44-e097b9c81c20.png)


- Day 16

 ![image](https://user-images.githubusercontent.com/113516635/218295416-24a63ac4-0568-46b3-9a00-b289375092af.png)
