def likelihood():
    likelihoods = (50,38,27,99,4)
    return min(likelihoods)
def run_task1():
    value = likelihood()
    print(f"Minimum likelihood of falling:{value}%")
run_task1()


def likelihood_min_max():
    likelihoods = (50,38,27,99,4)
    return min and max (likelihoods)

def run_task2():
    value = likelihood_min_max()
    print(f"Minimum likelihood{value}% maximum likelihood {value:}%")
run_task2()

