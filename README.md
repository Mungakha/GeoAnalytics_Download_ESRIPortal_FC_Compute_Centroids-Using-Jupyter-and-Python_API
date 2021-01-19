 
This repository executes the following process flow using the Python API;
   - Downloads a feature service with given a specific feature ID
   - Dissolves the polygon feature downloaded into multipart polygons with common 'PLANTATION','Ops_Code' and writes onto portal a new feature collection named 'findcentroids'
   - If successfully written, it extracts the above feature's id and and utilises it to compute the multipart polygon's centroids and saves the outcome on portal as "HealthLyrPolygonToPoint"
   - It gets the above feature's id, downloads it and extrcats the Lat/HealthLyrPolygonToPoint
   - It finishes of by searching and deleting the "HealthLyrPolygonToPoint" and "findcentroids" feature collections







