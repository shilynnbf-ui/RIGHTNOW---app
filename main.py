# ============================================================
# RIGHTSNOW
# An educational app that helps users understand
# their rights in different situations.
# ============================================================


# PARENT CLASS

class Scenario:
    def __init__(
        self,
        name,
        reminder,
        should_do,
        should_not_do,
        possible_concerns
    ):
        self.name = name
        self.reminder = reminder
        self.should_do = should_do
        self.should_not_do = should_not_do
        self.possible_concerns = possible_concerns

    # General scenario information
    def show_info(self):
        print()
        print("========================================")
        print("SCENARIO:", self.name)
        print("========================================")

        print()
        print("REMINDER:")
        print(self.reminder)

        print()
        print("WHAT YOU SHOULD DO:")
        print("-", self.should_do)

        print()
        print("WHAT YOU SHOULD NOT DO:")
        print("-", self.should_not_do)

        print()
        print("POSSIBLE RIGHTS CONCERNS:")
        for concern in self.possible_concerns:
            print("-", concern)

        print()
        print("IMPORTANT:")
        print("A possible concern does not automatically")
        print("mean that a law was violated.")
        print("Laws vary by location and situation.")

        print("========================================")


# ============================================================
# POLICE SCENARIO
# ============================================================

class PoliceScenario(Scenario):

    def __init__(
        self,
        name,
        reminder,
        should_do,
        should_not_do,
        possible_concerns,
        interaction_type
    ):
        super().__init__(
            name,
            reminder,
            should_do,
            should_not_do,
            possible_concerns
        )

        self.interaction_type = interaction_type

    # Police-specific information
    def show_info(self):
        print()
        print("========================================")
        print("           POLICE SCENARIO")
        print("========================================")

        print("Scenario:", self.name)
        print("Interaction Type:", self.interaction_type)

        print()
        print("REMINDER:")
        print(self.reminder)

        print()
        print("WHAT YOU SHOULD DO:")
        print("-", self.should_do)

        print()
        print("WHAT YOU SHOULD NOT DO:")
        print("-", self.should_not_do)

        print()
        print("POSSIBLE RIGHTS CONCERNS:")

        for concern in self.possible_concerns:
            print("-", concern)

        print()
        print("IMPORTANT:")
        print("A possible concern does not automatically")
        print("mean that a law was violated.")
        print("Laws vary by location and situation.")

        print("========================================")


# SCHOOL SCENARIO


class SchoolScenario(Scenario):

    def __init__(
        self,
        name,
        reminder,
        should_do,
        should_not_do,
        possible_concerns,
        school_issue
    ):
        super().__init__(
            name,
            reminder,
            should_do,
            should_not_do,
            possible_concerns
        )

        self.school_issue = school_issue

    # School-specific information
    def show_info(self):
        print()
        print("========================================")
        print("           SCHOOL SCENARIO")
        print("========================================")

        print("Scenario:", self.name)
        print("School Issue:", self.school_issue)

        print()
        print("REMINDER:")
        print(self.reminder)

        print()
        print("WHAT YOU SHOULD DO:")
        print("-", self.should_do)

        print()
        print("WHAT YOU SHOULD NOT DO:")
        print("-", self.should_not_do)

        print()
        print("POSSIBLE RIGHTS CONCERNS:")

        for concern in self.possible_concerns:
            print("-", concern)

        print()
        print("IMPORTANT:")
        print("A possible concern does not automatically")
        print("mean that a law was violated.")
        print("School policies and laws vary by location.")

        print("========================================")



# RIGHTSNOW APP CLASS


class RightsNow:

    def __init__(self):
        self.scenarios = []

    # Add a scenario to the list
    def add_scenario(self, scenario):
        self.scenarios.append(scenario)

    # Show all scenarios
    def show_all_scenarios(self):

        print()
        print("========================================")
        print("          RIGHTSNOW SCENARIOS")
        print("========================================")

        if len(self.scenarios) == 0:
            print("There are no scenarios.")
            return

        for number, scenario in enumerate(self.scenarios, start=1):
            print(number, "-", scenario.name)

        print("========================================")

    # Let the user choose a scenario
    def view_scenario(self):

        if len(self.scenarios) == 0:
            print("There are no scenarios.")
            return

        self.show_all_scenarios()

        while True:

            choice = input(
                "\nChoose a scenario number "
                "or B to go back: "
            )

            if choice.lower() == "b":
                return

            if choice.isdigit():

                number = int(choice)

                if 1 <= number <= len(self.scenarios):

                    selected = self.scenarios[number - 1]

                    selected.show_info()

                    input(
                        "\nPress Enter to return to the menu..."
                    )

                    return

            print("Invalid choice. Please try again.")

    # Let the user create a new scenario
    def create_scenario(self):

        print()
        print("========================================")
        print("           ADD A SCENARIO")
        print("========================================")

        print("1 - Police Scenario")
        print("2 - School Scenario")
        print("3 - Cancel")

        scenario_type = input("Choose a type: ")

        if scenario_type == "3":
            return

        if scenario_type != "1" and scenario_type != "2":

            print("Invalid choice.")
            return

        print()

        name = input("Scenario name: ")

        reminder = input(
            "General rights reminder: "
        )

        should_do = input(
            "What should the person do? "
        )

        should_not_do = input(
            "What should the person NOT do? "
        )

        print()
        print("Now add possible warning signs.")

        possible_concerns = []

        while True:

            concern = input(
                "Enter a possible rights concern "
                "(or type DONE): "
            )

            if concern.lower() == "done":
                break

            if concern.strip() != "":
                possible_concerns.append(concern)

        # ----------------------------------------
        # Police scenario
        # ----------------------------------------

        if scenario_type == "1":

            interaction_type = input(
                "Interaction type "
                "(traffic, questioning, walking, etc.): "
            )

            new_scenario = PoliceScenario(
                name,
                reminder,
                should_do,
                should_not_do,
                possible_concerns,
                interaction_type
            )

        # ----------------------------------------
        # School scenario
        # ----------------------------------------

        else:

            school_issue = input(
                "School issue "
                "(search, discipline, speech, etc.): "
            )

            new_scenario = SchoolScenario(
                name,
                reminder,
                should_do,
                should_not_do,
                possible_concerns,
                school_issue
            )

        self.add_scenario(new_scenario)

        print()
        print("Scenario added successfully!")

        input(
            "Press Enter to continue..."
        )

    # Run the entire program
    def run(self):

        print()
        print("========================================")
        print("           WELCOME TO RIGHTSNOW")
        print("========================================")

        print()
        print("RIGHTSNOW helps users understand")
        print("what they can do in different situations.")

        print()
        print("Educational use only.")
        print("Rights and laws can vary by location.")
        print("========================================")

        while True:

            print()
            print("              RIGHTSNOW MENU")
            print("----------------------------------------")
            print("1 - Show all scenarios")
            print("2 - View a scenario")
            print("3 - Add a scenario")
            print("4 - Quit")
            print("----------------------------------------")

            choice = input(
                "Choose an option: "
            )

            # Option 1
            if choice == "1":

                self.show_all_scenarios()

                input(
                    "\nPress Enter to return to the menu..."
                )

            # Option 2
            elif choice == "2":

                self.view_scenario()

            # Option 3
            elif choice == "3":

                self.create_scenario()

            # Option 4
            elif choice == "4":

                print()
                print("========================================")
                print("      THANK YOU FOR USING RIGHTSNOW")
                print("========================================")

                break

            # Invalid choice
            else:

                print()
                print("Invalid option.")
                print("Please choose 1, 2, 3, or 4.")


