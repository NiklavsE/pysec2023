listOfSubjects = [
    "Informācijas drošības risku pārvaldība",
    "Pitons drošības testētājiem",
    "Pienākumi, tiesības un atbildība internetā",
    "Drošības incidentu pārvaldība",
    "Informācijas drošības risku pārvaldība",
    "Drošības incidentu pārvaldība",
    "Informācijas drošības risku pārvaldība",
]

setOfSubjects = set(listOfSubjects)

differentCourseSubjects = set([
    "Drošības incidentu pārvaldība",
    "Informācijas drošības risku pārvaldība",
    "Interaktivitāte, scenāriju veidošana un intelektuālās spēles",
    "Mobilo tehnoloģiju risinājumi"
])

print("Set of subjects: ", setOfSubjects)

print("Common subjects between courses: ", setOfSubjects & differentCourseSubjects)

print("Different subjects between courses: ", setOfSubjects ^ differentCourseSubjects)

setOfSubjects.update(differentCourseSubjects)

print("All the subjects: ", setOfSubjects)
