# Number Conventer
This code is a web application and is built using a Python web framework called Flask. The purpose of this application is to allow the user to convert a given number to different number systems (binary, hexadecimal, octal or a special number system).

The application consists of a home page and four different pages. The home page directs the user to the conversion process. Other pages perform the conversion process according to the number system type selected by the user.

The Binary, Octal, Heexedecimal, and CustomBase classes are used to perform the conversion. Each page takes the number selected by the user and performs the conversion with the corresponding method of the respective class. The result is kept in the variable named result and displayed in the result.html file.

This application performs the conversion to different number systems using the classes in the conventer.py file. Each class has a method that performs the conversion to the corresponding number system. These methods are named binary_converter, octal_converter, hexedecimal_converter and custom_base_converter.

The application creates HTML templates using Flask's render_template() method. These templates are stored in a folder called templates and contain form fields and buttons for the user to enter the number and display the result.

The Flask framework must be installed for the app to work. After the installation is done, the main.py file is run and a web server running at localhost is started. The user can access the application and perform the conversion by going to localhost via a web browser.
## Flow diagram


                  +-------------+
                  |   index()   |
                  +-------------+
                         |
                         |
                         V
    +-----------------+    HTTP GET    +---------------------+
    |  binary()       | -------------> |  binary.html        |
    +-----------------+                +---------------------+
    | if method = GET | 
    |     return      |                +---------------------+
    | if method = POST| -------------> |  result.html        |
    |   get number    |                +---------------------+
    | convert to int  | 
    | call converter  | 
    +-----------------+ 
            |
            V
      +-------------+
      | hexedeciaml()|
      +-------------+
      | if method=GET|
      |     return   |
      | if method=POST|
      |   get number |
      | convert to int|
      | call converter|
      +-------------+
            |
            V
       +---------+
       | octal() |
       +---------+
       | if GET  |
       |  return |
       |if POST  |
       |get number|
       |convert  |
       |call conv|
       +---------+
            |
            V
    +---------------+
    | customBase()  |
    +---------------+
    | if method=GET |
    |     return    |
    | if method=POST|
    |   get number  |
    |   get base    |
    | convert to int|
    | call converter|
    +---------------+
            |
            V
      +-------------+
      |  result()   |
      +-------------+
      |  return res |
      +-------------+

  In this diagram, we start with a request to the application's home page (index()). There are links on the homepage to direct users to their trading pages. When users click on one of these links (binary(), hexedcimal(), octal() or customBase()), they are directed to the relevant conversion page. When they are redirected to the page, they can see a form on the page. Users need to use this form to enter the number and start the conversion process. After users fill out the form and hit the "Submit" button, the application receives the request and receives the number the user provided. It then sends the number to the appropriate conversion function and gets the result. Finally, the application displays the result in the result.html page. On this page, users can view the converted number.

## UML class diagram

      +---------------+ 1  +---------------+
    |     Flask     |----|     main      |
    +---------------+    +---------------+
                          | + main()      |
                          | + binary()    |
                          | + hexadecimal()|
                          | + octal()     |
                          | + customBase()|
                          +---------------+
    
    +----------------------+      +------------------+
    |    Binary            |      |   Hexadecimal    |
    +----------------------+      +------------------+
    | + binary_converter() |      | + hex_converter()|
    +----------------------|      ------------------+|
    
    +---------------------+       +-------------------------+
    |    Octal            |       |   CustomBase            |
    +---------------------+       +-------------------------+
    | + octal_converter() |       | + custom_base_converter()|
    +---------------------|       -------------------------+|

The application includes two main classes: Flask and main. The Flask class is used to start the Flask application. The main class contains all the Flask routes and related request functions.

Four separate classes namely Binary, Hexadecimal, Octal and CustomBase are used to support the functionality of the application. Each class has a single method that performs the conversion function. These methods are used to convert numbers entered by users into appropriate formats.

Each class is independent of other classes and is called only from the main class. The main class correctly converts the number entered by the user by calling the appropriate class method.

## Install
This file indicates that the application has a dependency on the Flask web framework version and that version will be installed. You can store this file in a separate text file and use the command pip install -r requirements.txt to start the application.

## How Do I Run
    #!bin/bash
    git clone https://github.com/Batuhanaydn/number-conventer.git
    cd number-conventer
    pip install -r requirements.txt
    python main.py

## Follow Me
<p>You can follow me on my social media accounts below:</p><ul><li>GitHub: <a href="https://github.com/batuhanaydn">Batuhanaydn</a></li><li>Twitter: <a href="https://twitter.com/telumak" target="_new">@telumak</a></li><li>LinkedIn: <a href="https://www.linkedin.com/in/batuhan-aydinn/" target="_new">Muhammed Batuhan Ayd??n</a></li></ul><p>You can easily access my articles, projects and posts, follow me and stay in touch with me...</p>
