/*
Find all searches for accommodations with an equal number of bedrooms bathrooms
*/

select * 
from airbnb_search_details 
where bathrooms = bedrooms;
