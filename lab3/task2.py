def find_common_participants(first_str, second_str, separator=","):
    first = first_str.split(separator)
    second = second_str.split(separator)
    return [name for name in first if name in second]


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
