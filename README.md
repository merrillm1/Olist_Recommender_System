# Analysis of the Olist dataset

**Increasing customer sales with a recommendation system**

Using LightFMs recommendation algorithm we were able to achieve a 97% AUROC* for customers.

This was achieved using a hybrid recommendation system that uses collaborative and content based approaches to suggest items, coupled with clustering techniques to introduce customer features into the model. 

## Project Proposal

Olist is an ecommerce website centered in Brazil that empowers small merchants to sell online. Founded in 2016, Olist sought to be the "market of marketplaces" that brings together the fragmented customer base for sellers and merchants. Unlike in the US and China, who have single players dominating the online marketplace, Brazils complex collection of merchants opened an opportunity for Olist to provide a similar service to the region. They provide support to merchants by managing all aspects of product retail from product catelog to payments. For users in Brazil they are able to come to one place to access the diverse marketplaces of the region. However, an immediate challenge in creating such a market is connecting users to the products they are looking for and helping sellers find the right users for their products. The solution to this problem is to implement a recommendation system, which this project will seek to create  [1](https://valorcapitalgroup.com/case-studies/olist-redesigned-the-marketplace-business-model-to-fit-the-realities-of-ecommerce-in-brazil/).

Recommendation systems offer benefits to the user, seller and the mediator of content. They provide users with personalized suggestions that help find items of interest quickly and efficiently. For sellers it helps them find the right user for their product and increases general exposure. Olist recently provided data from 2016 to 2018 from their collection of databases for public use that will allow us to make these connections. Our recommendation system will use a combination of user, product and seller data to give the most relevant suggestions for users with little to no purchase history.

Since Olist is so new, relative to say Amazon which was founded in 1994, they regularly bring on new users and merchants at an increasing volume. This creates major challenges to the process of connecting products to users; without a purchase history it is difficult to know users preferences without asking explicitly. For this reason our best approach will be to create a hybrid recommendation system for its ability to merge collaborative and content based approaches.

Collaborative techniques use user history to suggest items by finding where users preferences overlap. If two users happen to share purchase history for two items, there could be a third item that one user bought that could be recommended to the other. With enough users and purchase history this can be a very effective approach, but unfortunately it does not predict well for new users. Content based filtering techniques can use user information along with item information to suggest based on a number of factors. Combining these two helps to create accurate predictions for current users and relevant predictions for new users. 

The data used is provided by [kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce/data?select=product_category_name_translation.csv) and details all aspects of customer and merchant transactions throughout their database. The data will be loaded from the website onto a local jupyter notebook where I will produce my final product. The final recommender system will be deployed in a docker container for full serverless machine learning deployement.

-------------------

## Links

The work has been broken down in stages and summary slides have been created for a quick look at the results.

* [Data Wrangling and Cleaning](https://github.com/merrillm1/Olist_Recommender_System/blob/master/exploration/1Project_Proposal_and_Cleaning_Steps.ipynb) - Cleaning steps with justification.
* [Exploratory analysis](https://github.com/merrillm1/Olist_Recommender_System/blob/master/exploration/2Exploratory_Analysis.ipynb) - Analysis was conducted to reveal product preferences and seasonal trends in the data.
* [LigthFM recommender system](https://github.com/merrillm1/Olist_Recommender_System/blob/master/exploration/3LightFM_Recommender_System.ipynb) - Implemented lightfms recommender algorithm comparing results with and without clustered user behavior.
* [Clustering with KMeans to determine user groups](https://github.com/merrillm1/Olist_Recommender_System/blob/master/exploration/4Clustering_product_categories.ipynb) - Created 15 groups to place users in for use in LightFM as user features.
* [Spark ALS Recommendation system for comparison](https://github.com/merrillm1/Olist_Recommender_System/blob/master/exploration/5Spark_recommender.ipynb) - Created alternative algortithm for alternate baseline comparison.
* [Summary Slides](https://github.com/merrillm1/Olist_Recommender_System/blob/master/exploration/Increasing_Customer_Loyalty_with_LightFMs_Recommendation%20Algorithm.pdf) Link to ppt

## Author

* [Matthew Merrill](https://www.linkedin.com/in/matthew-merrill-246a1b55/)

## Acknowledgements

* **Dhiraj Khanna** - *Springboard mentor* 
