#!/bin/bash
#
wget -O ./data/"ds_data_$(date +%Y.%m.%d).txt" https://services.swpc.noaa.gov/text/daily-solar-indices.txt

