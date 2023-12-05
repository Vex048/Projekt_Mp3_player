import tkinter as tk
import buttons

root=tk.Tk()
root.title('MP3_Player')
Pause_button = tk.Button(root, text='Pause', width=15, command=root.destroy)
Stop_button = tk.Button(root, text='Stop', width=15, command=root.destroy)
Next_button = tk.Button(root, text='Next', width=15, command=root.destroy)
buttons.pauseButton.button=Pause_button

stopButton=buttons.stopButton()
pauseButton=buttons.pauseButton()
nextButton=buttons.nextButton()

stopButton.button=Stop_button
pauseButton.button=Pause_button
nextButton.button=Next_button

stopButton.button.pack()
pauseButton.button.pack()
nextButton.button.pack()
root.mainloop()