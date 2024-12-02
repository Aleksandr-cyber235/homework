grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students) # преобразовал в список
students.sort() # расставил в алфовитном порядке ['Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve']
average_score = {} # создал пустой словарь
'''Рассчитываю средний балл первого студента,добавляю в пустой словарь'''
one_list = grades[0]
one_list = sum(one_list) / len(one_list)
average_score[students[0]] = one_list
'''второго студента'''
two_list = grades[1]
two_list = sum(two_list) / len(two_list)
average_score[students[1]] = two_list
'''третьего'''
three_list = grades[2]
three_list = sum(three_list) / len(three_list)
average_score[students[2]] = three_list
'''4ого'''
four_list = grades[3]
four_list = sum(four_list) / len(four_list)
average_score[students[3]] = four_list
'''5ого'''
five_list = grades[4]
five_list = sum(five_list) / len(five_list)
average_score[students[4]] = five_list

print(average_score)