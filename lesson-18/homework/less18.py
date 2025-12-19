# TASK 1
import pandas as pd

tack = pd.read_csv('tackoverflow_qa.csv')

# 2014 dan oldinlar
tack.loc[tack.creationdate <= '2014-01-01']

#score 50 dan yuqori
tack.loc[tack.score > 50]

#score 50 10 orasida
tack.loc[tack.score.between(50,100)]

# Scott Boston tamonidan javoblar
tack.loc[tack.ans_name == 'Scott Boston']

# faqat shu 5 ta javob bergan savollar
tack.ans_name.value_counts()
users = ['Andy Hayden','Jeff','unutbu','DSM','EdChum']
tack.loc[tack.ans_name.isin(users)]

# loc dateframe qaytaradi (tack.colname) bu esa series qaytaradi 
#qaytgan sereie ni hammasini 1 ta date framga joyladim
result = tack.loc[
    (tack.creationdate.between('2014-03-01','2014-10-31')) &
    (tack.ans_name == 'unutbu') &
    (tack.score < 5)
]
result

# dateFrame loc bn or qilish
result2 = tack.loc[
                    (tack.score.between(5,10)) |
                    (tack.viewcount > 10_000)
                ]
result2

# Scott Boston bumaganlar
tack.loc[tack.ans_name != 'Scott Boston']



#TASK 2
import pandas as pd
titanic = pd.read_csv('titanic.csv')

# clas age va sex si buganlar feltiri
result1 = titanic.loc[
                    (titanic.Pclass == 1) &
                    (titanic.Sex == "female") &
                    (titanic.Age.between(20,30))
                    ]
result1


# 100$ dan kup tulagan pasangerlar
resultt2 = titanic.loc[
                     (titanic.Fare > 100)
                      ]
resultt2

# yolg`iz buganlar
result3 = titanic.loc[
                     (titanic.Survived == 1) &
                     (titanic.SibSp == 0) &
                     (titanic.Parch == 0)
                    ]
result3

# c da va 50 $ kup
result4 = titanic.loc[ 
                     (titanic.Embarked == 'C') &
                     (titanic.Fare > 50)
                    ]
result4

# ota onasi ayoli aka ukasi bn buganlar
result5  = titanic.loc[
                    (titanic["SibSp"] > 0) &
                    (titanic["Parch"] > 0)
                    ]
result5

# 15 yoshdan kichik uylaganlar
result6 = titanic.loc[ 
                    (titanic.Survived == 0) &
                    (titanic.Age <= 15)
                    ]
result6

# kabinasi aniq va 200 dan kup tulaganlar
import numpy as np
result7 = titanic.loc[ 
                    (titanic.Cabin.notna()) &
                    (titanic.Fare > 200)
                    ]
result7

# pas id si toq buanlar 
result8 = titanic.loc[ 
                    (titanic.PassengerId % 2 == 1 ) 
                    ]
result8

# uniq ticketli mijozlar

uniq_t = titanic.Ticket.value_counts() == 1
uniq_t_index = uniq_t.index

result9 = titanic.loc[ 
                    (titanic.Ticket.isin(uniq_t_index))
                    ]
result9

# ayollar
result10 = titanic.loc[
                    (titanic["Sex"] == "female") &
                    (titanic["Name"].str.contains("Miss", na=False)) &
                    (titanic["Pclass"] == 1)
                    ]
result10
