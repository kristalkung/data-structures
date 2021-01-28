"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    
    houses = set()

    # filename = open(cohort_data.txt)
    cohort_data = open(filename)

    for line in cohort_data:
      house = line.rstrip().split("|")[2]

      if house:
        #something add 
        houses.add(house)

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []

    cohort_data = open(filename)
    
    for line in cohort_data:
      first_name, last_name, _, _, cohort_name = line.rstrip().split("|")

      if cohort_name not in ('I', 'G') and cohort in ('All', cohort_name):
        students.append(f"{first_name} {last_name}")


    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    # TODO: replace this with your code

    cohort_data = open(filename)
    
    for line in cohort_data:
      first_name, last_name, house, _, cohort_name = line.rstrip().split("|")

      if cohort_name in ("I", "G"):
      # if not in a house, then the person is an instructor or ghost
        if cohort_name == "I":
          instructors.append(f"{first_name} {last_name}")
        else:
          ghosts.append(f"{first_name} {last_name}")
      else:
        if house == "Dumbledore's Army":
          dumbledores_army.append(f"{first_name} {last_name}")
        elif house == "Gryffindor":
          gryffindor.append(f"{first_name} {last_name}")
        elif house == "Hufflepuff":
          hufflepuff.append(f"{first_name} {last_name}")
        elif house == "Ravenclaw":
          ravenclaw.append(f"{first_name} {last_name}")
        elif house == "Slytherin":
          slytherin.append(f"{first_name} {last_name}")

    return [sorted(dumbledores_army), sorted(gryffindor), sorted(hufflepuff), sorted(ravenclaw), sorted(slytherin), sorted(ghosts), sorted(instructors)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    cohort_data = open(filename)

    for line in cohort_data:
      first_name, last_name, house, advisor, cohort_name = line.rstrip().split("|")
      line_tuple = (f"{first_name} {last_name}", house, advisor, cohort_name)

      all_data.append(line_tuple)

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # cohort_data = open(filename)
    # name_split = name.split(" ")
    # for line in cohort_data:
    #   first_name, last_name, _, _, cohort_name = line.rstrip().split("|")

    #   if name_split[0] == first_name and name_split[1] == last_name:
    #     return cohort_name
    
    for full_name, _, _, cohort_name in all_data(filename):
    # call all_data and set full_name as f"{first_name} {last_name}"
      if full_name == name:
        return cohort_name



def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    lasts = []
    duplicates = []

    for full_name, _, _, _ in all_data(filename):
      last_name = full_name.split(" ")[1]
      if last_name not in lasts:
        lasts.append(last_name)
      else:
        duplicates.append(last_name)

    duplicates = set(duplicates)
 
    return duplicates


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code

    housemates = set()
    same_house = ""
    same_cohort = ""


    for person in all_data(filename):
      full_name, house, _, cohort_name = person

      if name == full_name:
        target_person = person
        break 
    if target_person:
      _, same_house, _, same_cohort = target_person 
      
      for full_name, house, _, cohort_name in all_data(filename):
        if house == same_house and cohort_name == same_cohort and full_name != name:
          housemates.add(full_name)
    return housemates
    


        

##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
