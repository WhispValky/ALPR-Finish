# Automatic License Plate Recognition App

## Login Page
![Screenshot 2023-06-06 180610](https://github.com/WhispValky/ALPR-Finish/assets/92744133/a6aa7b41-18bf-4f06-96b8-91e363677166)



Open terminal:

Clone repository in your machine:
```
git clone https://github.com/WhispValky/ALPR-Finish.git
```

Change directory to the location:
```
cd ALPR-Finish
```

Create a virtual environment:

For MAC

``` 
python3 -m venv env
```
For Windows
``` 
python -m venv env
```

Start the virtual environment:

For MAC
```
source env/bin/activate
```
For Windows

```
myenv\Scripts\activate
```
Install PIP:
```
python3 -m pip install --upgrade pip
```

Install all imports using requirements.txt
```
pip3 install -r requirements.txt 
```

Before run the server create an account
```
python manage.py createsuperuser
```

Run the server:
```
python manage.py runserver
```


