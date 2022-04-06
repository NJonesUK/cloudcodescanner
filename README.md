# CloudCodeScanner

Dockerfile for running multiple tools against a load of different terraform repositories at once. Will eventually evolve into something a bit fancier, for now, instructions are below.

* clone this repository
* `cd cloudcodescanner`
* `docker build -t ccs:latest .`
* `sudo docker run -v /path/to/folder/of/terraform/folders:/code -v /where/you/want/the/results:/results -it ccs:latest`$$