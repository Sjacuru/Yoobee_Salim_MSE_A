import numpy
def cels_to_fahr():
    temp_list = [18.5, 19.0, 20.0, 25.0, 2.0, 30.0, 13.9]

    temp_list_t = numpy.array(temp_list)
    
    indices = numpy.where(temp_list_t > 20)[0]
    print ("There will be temperature above 20°C on weekdays ",indices, "where \n" \
    "0 represents Sunday and 6 represents Saturday.")

    print ("Temperatures above 20°C are: ", temp_list_t[temp_list_t>20]) 
    #above_20 = temp_list_t > 20 # AI alternative to show elements above 20
    #print ("Temperatures above 20°C are: ", temp_list_t[above_20]) # AI alternative to show elements above 20

    avg = 0 
    total = 0
    for temp in temp_list:
        total += temp
        #total = sum(temp_list) - Alternative
    
    total = numpy.mean(temp_list)
    print ("The average temperature is: ", round(total, 2))
    print ("The highest temperature is: ", round(numpy.max(temp_list),2))
    print ("The lowest temperature is: ", round(numpy.min(temp_list),2))
    i = 0

    for temp_cel in temp_list:
        temp_far = temp_cel * 9/5 + 32
        print ("Temperature in Celsius in ", i, " is :", temp_cel, "=", temp_far, "degrees Fahrenheit")
        i = i + 1

if __name__ == "__main__":
    ans = cels_to_fahr()