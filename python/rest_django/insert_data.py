import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from selenium import webdriver
from selenium.webdriver.common.by import By
from chromedriver_py import binary_path
from apps.framedata.models import Character, Move

def insert_data():
    svc = webdriver.ChromeService(executable_path=binary_path)
    driver = webdriver.Chrome(service=svc)
    
    driver.get(f"https://www.streetfighter.com/6/character/")
    characters_as = driver.find_elements(By.CSS_SELECTOR, ".select_character__select__list__bgBGl > ul > li > a")
    print(len(characters_as))
    characters = {}


    for elements in characters_as:
        current_character_url = elements.get_attribute("href")
        current_character_name = os.path.split(current_character_url)  # current_character_name[1] é o nome do personagem
        c = Character(character_name = current_character_name[1]) # inserir o personagem no banco de dados (colocar em django)
        c.save()
        print(f'{current_character_name[1]} adicionado')
        characters[c] = current_character_url

    for c, url in characters.items():
        driver.get(f"{url}/frame")
        current_character_move_list = driver.find_elements(By.CSS_SELECTOR, 'table > tbody > tr:not([class])')
        for move in current_character_move_list:
            colunas = move.find_elements(By.TAG_NAME, "td") # mudar o nome das colunas para igual o nome do model
            move_name = colunas[0].find_element(By.TAG_NAME, "span").get_attribute("innerText")
            startup_frames = colunas[1].get_attribute("innerText")
            active_frames = colunas[2].get_attribute("innerText")
            recovery_frames = colunas[3].get_attribute("innerText")
            on_hit = colunas[4].get_attribute("innerText")
            on_block = colunas[5].get_attribute("innerText")
            cancel = colunas[6].get_attribute("innerText")
            damage = colunas[7].get_attribute("innerText")
            scaling = colunas[8].get_attribute("innerText")
            drive_increase = colunas[9].get_attribute("innerText")
            drive_decrease = colunas[10].get_attribute("innerText")
            drive_decrease_pc = colunas[11].get_attribute("innerText")
            sa_increase = colunas[12].get_attribute("innerText")
            high_low = colunas[13].get_attribute("innerText")
            misc = colunas[14].get_attribute("innerText")
            m = Move(move_name=move_name, startup_frames=startup_frames, active_frames=active_frames, recovery_frames=recovery_frames,
                    on_hit=on_hit, on_block=on_block, cancel=cancel, damage=damage, scaling=scaling, drive_increase=drive_increase,
                    drive_decrease=drive_decrease, drive_decrease_pc=drive_decrease_pc, sa_increase=sa_increase, high_low=high_low, misc=misc,
                    character=c)
            m.save()
            print(f'{move_name} adicionado')

insert_data()
