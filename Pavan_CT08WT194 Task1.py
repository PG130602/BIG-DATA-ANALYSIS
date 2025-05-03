#!/usr/bin/env python
# coding: utf-8

# # BIG DATA ANALYSIS

# # Import Libraries & Create SparkSession

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('ratings_Beauty.csv')


# In[3]:


df.head()


# In[4]:


df.tail()


# ## 2. Schema & Basic Stats

# In[5]:


df.describe()


# In[6]:


df.info


# In[7]:


df.columns


# ## Start Spark Session

# In[8]:


get_ipython().system('pip install pyspark')


# In[9]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark
spark0 = SparkSession.builder.appName("AmazonBeautyAnalysis").getOrCreate()


# In[10]:


from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("AmazonBeautyAnalysis").getOrCreate()
from pyspark.sql.functions import col, avg, count, desc


# In[11]:


file_path = r"C:\Users\gokak\Documents\CODT\ratings_Beauty.csv"  # Update if needed
df = spark.read.csv(file_path, header=True, inferSchema=True)
df.show(5)


# In[12]:


print(f"Total records: {df.count()}")
df.printSchema()


# ## 3. Check for Missing Values

# In[13]:


df.select([col(c).isNull().cast("int").alias(c) for c in df.columns]).groupBy().sum().show()


# In[14]:


df_clean = df.dropna()
print(f"Cleaned record count: {df_clean.count()}")


# In[15]:


df.select([col(c).isNull().cast("int").alias(c) for c in df.columns]).groupBy().sum().show()


# ## 4. Average Rating Per Product

# In[16]:


avg_rating_df = df_clean.groupBy("ProductId").agg(avg("Rating").alias("average_rating"))
avg_rating_df.orderBy(desc("average_rating")).show(5)


# ## 5. Top 10 Most Reviewed Products

# In[17]:


top_reviewed = df_clean.groupBy("ProductId").agg(count("*").alias("review_count"))
top_reviewed.orderBy(desc("review_count")).show(10)


# ## 6. Best Rated Products (with at least 100 reviews)

# In[ ]:


best_rated = df_clean.groupBy("ProductId") \
    .agg(avg("Rating").alias("avg_rating"), count("*").alias("num_reviews")) \
    .filter(col("num_reviews") >= 100) \
    .orderBy(desc("avg_rating"))
best_rated.show(5)


# ##  7. Worst Rated Products (with at least 100 reviews)

# In[ ]:


worst_rated = df_clean.groupBy("ProductId") \
    .agg(avg("Rating").alias("avg_rating"), count("*").alias("num_reviews")) \
    .filter(col("num_reviews") >= 100) \
    .orderBy("avg_rating")
worst_rated.show(5)


# ## ## 8. Most Active Users

# In[ ]:


most_active_users = df_clean.groupBy("UserID").count().orderBy(desc("count"))
most_active_users.show(5)


# ## 9. Average Rating Given by Users

# In[ ]:


user_avg = df_clean.groupBy("UserID").agg(avg("Rating").alias("user_avg_rating"))
user_avg.orderBy(desc("user_avg_rating")).show(5)


# ## 10.Visualizations 

# In[ ]:


ratings_dist = df_clean.groupBy("Rating").count().orderBy("Rating").toPandas() #asin ➝ ProductId  ||| overall ➝ Rating  ||| reviewerID ➝ UserId

# Bar Chart
plt.figure(figsize=(8,5))
plt.bar(ratings_dist["Rating"], ratings_dist["count"], color="skyblue")
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks([1, 2, 3, 4, 5])
plt.grid(axis="y")
plt.show()


# ## 11: Visualization – Worst Rated Products

# In[ ]:


pandas_best_rated = best_rated.toPandas()
pandas_best_rated.plot(kind='bar', x='ProductId', y='avg_rating',
                       title='Top 10 Best Rated Products (≥100 Reviews)',
                       figsize=(10,6), color='green')
plt.tight_layout()
plt.show()


# ## 12: Visualization – Worst Rated Products

# In[ ]:


pandas_worst_rated = worst_rated.toPandas()
pandas_worst_rated.plot(kind='bar', x='ProductId', y='avg_rating',
                        title='Top 10 Worst Rated Products (≥100 Reviews)',
                        figsize=(10,6), color='red')
plt.tight_layout()
plt.show()


# In[ ]:


spark.stop()


# In[ ]:




