import copy, random, datetime
suppliesDataSets = [
    [
        {
            "labels": [], #food
            "data": []
        },
        {
            "labels": [], #drink
            "data": []
        },
        {
            "labels": [], #medicine
            "data": []
        }
    ]
]
now = datetime.datetime.now()
for i in range(3):
    for j in range(42):
        t_ = (now + datetime.timedelta(days=-j)).strftime('%Y-%m-%d')
        suppliesDataSets[0][i]["labels"].append(t_)
        k = random.randint(0, 200)
        suppliesDataSets[0][i]["data"].append(k)
for i in range(8):
    cloned_ = copy.deepcopy(suppliesDataSets[0])
    suppliesDataSets.append(cloned_)