# STARTING SCENARIOS


# ------------------------------------------------------------
# 1. TRAFFIC STOP
# ------------------------------------------------------------

scenario1 = PoliceScenario(

    "Traffic Stop",

    "Stay calm and pay attention to what is happening.",

    "Stay calm, keep your hands visible, "
    "provide required documents, and ask "
    "questions if you are unsure.",

    "Do not physically resist, threaten the officer, "
    "or make sudden movements.",

    [
        "The stop appears to continue longer than "
        "necessary without additional legal justification.",

        "The officer searches you or your vehicle "
        "without consent or another lawful basis.",

        "The officer uses excessive force.",

        "The stop or search appears to be based "
        "on race or ethnicity."
    ],

    "Traffic"
)


# ------------------------------------------------------------
# 2. QUESTIONED BY POLICE
# ------------------------------------------------------------

scenario2 = PoliceScenario(

    "Questioned by Police",

    "Stay calm and pay attention to what you "
    "are being asked.",

    "Stay calm, listen carefully, and ask whether "
    "you are free to leave.",

    "Do not threaten the officer, physically resist, "
    "or interfere with the investigation.",

    [
        "You are detained without a clear legal basis.",

        "You are prevented from leaving when you "
        "are legally free to do so.",

        "Officers use excessive force.",

        "The questioning or detention appears to be "
        "based on race or ethnicity."
    ],

    "Questioning"
)


# ------------------------------------------------------------
# 3. STOPPED WHILE WALKING
# ------------------------------------------------------------

scenario3 = PoliceScenario(

    "Stopped While Walking",

    "Stay calm and try to understand why "
    "the interaction is happening.",

    "Stay calm and ask why you are being stopped. "
    "Ask whether you are free to leave.",

    "Do not run, threaten the officer, "
    "or physically resist.",

    [
        "You are detained without a lawful basis.",

        "The officer uses excessive force.",

        "The stop or search appears to be based "
        "on race or ethnicity.",

        "A search is conducted without consent "
        "or another lawful basis."
    ],

    "Walking"
)


# ------------------------------------------------------------
# 4. SCHOOL SEARCH
# ------------------------------------------------------------

scenario4 = SchoolScenario(

    "School Search",

    "Ask why the search is happening "
    "and stay calm.",

    "Stay calm and ask what the school is "
    "looking for and why the search is taking place.",

    "Do not physically resist the search "
    "or become aggressive.",

    [
        "School officials conduct a search that "
        "may not be justified under applicable "
        "school rules or law.",

        "You are not given an explanation when "
        "one is appropriate.",

        "The search appears to target you based "
        "on discrimination."
    ],

    "Search"
)


# ------------------------------------------------------------
# 5. SCHOOL DISCIPLINE
# ------------------------------------------------------------

scenario5 = SchoolScenario(

    "School Discipline",

    "Ask what rule or policy you are "
    "being disciplined for.",

    "Stay calm, ask questions, and ask about "
    "the school's policy or disciplinary process.",

    "Do not threaten staff, damage property, "
    "or physically resist.",

    [
        "You are disciplined in a way that may "
        "conflict with applicable school policy "
        "or legal protections.",

        "You are treated differently because "
        "of a protected characteristic.",

        "You are not given information about "
        "the disciplinary process when you "
        "are entitled to it."
    ],

    "Discipline"
)



# CREATE THE APP


app = RightsNow()


# Add the five starting scenarios
app.add_scenario(scenario1)
app.add_scenario(scenario2)
app.add_scenario(scenario3)
app.add_scenario(scenario4)
app.add_scenario(scenario5)



# START RIGHTSNOW

app.run()