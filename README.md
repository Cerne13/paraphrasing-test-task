# Syntactic tree paraphrasing project

## Installing the app
* Use your terminal and create a local repository in any folder using command
```commandline
git init
```
* Clone the app:
```commandline
https://github.com/Cerne13/paraphrasing-test-task.git
```

* Move to the created folder that contains the app

<br/>

#### If you are using Linux/Mac:
First check if you have virtualenv installed:
```commandline
virtualenv --version
```
If you don't get version, you'll need to install the module:
```commandline
pip3 install virtualenv
```

* Create the environment
```commandline
python3 -m venv venv
```

* Activate it
```commandline
source venv/bin/activate
```

* Install all the needed dependencies:
```commandline
python -p install requirements.txt
```
<br/>

#### If you are on Windows:
* Create virtual environment by entering:
```commandline
python -m venv venv
```

* Activate the environment:
```commandline
venv\Scripts\activate
```

* Install all the needed dependencies:
```commandline
python -p install requirements.txt
```

## Launching and using the app
To start the server, enter the following in the command line while inside the project's root folder:
```commandline
uvicorn main:app --reload
```
Enter the following into your browser:
```commandline
http://localhost:8000/docs
```
You will see Swagger autogenerated documentation with one endpoint.

### Rephrasing the tree using Swagger
* open your /paraphrase endpoint
* click 'Try it out'
* enter your syntactic tree, i.e:
```commandline
(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP
Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP
(JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ
trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS
restaurants) ) ) ) ) ) ) )
```
* (optionally) set the limit
* click 'Execute'

### Rephrasing the tree using your browser address line and query parameters

##### If you prefer to use this method, a browser plugin like JSON Viewer for Chrome or any analogue is recommended for better results readability.

* Enter the endpoint's address with all the needed query parameters into your browswer's address line, i.e:
```commandline
127.0.0.1:8000/paraphrase?tree=(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP
Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP
(JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ
trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS
restaurants) ) ) ) ) ) ) )
```
optionally you can add the limit query parameter at the end of the address, after the syntactic tree i.e:
```commandline
&limit=20
```
<br/>
In both cases a result you'll get will be a JSON object with rephrases of the syntactic tree you've provided.
