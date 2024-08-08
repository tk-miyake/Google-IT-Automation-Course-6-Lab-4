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
