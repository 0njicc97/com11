print("howmany apples should I remove")
apples_to_remove = int(input())

apples_removed = 0


print()

while apples_removed < apples_to_remove:
    apples_to_remove = apples_to_remove - apples_removed
    print("apples_to_remove")
    apples_removed = apples_to_remove + 1

