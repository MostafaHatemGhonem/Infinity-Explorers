def get_people_scores(*args, **scores):
    if args:
        name = args[0]
        if scores:
            print(f"Hello {name} This Is Your Score Table:")
            for subject, score in scores.items():
                print(f"{subject} => {score}")
        else:
            print(f"Hello {name} You Have No Scores To Show")
    else:
        for subject, score in scores.items():
            print(f"{subject} => {score}")
# Test 1
get_people_scores("Osama", Math=90, Science=80, Language=70)

# Test 2
get_people_scores("Mahmoud", Logic=70, Problems=60)


# Test 3
get_people_scores(Logic=70, Problems=60)


# Test 4
get_people_scores("Ahmed")
