
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

    # Displays basic scenario information
    def show_info(self):
        print("Scenario:", self.name)
        print("Importance:", self.importance)
        print("Reminder:", self.reminder)


# KIND 1 - POLICE SCENARIO

class PoliceScenario(Scenario):

    def __init__(self, name, importance, reminder, interaction_type):
        super().__init__(name, importance, reminder)
        self.interaction_type = interaction_type

    # Displays information specifically for police scenarios
    def show_info(self):
        print("\nPOLICE SCENARIO")
        print("Scenario:", self.name)
        print("Importance:", self.importance)
        print("Reminder:", self.reminder)
        print("Interaction Type:", self.interaction_type)


# KIND 2 - SCHOOL SCENARIO


class SchoolScenario(Scenario):

    def __init__(self, name, importance, reminder, school_issue):
        super().__init__(name, importance, reminder)
        self.school_issue = school_issue

    # Displays information specifically for school scenarios
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

  
    def add_scenario(self, scenario):
        self.scenarios.append(scenario)



    def show_scenarios(self):

        if len(self.scenarios) == 0:
            print("There are no scenarios.")
            return

        print("\nRIGHTSNOW SCENARIOS")

        for i in range(len(self.scenarios)):
            print(i + 1, "-", self.scenarios[i].name)

 

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

        # Get basic information
        name = input("Scenario name: ")

        reminder = input("Rights reminder: ")

        # Get importance
        try:
            importance = int(input("Importance from 1 to 5: "))

            if importance < 1 or importance > 5:
                print("Importance must be between 1 and 5.")
                return

        except ValueError:
            print("Please enter a number for importance.")
            return

        # Create a Police Scenario
        if scenario_type == 1:

            interaction_type = input(
                "Interaction type "
                "(traffic, questioning, walking, etc.): "
            )

            new_scenario = PoliceScenario(
                name,
                importance,
                reminder,
                interaction_type
            )

        # Create a School Scenario
        else:

            school_issue = input(
                "School issue "
                "(search, discipline, speech, etc.): "
            )

            new_scenario = SchoolScenario(
                name,
                importance,
                reminder,
                school_issue
            )

        # Add the new object to the list
        self.add_scenario(new_scenario)

        print("Scenario added successfully.")


    def show_total_importance(self):

        if len(self.scenarios) == 0:
            print("There are no scenarios to add up.")
            return

        total = 0

        for scenario in self.scenarios:
            total = total + scenario.importance

        print("\nTotal importance points:", total)



    def run(self):

        print("\nWelcome to RIGHTSNOW")
        print(
            "Educational use only. "
            "Laws and rights can vary by location."
        )

        while True:

            print("\nRIGHTSNOW MENU")
            print("1 - Show all scenarios")
            print("2 - View one scenario")
            print("3 - Add a scenario")
            print("4 - Show total importance")
            print("5 - Quit")

            choice = input("Choose an option: ")

            # Option 1
            if choice == "1":
                self.show_scenarios()

            # Option 2
            elif choice == "2":
                self.view_scenario()

            # Option 3
            elif choice == "3":
                self.create_scenario()

            # Option 4
            elif choice == "4":
                self.show_total_importance()

            # Option 5
            elif choice == "5":
                print("Thanks for using RIGHTSNOW.")
                break

            # Anything else
            else:
                print("Please choose a number from 1 to 5.")




scenario1 = PoliceScenario(
    "Traffic Stop",
    5,
    "Stay calm and ask questions if you are unsure "
    "what is happening.",
    "Traffic"
)

scenario2 = PoliceScenario(
    "Questioned by Police",
    5,
    "Stay calm and pay attention to what you are "
    "being asked.",
    "Questioning"
)

scenario3 = PoliceScenario(
    "Stopped While Walking",
    4,
    "Stay calm and ask for clarification about "
    "the situation.",
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



# START THE RIGHTSNOW APP


# Create the RightsNow boss object
app = RightsNow()

# Add the five starting scenarios
app.add_scenario(scenario1)
app.add_scenario(scenario2)
app.add_scenario(scenario3)
app.add_scenario(scenario4)
app.add_scenario(scenario5)

# Start the program
app.run()