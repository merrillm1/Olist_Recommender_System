# Analysis of the Olist dataset

One of the prominent e-commerce sites for sellers in Brazil is OList, a company that connects merchants and their products to the main marketplaces in the country. In order to maintain a balance in the relationship with merchants and customers they must monitor and maintain a number of different areas of their business such as customer satisfaction, product quality, and delivery performance. Being that OList is a relatively new privately owned company that is up and coming in Brazil, one of the most important factors in maintaining their brand reputation and integrity is customer satisfaction. Since OList connects merchants with customers it is important to identify which products in what areas are contributing to high satisfaction. Similarly, they need to monitor areas of low satisfaction and make decisions on how to manage them.

The purpose of my work will be to analyze customer satisfaction and identify what factors contribute to high and low ratings. What are the highest indicators of whether a product will be successful? What areas of the supply chain correlate most to customer satisfaction? How do successful merchants relate to one another, and similarly with unsuccessful ones? What types of products are most prone to polarizing ratings? When are customers more likely to be satisfied with their purchase? My goal is to use exploratory analysis as a starting point to investigate the overall problem of improving customer satisfaction, and by clearly identifying what areas are most important in determining the outcome of a product's success. 

I eventually want to predict customer satisfaction based on clustering techniques that may identify where more complex commonalities may occur. This can be done with scikit- learn's clustering library for grouping through unsupervised means. My approach will be informed by learnings from the exploratory and statistical analysis phases primarily and will use data from customer reviews and ratings along with merchant-ids and detailed product information. 

The data used is provided by [kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce/data?select=product_category_name_translation.csv) and details all aspects of customer and merchant transactions throughout their database. The data will be loaded from the website onto a local jupyter notebook where I will produce my final product. I plan to provide OList with recommendations of where to focus efforts in order to improve customer satisfaction in specific product areas. This will come in the form of a slide deck and code for reproducibility.