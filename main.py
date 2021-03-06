from classes.team import team
from classes.member import member
import random

teams = []

def check_if_team_exists_by_name(name):
    if name is None:
        raise "You must provide a team name"
    try:
        if len(teams)==0:
            return False
        else:
            for team in teams:
                if(team.name == name):
                    return True
    except:
        print("An error must have occurred trying to find that team")
    return False

def get_team_by_name(name):
    for team in teams:
        print("\n iterating through team", team.name)
        if(team.name == name):
            print("Found the team! ", team.name)
            return team
    return None


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
        print('\nthe check if team exists function returned ', team)
        new_member = member(member_name)
        team.members.append(new_member)
        print(new_member.name, " has been added to ", team.name)
        print(team.name, " now has ", len(team.members), " members")
        main()
    else:
        print("Sorry that team doesn't exist!")
        main()


def print_each_member_in_team(name):
    team = get_team_by_name(name)
    try:
        for member in team.members:
            print(member.name)
    except:
        print("Sorry that team doesn't seem to exist")


def chunk_team_members(team, num):
    print("Chunking team ", team, " into ", num, " chunks...")
    list_of_chunks =[]
    start_chunk = 0
    end_chunk = start_chunk+num
    while end_chunk <= len(team.members)+num:
        chunk_ls = team.members[start_chunk: end_chunk]
        list_of_chunks.append(chunk_ls)
        start_chunk = start_chunk +num
        end_chunk = end_chunk+num    
    
    return list_of_chunks
    print("Chunking is complete.")
    print("\n LIST OF CHUNKS: ", list_of_chunks)

def init_shuffle_team():
    team_name = input("What team would you like to shuffle?")
    print_each_member_in_team(team_name)
    try:
        team = get_team_by_name(team_name)
        print("About to shuffle ", team)
        number_of_chunks = input("How many people per each team would you like?")
        random.shuffle(team.members)
        
        chunk_team_members(team, number_of_chunks)

        print(team_name, " has been shuffled and chunked")
        print_each_member_in_team(team_name)
    except:
        print("Error occured attempting to shuffle team")



def test():
     # setup teams
    print("testing...")
    team_1 = team("team 1")
    team_2 = team("team 2")
    team_3 = team("team 3")

    # add members to team 1
    team_1.members = [member("a"), member("b"), member("c"), member("d"), member("e"), member("f"), member("g"), member("h"), member("i"), member("j")]

    teams.append(team_1)
    teams.append(team_2)
    teams.append(team_3)

    print("There are ", len(teams), "teams ")

    # Check team 1 initially
    print_each_member_in_team("team 1")

    random.shuffle(team_1.members)

    chunk_team_members(team_1, 3)

    print_each_member_in_team(team_1.name)




def print_pretty_headers():
    print('////////////////////////////////////////')
    print('//WELCOME TO THE PYTHON SHUFFLE CLI/////')
    print('///////////////////////////////////////')


def main():
    action = Number = input("What would you like to do?\n\n 1: Create a Team \n\n 2: Add A Member To a Team\n\n 3: Shuffle a Team? \n\n 4: To test a sample shuffle and chunk")
    if action == "1":
        init_create_team()
    elif action == "2":
        init_add_member()
    elif action =="3":
        init_shuffle_team()
    elif action == "4":
        test()
    else:
        print("")
        print("Sorry! That's not an option. Please Try again. ")
        main()

def start():
    print_pretty_headers()
    main()


start()