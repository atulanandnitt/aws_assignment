# aws_assignment


#Requirement:

Multiple json files ( having data in nested structure) getting copied in a particular bucket in s3 of aws.Each json file may have different number of records.This python code parse newly came json files and add these data into separate Excel files and store at different s3 bucket of aws.

json data files are stored at #atul-bucket-1-input-json-files. and after processsing converted data in csv should be stored at bucket name :  #atul-bucket-1-output-csv-files

All Json file need to be processed once only.Rows of the excel data should not be repeated.

#Approach: 

Step 1 : create a lambda handler to keep checking bucket #atul-bucket-1-input-json-files.

Step 2 : Whenever a new json files get copied in #atul-bucket-1-input-json-files, its should be copied in s3 local machine.

Step3: with the help of function: jsonToCsv()  the json file get converted into csv.

Step4: copy this new csv file to bucket:  #atul-bucket-1-output-csv-files
