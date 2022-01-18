# Testing

During the code development of each function, tests were in place to be sure that it was running as expected. The following sections describe all tests and error handling in place.

## Testing Plan

Testing will be conducted regularly alongside development of this project. Each User Story will include Unit testing of the code being developed and a manual exploratory test session.

### Sprint 1 - 04/01/2022 - 11/01/2022 (Finished at 09/01/2022)

Unittest were done to ensure all home app functionality were working as expected. 

<img width= "800" src="media/readme/unittests/sprint1/unittest_home_url.jpg">

### Sprint 2 - 09/11/2022 - 16/01/2022

Unittest were done to ensure all products, bag an order functionality developed until this point were working as expected.

+ Functions tested: 

| App | File | Class/Function Name |
|:---:|:---:|:---:|
| Product | Views | boxes |
| Product | Views | product_details |
| Product | Models | Product |
| Product | Models | Box |
| Product | Models | Product_On_Box |
| Cart | Models | cart |
| Cart | Models | updateCart |

+ Products View

<img width= "800" src="media/readme/unittests/sprint2/unittest_views_products.jpg">

+ Products Models Initial

<img width= "800" src="media/readme/unittests/sprint2/unittest_models_products.jpg">

+ Products Models Final

<img width= "800" src="media/readme/unittests/sprint2/unittest_models_products_2.jpg">

+ Products Final All

<img width= "800" src="media/readme/unittests/sprint2/coverage_products_all.jpg">

+ Cart Views

<img width= "800" src="media/readme/unittests/sprint2/unittest_views_cart.jpg">

+ Cart Final All

<img width= "800" src="media/readme/unittests/sprint2/coverage_cart_all.jpg">

+ Sprint 2 Unittest Coverage

<img width= "800" src="media/readme/unittests/sprint2/coverage_all_sprint2.jpg">

### User Stories

<img width= "80%" src="media/Readme/sprints/sprint_1.jpeg">
    
### Unit Tests conducted

Exploratory Test Session Goals

    I want to confirm that the base templates load as expected
    I want to confirm that the homepage load as expected
    I want to confirm that the registration, login and logout works as expected
    I want to confirm that all User Stories are done to my satisfaction
    I want to identify any potential test cases for automation

## Integration Test Case

+ On this project, the Incremental Testing method was used.

 Integrated units were checked after the developer finished writing code for every new feature. This approach was used to find defects early and because it was easy to find the cause of the defect thanks to a step-by-step examination. 

+ The integration tests were divided by features/pages and its described below: 

### **Navbar**

| Test Case Id | Description | Expect result|
|:----:|:----:|:----:|
| 1 | Click login's navbar button | To be directed to the Login Page|
| 2 | A logged User click logout's navbar button | To be logged out and directed to the Home Page|

### **Footer** 

| Test Case Id | Description | Expect result|
|:----:|:----:|:----:|
| 1 | Click on the LinkedIn button| To be directed to the developer's LinkedIn page. |
| 2 | Click on the Github button | To be directed to the developer's GitHub page.|
| 3 | Click on the Facebook button | To be directed to the store Facebook page.|

### **Login**

| Test Case Id | Description | Expect result|
|:----:|:----:|:----:|
| 1 | Enter login credentials and click on the Login button| To be directed to the home page|
| 2 | Enter invalid login credentials and click on the Login button| To be presented to an error message for each invalid field|

### **Register**

| Test Case Id | Description | Expect result|
|:----:|:----:|:----:|
| 1 | Enter all register data and click on the Sign In button| To be directed to the home page, presented to a success message and already logged in|
| 2 | Enter invalid register data in any field and click on the Login button| To be given to an error message|

## Python (PEP8) Validation

###  **PLACEHOLDER App** 

<p float="left">
        <img src="" width="400" height="200" alt=""/>
       
</p>

## HTML Code Validation

All Html pages were validated using W3 tool. 

All results can be foound here

<img src="" width="400" height="200" alt=""/>

## CSS Code Validation

<p float="left">
        <img src="" width="40%" alt="W23C css validation"/>
</p>

## JavaScript Code Validation

### **PLACEHOLDER** 

   <img src= "" width="40%" alt="JShint validation - before"/>
</p>

## Exploratory Testing
========================================================================================

### Initial User Testing (Alpha)

A session was held with an end-user. The feedback obtained is listed below:

### **Response to the user experience test:**

+ 

### Final User Testing (Beta)

On this test, a checklist was developed to guide the user along with all pages and features on the platform. This checklist and the results can be viewed here: 

[Features]() <br>
[Pages]()

### **Response to the user experience test:**

+ 

## Manual Testing
========================================================================================
### Desktop



### Mobile

  Tested with **PLACEHOLDER** 

### WAVE Accessibility validation

**PLACEHOLDER WAVE analysis**
    
<p>
    <img  src="" width="60%" alt="Home Page WAVE Results"/>
</p>

# Unfixed bugs

- 
