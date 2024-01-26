# # POLYMORPHISM : > Taking multiple forms > in built ex : len() -> can use to find length of any data type
# class CSK:
#     def captain(self):
#         print("Captain of CSK is M.S Dhoni.")

#     def homeGround(self):
#         print("Homeground of CSK is Chepauk.")

#     def wk(self):
#         print("Wicket Keeper of CSK is M.S dhoni.")

# class SRH:
#     def captain(self):
#         print("Captain of SRH is Aiden Markram.")

#     def homeGround(self):
#         print("Homeground of SRH is 'The Rajiv Gandhi International Cricket Stadium.'")

#     def wk(self):
#         print("Wicket Keeper of SRH is Henric Klasen.")

# print("\n")
# csk = CSK()
# csk.captain()
# print("\n")
# srh = SRH()
# srh.captain()

#  Function Overloading
class Team:
    def __init__(self, team_name, captain_name="Unknown", home_ground="Unknown", wk_name="Unknown"):
        self.team_name = team_name
        self.captain_name = captain_name
        self.home_ground = home_ground
        self.wk_name = wk_name

    def display_info(self):
        print(f"Team: {self.team_name}")
        print(f"Captain: {self.captain_name}")
        print(f"Homeground: {self.home_ground}")
        print(f"Wicket Keeper: {self.wk_name}")
        print()

class CSK(Team):
    def __init__(self):
        super().__init__("Chennai Super Kings", "M.S Dhoni", "Chepauk", "M.S Dhoni")

    def display_info(self):
        super().display_info()
        print("Additional information specific to CSK")

class SRH(Team):
    def __init__(self):
        super().__init__("Sunrisers Hyderabad", "Aiden Markram", "The Rajiv Gandhi International Cricket Stadium", "Henric Klaasen")

    def display_info(self):
        super().display_info()
        print("Additional information specific to SRH")

# Example usage demonstrating function overloading
csk_team = CSK()
srh_team = SRH()

teams = [csk_team, srh_team]

for team in teams:
    team.display_info()
