- <a href="#Performance-Marketing-Objectives">What is Performance Marketing and its objectives?</a>

# Performance Marketing Acceleration

<img src=/images/PMA_Flow.jpg>

## Table Of Content

- [What is Performance Marketing and objectives?] (#Performance-Marketing-Objectives)
- [Methodology & Framework] (#Methodology-&-Framework)
- [Embeddings Process] (#Embeddings-Process)
- [Embedding Repositoiry] (#Embedding-Repositoiry)
- [License] (#License)
- [References] (#References)

- [References](#References)


## Performance Marketing Objectives
A strategic marketing approach using digital marketing ads targeted to audiences who have higher response rates for brand/category via personalized campaigns and messaging. In the long run, our goal is to reduce Cost Per Acquisition (**CPA**) and raise Return On Investment (**ROI**)/ Return on advertising spend (**ROAS**).

#### Objective: 

To Increase conversion Per customer
  - **Penetration Rate**: Buy new segment.
  - **Buy Rate**: Increase frequency/size/count of an already purchased segment.
  
## Methodology & Framework:
<img src=/images/Model_Framework.jpg>

Exploring huge, diverse sources of raw data in order to find patterns, obtain insights, and inform smart marketing decisions is one of the key objectives of marketing data analytics.

Over here we face a challenge of going through the path of building & executing analytical journey for each and very brand/category/segment resulting in logging more resources in terms of manpower hours and computational costs.

We adopt to have a centralized 360-degree picture of a customer and use it for downstream brand/category/segment specific model objectives together with its own special features in order to scale and smooth the process.

We create this consumer profile using embeddings and the various dimensions they offer:
  **Numeric Embeddings**:
   - Purchase Metrics (Visits, spend, etc.) across product taxonomy and stores. 
   - Preferred Store 
   - Precision Area Demographics
  **Text Embeddings**:
   - Most visited Location (state)
   - Top # Product-UPC Purchased 
   - Top # Associated opportunity clusters
   - Recently # shopped Baskets’ Product Description 

**Embeddings results in a dense representation** in which similar entities (store, location, products, customers) have a similar encoding.
Using embeddings to reduce feature/dimensionality and computing needs is made possible by the aforementioned approach.

All the above embeddings concatenated on user level can be stored therefore every user is represented by vectors (arrays of continuous numbers)  
 
| user embeddings e.g.  |                                                                                                                                                                                                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  user1 ==>  |[0.32,0.27,0.83,0.12………………………..,0.64] |
|  user2 ==>  |[0.30,0.47,0.63,0.77………………………..,0.39] |
|  user3 ==>  |[0.11,0.58,0.66,0.45………………………..,0.82] |

Mathematical operations can be performed on above numbers.

We benefit from this representational form in a number of use scenarios.
 - Used as features for downstream models like Propensity Modeling
 - Lookalike Modeling
 - Recommendation systems

## GCP Architecture
<img src=/images/GCP_Architecture.jpg>


## Embeddings Process
  •	**Numeric Sparse Features Embedding**: Done via Autoencoder which is a type of neural network where the inputs and outputs are the same but in the hidden layer (the “embedding”) the dimensionality is reduced in order to get a more dense representation of the data.
  <img src=/images/autoencoder.jpg>

  •	**Store Embedding**: Done via Keras Embedding layer is only a "simple" layer in a neural network. You can imagine it as a dictionary where a category (i.e word) is represented as a vector (list of numbers). The value of the vectors are defined by backpropagating the errors of the network. 
  
  •	**Product Purchased & Associated Opportunity Clusters**: Used Word2vec that contains only 1 hidden layer but the inputs are the neighborhood words and the output is the word itself (or the other way around). 
 <img src=/images/PMA_Prod_desc_embeddings.gif>



## Embedding Repositoiry
```
.
├── train
│   └── train.py (main execution file)
├── sql (all of the SQL data definition language (DDL) used )
├── utils (function /modules)
│   ├── utils.py (Data extract, embedding functions)
    ├── store (preferred store embeddings)
    ├── location (Most Frequented Location (State) pretrained embeddings)
    ├── Purchase history (embeddings of avg visits & vpend across nielsen categories )
    ├── upc (embeddings of top 20 products)
    ├── opp.cluster (embeddings of top 20 asscoiated clusters)
    ├── basket products (embeddings of Last 3 Shopping Baskets’ Receipt Product Description )
    ├── demographics (embeddings of precision area demographic variables )
├── README.md (this file!)
```


## License
 <img src=/images/Fetch-ScreenCapture_compressed_gif.gif>
## References
