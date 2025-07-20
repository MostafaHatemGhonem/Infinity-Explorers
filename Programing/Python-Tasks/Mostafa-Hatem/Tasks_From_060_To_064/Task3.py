def get_the_scores(*args, **scores):
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

scores_list = {
    "Math": 90,
    "Science": 80,
    "Language": 70
}

get_the_scores("Osama", **scores_list)



# Test 2
get_the_scores("Osama")

# Test 3
get_the_scores(**scores_list)
