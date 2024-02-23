rm result.txt
echo This is test one
python3 setops_1.py "set1=a1.txt;set2=b1.txt;operation=intersection"
diff result.txt result1.txt
rm result.txt
echo This is test two
python3 setops_1.py "set1=a2.txt;set2=b2.txt;operation=difference"
diff result.txt result2.txt
rm result.txt
echo This is test three
python3 setops_1.py "set1=a3.txt;set2=b3.txt;operation=union"
diff result.txt result3.txt
rm result.txt
echo This is test four
python3 setops_1.py "set1=a4.txt;set2=b4.txt;operation=intersection"
diff result.txt result4.txt
rm result.txt
echo This is MY OWN TEST CASE
python3 setops_1.py "set1=myTesting.txt;set2=yourTesting.txt;operation=intersection"
diff result.txt inter_result.txt
