HP = 100
damage_by_skeleton = 15
damage_by_zombi = 5
damage_by_spider = 40
coef_of_skeleton = 1
coef_pf_zombi = 5
coef_of_spider = 2
result = damage_by_skeleton * coef_of_skeleton + damage_by_spider * \
    coef_of_spider + damage_by_zombi * coef_pf_zombi
if result > HP:
    print("You die!")
else:
    print("You have only", HP-result, "HP")
