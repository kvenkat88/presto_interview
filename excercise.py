rec = '''
Selenium was originally developed by Jason Huggins in 2004 as an internal tool at ThoughtWorks. Huggins was later joined by other programmers and testers at ThoughtWorks, before Paul Hammant joined the team and steered the development of the second mode of operation that would later become "Selenium Remote Control" (RC). The tool was open sourced that year.
In 2007, Huggins joined Google. Together with others like Jennifer Bevan, he continued with the development and stabilization of Selenium RC. At the same time, Simon Stewart at ThoughtWorks developed a superior browser automation tool called WebDriver. In 2009, after a meeting between the developers at the Google Test Automation Conference, 
it was decided to merge the two projects, and call the new project Selenium WebDriver, or Selenium 2.0.
'''
from collections import Counter

# Problem - Find 3rd most repeated text in the string

def most_repeated_words(st, repeat_no):
    """
    Program to find the 3rd most repeated count of words in the string available
    :param st: st as string
    :param repeat_no: repeat_no as string
    :return: List of dict(with strings and counts)
    """
    necessary_list = [] # Assigning the empty list for holding the result
    splitted_texts = st.replace('\"','').replace('\"','').split() # Splitting the string based upon space and by default split() method accept delimiter as space

    # print(sorted(Counter(splitted_texts).items(), key=lambda kv: kv[1]))
    # Counter() method from python Collections library, would return the strings and counts in dictionary/hash map object

    for k,v in Counter(splitted_texts).items():
        if v == repeat_no:
            necessary_list.append({k:v})

    return necessary_list

print(most_repeated_words(st=rec,repeat_no=3)) #Output is ->  [{'Huggins': 3}, {'tool': 3}, {'joined': 3}, {'of': 3}]

