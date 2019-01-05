import boto3;

print("Hello from Python");
name = 'Shad';
print('My Name is {}'.format(name));

tpl=(40,50,60,"XYZ", 40);
print(tpl);
print(tpl[3]);
print(tpl * 3);
print(tpl.count(40));

mylist = [23,55,64,67,21,43];
print(type(mylist))
print(mylist);

#convert list to an tuple
tpl2 = tuple(mylist)
print(type(tpl2))
print(tpl2)

#Convert  list to an byte array
b = bytes(mylist)
print(type(b))

b1 = bytearray(mylist)
print(type(b1))
print(b1)


#Set demo - exclude the duplicate items;
s={10,20,15,35,20, 'XYZ', 10,15}
print('Set: {}'.format(s))
print(type(s))


#Dictionary type
dict = {1:"John", 2:"Smith", 3:"Bob"}
print('Dictionary: {}'.format(dict))

print(dict.items())
print(dict.keys())
print(dict.values())

#Let's use Amazon S3
#s3 = boto3.resources('s3');
#Print out bucket names
#for bkt in s3.bucket:
#    print(bkt);

