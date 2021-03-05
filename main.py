from classes.team import team
from classes.member import member

teams = []

def check_if_team_exists_by_name(name):
    if len(teams)==0:
        return False
    else:
        for team in teams:
            if(team.name == name):
                return True
    return False

def get_team_by_name(name):
    for team in teams:
        if(team.name == name):
            return team


def init_create_team():
    team_name = input("What would you like to call your new team?")
    if check_if_team_exists_by_name(team_name):
        print("Sorry! A team with that name already exist. Please try again.")
        init_create_team()
    else:
        new_team = team(team_name)
        teams.append(new_team)

    print(new_team.name, "was created")
    print("You now have ", len(teams), "teams")
    main()



def init_add_member():
    team_name = input("What team would you like to add this new member to?")

    if check_if_team_exists_by_name(team_name):
        member_name = input("What would you like to name your new team member?")
        team = get_team_by_name(team_name)
        new_member = member(member_name)
        team.members.append(new_member)
        print(new_member.name, " has been added to ", team.name)
        print(team.name, " now has ", len(team.members), " members")
        main()
    else:
        print("Sorry that team doesn't exist!")
        main()



def init_shuffle_team():
    print("Not implemented yet")


def print_pretty_headers():
    print('////////////////////////////////////////')
    print('//WELCOME TO THE PYTHON SHUFFLE CLI/////')
    print('///////////////////////////////////////')



def main():
    action = Number = input("What would you like to do?\n\n 1: Create a Team \n\n 2: Add A Member To a Team\n\n 3: Shuffle a Team?")
    if action == "1":
        init_create_team()
    elif action == "2":
        init_add_member()
    elif action =="3":
        init_shuffle_team()
    else:
        print("")
        print("Sorry! That's not an option. Please Try again. ")
        main()

def start():
    print_pretty_headers()
    main()


start()
