#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sort_collections
import time
import random
# TEST
print("Test: Sort")
int_array = random.sample(list(range(0, 49)), k=49)
print("ソートする配列の数:")
print(len(int_array))
start = time.time()
sort_array = sort_collections.sort(int_array)
print(sort_array)
process_time = time.time() - start
print(process_time)
print("-----------")

int_array = random.sample(list(range(0, 50)), k=50)
print("ソートする配列の数:")
print(len(int_array))
start = time.time()
sort_array = sort_collections.sort(int_array)
print(sort_array)
process_time = time.time() - start
print(process_time)
print("-----------")

int_array = random.sample(list(range(0, 101)), k=101)
print("ソートする配列の数:")
print(len(int_array))
start = time.time()
sort_array = sort_collections.sort(int_array)
print(sort_array)
process_time = time.time() - start
print(process_time)
print("-----------")
