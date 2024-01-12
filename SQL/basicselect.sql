/*Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.*/

Select * from city where population > 100000 and countrycode = 'USA';

/*Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.*/
SELECT ( (
            SELECT
                COUNT(CITY)
            FROM STATION
        ) - (
            SELECT
                COUNT(DISTINCT CITY)
            FROM STATION
        )
    );

/*Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths 
 (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.*/

select t.city, t.lent
from (
        select
            city,
            len(city) lent
        from station
    ) t
where t.lent in (
        select max(len(city))
        from station
    )
union
select t.city, t.lent
from (
        select
            city,
            len(city) lent
        from station
    ) t
where t.lent in (
        select min(len(city))
        from station
    )
order by lent desc
OFFSET
    0 ROWS FETCH FIRST 2 ROWS ONLY;