from tkinter import Tk, Button, Label, Frame
import webbrowser


def openLink(url):
    baseURL = "https://www.epicgames.com/store/en-US/product/"
    url = baseURL + url
    # The url is then opened in the users web browser in a new tab
    webbrowser.open(url, new=2)


def openAll(game_list):
    # Calls the function to open a link but for each game in the list
    for game in game_list:
        openLink(game[1])


def createWindow(game_list):
    # Creates a window assigned to root
    root = Tk()
    root.wm_title("Free Epic Games Games List")
    # A width and height for the window
    w = 300
    h = 200
    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.wm_geometry('%dx%d+%d+%d' % (w, h, x, y))
    # A frame to group all the information into, not much is used with it however
    frame = Frame(root)
    # A text label with green text and a custom font
    title_label = Label(frame, text="Free Epic Games Games",
                        fg="green", font=("Helvetica", 18))
    title_label.pack()
    # The button at the top which when pressed will open the links for all the games
    # The function being called needs parameters passed through so a lambda is used
    allButton = Button(
        frame, text="Open all", fg="red", command=lambda: openAll(game_list), font=("Helvetica", 10))
    allButton.pack()
    # For each game in the list there is a button that will appear on the window
    # This is not a set amount each week so will be different
    for game in game_list:
        # The lambda is set different here as otherwise the url that is used when a button is pressed
        # will be the same url for each of the buttons, when really they should be
        # different, with this lambda this is done so
        gameButton = Button(
            frame, text=game[0], fg="black", command=lambda game_url=game[1]: openLink(game_url), font=("Helvetica", 10))
        gameButton.pack()
    frame.pack()
    # Packs the frame to the window and then with mainloop the window is run
    root.mainloop()


if __name__ == "__main__":
    # This list is only used as a testing phase hence being under an __name__ == __main__
    game_list = [["Watch Dogs 2", "url"], ["Hitman", "url"]]
    createWindow(game_list)
