# devopsexam
This is for the devops exam  
web log analyzer

usage :::::::  python3  analyzer.py  "weblogfile path"

The provided Python script will attempt to identify anonymous url entries in Apache web server logs that could indicate the presence of a web shell. The script calculates the URIs successfully handled by the server (status code 200-299) which have been requested by the least number of user agents or IP addresses. This analytic will always produce results regardless of whether a web shell is present or not. The URIs in the results should be verified benign.Then 
