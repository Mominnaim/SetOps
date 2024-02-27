rm result.txt
echo This is test one
node Jay_js.js "set1=a1.txt;set2=b1.txt;operation=intersection"
cmp result.txt result1.txt
rm result.txt
echo This is test two
node Jay_js.js "set1=a2.txt;set2=b2.txt;operation=difference"
cmp result.txt result2.txt
rm result.txt
echo This is test three
node Jay_js.js "set1=a3.txt;set2=b3.txt;operation=union"
cmp result.txt result3.txt
rm result.txt
echo This is test four
node Jay_js.js "set1=a4.txt;set2=b4.txt;operation=intersection"
cmp result.txt result4.txt
rm result.txt
