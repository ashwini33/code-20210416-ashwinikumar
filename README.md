# Assessment
1. Please download both the file code.py and health_data.json. You can also provide new file in that case please change the argument of function getOverWeightNumber("fileName").
2. Make sure both code and json data is in the same folder.
3. execute the program using 
```bash
>> python3 code.py
```
4.  It will return the number of only overweight people as per specified in question. It will print the table with modified columns and also prints the number of overweight people. Finally, the program exports the modified table in a csv file.

### Example
```bash
ashwini@debian:~/newtest$ git clone https://github.com/ashwini33/code-20210416-ashwinikumar
Cloning into 'code-20210416-ashwinikumar'...
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 9 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (9/9), done.

```
######
```bash
ashwini@debian:~/newtest$ ls
code-20210416-ashwinikumar
```
#######
```bash
ashwini@debian:~/newtest$ cd code-20210416-ashwinikumar/
```
#######
```bash
ashwini@debian:~/newtest/code-20210416-ashwinikumar$ ls
code.py  health_data.json  README.md
```
########
```bash
ashwini@debian:~/newtest/code-20210416-ashwinikumar$ python3 code.py

   Gender  HeightCm  WeightKg     BMI      BMICategory    HealthRisk
0    Male       171        96  32.831  ModeratelyObese    MediumRisk
1    Male       161        85  32.792  ModeratelyObese    MediumRisk
2    Male       180        77  23.765     NormalWeight       LowRisk
3  Female       166        62  22.500     NormalWeight       LowRisk
4  Female       150        70  31.111  ModeratelyObese    MediumRisk
5  Female       167        82  29.402       OverWeight  EnhancedRisk
#################################################################
Number of Over weight people is: 1
```
#####
```bash
ashwini@debian:~/newtest/code-20210416-ashwinikumar$ ls
analysedData.csv  code.py  health_data.json  README.md
```
#####
```bash
ashwini@debian:~/newtest/code-20210416-ashwinikumar$ cat analysedData.csv 
Gender,HeightCm,WeightKg,BMI,BMICategory,HealthRisk
Male,171,96,32.831,ModeratelyObese,MediumRisk
Male,161,85,32.792,ModeratelyObese,MediumRisk
Male,180,77,23.765,NormalWeight,LowRisk
Female,166,62,22.5,NormalWeight,LowRisk
Female,150,70,31.111,ModeratelyObese,MediumRisk
Female,167,82,29.402,OverWeight,EnhancedRisk
ashwini@debian:~/newtest/code-20210416-ashwinikumar$ 
```
