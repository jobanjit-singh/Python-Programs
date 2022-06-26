# import pickle
# f= open("abc1.txt","wb")
# row = [9,32,"joban"]
# pickle.dump(row,f)
# # f.close()
# Example for pickle load
import pickle

dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }

filename = 'dogs'

infile = open(filename,'rb')

new_dict = pickle.load(infile)

infile.close()

print(new_dict)

print(new_dict==dogs_dict)

print(type(new_dict))