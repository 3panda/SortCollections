#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List
import random


sort_size = {
    "small": 50,
    "middle": 100
}


def sort(int_array: List[int]) -> List[int]:
    length = len(int_array)
    if length < sort_size['small']:
        print("bubble_sort")
        sort_array = bubble_sort(int_array)
        return sort_array
    elif length >= sort_size['small'] and length <= sort_size['middle']:
        print("merge_sort")
        sort_array = merge_sort(int_array)
        return sort_array
    elif length > sort_size['middle']:
        print("quick_sort")
        sort_array = quick_sort(int_array)
        return sort_array


def bubble_sort(int_array: [int]) -> List[int]:
    result = int_array
    if len(result) <= 1:
        return result

    for i in range(len(result)):
        # 各要素のループ
        for j in range(len(result)-1):
            # 左の要素のほうが大きかったら要素を入れ替える
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
    return result


def merge_sort(int_array: [int]) -> List[int]:
    result = int_array
    mid = len(result)
    if mid <= 1:
        return result

    if mid > 1:
        left = merge_sort(result[:(mid // 2)])
        right = merge_sort(result[(mid // 2):])
        result = []
        while len(left) != 0 and len(right) != 0:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        if len(left) != 0:
            result.extend(left)
        elif len(right) != 0:
            result.extend(right)
    return result


def quick_sort(int_array: [int]) -> List[int]:
    result = int_array
    left = []
    right = []
    if len(result) <= 1:
        return result

    # データの状態に左右されないためにrandom.choice()を用いる
    ref = random.choice(result)
    ref_count = 0

    for ele in result:
            if ele < ref:
                left.append(ele)
            elif ele > ref:
                right.append(ele)
            else:
                ref_count += 1
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right
