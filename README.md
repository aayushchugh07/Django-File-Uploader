Django-File-Uploader
====================

<p> <strong> A basic file uploader built using django, covering all essential functionalities in the backend. </strong> </p>
To try, follow these simple steps: <br />
1. Checkout the source code ( git clone https://github.com/aayushchugh07/Django-File-Uploader ) <br />
2. Make sure you have django installed <br />
3. Change the directory to mysite (cd mysite). current directory should be mysite only, this is essential. <br />
4. Run the server ( python manage.py runserver ). <br /> <br />

<a href="http://localhost:8000/signin.html" >To see the UI, visit http://localhost:8000/signin.html </a> <br /> <br />

You will see the website with options to upload/download  login page and the file upload/download feature. All the parts are coded to be authenticated and secured.
<br /> <br />

Features:
<ul> 
  <li> Use django for templates. These are found in mysite/templates/fileapp/ </li>
  <li> Use sqlite for database storage. These will store Users and Files </li>
  <li> Passwords are hashed and salted </li>
  <li> Mantain session for each user, to track users </li>
  <li> Verify ownership of file, before serving file names or the file itself </li>
  <li> Most of the application logic can be found in mysite/fileapp/views.py </li>
</ul>
