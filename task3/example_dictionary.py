hello_world_translations = {
    "Afrikaans": "Hallo, wêreld!",
    "Albanian": "Pershëndetje Botë",
    "Arabic": "أهلاً بالعالم",
    "Armenian": "Բարե՛ւ, աշխարհ",
    "Azeri": "Salam Dünya",
    "Basque" : "Kaixo mundua!",
    "Belarusian" : "Прывітанне свет",
    "Bemba" : "Shani Mwechalo!",
    "Bengali" : "Shagatam Prithivi!",
    "Bosnian" : "Zdravo Svijete!",
    "Bulgarian" : "Здравей, свят!",
}

print('Displaying "Hello World" in different languages')

for language, text in hello_world_translations.items():
    print('{}: {}'.format(language, text))
    print("\n -----------------------")
    