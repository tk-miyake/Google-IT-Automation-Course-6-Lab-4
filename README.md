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


