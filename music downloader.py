import requests
from mutagen.mp3 import MP3
from tqdm import tqdm
from tkinter import *
from tkinter import filedialog

# Define the download function
def download_music():
    try:
        # Get the URL from the text box
        url = url_textbox.get()

        # Send a request to the server to get the file size
        response = requests.head(url)
        file_size = int(response.headers.get("Content-Length", 0))

        # Ask the user to select a file name and location
        filename = filedialog.asksaveasfilename(defaultextension=".mp3")

        if filename:
            # Start downloading the file and display a progress bar
            with requests.get(url, stream=True) as request:
                with open(filename, "wb") as file:
                    with tqdm(total=file_size, unit="B", unit_scale=True, desc=filename, initial=0, miniters=1) as progress_bar:
                        for chunk in request.iter_content(chunk_size=1024):
                            if chunk:
                                file.write(chunk)
                                progress_bar.update(len(chunk))

            # Print the music details and file path
            metadata = MP3(filename).info
            details_textbox.config(state="normal")
            details_textbox.delete("1.0", END)
            details_textbox.insert(END, f"Music downloaded successfully!\nTitle: {metadata.title}\nArtist: {metadata.artist}\nAlbum: {metadata.album}\nDuration: {metadata.length/60:.2f} minutes\nFile saved to: {filename}")
            details_textbox.config(state="disabled")

            # Show a message on the output screen
            message_label.config(text="Music downloaded successfully!")

        else:
            # Show an error message if the user cancels the file dialog
            message_label.config(text="Download cancelled.")

    except requests.exceptions.RequestException as e:
        details_textbox.config(state="normal")
        details_textbox.delete("1.0", END)
        details_textbox.insert(END, f"Error downloading file: {e}")
        details_textbox.config(state="disabled")

# Create a GUI window for the music downloader
root = Tk()
root.geometry("500x250")
root.title("Music Downloader")

# Create a label and text box for the URL
url_label = Label(root, text="Enter URL:")
url_label.pack()
url_textbox = Entry(root)
url_textbox.pack()

# Create a button to trigger the download
download_button = Button(root, text="Download", command=download_music)
download_button.pack(pady=20)

# Create a label to show the download message
message_label = Label(root, text="")
message_label.pack()

# Create a text box to display the download details
details_textbox = Text(root, height=5, width=50, state="disabled")
details_textbox.pack()

# Start the GUI main loop
root.mainloop()
