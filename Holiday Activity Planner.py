print("Welcome to the Holiday Activity Planner!")

holiday = input("What type of holiday do you prefer? (beach / adventure / city): ").lower()

if holiday == "beach":
    water = input("Do you prefer swimming or sunbathing? ").lower()
    if water == "swimming":
        print("Plan: Pack your snorkel gear and head to a coral reef!")
    else:
        print("Plan: Book a quiet seaside spot and bring your favourite book.")

elif holiday == "adventure":
    thrill = input("Do you prefer hiking or climbing? ").lower()
    if thrill == "hiking":
        print("Plan: Try a scenic mountain trail with a guided group.")
    else:
        print("Plan: Visit an indoor climbing centre to sharpen your skills.")

elif holiday == "city":
    vibe = input("Do you prefer museums or shopping? ").lower()
    if vibe == "museums":
        print("Plan: Explore the top-rated history and art museums downtown.")
    else:
        print("Plan: Spend the day discovering local boutiques and cafés.")

else:
    print("Sorry, that holiday type isn’t recognised.")
