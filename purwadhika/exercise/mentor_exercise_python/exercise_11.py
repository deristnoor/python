# 11
# Buatlah fungsi urai
# print(urai('Code'))
# print(urai('Python'))
# print(urai('Purwadhika'))

# Output:
# CCoCodCode
# PPyPytPythPythoPython
# PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika

def urai(word):
    for i in range(len(word)+1):
        print(word[:i], end = "")
    return

x = 'Python'
urai(x)
