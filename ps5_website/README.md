# PS5 Website

An unofficial fan website which shows an index with basic options, games both old and new with working account system and games cart(with add and remove game function)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

[Python](https://www.python.org/downloads/), Virtualenv, Flask and [sqlite3](https://www.sqlite.org/download.html)

```
pip3 install virtualenv flask
```

### Installing

* Clone this file to your system
* Run app.py 

## Modifying

In order to change the ip address and port, go to line 147 in app.py and change it to
```
if __name__ == '__main__':
    app.run(debug=False, ip="your_ip", port="your_port")
```
You can make your website available in LAN through port forwarding.


## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [Pycharm](https://www.jetbrains.com/pycharm/) - IDE used




## Authors

* **Tanush R** - [tanushmal](https://github.com/tanushmal)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.



## Acknowledgments

* This project was made as an assignment for Rapidd Academy class

