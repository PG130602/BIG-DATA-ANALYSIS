# BIG-DATA-ANALYSIS

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : Pavan Vadiraj Gokak

*INTERN ID* : CT08WT194

*DOMAIN* : Data Analytics

*DURATION* : 8 WEEKS

*MENTOR* : Neela Santhosh Kumar 

# Amazon Beauty Ratings Analysis Using PySpark
This project presents a scalable data analysis pipeline built using PySpark, focusing on user ratings for beauty products sold on Amazon. The main objective is to demonstrate how distributed computing tools like PySpark can efficiently process large datasets, uncovering valuable insights from millions of rows of data. This project also showcases how powerful tools like PySpark can handle complex data processing tasks in a fraction of the time compared to traditional methods.
📁 Dataset Description
 The dataset used is part of Amazon’s open product data series, specifically ratings_Beauty.csv. It consists of customer reviews and ratings for beauty products. The file is quite large, making it ideal for practicing scalable data processing.


# Features:
UserId: Unique identifier for the reviewer.
ProductId: Unique identifier for the product.
Rating: Star rating provided by the user (1 to 5).
Timestamp: Unix timestamp of when the rating was given.


The dataset captures a variety of product interactions and customer feedback patterns that are valuable for marketing, quality assurance, and user engagement analysis. By processing this large dataset with PySpark, we can derive insights that are valuable not only for understanding customer sentiment but also for improving product offerings and sales strategies.

# 🎯 Project Goals
>Load and process a large dataset using PySpark.
>Perform data cleaning and transformation.
>Derive insights such as the most-reviewed or highest-rated products.
>Visualize key findings using simple Python plots.
>Create a recruiter-ready mini-project that demonstrates practical big data skills.
>Highlight the power of distributed computing to handle large datasets efficiently and the ability to derive business-critical insights in real-time.

# ⚙️ Tools & Technologies
>Python 3.x
>Apache Spark (with Hadoop)
>PySpark library
>Jupyter Notebook or .py script
>Matplotlib & Pandas for visualizations

# 🧪 Step-by-Step Breakdown
>Data Loading
The CSV is loaded using spark.read.csv() with the header and schema inference enabled. This avoids memory overhead and is much faster than using pandas for large datasets.

>Cleaning and Preprocessing
Rows with null or missing fields are dropped.
Column names are standardized for consistency.
Data types are confirmed, and conversion is applied if necessary.

>Data Analysis
Basic stats: Total rows and columns.
Top-reviewed products: Using groupBy().count().orderBy().
Most active users: Those who wrote the most reviews.
Average product ratings: Products with a significant number of ratings are considered for fair evaluation.

>Visualization 
Rating distribution pie/bar chart.
Bar chart for top 10 most-reviewed products.
Top-rated and low-rated products with at least 100 reviews.
Most active reviewers visualized for engagement patterns.

# 🔍 Insights Derived
The majority of reviews are positive, suggesting general satisfaction in the beauty category.
A few products receive a disproportionately large number of reviews.
Some users have reviewed hundreds of products—likely power users or influencers.
The lowest-rated products still had significant engagement, indicating potentially controversial or poor-quality items that drew attention.
A key insight was that high ratings don't necessarily correlate with the number of reviews. Some lesser-known products are still highly rated by those who engage with them.

# 🧑‍💻 How to Run
>Install Java JDK 8+ and set JAVA_HOME.
>Download and extract Apache Spark, and set SPARK_HOME.
>Install dependencies: pip install pyspark matplotlib pandas.
>Place ratings_Beauty.csv in the working directory.
>Run the notebook or script cell-by-cell to perform the analysis.

## 👤 Author
This project was created by Pavan Gokak as part of a task for a company “CODTECH IT SOLUTIONS”, showcasing the power of PySpark for large-scale data analysis. It demonstrates how scalable data processing can uncover valuable insights in the e-commerce and beauty industries, emphasizing the importance of data-driven decision-making and the practical application of big data tools in real-world scenarios.

# OUTPUT

![Image](https://github.com/user-attachments/assets/1b027f3c-687c-4342-9be7-aa603ea096c7)
![Image](https://github.com/user-attachments/assets/361ad29a-55d4-4504-90b8-dd7d7d2d0070)
![Image](https://github.com/user-attachments/assets/3f437e8b-6b75-4063-9fb8-7beb7f3f9fa0)

![Image](https://github.com/user-attachments/assets/dae2d705-319e-4dc2-b5eb-6ef58caae59b)
![Image](https://github.com/user-attachments/assets/fc127f68-4cda-4f83-a2b3-ce8fd1468340)
![Image](https://github.com/user-attachments/assets/7b93cfae-de4f-45d9-bdb7-f482016521c2)
![Image](https://github.com/user-attachments/assets/5f28770c-623b-4839-a6b9-df2527c11e08)
