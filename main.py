data = {
    'place': ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th'],
    'Associate': [
        'Associate_1', 'Associate_2', 'Associate_3', 'Associate_4',
        'Associate_5', 'Associate_6', 'Associate_7', 'Associate_8',
        'Associate_9', 'Associate_10'
    ],
    'Points': [50, 70, 80, 60, 90, 30, 40, 85, 95, 65]
}

def format_diary_entry(data):
    diary_entry = "Diary Entry\n\n"
    num_entries = min(len(data['place']), len(data['Associate']), len(data['Points']))
    for i in range(num_entries):
        place = data['place'][i] if i < len(data['place']) else ""
        associate = data['Associate'][i] if i < len(data['Associate']) else ""
        points = data['Points'][i] if i < len(data['Points']) else ""
        diary_entry += f"Place: {place}, Associate: {associate}, Points: {points}\n"
    return diary_entry

def save_diary_entry(filename, diary_entry):
    with open(filename, 'w') as file:
        file.write(diary_entry)

# Example usage
diary_entry = format_diary_entry(data)
print(diary_entry)

filename = "diary_entry.txt"
save_diary_entry(filename, diary_entry)