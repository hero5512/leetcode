# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:58:40 2017

@author: Crystal
"""

awk '
{
    for (i = 1; i <= NF; i++) {
        if(NR == 1) {
            s[i] = $i;
        } else {
            s[i] = s[i] " " $i; 
        }
        print s[i]
        print i
    }
}
END {
    for (i = 1; s[i] != ""; i++) {
        print s[i];
    }
}' file.txt