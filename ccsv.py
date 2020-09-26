import PySimpleGUI as sg
from tkinter.filedialog import askopenfilenames
import pandas as pd
from pathlib import Path


def ccsv():

    sg.theme('DarkPurple7')

    window = sg.FlexForm('Concatenate CSV Files', auto_size_text=True, font=("Ubuntu Mono derivative Powerline", 14))

    layout = [[sg.T("Select Multiple 'CSV' Files:"),
               sg.B("Browse", size=(15, 0))],
              [sg.T('Output File Name:'),
               sg.I(size=(25, 0), key='input')], [sg.B("Concatenate")]]

    window = window.Layout(layout)

    while True:
        event, values = window.read()

        if event == "Browse":
            files = list(askopenfilenames(title="Open '.csv' Files"))
            if any(".csv" not in x for x in files):
                sg.Popup('You can only select CSV files!')

        elif event == "Concatenate":
            try:
                files
            except NameError:
                sg.Popup('You Haven Not Selected Any File to Concatenate!')
            else:
                combined_csv = pd.concat([pd.read_csv(f) for f in files])
                combined_csv.to_csv(f'{Path(files[0]).parent}/{values["input"]}.csv',
                                    index=False,
                                    encoding='utf-8-sig')
                sg.Popup('Done!')

        elif event == sg.WIN_CLOSED:
            break


if __name__ == "__main__":
    ccsv()
else:
    window.close()
