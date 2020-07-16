import sys

liczby_4=open("", "r")    #get data to tests
liczby_8=open("", "r")
liczby_7=open("", "rb")


#----------------------------4 CRAPS TEST---------------------------------
print("CRAPS TEST")
Craps_txt=open("craps_result.txt","a+")
number_to_float_craps=[]
lose = 0
win = 0
throw = 0
throw_tab=[]

for i in liczby_4:
    number_to_float_craps.append(int(float(((float(i)/4294967296)*6)+1)))
for m in range (0,4,1):
    for i in range (0,10000,2):
        throw+=1
        sum = 0
        sum = number_to_float_craps[i]+number_to_float_craps[i+1]

        if(sum==7 or sum==11):
            lose+=1
            if(throw > 21):
                throw_tab.append(throw)
                throw = 0
            else:
                throw_tab.append(throw)
                throw = 0

        if(sum==2 or sum==3 or sum==12):
            win+=1
            if (throw > 21):
                throw_tab.append(throw)
                throw = 0
            else:
                throw_tab.append(throw)
                throw = 0

for x in throw_tab:
    Craps_txt.write(str(x) + "\n")
Craps_txt.write("Liczba gier: 200000" + "\n")
Craps_txt.write("Win counter: " + str(win) + "\n")
Craps_txt.write("Lose counter: " + str(lose) + "\n")
Craps_txt.write("p=win/lose: " + str(win) + "/" +  str(lose) + " = " + str(win/lose) + "\n")
Craps_txt.write("Średnia N*p: " + str((win/lose)*200000) + "\n")
Craps_txt.write("Wariancja N*p(1-p): " + str(((win/lose)*200000)*(1-win/lose)) + "\n")

#----------------------------8 Overlapping Sums Test ---------------------------------

print("Overlapping Sums Test")
Overlapping_txt=open("overlapping_result.txt","a+")

number_to_float_overlapping=[]
result_overlapping=[]

counter=0

for j in liczby_8:
    number_to_float_overlapping.append(float(j)/4294967296)

for x in number_to_float_overlapping:
    sum = 0
    for y in range (0,100):
        sum+=number_to_float_overlapping[counter+y]

    result_overlapping.append(sum)
    Overlapping_txt.write(str(sum)+"\n")
    counter+=1

    if(counter==10000):
        break

#----------------------------7 Count-the-Ones Tests ---------------------------------
print("Count-the-Ones Tests")
Count_the_ones_txt=open("Count_the_ones.txt","a+")

prob_A = 37/256
prob_B = 56/256
prob_C = 70/256
prob_D = 56/256
prob_E = 37/256

int_tab = []
letter_tab = []

mask_32 = 0xFF000000
mask_24 = 0x00FF0000
mask_16 = 0x0000FF00
mask_8 = 0x000000FF

for i in liczby_7:
    int_tab.append(int(i))
for j in int_tab:

    j_8 = j & mask_8
    j_16 = j & mask_16
    j_24 = j & mask_24
    j_32 = j & mask_32

    # 0<A<3
    # B = 3
    # C = 4
    # D = 5
    # 5<E<9

    if(bin(j_8).count("1") <3):
        letter_tab.append("A")

    if (bin(j_8).count("1") == 3):
        letter_tab.append("B")

    if (bin(j_8).count("1") == 4):
        letter_tab.append("C")

    if (bin(j_8).count("1") == 5):
        letter_tab.append("D")

    if (bin(j_8).count("1") > 5):
        letter_tab.append("E")

    if(bin(j_16).count("1") <3):
        letter_tab.append("A")

    if (bin(j_16).count("1") == 3):
        letter_tab.append("B")

    if (bin(j_16).count("1") == 4):
        letter_tab.append("C")

    if (bin(j_16).count("1") == 5):
        letter_tab.append("D")

    if (bin(j_16).count("1") > 5):
        letter_tab.append("E")

    if(bin(j_24).count("1") <3):
        letter_tab.append("A")

    if (bin(j_24).count("1") == 3):
        letter_tab.append("B")

    if (bin(j_24).count("1") == 4):
        letter_tab.append("C")

    if (bin(j_24).count("1") == 5):
        letter_tab.append("D")

    if (bin(j_24).count("1") > 5):
        letter_tab.append("E")

    if(bin(j_32).count("1") <3):
        letter_tab.append("A")

    if (bin(j_32).count("1") == 3):
        letter_tab.append("B")

    if (bin(j_32).count("1") == 4):
        letter_tab.append("C")

    if (bin(j_32).count("1") == 5):
        letter_tab.append("D")

    if (bin(j_32).count("1") > 5):
        letter_tab.append("E")


