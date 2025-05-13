def create_multiplier(factor):
    
    def multiplier(x):
        return factor * x
    return multiplier

# Example usage:
double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  
print(triple(5)) 