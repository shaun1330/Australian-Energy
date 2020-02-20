#!/bin/bash

for i in *;
do 
	cd "$i";
	rm *.zip
	cd ../;
done

