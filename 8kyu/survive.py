"""
A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

Return true if yes, false otherwise :)
"""

#Input two positive number parameters
#Output Boolean

def hero(bullets, dragons):
    # Check if dragons are divisiable by bullets
    if (bullets//dragons==2):
        return True
    return False

#Other solutions
def hero(bullets, dragons):
    # Check if the number of bullets is sufficient to defeat the dragons
    return bullets >= dragons * 2