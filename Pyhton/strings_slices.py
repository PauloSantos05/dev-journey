google = 'http://www.google.com'
bing = 'http://www.bing.com'
youtube = 'http://www.youtube.com'

name = 'Neo The Matrix'
first_name = name[:3]  # slicing the first three characters
middle_name = name[4:7]  # slicing the middle characters
last_name = name[8:14]  # slicing the last characters

reversed_name = name[::-1]  # reversing the string

# slicing =  slicing is the process of extracting a portion of a string using a specified range of indices. In Python, you can use slicing to create substrings from a larger string. The syntax for slicing is as follows:
# string[start:stop:step]

google_name = google[google.find('www.') + 4:google.find('.com')]
bing_name = bing[bing.find('www.') + 4:bing.find('.com')]
youtube_name = youtube[youtube.find('www.') + 4:youtube.find('.com')]

print('Google name: ', google_name)
print('Bing name: ', bing_name)
print('YouTube name: ', youtube_name)

print('First name: ', first_name)
print('Middle name: ', middle_name)
print('Last name: ', last_name)

print('Reversed name: ', reversed_name)