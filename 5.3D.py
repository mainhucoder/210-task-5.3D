import tkinter as tk
import RPi.GPIO as GPIO
import time

# Configure GPIO
GPIO.setmode(GPIO.BCM)  # Set GPIO numbering mode to BCM
LED_PIN = 10  # Enter the GPIO pin you are using for the LED
GPIO.setup(LED_PIN, GPIO.OUT) # Configure the LED pin as an output
GPIO.output(LED_PIN, GPIO.LOW)  # Initially turn off the LED

# Morse Code Dictionary
morse_alphabets = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

# Function to convert user input to Morse code
def input_into_alphabets(input_text):
    morse = ''
    for char in input_text.upper():
        if char in morse_alphabets:
            morse += morse_alphabets[char] + ' '
        else:
            morse += char + ' '  
    return morse

# Function to blink a dot
def blink_dot():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.4)  # Duration of a dot
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.4)  # Duration between dots and dashes

# Function to blink a dash
def blink_dash():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.7)  # Adjust the duration of a dash
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.4)  # Adjust the duration between dots and dashes

# Function to blink Morse code based on input
def blink_morse_code(message):
    for char in message:
        if char == '.':
            blink_dot()
        elif char == '-':
            blink_dash()
        elif char == ' ':
            time.sleep(1)  # Duration between words

# Function to translate user input and blink Morse code
def morse_translation():
    input_text = entry.get()  # Get user input from the text entry field
    morse_message = input_into_alphabets(input_text)  # Translate the input to Morse code
    blink_morse_code(morse_message)  # Blink the Morse code pattern

# Create the GUI window
uday_screen = tk.Tk()
uday_screen.title("||210 TASK 5.3D||")
uday_screen.geometry('700x500')

# Label for user input
label = tk.Label(uday_screen, text="Please enter a name:")
label.pack(padx=20, pady=10)

# Entry field for user input
entry = tk.Entry(uday_screen)
entry.pack(padx=20, pady=5)

# Button to convert and blink Morse code
convert_button = tk.Radiobutton(uday_screen, text="Convert and Blink the Morse Code", command=morse_translation)
convert_button.pack(pady=10)

# Start the GUI main loop
uday_screen.mainloop()

# Cleanup GPIO
GPIO.cleanup()