A = letter_tab.count("A")
B = letter_tab.count("B")
C = letter_tab.count("C")
D = letter_tab.count("D")
E = letter_tab.count("E")

Count_the_ones_txt.write("A: " + str(A) + "\n")
Count_the_ones_txt.write("B: " + str(B) + "\n")
Count_the_ones_txt.write("C: " + str(C) + "\n")
Count_the_ones_txt.write("D: " + str(D) + "\n")
Count_the_ones_txt.write("E: " + str(E) + "\n")


#żeby przedłużyć tablice
letter_tab.append(letter_tab[0])
letter_tab.append(letter_tab[1])
letter_tab.append(letter_tab[2])
letter_tab.append(letter_tab[3])
letter_tab.append(letter_tab[4])

Count_the_ones_txt.write("----------------------------- 5-letter  --------------" "\n")
word_tab = []

for i in range (0,256000):
    word = letter_tab[i]+letter_tab[i+1]+letter_tab[i+2]+letter_tab[i+3]+letter_tab[i+4]
    word_tab.append(word)

print(len(word_tab))

word_count = []
counted = []
for i in word_tab:
    if i not in counted:
        counted.append(i)
        sum = word_tab.count(i)
        word_count.append(i + ": " + str(sum))
        Count_the_ones_txt.write(i + ": " + str(sum) + "\n")



Count_the_ones_txt.write("----------------------------- 4-letter --------------" "\n")


word_tab_4 = []

for i in range (0,256000):
    word_4 = letter_tab[i]+letter_tab[i+1]+letter_tab[i+2]+letter_tab[i+3]
    word_tab_4.append(word_4)

word_count_4 = []
counted_4 = []
for i in word_tab_4:
    if i not in counted_4:
        counted_4.append(i)
        sum = word_tab_4.count(i)
        word_count_4.append(i + ": " + str(sum))
        Count_the_ones_txt.write(i + ": " + str(sum) + "\n")


ideal_prob = []
probability = []
letters = ["A","B","C","D","E"]
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                for e in letters:
                    ideal_prob.append(a + b + c + d + e)

for x in ideal_prob:
    sum_prob = 0
    A = x.count("A")
    B = x.count("B")
    C = x.count("C")
    D = x.count("D")
    E = x.count("E")

    mul_A = prob_A ** A
    mul_B = prob_B ** B
    mul_C = prob_C ** C
    mul_D = prob_D ** D
    mul_E = prob_E ** E


    sum_prob = mul_A * mul_B * mul_C * mul_D * mul_E * 256000
    Count_the_ones_txt.write("Probability " + x + ": " + str(sum_prob) + "\n")

ideal_prob = []
probability = []
letters = ["A", "B", "C", "D","E"]
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                ideal_prob.append(a + b + c + d)

for x in ideal_prob:
    sum_prob = 0
    A = x.count("A")
    B = x.count("B")
    C = x.count("C")
    D = x.count("D")
    E = x.count("E")
    mul_A = prob_A ** A
    mul_B = prob_B ** B
    mul_C = prob_C ** C
    mul_D = prob_D ** D
    mul_E = prob_E ** E


    sum_prob = mul_A * mul_B * mul_C * mul_D *  mul_E * 256000
    Count_the_ones_txt.write("Probability " + x + ": " + str(sum_prob) + "\n")


#----------------------------Close file ---------------------------------
liczby_4.close()
liczby_8.close()
liczby_7.close()
Overlapping_txt.close()
Craps_txt.close()
Count_the_ones_txt.close()
