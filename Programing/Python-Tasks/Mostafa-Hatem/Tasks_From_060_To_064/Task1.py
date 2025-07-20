
def get_score(**subjects):
    for subject, score in subjects.items():
        print(f"{subject} => {score}")


# Tests
get_score(Math=90, Science=80, Language=70)


# Tests
get_score(Logic=70, Problems=60)
