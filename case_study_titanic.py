#GÖREV 1 Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
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


# GÖREV 2 Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.

df["sex"].value_counts()

print(f'Veri setimizdeki erkeklerin sayısı{df["sex"].value_counts()[0]} kadınların sayısı {df["sex"].value_counts()[1]}')

# GÖREV 3 Her bir sutuna ait unique değerlerin sayısını bulunuz.

df.nunique()  # değerlerin sayısını veriyor

df["sex"].unique()  # sex değişkeninin değerlerini gösteriyor


# GÖREV 4 pclass değişkeninin unique değerlerinin sayısını bulunuz.

df["pclass"].unique()
df.pclass.nunique()

# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.

df[["pclass", "parch"]].nunique()

# Görev 6:embarked değişkeninin tipini kontrol ediniz.Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.

df[["embarked"]].info()
df["embarked"] = df["embarked"].astype('category')
df.dtypes


# Görev7:embarked değeri C olanların tüm bilgelerini gösteriniz.

df.loc[df["embarked"] == "C"]

# 2. yol
df[df["embarked"] == "C"].head()

# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.

df.loc[df["embarked"] != "S"].head()

# 2. yol

df[~(df["embarked"] == "S")]["embarked"].unique()

# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

df[df["age"] < 30].head()

df.loc[(df["age"] < 30) & (df["sex"] == "female")].head()  # birden fazla koşul girilmesi durumunda koşulları parantez içerisine almalıyız !!!!!!!


# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.

df.loc[(df["age"] > 70) | (df["fare"] > 500)].head()


# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.

df.isnull().values.any()  # boş değerler var mı?
df.isnull().sum()  # boş değerlerin


# Görev 12: who değişkenini dataframe’den çıkarınız.

df.drop("who", axis=1).head()

# df.drop("who", axis=1, inplace=True)
# del df["who"] inplace yapmadan ya da atama yapmaya gerek olmadan silme işlemi

# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.

df["deck"].mode()
df["deck"].mode()[0]
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df.isnull().sum()

2.yol
df["deck"].mode()
df["deck"].fillna(value="C", inplace=True)

# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
df["age"].isnull().sum()
df["age"].fillna(df["age"].median(), inplace=True) # ortanca değeri ile doldurduk
df["age"].median()


# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.

df.groupby(["sex", "pclass"]).agg({"survived": ["mean", "sum", "count"]})

# 2. yol

df.pivot_table("survived", "sex", "pclass", aggfunc=["mean", "sum", "count"])


# Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri
#setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df['age_flag'] = df.loc[:, 'age'].apply(lambda x: 1 if x < 30 else 0)
df.head()

# 2. yol

def changer(age):
 if age < 30:
  return 1
 else:
  return 0

df["age"].apply(lambda age: changer(age))


# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız
import seaborn as sns
sns.set_theme()
tips = sns.load_dataset("tips")

# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.

tips.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]})


# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz

tips.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

# 2. yol
tips.pivot_table("total_bill", "day", "time", aggfunc=["min", "max", "sum", "mean"])

# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.

tips.loc[(tips["sex"] == "Female") & (tips["time"] == "Lunch")].groupby("day").agg({
    "total_bill": ["sum", "min", "max", "mean"],
    "tip": ["sum", "min", "max", "mean"]})

tips[(tips["sex"] == "Female") & (tips["time"] == "Lunch")].groupby("day").agg({
    "total_bill": ["sum", "min", "max", "mean"],
    "tip": ["sum", "min", "max", "mean"]})
"""
# 2. yol
tips[(tips["sex"] == "Female") & (tips["time"] == "Lunch")].groupby("day").agg({"total_bill": ["sum","min","max","mean"],
                                                                           "tip":  ["sum","min","max","mean"],
                                                                            "time" : lambda x:  x.unqiue()})
"""

# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)

tips.loc[(tips["size"]<3) & (tips["total_bill"] >10 )].mean()

# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.

tips["total_bill_tip_sum1"] = tips["total_bill"] + tips["tip"]

#2. yol

tips["total_bill_tip_sum"] = tips.apply(lambda x: x.total_bill+x.tip, axis=1)


# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız

new_tips = tips.sort_values("total_bill_tip_sum", ascending=False)[:30]  # ascending in ön tanımlı değeri True şeklindedir. Yani küçükten büyüğe sıralamalı şeklindedir. False yapınca büyükten küçüğe sıraladı
new_tips.shape
new_tips.head()



def alternating(string):
    new_string = " "

    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
        print(new_string)

 alternating("Ayse")