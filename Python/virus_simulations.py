import math
import matplotlib.pyplot as plt
import numpy as np

# A quick function to help us make sure our parameters don't spiral out of control: 
# Takes in a value and an upper and lower limit and if the value is outside of the limits, "round" it to the edge of the limit
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))



max_weeks = 104                      # How many iterations until we end one simulation--if the curves start flattening out you might want to increase this
num_sims = 7                        # How many simulations you want to do--one simulation is fine, but multiple allows you to see the variance.


fig, axs = plt.subplots(2)          # Setting up plots
#fig, axs = plt.subplots()
weeks = range(1, max_weeks + 1)     # X-axis vector
Quarantine=True
Masks=False
Vaccine=False    

for i in range(num_sims):

    # P(opulation) = S(usceptible) + I(nfected) + R(ecovered)
    total_population = 330000000
    num_infected = 10
    num_susceptible = total_population - num_infected   
    num_recovered = 0
    
    
        # Num interactions/person/week: does this seem like a reasonable assumption?
              # Chance that an interaction creates an infection (given susceptibility): does this seem reasonable?

    recovery_prob = .6               # Chance that an infected person recovers (or dies) by the next week

    new_cases = []
    total_cases = []
    for week in range(1, max_weeks + 1):
        if week==0:
            Quarantine=True
            Masks=False
            Vaccine=False
        if week==8:
            Quarantine=False
        if week==4:
            Masks=True
        if week==75:
            Masks=False
        if week==52:
            Vaccine=True

            

        if Quarantine:
            avg_interactions_per_week = 1
            avg_interactions_per_week += np.random.normal(0,.1,1)[0]
            avg_interactions_per_week = constrain(avg_interactions_per_week, 1, 3)
        else:
            avg_interactions_per_week=5
            avg_interactions_per_week += np.random.normal(0,.1,1)[0]
            avg_interactions_per_week = constrain(avg_interactions_per_week, 4, 10)

        if Masks and Vaccine:
            infection_prob = .1 
            infection_prob += np.random.normal(0,.005,1)[0]             # But it's not clear if they trend in any particular direction
            infection_prob = constrain(infection_prob, .05, .2)
        elif Masks:
            infection_prob = .3 
            infection_prob += np.random.normal(0,.005,1)[0]             # But it's not clear if they trend in any particular direction
            infection_prob = constrain(infection_prob, .1, .5)
        elif Vaccine:
            infection_prob = .2 
            infection_prob += np.random.normal(0,.005,1)[0]             # But it's not clear if they trend in any particular direction
            infection_prob = constrain(infection_prob, .1, .4)
    


      


        recovery_prob += np.random.normal(0,.005,1)[0]              # No matter what, they don't go outside of some reasonable bounds
        recovery_prob = constrain(recovery_prob, .5, .7)


        prop_susceptible = num_susceptible / total_population
        new_recoveries = math.floor(num_infected * recovery_prob)
        new_cases.append(math.floor(num_infected * avg_interactions_per_week * prop_susceptible * infection_prob))  
    

        
        num_recovered += new_recoveries                             # Move new recoveries from infected to recovered
        num_infected -= new_recoveries  

       
        num_infected += new_cases[week-1]                           # Move new cases from susceptible to infected
        num_susceptible -= new_cases[week-1]   

        total_cases.append(num_recovered+num_infected)  
    

        #print(f"Week {week}:")
        #print(f"There were {new_cases[week-1]} new cases this week.")
        #print(f"That makes our new cumulative case count {num_recovered + num_infected}")
        #print(f"{new_recoveries} people recovered this week.")

    axs[0].plot(weeks, new_cases)                                   # Draw plots of the new cases each week and the total cases
    axs[1].plot(weeks, total_cases)
    #axs.plot(weeks, new_cases)
    


    
plt.xlabel("Week")
plt.ylabel("Infections")
plt.show()
