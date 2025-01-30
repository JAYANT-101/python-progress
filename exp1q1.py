input_str = "programming"
unique_chars = ""
repeated_chars = ""
# Count frequency of each character
char_count = {}
for char in input_str:
 char_count[char] = char_count.get(char, 0) + 1
# Create strings based on the frequency
for char, count in char_count.items():
 if count == 1:
  unique_chars += char
 elif count > 1:
  repeated_chars += char
print("Unique characters:", unique_chars)
print("Repeated characters:", repeated_chars)