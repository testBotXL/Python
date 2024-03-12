language_pref = 'python      '
language_pref1 = 'C#'

print(language_pref+ language_pref1)
print("\n")
print(language_pref.rstrip()+ language_pref1)

#remove whitespace from right side permanently
language_pref = language_pref.rstrip()
print(language_pref+ language_pref1)

#also available lstrip() --> to clear left whitespace
# strip() --> to clear both side whitespace