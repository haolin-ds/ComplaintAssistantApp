# Complaint Assistant

## Problem
Every company receives complaints, however, if complaints escalate and are not 
detected timely, it might cause huge money loss. In 2011, a guy sued Bank of 
American asking for 1784 billion, trillion dollars, which is more than the 
GDP of the WHOLE planet.  This ridiculous lawsuit starts just from several 
frustrating phone calls he made to settle some incorrectly deposited checks. 
Except for these extreme case, complaint escalation might make 
you company lose your customer or ruin your reputation.  There is a study 
showing 58% customers will never use the company again after a negative 
experience, 49% will tell their friends not to use the business, and 34% will 
post a review online or share a poor experience on social media.  

## Solution
This is a web app to help companies using their historical customer complaints to 
predict complaint escalation and adopt better response type.  It is leveraged by 
machine learning and natural language processing (NLP) techniques. The website is 
[Complaint Assistant](http://complaintassistant.best), developed using Flask and 
is deployed on Amazon Web Service (AWS). If you want to understand the machine learning
 model used, please refer to the kernel repository [Complaints Analysis](https://github.com/atuSpirit/ComplaintsAnalysis)

## Website
[http://complaintassistant.best](http://complaintassistant.best)

## Historical Data Used
The historical data used to build the app are more than 16K consumer complaints about
financial products and services in [Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/search/?from=0&searchField=all&searchText=&size=25&sort=created_date_desc) 
in US government website. 

## What can Complaint Assistant do?
When a complaint narrative is entered in the website, the product category that the complaint
is about will be reported. If there is a chance of escalation, a WARNING will be given. Also, 
the probabilities of escalation adopting different response type will be illustrated in a 
figure.  The web app will suggest a response type.  The suggested response type is the response
type with maximum probability of escalation under a given threshold(currently 0.35).  I didn't 
use the response with lowest escalation probability as suggested response types, because 
"Money Relief" is always the winner.  However, "Money Relief" has more cost than other 
response type for a company. Later, I will consider the cost of response type in my model. 
![Website Example](static/img/website_view.png)

