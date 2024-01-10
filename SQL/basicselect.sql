/*Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.*/

Select * from city where population > 100000 and countrycode = 'USA';

/*Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.*/
SELECT ( (
            SELECT COUNT(CITY)
            FROM STATION
        ) - (
            SELECT COUNT(DISTINCT CITY)
            FROM STATION
        )
    );