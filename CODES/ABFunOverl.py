class Team:
    def __init__(self, team_name, captain_name, home_ground, wk_name):
        self.team_name = team_name
        self.captain_name = captain_name
        self.home_ground_name = home_ground
        self.wk_name = wk_name

class CSK(Team):

    def iplTeam(self):
        print(f"Team: {self.team_name}")
        print(f"Captain: {self.captain_name}")
        print(f"Homeground: {self.home_ground_name}")
        print(f"Wicket Keeper: {self.wk_name}")
        print()

class SRH(Team):

    def iplTeam(self):
        print(f"Team: {self.team_name}")
        print(f"Captain: {self.captain_name}")
        print(f"Homeground: {self.home_ground_name}")
        print(f"Wicket Keeper: {self.wk_name}")
        print()

# Example usage demonstrating polymorphism
csk = CSK("Chennai Super Kings", "M.S Dhoni", "Chepauk", "M.S Dhoni")
srh = SRH("Sunrisers Hyderabad", "Aiden Markram", "The Rajiv Gandhi International Cricket Stadium", "Henric Klaasen")

teams = [csk, srh]

for team in teams:
    team.iplTeam()
