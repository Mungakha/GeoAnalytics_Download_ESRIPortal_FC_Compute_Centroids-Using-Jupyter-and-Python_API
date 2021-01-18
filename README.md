#Introduction   
This repository execute the following process flow using the Python API;
   - Download a feature service with given a sepcific feature ID
   - Dissolves the polygon feature downloaded into multipart polygons with common 'PLANTATION','Ops_Code' and write onto portal a new feature collection named 'findcentroids'
   - If successfully written, it extracts the above feature's id and and utilises it to compute the multipart polygon's centroids and saves the outcome on portal as "HealthLyrPolygonToPoint"
   - It gets the above feature's id, doenloads it extrcats the Lat/HealthLyrPolygonToPoint
   - Once complete, the message that was used to trigger this function is saved into another queue named outqueue13.







