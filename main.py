import requests
from tkinter import *

root = Tk()
root.title("Парсер")
root.geometry("450x290")
root.resizable(width=False, height=False)


def clear():
    ent1.delete(0, END)


def exit():
    root.destroy()


def night():
    root['bg'] = '#049299'
    lbl1['bg'] = '#049299'
    lbl2['bg'] = '#049299'
    lbl3['bg'] = '#049299'
    rad1['bg'] = '#049299'
    rad2['bg'] = '#049299'


def light():
    root['bg'] = '#f7f7f7'
    lbl1['bg'] = '#f7f7f7'
    lbl2['bg'] = '#f7f7f7'
    lbl3['bg'] = '#f7f7f7'
    rad1['bg'] = '#f7f7f7'
    rad2['bg'] = '#f7f7f7'


def entry(token):
    r = requests.get(f'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=100', ).json()

    for coin in r['data']['cryptoCurrencyList']:
        if coin['symbol'].lower() == token.lower() or coin['name'].lower() == token.lower():
            name = coin['name']
            symbol = coin['symbol']
            price = coin['quotes'][0]['price']
            total_supply = coin['totalSupply']

            output = (
                f'Монета - {name} ({symbol})\n'
                f'Цена - {round(price, 2)} $ USD\n'
                f'Кол-во монет - {round(total_supply, 2)}\n')
            lbl1.configure(text=output)


# оглавление
lbl1 = Label(root, text='', font=('Times New Roman&', 16))
lbl1.place(x=15, y=130)
lbl2 = Label(root, text='Криптовалюта:', font=('Times New Roman&', 12))
lbl2.place(x=12, y=60)
lbl3 = Label(root, text='Парсер', font=('Times New Roman&', 16))
lbl3.place(x=180, y=20)
# Поля
ent1 = Entry(root, width=30, border=5)
ent1.place(x=130, y=60)
# Кнопки
btn1 = Button(root, width=12, height=1, text='Показать курс', border=5, command=lambda: entry(ent1.get()))
btn1.place(x=340, y=57)
btn2 = Button(root, width=10, height=1, text='Очистить', border=5, command=clear)
btn2.place(x=340, y=107)
btn3 = Button(root, width=10, height=1, text='Выход', border=5, command=exit)
btn3.place(x=340, y=157)
# radio_button
var = IntVar()
rad1 = Radiobutton(root, text='Темная тема', fg='black', variable=var, value=1, command=night)
rad1.place(x=340, y=210)
rad2 = Radiobutton(root, text='Светлая тема', fg='black', variable=var, value=2, command=light)
rad2.place(x=340, y=240)

root.mainloop()
