#!/bin/bash

for i in *;
do 
	cd "$i";
	for j in *.zip;
	do 
		unzip "$j" -d "${j%%.zip}";
	done
	cd ../;
done

