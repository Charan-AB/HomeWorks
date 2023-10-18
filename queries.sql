# sql Queries 

# 1) How many animals of each type have outcomes?

select a.animal_type, count(distinct a.animal_id) from animaldimension a,
animalfact af, outcomedimension o where af.animalkey = a.animalkey 
and af.outcomekey = o.outcomekey and o.outcome_type != 'unknown'
group by a.animal_type ;

# 2) How many animals are there with more than 1 outcome?

select count(animal_id) as animals_morethan_one
from(select a.animal_id from animaldimension a,
animalfact af, outcomedimension o where af.animalkey = a.animalkey 
and af.outcomekey = o.outcomekey and o.outcome_type != 'unknown'
group by a.animal_id having count(*)>1) as query;


# 3) What are the top 5 months for outcomes? 

SELECT month, COUNT(*) as outcome_count
FROM timedimension
JOIN animalfact ON timedimension.timekey = animalfact.timekey
GROUP BY month
ORDER BY outcome_count DESC
LIMIT 5;



# Haven't done 4th and 5th