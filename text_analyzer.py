import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox

# Stoppwörter definieren
stoppwoerter = ["der", "die", "das", "und", "ist", "ein", "eine", "zu", "im", "in", "wie", "auf", "an", "du", "bist"]

def analyze_text(file_path):
    try:
        # Datei einlesen
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Text in Wörter aufteilen und Stoppwörter filtern
        words = [word for word in text.split() if word.lower() not in stoppwoerter]
        
        # Häufigkeit der Wörter berechnen
        word_count = pd.Series(words).value_counts()

        # Top 10 häufigste Wörter anzeigen
        result_text.set("Top 10 häufigste Wörter:\n" + str(word_count.head(10)))

        # Wortwolke erstellen
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(words))

        # Wortwolke anzeigen
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title("Wortwolke ohne Stoppwörter")
        plt.show()
    except Exception as e:
        messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten:\n{e}")

def open_file():
    file_path = filedialog.askopenfilename(title="Textdatei auswählen", filetypes=[("Text files", "*.txt")])
    if file_path:
        analyze_text(file_path)

# GUI erstellen
root = tk.Tk()
root.title("Text Analyzer")

# Ergebnis-Label
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", padx=10, pady=10)
result_label.pack()

# Datei auswählen Button
select_button = tk.Button(root, text="Textdatei auswählen", command=open_file, padx=10, pady=5)
select_button.pack()

# Programm starten
root.mainloop()
