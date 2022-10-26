#GÖREV 1 Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız. / Import Titanic dasets
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
"""
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
"""
df = sns.load_dataset("titanic")
df.head()


# GÖREV 2 Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz. / Find the number of male and female passengers 

df["sex"].value_counts()


# GÖREV 3 Her bir sutuna ait unique değerlerin sayısını bulunuz. / Find the unique values for each column

df.nunique()  # değerlerin sayısını veriyor / it gives us  numbers of unique values

df["sex"].unique()  # sex değişkeninin değerlerini gösteriyor / ıt shows the values of the sex variable


# GÖREV 4 pclass değişkeninin unique değerlerinin sayısını bulunuz. / Find the number of unique values of the variable pclass.

df["pclass"].unique()
df.pclass.nunique()

# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz. / Find the number of unique values of pclass and parch variables.

df[["pclass", "parch"]].nunique()

# Görev 6:embarked değişkeninin tipini kontrol ediniz.Tipini category olarak değiştiriniz ve tekrar kontrol ediniz. / Check the "embarked" variables type.  
# Change the type of "embarked" variables as "category"

df[["embarked"]].info()
df["embarked"] = df["embarked"].astype('category')
df.dtypes


# Görev7:embarked değeri C olanların tüm bilgelerini gösteriniz. / Show all information for those with an embarked value equal to C.

df.loc[df["embarked"] == "C"]

# 2. yol
df[df["embarked"] == "C"].head()

# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz. / Show all information for those whose embarked value is not equal to S.

df.loc[df["embarked"] != "S"].head()

# 2. yol

df[~(df["embarked"] == "S")]["embarked"].unique()

# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz. / Show all information for passengers younger than 30 years old and female.

df[df["age"] < 30].head()

df.loc[(df["age"] < 30) & (df["sex"] == "female")].head()  # birden fazla koşul girilmesi durumunda koşulları parantez içerisine almalıyız 
# If more than one condition is entered, we must enclose the conditions in parentheses.


# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz. / Show information for passengers whose Fare is over 500 or 70 years of age.

df.loc[(df["age"] > 70) | (df["fare"] > 500)].head()


# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz. / Find the sum of the null values in each variable.

df.isnull().values.any()  # boş değerler var mı? / is there any null variable?
df.isnull().sum()  # sum of the null values in each variable.


# Görev 12: who değişkenini dataframe’den çıkarınız. / Remove the variable who from the dataframe.

df.drop("who", axis=1).head()


# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz. /
# Fill in the empty values in the deck variable with the most repeated value (mode) of the deck variable.

df["deck"].mode()
df["deck"].mode()[0]
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df.isnull().sum()

2.yol / 2nd way
df["deck"].mode()
df["deck"].fillna(value="C", inplace=True)

# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
df["age"].isnull().sum()
df["age"].fillna(df["age"].median(), inplace=True) # ortanca değeri ile doldurduk
df["age"].median()


# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz. /
# Find the sum, count, mean values of the pclass and sex variables of the survived variable.

df.groupby(["sex", "pclass"]).agg({"survived": ["mean", "sum", "count"]})

# 2. yol / 2nd way

df.pivot_table("survived", "sex", "pclass", aggfunc=["mean", "sum", "count"])


# Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri
#setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız) / 
# Write a function that returns 1 for those under 30, 0 for those equal to or above 30. Using the function you wrote, create a variable named age_flag in the titanic data set.
# (use apply and lambda constructs)

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()


df['age_flag'] = df.loc[:, 'age'].apply(lambda x: 1 if x < 30 else 0)
df.head()

# 2. yol / 2nd way

def changer(age):
 if age < 30:
  return 1
 else:
  return 0

df["age"].apply(lambda age: changer(age))


# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız / Define Tips dataset from Seaborn library
import seaborn as sns
sns.set_theme()
tips = sns.load_dataset("tips")

# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz. /
# Find the sum, min, max and average of the total_bill values according to the categories (Dinner, Lunch) of the time variable.

tips.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]})


# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz /
# Find the sum, min, max and average of total_bill values by days and time

tips.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

# 2. yol
tips.pivot_table("total_bill", "day", "time", aggfunc=["min", "max", "sum", "mean"])

# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz. / 
# Find the sum, min, max and average of the total_bill and tip values of the lunch time and female customers according to the day.

tips.loc[(tips["sex"] == "Female") & (tips["time"] == "Lunch")].groupby("day").agg({
    "total_bill": ["sum", "min", "max", "mean"],
    "tip": ["sum", "min", "max", "mean"]})

"""
# 2. yol / 2nd way

tips[(tips["sex"] == "Female") & (tips["time"] == "Lunch")].groupby("day").agg({"total_bill": ["sum","min","max","mean"],
                                                                           "tip":  ["sum","min","max","mean"],
                                                                            "time" : lambda x:  x.unqiue()})
"""

# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız) / 
# What is the average of orders with size less than 3 and total_bill greater than 10? (use loc function)

tips.loc[(tips["size"]<3) & (tips["total_bill"] >10 )].mean()

# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin. /
# Create a new variable called total_bill_tip_sum. Give the sum of the total bills and tips paid by each customer.

tips["total_bill_tip_sum1"] = tips["total_bill"] + tips["tip"]

#2. yol / 2nd way

tips["total_bill_tip_sum"] = tips.apply(lambda x: x.total_bill+x.tip, axis=1)


# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız /
# Sort from largest to smallest according to the total_bill_tip_sum variable and assign the first 30 people to a new dataframe

new_tips = tips.sort_values("total_bill_tip_sum", ascending=False)[:30]  # ascending in ön tanımlı değeri True şeklindedir. False yapınca büyükten küçüğe sıraladı / 
# The default value of ascending is True. Sorts from largest to smallest when false

new_tips.shape
new_tips.head()

