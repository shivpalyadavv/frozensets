# Same as {"a", "b", "c"}
normal_set = set(["a", "b","c"])

print("Normal set")
print(normal_set)

# A Frozen set
frozen_set = frozenset(["e", "f", "g"])

print("\nFrozen Set")
print(frozen_set)

# uncommenting below line would cause error as
# we are trying to add element to a frozen set
# frozen_set.add("h")