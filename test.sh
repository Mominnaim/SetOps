python3 setops.py "set1=a1.txt;set2=b1.txt;operation=intersection"
python3 setops.py "set1=a2.txt;set2=b2.txt;operation=difference"
python3 setops.py "set1=a3.txt;set2=b3.txt;operation=union"
python3 setops.py "set1=a4.txt;set2=b4.txt;operation=intersection"
:'
echo This is A and B testing
python3 SetopsMain.py "set1=a.txt;set2=b.txt;operation=union"
diff result.txt a_b_union.txt
rm result.txt
echo This is C and D difference testing
python3 SetopsMain.py "set1=c.txt;set2=d.txt;operation=difference"
diff result.txt c_d_difference.txt
rm result.txt
echo This is C and D intersection testing
python3 SetopsMain.py "set1=c.txt;set2=d.txt;operation=intersection"
diff result.txt c_d_intersection.txt
rm result.txt
echo This is C and D union testing
python3 SetopsMain.py "set1=c.txt;set2=d.txt;operation=union"
diff result.txt c_d_union.txt
rm result.txt
'