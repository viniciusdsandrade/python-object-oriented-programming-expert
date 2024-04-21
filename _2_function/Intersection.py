from collections import Counter
from typing import List


def intersection_1(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Retorna a interseção entre duas listas. Usando operador de conjuntos.
    """
    return list(set(nums1) & set(nums2))


def insersection_2(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Retorna a interseção entre duas listas. Usando função intersection.
    """
    return list(set(nums1).intersection(nums2))


def intersection_3(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Retorna a interseção entre duas listas. Usando dois ponteiros.
    """
    nums1.sort()
    nums2.sort()
    i, j = 0, 0
    intersection = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            intersection.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return intersection


def intersection_4(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Retorna a interseção entre duas listas. Usando dicionário.
    """
    counts = {}
    for num in nums1:
        counts[num] = counts.get(num, 0) + 1

    intersection = []
    for num in nums2:
        if num in counts and counts[num] > 0:
            intersection.append(num)
            counts[num] -= 1
    return intersection


def intersection_5(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Retorna a interseção entre duas listas. Usando Counter.
    """

    counts1 = Counter(nums1)
    counts2 = Counter(nums2)
    intersection = list((counts1 & counts2).elements())  # Interseção de contagens e extração de elementos
    return intersection


def intersection_6(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Retorna a interseção entre duas listas. Usando filter.
    """
    return list(filter(lambda x: x in nums1, nums2))


def test_intersection():
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    nums2 = [5, 6, 7, 8, 9, 10]

    print("nums1:", nums1)
    print("nums2:", nums2)

    for intersection in [intersection_1, insersection_2, intersection_3,
                         intersection_4, intersection_5, intersection_6]:
        print(intersection.__name__, intersection(nums1, nums2))


def main():
    test_intersection()


if __name__ == "__main__":
    main()
