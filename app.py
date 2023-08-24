class FlightTable:
    def _init_(self):
        self.matches = []
        self.teams = set()
        self.locations = set()
        self.timings = set()

    def add_match(self, location, teams, timing):
        self.matches.append({
            "Location": location,
            "Team 01": teams[0],
            "Team 02": teams[1],
            "Timing": timing
        })
        self.teams.update(teams)
        self.locations.add(location)
        self.timings.add(timing)

    def get_matches_by_team(self, team_name):
        return [match for match in self.matches if team_name in (match["Team 01"], match["Team 02"])]

    def get_matches_by_location(self, location):
        return [match for match in self.matches if match["Location"] == location]

    def get_matches_by_timing(self, timing):
        return [match for match in self.matches if match["Timing"] == timing]

    def display_teams(self):
        print("Teams:", ', '.join(self.teams))

    def display_locations(self):
        print("Locations:", ', '.join(self.locations))

    def display_timings(self):
        print("Timings:", ', '.join(self.timings))


def main():
    flight_table = FlightTable()

    flight_table.add_match("Mumbai", ["India", "England"], "DAY")
    flight_table.add_match("Delhi", ["India", "England"], "DAY-NIGHT")
    flight_table.add_match("Chennai", ["Australia", "India"], "DAY")
    flight_table.add_match("Indore", ["India", "Australia"], "DAY-NIGHT")
    flight_table.add_match("Mohali", ["Australia", "India"], "DAY")
    flight_table.add_match("Delhi", ["South Africa", "Australia"], "DAY-NIGHT")

    while True:
        print("\nSearch Options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Display Teams")
        print("5. Display Locations")
        print("6. Display Timings")
        print("7. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            team_name = input("Enter team name: ")
            matches = flight_table.get_matches_by_team(team_name)
            if matches:
                print("Matches:")
                for match in matches:
                    print(match)
            else:
                print("No matches found for the given team.")

        elif choice == 2:
            location = input("Enter location: ")
            matches = flight_table.get_matches_by_location(location)
            if matches:
                print("Matches:")
                for match in matches:
                    print(match)
            else:
                print("No matches found for the given location.")

        elif choice == 3:
            timing = input("Enter timing: ")
            matches = flight_table.get_matches_by_timing(timing)
            if matches:
                print("Matches:")
                for match in matches:
                    print(match)
            else:
                print("No matches found for the given timing.")

        elif choice == 4:
            flight_table.display_teams()

        elif choice == 5:
            flight_table.display_locations()

        elif choice == 6:
            flight_table.display_timings()

        elif choice == 7:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if _name_ == "_main_":
    main()
