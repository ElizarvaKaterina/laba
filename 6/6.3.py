student={"Горохов": ["Немецкий", "Французский", "Китайский"], "Лавров": ["Английский", "Испанский", "Французский"], "Канев": ["Китайский"],  "Логунов": ["Русский"]}
all_languages = []
for languages in students.values():
    all_languages.extend(languages)
    unique_languages = sorted(set(all_languages))
print("Список всех языков:", unique_languages)
chinese_speakers = []
for name, languages in students.items():
    if "Китайский" in languages:
        chinese_speakers.append(name)
        print("Список студентов, знающих китайский язык:", chinese_speakers)
