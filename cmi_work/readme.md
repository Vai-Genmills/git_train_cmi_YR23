
To build the audience propensity model, we need a comprehensive dataset at the user level that captures purchase history. This includes not only transactional data but also details about the products they buy, the attributes of these products, demographic information, and the profiles of the stores they visit. The dataset should cover a sufficient time period to enable accurate predictions about future purchases. In this case, we use at least one year of data to capture patterns over 12 months.


From this model, we extract valuable insights and features to understand the driving factors behind purchases, product affinity, and basket economics. These insights help us to comprehend what influences customer behavior and preferences.

For customer data, we use Fetch as our primary source, which acts as first-party proxy data. Additionally, we incorporate data from Nielsen's source to extract product attributes and taxonomy which provides a holistic view of the products and their characteristics.

We also leverage the Opportunity Cluster data, which lists the claims associated with each product. This information is crucial in building a comprehensive audience 360 view by understanding the role of attributes like calorie consciousness, heart health, and allergens,etc in shaping customer food choices.



## Data Sources


<table>
  <tr>
    <th>Source</th>
    <th>Project ID</th>
    <th>Schema</th>
    <th>Table ID</th>
    <th>Short Descriptoion</th>
  </tr>
  <tr>
    <td rowspan="2"><strong>Nielsen</strong></td>
    <td rowspan="2">edw-prd-e567f9</td>
    <td rowspan="2">syndicated_nielsen</td>
    <td>nielsen_tsr_pos_us_dim_product </td>
    <td>Leveraging the total store report on Food and Beverage product taxonomy from a nationwide retail grocery industry perspective</td>
  </tr>
  <tr>
   <td>dim_nielsen_connect_pos_us_product </td>
  <td>Leveraging the GMI product taxonomy </td>
  </tr>
  <tr>
    <td rowspan="3"><strong>Nielsen</strong></td>
    <td rowspan="3">edw-prd-e567f9</td>
    <td rowspan="3">syndicated_data</td>
    <td>dim_nielsen_precision_area_us_purchase_power</td>
    <td>precision area data</td>
  </tr>
  <tr>
    <td>nielsen_precision_area_us_demographics_fact</td>
    <td>precision area data Demographics</td>
  </tr>
  <tr>
    <td>dim_nielsen_precision_area_us_life_stages</td>
    <td>precision area data life stage</td>
  </tr>

  

  
  <tr>
    <td rowspan="3"><strong>Fetch</strong></td>
    <td rowspan="3">edw-prd-e567f9</td>
    <td rowspan="3">cdf</td>
    <td>dim_fetch_user</td>
    <td>User Level Fetch Data</td>
  </tr>
  <tr>
    <td>fetch_rewards_receipt_fact</td>
    <td>Receipt Level Data bought by users - Store, Store Address, Receipt Total $ and item count</td>
  </tr>
  <tr>
    <td>fetch_rewards_receipt_item_fact</td>
    <td>Item level Data listed on Receipts - Product description, Item cost and Quantity, Points associated</td>
  </tr>


  
</table>


## Derived Sets

<table>
  <tr>
    <th>Source</th>
    <th>Project ID</th>
    <th>Schema</th>
    <th>Table ID</th>
    <th>Short Descriptoion</th>
  </tr>
  <tr>
    <td rowspan="2"><strong>Nielsen</strong></td>
    <td rowspan="2">edw-prd-e567f9</td>
    <td rowspan="2">syndicated_nielsen</td>
    <td>nielsen_tsr_pos_us_dim_product </td>
    <td>Leveraging the total store report on Food and Beverage product taxonomy from a nationwide retail grocery industry perspective</td>
  </tr>
  <tr>
   <td>dim_nielsen_connect_pos_us_product </td>
  <td>Leveraging the GMI product taxonomy </td>
  </tr>
  <tr>
    <td rowspan="3"><strong>Fetch</strong></td>
    <td rowspan="3">edw-prd-e567f9</td>
    <td rowspan="3">cdf</td>
    <td>dim_fetch_user</td>
    <td>Leveraging the total store report on Food and Beverage product taxonomy from a nationwide retail grocery industry perspective</td>
  </tr>
  <tr>
    <td>fetch_rewards_receipt_fact</td>
    <td>Leveraging the total store report on Food and Beverage product taxonomy from a nationwide retail grocery industry perspective</td>
  </tr>
  
  <tr>
    <td>fetch_rewards_receipt_item_fact</td>
    <td>Leveraging the total store report on Food and Beverage product taxonomy from a nationwide retail grocery industry perspective</td>
  </tr>
</table>





End-to-End Steps:
## Table of Contents
1. [Section 1: Introduction](#section-1-introduction)
2. [Section 2: Installation](#section-2-installation)
3. [Section 3: Usage](#section-3-usage)

## Section 1: Introduction
[Link to Introduction file](https://github.com/your-repo/your-project/blob/main/docs/introduction.md)

<details>
  <summary>Details about Introduction</summary>
  This section provides an overview of the project, its purpose, and its main features.
</details>

## Section 2: Installation
[Link to Installation file](https://github.com/your-repo/your-project/blob/main/docs/installation.md)

<details>
  <summary>Details about Installation</summary>
  This section describes the steps needed to install the project, including system requirements and dependencies.
</details>

## Section 3: Usage
[Link to Usage file](https://github.com/your-repo/your-project/blob/main/docs/usage.md)

<details>
  <summary>Details about Usage</summary>
  This section explains how to use the project, with examples and command descriptions.
</details>



[Audience generation File] (https://github.com/gmi-common/marketing-pma-dna-gcp/blob/main/dbt/models/output/audience/audience_seed.sql)
 
<details><summary><b> 1. Audience generation </b></summary>

</details>
  1. 
2. ML data preparation - [02.ml_data_preparation.ipynb](02.ml_data_preparation.ipynb).
3. ML data preprocessing - [03.ml_data_preprocessing.ipynb](03.ml_data_preprocessing.ipynb).
4. ML model training - [04.model_training.ipynb](04.model_training.ipynb).
5. ML model evaluation and diagnostics - [05.model_evaluation_and_diagnostics.ipynb](05.model_evaluation_and_diagnostics.ipynb).
6. Media experiment design - [06.media_experiment_design.ipynb](06.media_experiment_design.ipynb).
