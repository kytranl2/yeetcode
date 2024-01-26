def find_max_copies_after_updates(updates):
    inventory = {}
    max_count = 0
    max_counts = []
    max_count_bug = None  # Track the bug ID with the current max count

    for update in updates:
        if update > 0:  # Adding a bug
            inventory[update] = inventory.get(update, 0) + 1
            # Update max_count and max_count_bug if necessary
            if inventory[update] > max_count:
                max_count = inventory[update]
                max_count_bug = update
        else:  # Removing a bug
            if -update in inventory:
                inventory[-update] -= 1
                if inventory[-update] == 0:
                    del inventory[-update]
                # Find the new max count if the current max count bug is removed or its count is reduced
                if -update == max_count_bug and (inventory.get(max_count_bug, 0) < max_count):
                    if inventory:
                        max_count = max(inventory.values())
                        max_count_bug = max(inventory, key=inventory.get)  # Update max_count_bug
                    else:
                        max_count = 0
                        max_count_bug = None

        max_counts.append(max_count)

    return max_counts

# Retest with the corrected code
updates = [1,2,-1,2]
print(find_max_copies_after_updates(updates))

updates1 = [6,6,-6,-2,-6]
print(find_max_copies_after_updates(updates1))