class Scenario:
    def __init__(self, name, importance, reminder):
        self.name = name
        self.importance = importance
        self.reminder = reminder

    def show_info(self):
        print("Scenario:", self.name)
        print("Importance:", self.importance)
        print("Reminder:", self.reminder)

class PoliceScenario(Scenario):
    def __init__(self, name, importance, reminder, interaction_type):
        super().__init__(name, importance, reminder)
        self.interaction_type = interaction_type

    def show_info(self):
        print("POLICE SCENARIO")
        print("Scenario:", self.name)
        print("Importance:", self.importance)
        print("Reminder:", self.reminder)
        print("Interaction Type:", self.interaction_type)

class SchoolScenario(Scenario):
    def __init__(self, name, importance, reminder, school_issue):
        super().__init__(name, importance, reminder)
        self.school_issue = school_issue

    def show_info(self):
        print("SCHOOL SCENARIO")
        print("Scenario:", self.name)
        print("Importance:", self.importance)
        print("Reminder:", self.reminder)
        print("School Issue:", self.school_issue)

scenario1 = PoliceScenario(
    "Traffic Stop",
    5,
    "Stay calm and remember your rights.",
    "Traffic"
)

scenario2 = PoliceScenario(
    "Questioned by Police",
    5,
    "Stay calm and ask if you are free to leave.",
    "Questioning"
)

scenario3 = SchoolScenario(
    "School Search",
    4,
    "Ask why you are being searched.",
    "Search"
)

scenario4 = SchoolScenario(
    "School Discipline",
    3,
    "Ask what rule you are accused of breaking.",
    "Discipline"
)

scenarios = [scenario1, scenario2, scenario3, scenario4]

for scenario in scenarios:
    scenario.show_info()
    print()