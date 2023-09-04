import os
import time
import webbrowser
import keyboard
import requests

while True:
    time.sleep(0.5)
    command = input("\nccmd >")
#############################################################
    if command == "help+":
        print('''\nhere all the custom commands:
        
-"help+" to see al the command of cmdL+
        
-"///update" to update / look for a update of cmdL+

-"link" will ask you after for a url and then place it to open it on your web browser (add "www." of the start to open on the main one)

-"///cmdL+" version info

-"-b.sama" will download a pic of b sama''')

    elif command == "///update":
        os.system("cls")

        print("do you want to install the new update of cmdL+ ? [enter]")

        keyboard.wait("enter")

        os.system("cls")

        print("""

        wait please...
        ------------------------------

        |🟪                    |15%
        """)

        time.sleep(2)
        os.system("cls")

        print("""

        wait please...
        ------------------------------

        |🟪🟪                  |25%
        """)

        time.sleep(1)
        os.system("cls")

        print("""

        wait please...
        ------------------------------

        |🟪🟪🟪               |40%
        """)
        time.sleep(0.3)
        os.system("cls")

        print("""

        wait please...
        ------------------------------

        |🟪🟪🟪🟪             |45%
        """)
        time.sleep(0.3)
        os.system("cls")

        print("""

        wait please...
        ------------------------------

        |🟪🟪🟪🟪🟪           |50%
        """)
        time.sleep(0.3)
        os.system("cls")

        print("""

        wait please...
        ------------------------------

        |🟪🟪🟪🟪🟪🟪         |60%
        """)
        time.sleep(2)
        os.system("cls")

        print("""

        wait please...
        ------------------------------

        |🟪🟪🟪🟪🟪🟪🟪       |70%
        """)
        time.sleep(1)
        os.system("cls")

        print("""

        wait please...
        ------------------------------

        |🟪🟪🟪🟪🟪🟪🟪🟪     |80%
        """)
        time.sleep(5)
        os.system("cls")

        print("""

        wait please...
        ------------------------------

        |🟪🟪🟪🟪🟪🟪🟪🟪🟪   |90%
        """)
        time.sleep(2)
        os.system("cls")

        print("""

        wait please...
        ------------------------------

        |🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪 |95%
        """)
        time.sleep(2)
        os.system("cls")

        print("""cmdL+ has been succefully installed !

        """)

    elif command == "link":
        url = input("url :")
        webbrowser.open(url)

    elif command == "///cmdL+":
        print("")
        print("version of cmdL+ : ")
        print("-windows cmdL+ custom B_0.0.1")
        print("-discord: https://discord.gg/GjeAjGxsfP")

    elif command == "-b.sama":

        # GitHub repository information
        repository_url = 'https://github.com/LascAAr/test_______wawaa'
        branch = 'main'  # Replace with the branch name
        file_path = '''Capture d'écran 2023-05-30 194302.png'''  # Replace with the file path in the repository

        # Construct the URL for the raw file
        raw_url = f'{repository_url}/raw/{branch}/{file_path}'

        # Send a GET request to the raw URL
        response = requests.get(raw_url)

        if response.status_code == 200:
            # Save the file to your local system
            with open('''Capture d'écran 2023-05-30 194302.png''', 'wb') as file:
                file.write(response.content)
            print(f'bb sama has been succefully downloaded.')
        else:
            print(f'Failed to download file. HTTP status code: {response.status_code}')


#############################################################
    else:
        os.system(command)