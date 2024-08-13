# Introduction
You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. 
The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). 
The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. 
The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.
You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.
Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs).
Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong.

# What you'll do
  - Write a script that summarizes and processes sales data into different categories
  - Generate a PDF using Python
  - Automatically send a PDF by email
  - Write a script to check the health status of the system

# Working with supplier images
In this section, you will write a Python script named changeImage.py to process the supplier images. 
You will be using the PIL library to update all images within ~/supplier-data/images directory to the following specifications:
  - Size: Change image resolution from 3000x2000 to 600x400 pixel
  - Format : Change image format from .TIFF to .JPEG
      - Note: The raw images from images subdirectory contains alpha transparency layers. So, it is better to first convert RGBA 4-channel format to RGB 3-channel format before processing the images. Use convert("RGB") method for converting RGBA to RGB image.

# Uploading images to web server
You have modified the fruit images through changeImage.py script. Now, you will have to upload these modified images to the web server that is handling the fruit catalog. To do that, you'll have to use the Python requests module to send the file contents to the [external-IP-address]/upload URL.

Copy the external IP address of your instance from the Connection Details Panel on the right side and enter the IP address in a new web browser tab. This opens a web page displaying the text "Fruit Catalog".

In the home directory, you'll have a script named example_upload.py to upload images to the running fruit catalog web server. To view the example_upload.py script use the cat command.

# Uploading the descriptions
The Django server is already set up to show the fruit catalog for your company. You can visit the main website by entering external-IP-address in the URL bar or by removing /media/images from the existing URL opened earlier. 

To add fruit images and their descriptions from the supplier on the fruit catalog web-server, create a new Python script that will automatically POST the fruit images and their respective description in JSON format.

Write a Python script named run.py to process the text files (001.txt, 003.txt ...) from the supplier-data/descriptions directory. The script should turn the data into a JSON dictionary by adding all the required fields, including the image associated with the fruit (image_name), and uploading it to http://[external-IP-address]/fruits using the Python requests library.

Create run.py using the nano editor.

Now, you'll have to process the .txt files (named 001.txt, 002.txt, ...) in the supplier-data/descriptions/ directory and save them in a data structure so that you can then upload them via JSON. Note that all files are written in the following format, with each piece of information on its own line:

  - name
  - weight (in lbs)
  - description

The data model in the Django application fruit has the following fields: name, weight, description and image_name. The weight field is defined as an integer field. So when you process the weight information of the fruit from the .txt file, you need to convert it into an integer. For example if the weight is "500 lbs", you need to drop "lbs" and convert "500" to an integer.

The image_name field will allow the system to find the image associated with the fruit. Don't forget to add all fields, including the image_name!

Iterate over all the fruits and use post method from Python requests library to upload all the data to the URL http://[external-IP-address]/fruits

Now go to the main page of your website (by going to http://[external-IP-address]/) and check out how the new fruits appear.

# Generate a PDF report and send it through email
Once the images and descriptions have been uploaded to the fruit store web-server, you will have to generate a PDF file to send to the supplier, indicating that the data was correctly processed. To generate PDF reports, you can use the ReportLab library. The content of the report should look like this:

  Processed Update on <Today's date>

  [blank line]

  name: Apple

  weight: 500 lbs

  [blank line]

  name: Avocado

  weight: 200 lbs

  [blank line]

  ...

Script to generate a PDF report
Create a script reports.py to generate PDF report to supplier using the nano editor.

Using the reportlab Python library, define the method generate_report to build the PDF reports. We have already covered how to generate PDF reports in an earlier lesson; you will want to use similar concepts to create a PDF report named processed.pdf.

Create another script named report_email.py to process supplier fruit description data from supplier-data/descriptions directory. Use the following command to create report_email.py.

Import all the necessary libraries(os, datetime and reports) that will be used to process the text data from the supplier-data/descriptions directory into the format below:

  name: Apple

  weight: 500 lbs

  [blank line]

  name: Avocado

  weight: 200 lbs

  [blank line]

  ...

Once you have completed this, call the main method which will process the data and call the generate_report method from the reports module.

You will need to pass the following arguments to the reports.generate_report method: the text description processed from the text files as the paragraph argument, the report title as the title argument, and the file path of the PDF to be generated as the attachment argument (use ‘/tmp/processed.pdf')

Once you have completed the report_email.py script. Save the file by typing Ctrl+o, Enter key, and Ctrl+x.

Send report through email
Once the PDF is generated, you need to send the email using the emails.generate_email() and emails.send_email() methods.

Define generate_email and send_email methods by importing necessary libraries.
Once you define the generate_email and send_email methods, call the methods under the main method after creating the PDF report:

Use the following details to pass the parameters to emails.generate_email():
  - From: automation@example.com
  - To: student@example.com
  - Subject line: Upload Completed - Online Fruit Store
  - E-mail Body: All fruits are uploaded to our website successfully. A detailed list is attached to this email.
  - Attachment: Attach the path to the file processed.pdf

Once you have finished editing the report_email.py script, save the file by typing Ctrl+o, Enter key, and Ctrl+x.

Now, check the webmail by visiting [external-IP-address]/webmail. Here, you'll need a login to roundcube using the student as username and password for the password, followed by clicking Login.

Now you should be able to see your inbox, with one unread email. Open the mail by double clicking on it. There should be a report in PDF format attached to the mail. View the report by opening it.

# Health check
This is the last part of the lab, where you will have to write a Python script named health_check.py that will run in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution. Moreover, this Python script should send an email if there are problems, such as:

  - Report an error if CPU usage is over 80%
  - Report an error if available disk space is lower than 20%
  - Report an error if available memory is less than 100MB
  - Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"

Import the necessary Python libraries (eg. shutil, psutil) to write this script.

Complete the script to check the system statistics every 60 seconds, and in event of any issues detected among the ones mentioned above, an email should be sent with the following content:

From: automation@example.com
To: student@example.com
Subject line:
E-mail Body: Please check your system and resolve the issue as soon as possible.

Note: There is no attachment file here, so you must be careful while defining the generate_email() method in the emails.py script or you can create a separate generate_error_report() method for handling non-attachment email.
