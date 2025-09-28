
#%%v
def isValid(s):
    
    # brackets mapping

    brackets_map = {
        ')':'(',
        ']':'[',
        '}':'{'
    }

    open_brackets_stack = []

    for bracket in s:
        if bracket in brackets_map.values():
            open_brackets_stack.append(bracket)
        else:
            # THIS IS A CLOSING BRACKET
            # EACH CLOSING BRACKET HAS TO HAVE A CORRESPONDING OPENING BRACKET
            if not open_brackets_stack:
                return False
            else:
                last_open_bracket = open_brackets_stack.pop()
                if last_open_bracket != brackets_map[bracket]:
                    return False
    return not open_brackets_stack



# TESTING

test1 = "([)]"
test2 = "[()]"
test3 = "("

print("--> ", isValid(test1))
print("--> ", isValid(test2))
print("--> ", isValid(test3))

# %%
