import flet as ft
import random
import re
import time

choice = ['umbrella','apple','orange','grapes','milk','coffee']
level = 0
level_count = 0
n=0
chances = 3
def main(page : ft.Page):

    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    container = ft.Container(
        width=1500, height=100, 
        bgcolor=ft.colors.BLUE_200,
        border_radius=ft.border_radius.all(5),
        content = ft.Row(
                controls=[
                ft.Text(value="Fast Typing Practise",
                    font_family = "Roboto_Slab",
                    weight= ft.FontWeight.BOLD,
                    size=50,
                    text_align = ft.TextAlign.CENTER,
                    )
                ],
                alignment = ft.MainAxisAlignment.CENTER,
            )
                )


    level_indication = ft.Text(size=25,weight=ft.FontWeight.BOLD,
        color='black'
        )
    lifes = ft.Text(size=25,weight=ft.FontWeight.BOLD,color='violet')
    timer = ft.Text(size=25,weight=ft.FontWeight.BOLD,color='red')
    text = ft.Text(value=random.choice(choice)
        ,size=30,weight=ft.FontWeight.BOLD,color='green')
    input_box = ft.TextField(width=300)
    
    lifes.value = f"Attempts {chances}"
    level_indication.value =  f"Level :: {level_count}"
    def change_words(e : ft.KeyboardEvent):
        global level,n,chances,level_count
        word_by_word = []

        try:
            with open("para.txt","r") as file:
                rd = file.read()
                if level <=10:
                    word_by_word = re.findall(r'\S+', rd)
                    word_by_word = [item.strip() for item in word_by_word]
                    level_indication.value = f"Level :: {level_count}"
                    level_count=1
                    
                elif level >10 and level <=20:
                    word_by_word = re.findall(r'\S+\s+\S+\s+\S+', rd)
                    word_by_word = [item.strip() for item in word_by_word]
                    level_indication.value = value=f"Level :: {level_count}"
                    level_count=2

                elif level >20 and level <=30:
                    word_by_word = re.findall(r'\S+\s+\S+\s+\S+\s+\S+\s+\S+', rd)
                    word_by_word = [item.strip() for item in word_by_word]
                    level_indication.value = value=f"Level :: {level_count}"
                    level_count=3
                else:
                    word_by_word = re.findall(r'\S+\s+\S+\s+\S+\s+\S+\s+\S+\S+\s+\S+\s+\S+\s+\S+\s+\S+', rd)
                    word_by_word = [item.strip() for item in word_by_word]
                    level_indication.value = value=f"Level :: {level_count}"
                    level_count=4

        except Exception as ez:
            text.color = 'yellow'
            text.value = 'Text File Missing Error Contact Dev'
            page.update()
       
        if e.key == 'Enter':

            if input_box.value.strip() == text.value.strip() and n<=15:
                n=0
                page.update()
                text.value = random.choice(word_by_word)
                text.color = 'green'
                input_box.value=""
                page.update()
                input_box.focus()
                if level >50:
                    text.value = "Congrats You Made It"
                    level=0
                    level_count=1
                    chances = 3
                    lifes.value = f"Attempts {chances}"
                    page.update()
                level+=1
            else:
                chances-=1
                lifes.value = f"Attempts {chances}"
                page.update()
                if chances == 0:
                    chances = 3
                    lifes.value = f"Attempts {chances}"
                    page.update()
                text.color='red'
                input_box.value=""
                page.update()
                input_box.focus()
                
    page.on_keyboard_event = change_words
    page.add(container,level_indication,lifes,timer,text,input_box)
    input_box.focus()

    def run_timer():
        global n
        n+=1
        timer.value=f'Time :: {n}'
        if n == 15:
            n = 0
            input_box.value=""
            page.update()
            
        page.update()
    while True:
        run_timer()
        time.sleep(1)
   

ft.app(target=main)