# Класс "Команды".
class Team:
    def __init__(self, name, number_of_members, scores, times):
        self.name = name
        self.number_of_members = number_of_members
        self.scores = scores
        self.times = times

    def challenge_result(self, other):
        if self.scores >= other.scores and self.times < other.times:
            result = f'Победа команды "{self.name}"!'
        elif self.scores <= other.scores and self.times > other.times:
            result = f'Победа команды "{other.name}"!'
        else:
            result = 'Ничья!'
        return result

    def sum_tasks(self, other):
        tasks_total = int(self.scores) + int(other.scores)
        return tasks_total

    def time_avg(self, other):
        Avg_time = (float(self.times) + float(other.times)) / Team.sum_tasks(self, other)
        return Avg_time
    

Team1 = Team('Мастера кода', '', '', '')
Team2 = Team('Волшебники данных', '', '', '')

# Использование оператора %.
Team1.number_of_members = input("Введите количество участников в команде Team1.name: ")
Team2.number_of_members = input("Введите количество участников в команде Team2.name: ")
print('В команде "%s": %s участников!' % (Team1.name, Team1.number_of_members))
print('В команде "%s": %s участников!' % (Team2.name, Team2.number_of_members))
print('Итого cегодня количество участников в командах: %s и %s!'
      % (Team1.number_of_members, Team2.number_of_members))

# Использование оператора format().
Team1.scores = input("Введите количество задач, решённых командой Team1.name: ")
Team2.scores = input("Введите количество задач, решённых командой Team2.name: ")
print('Команда {0} решила задач: {1}!'.format(Team1.name, Team1.scores))
print('Команда {0} решила задач: {1}!'.format(Team2.name, Team2.scores))

Team1.times = input("Введите (в секундах) время, за которое команда Team1.name решила задачи: ")
Team2.times = input("Введите (в секундах) время, за которое команда Team2.name решила задачи: ")
print('Команда {0} решила задачи за: {1} с!'.format(Team1.name, Team1.times))
print('Команда {0} решила задачи за: {1} с!'.format(Team2.name, Team2.times))

# Использование f-строк.
print(f'Команды решили {Team1.scores} и {Team2.scores} задач.')
print(f'Сегодня было решено {Team.sum_tasks(Team1, Team2)} '
      f'задач, в среднем за {Team.time_avg(Team1, Team2):.1f} с одна задача!')
print(Team.challenge_result(Team1,Team2))


