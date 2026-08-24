# RIGHTSNOW
# An educational app that reminds users about rights-related scenarios.


# BLUEPRINT CLASS
class Scenario:
    def __init__(self, name, importance, reminder):
        self.name = name
        self.reminder = reminder
        self.set_importance(importance)

    # Keeps importance between 1 and 5
    def set_importance(self, importance):
        if importance >= 1 and importance <= 5:
            self.importance = importance
        else:
            print("Importance must be between 1 and 5.")
            self.importance = 1

    def show_info(self):
        print("Scenario:", self.name)
        print("Importance:", self.importance)
        print("Reminder:", self.reminder)


# KIND 1
class PoliceScenario(Scenario):
    def __init__(self, name, importance, reminder, interaction_type):
        super().__init__(name, importance, reminder)
        self.interaction_type = interaction_type

    # Same method name, but works differently
    def show_info(self):
        print("\nPOLICE SCENARIO")
        print("Scenario:", self.name)
        print("Importance:", self.importance)
        print("Reminder:", self.reminder)
        print("Interaction Type:", self.interaction_type)


# KIND 2
class SchoolScenario(Scenario):
    def __init__(self, name, importance, reminder, school_issue):
        super().__init__(name, importance, reminder)
        self.school_issue = school_issue

    # Same method name, but works differently
    def show_info(self):
        print("\nSCHOOL SCENARIO")
        print("Scenario:", self.name)
        print("Importance:", self.importance)
        print("Reminder:", self.reminder)
        print("School Issue:", self.school_issue)


# BOSS CLASS
class RightsNow:
    def __init__(self):
        self.scenarios = []

    # Adds a scenario to the list
    def add_scenario(self, scenario):
        self.scenarios.append(scenario)

    # Shows every scenario with a number
    def show_scenarios(self):
        if len(self.scenarios) == 0:
            print("There are no scenarios.")
            return

        print("\nRIGHTSNOW SCENARIOS")

        for i in range(len(self.scenarios)):
            print(i + 1, "-", self.scenarios[i].name)

    # Lets the user choose one scenario
    def view_scenario(self):
        if len(self.scenarios) == 0:
            print("There are no scenarios.")
            return

        self.show_scenarios()

        try:
            choice = int(input("\nChoose a scenario number: "))

            if choice < 1 or choice > len(self.scenarios):
                print("That scenario does not exist.")
                return

            selected = self.scenarios[choice - 1]
            selected.show_info()

        except ValueError:
            print("Please enter a number.")

    # Lets the user add a new scenario
    def create_scenario(self):
        print("\nADD A SCENARIO")
        print("1 - Police Scenario")
        print("2 - School Scenario")

        try:
            scenario_type = int(input("Choose a type: "))

            if scenario_type != 1 and scenario_type != 2:
                print("Please choose 1 or 2.")
                return

        except ValueError:
            print("Please enter a number.")
            return

        name = input("Scenario name: ")
        reminder = input("Rights reminder: ")

        try:
            importance = int(input("Importance from 1 to 5: "))

            if importance < 1 or importance > 5:
                print("Importance must be between 1 and 5.")
                return

        except ValueError:
            print("Please enter a number for importance.")
            return

        if scenario_type == 1:
            interaction_type = input(
                "Interaction type (traffic, questioning, walking, etc.): "
            )

            new_scenario = PoliceScenario(
                name,
                importance,
                reminder,
                interaction_type
            )

        else:
            school_issue = input(
                "School issue (search, discipline, speech, etc.): "
            )

            new_scenario = SchoolScenario(
                name,
                importance,
                reminder,
                school_issue
            )

        self.add_scenario(new_scenario)
        print("Scenario added successfully.")

    # Adds up the importance numbers
    def show_total_importance(self):
        if len(self.scenarios) == 0:
            print("There are no scenarios to add up.")
            return

        total = 0

        for scenario in self.scenarios:
            total = total + scenario.importance

        print("\nTotal importance points:", total)

    # Runs the whole app
    def run(self):
        print("\nWelcome to RIGHTSNOW")
        print("Educational use only. Laws and rights can vary by location.")

        while True:
            print("\nRIGHTSNOW MENU")
            print("1 - Show all scenarios")
            print("2 - View one scenario")
            print("3 - Add a scenario")
            print("4 - Show total importance")
            print("5 - Quit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.show_scenarios()

            elif choice == "2":
                self.view_scenario()

            elif choice == "3":
                self.create_scenario()

            elif choice == "4":
                self.show_total_importance()

            elif choice == "5":
                print("Thanks for using RIGHTSNOW.")
                break

            else:
                print("Please choose a number from 1 to 5.")


# --------------------------------------------------
# FIVE STARTING OBJECTS
# --------------------------------------------------

scenario1 = PoliceScenario(
    "Traffic Stop",
    5,
    "Stay calm and ask questions if you are unsure what is happening.",
    "Traffic"
)

scenario2 = PoliceScenario(
    "Questioned by Police",
    5,
    "Stay calm and pay attention to what you are being asked.",
    "Questioning"
)

scenario3 = PoliceScenario(
    "Stopped While Walking",
    4,
    "Stay calm and ask for clarification about the situation.",
    "Walking"
)

scenario4 = SchoolScenario(
    "School Search",
    4,
    "Ask why the search is happening and stay calm.",
    "Search"
)

scenario5 = SchoolScenario(
    "School Discipline",
    3,
    "Ask what rule you are accused of breaking.",
    "Discipline"
)


# --------------------------------------------------
# START THE APP
# --------------------------------------------------

app = RightsNow()

app.add_scenario(scenario1)
app.add_scenario(scenario2)
app.add_scenario(scenario3)
app.add_scenario(scenario4)
app.add_scenario(scenario5)

app.run()