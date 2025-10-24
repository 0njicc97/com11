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

def steps():
  likelihoods = ("steps 1",50),("steps 2",38),("steps 3",27), ("steps 4",99),("steps 5",4)
  return likelihoods
def run_task3():
     value = steps()
     good = 3
     bad = 2
     for i in range(0,2,len(value), ):
             print(f"Good steps: {good},bad steps: {bad}")
run_task3()




