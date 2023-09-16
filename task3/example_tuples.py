profile = (
    "Niklavs",
    "Eglitis",
    "Student",
    (
        "Informācijas drošības risku pārvaldība",
        "Pitons drošības testētājiem",
        "Pienākumi, tiesības un atbildība internetā",
        "Drošības incidentu pārvaldība"
    )
)

firstname, lastname, role, subjects = profile

print("name: ", firstname)
print("lastname: ", lastname)
print("role: ", role)
print("subjects: ", subjects)

print("First subject: ", profile[3][0])
print("PySec subject index: ", subjects.index("Pitons drošības testētājiem"))

subjectsWithDuplicate = (*subjects, "Pitons drošības testētājiem")

print("Count of PySec subject in new tuple: ",
      subjectsWithDuplicate.count("Pitons drošības testētājiem"))
