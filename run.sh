#!/bin/bash



function AddZabbix() {
    cd zabbix
    python init.py
    cd ..
}


AddZabbix
