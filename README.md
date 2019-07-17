## Fixed issues
1. someone can ask for a password reset email to be send unlimited number of times, if someone put a BOT on that he will probably make continues load on the server to process the continuous requests. a captcha or a limit on the IP address would be nice.
* A captcha is added. ```pip install django-simple-captcha```
2. even when specifying a birth date for the patient we had to input the age ourselves, it should be completed automatically.
* Age is computed from today and birth date and showed in the view page, but removed in the input form.
3. we was allowed to enter a patient with digits as his first and last name, it even allowed a birth date of 1800, it also allowed us to enter 1500kg as his weight.
- Only letters and spaces are allowed in names. Birth date is in the range of 1900/1/1 and today. Weight is in the range of 0-300 kg.
4. when adding scans, we had to select the date of the scan ourselves, some would think that a default value of today's date should be there at the beginning. it also allowed a date of 1/1/1. we were also able to add a scan record with no data and no image just a date.
- Default date is set. Allowed date is between patient's birthday and today. Image is a required field.
5. In adding scans, we were allowed to simply upload a PDF file (your project report), and it will allow uploading any type of files, we just changed the extension of the file to jpg and we were successful in uploading it. we suppose it will allow any size of files too? we didn't check that though.
- Only image file types are allowed. The size limit is decreased from 200MB to 2MB for easy checking.
---

## Installation Guide
1) First, install python3.X (recommended version: 3.6+)

2) Then install python package dependencies
```
pip install Django
pip install Pillow
pip install django-simple-captcha
```
3) Clone this repo

4) You're ready! 
run the following command in website folder:
```
python manage.py runsever
```
Navigate to localhost:8000 

Default user and password:
docy, docy

