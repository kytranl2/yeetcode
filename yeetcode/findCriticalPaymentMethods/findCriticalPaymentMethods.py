def find_critical_payment_methods_v2(groups, target_reduction):
    # Step 1: Aggregate payment methods across groups
    payment_method_usage = {}
    for group_name, methods in groups.items():
        for method in methods:
            if method not in payment_method_usage:
                payment_method_usage[method] = set()
            payment_method_usage[method].add(group_name)

    # Step 2: Calculate total unique payment methods
    total_methods = sum(len(groups[group_name]) for group_name in groups)

    # Step 3: Find critical payment methods
    critical_methods = []
    current_methods = total_methods
    sorted_methods = sorted(payment_method_usage, key=lambda x: len(payment_method_usage[x]), reverse=True)

    for method in sorted_methods:
        reduction_count = len(payment_method_usage[method])
        current_methods -= reduction_count
        critical_methods.append(method)
        current_reduction = 100 * (total_methods - current_methods) / total_methods
        if current_reduction >= target_reduction:
            break

    # Step 5: Return the list of critical payment methods
    return critical_methods
# Example Usage
groups = {
    "Group 1": ["Payment Method A", "Payment Method B"],
    "Group 2": [],
    "Group 3": ["Payment Method B"]
}

# Test for 50% reduction
result_50_v2 = find_critical_payment_methods_v2(groups, 50)

# Test for 80% reduction
result_80_v2 = find_critical_payment_methods_v2(groups, 80)

print(result_50_v2, result_80_v2)



