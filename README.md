TASK 1. Create a pipeline to fetch the 5 countries (india,us,uk,china,russia) data from Rest API (https://restcountries.com/v3.1/name/{name} here replace the {name} with Country name like https://restcountries.com/v3.1/name/us) and save it in separate file as JSON with File name equal to Country name.
TASK 2. Add the trigger to above pipeline in such a way that it will automatically run two times in a day ( 12:00 AM and 12:00 PM IST) 
TASK 3. Create a pipeline to copy customer data from db to adls only if record count is more than 500. Once a data get copy it should call a child pipeline (which will copy the product data from table if customer record count is > 600). 
TASK 4. Design the pipeline in such a manner that it will pass the Customer pipeline pass the customer count to the child product pipeline via Pipeline parameter.


Project/
fetch_country_data.py  Task 1: API fetch
Task 2 Use Windows Task Scheduler to run fetch_country_data.py twice a day:Trigger at 12:00 AM and 12:00 PM IST
pipeline.py  Task 3 & 4: Customer pipeline with child call
child_pipeline.py  Task 4: Product pipeline
mydb.sqlite  SQLite DB with Customer & Product tables
customer_data.json  Output of pipeline.py
product_data.json  Output of child_pipeline.py
