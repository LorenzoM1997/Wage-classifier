# created by Lorenzo Mambretti

# function to read the file and normalize the database
# it works only with the "adult" database
def normalize(in_filename, out_filename):

    input_file = open(in_filename,"r")
    output_file = open(out_filename,"w")
    
    for line in input_file:
        
        #the age is a continuous value, so we can convert it directly
        age = (int(line.split(',')[0])-17)/(90-17)
        
        #the education is a continuous value with range from 1 to 16
        education = str((int(line.split(',')[4])-1)/15)
        
        # the sex value is binary so we give 0 to one value and 1 to the other
        sex = line.split(',')[9]
        if sex == " Male":
            sex = "0"
        elif sex == " Female":
            sex = "1"
        
        # since the occupation has 5 classes, we can interpret it as a matrix with 5 entries
        race = line.split(',')[8]
        if race==" White":
            race = "1,0,0,0,0"
        elif race==" Asian-Pac-Islander":
            race = "0,1,0,0,0"
        elif race==" Amer-Indian-Eskimo":
            race = "0,0,1,0,0"
        elif race==" Other":
            race = "0,0,0,1,0"
        elif race==" Black":
            race = "0,0,0,0,1"
           
        # since the occupation variable has 14 classes, we can interpret it as a matrix with 14 entries
        occupation = line.split(',')[6]
        if occupation == " Tech-support":
            occupation = "1,0,0,0,0,0,0,0,0,0,0,0,0,0"
        elif occupation == " Craft-repair":
            occupation = "0,1,0,0,0,0,0,0,0,0,0,0,0,0"
        elif occupation == " Other-service":
            occupation = "0,0,1,0,0,0,0,0,0,0,0,0,0,0"
        elif occupation == " Sales":
            occupation = "0,0,0,0,0,0,0,0,0,0,0,0,0,1"
        elif occupation == " Exec-managerial":
            occupation = "0,0,0,1,0,0,0,0,0,0,0,0,0,0"
        elif occupation == " Prof-specialty":
            occupation = "0,0,0,0,1,0,0,0,0,0,0,0,0,0"
        elif occupation == " Handlers-cleaners":
            occupation = "0,0,0,0,0,1,0,0,0,0,0,0,0,0"
        elif occupation == " Machine-op-inspct":
            occupation = "0,0,0,0,0,0,1,0,0,0,0,0,0,0"
        elif occupation == " Adm-clerical":
            occupation = "0,0,0,0,0,0,0,1,0,0,0,0,0,0"
        elif occupation == " Farming-fishing":
            occupation = "0,0,0,0,0,0,0,0,1,0,0,0,0,0"
        elif occupation == " Transport-moving":
            occupation = "0,0,0,0,0,0,0,0,0,1,0,0,0,0"
        elif occupation == " Priv-house-serv":
            occupation = "0,0,0,0,0,0,0,0,0,0,1,0,0,0"
        elif occupation == " Protective-serv":
            occupation = "0,0,0,0,0,0,0,0,0,0,0,1,0,0"
        elif occupation == " Armed-Forces":
            occupation = "0,0,0,0,0,0,0,0,0,0,0,0,1,0"
            
        # since hours is a countinuous function, we can directly convert it
        # we know the maximum of the function is 99 and the minimum is 1
        hours = (int(line.split(',')[12])-1)/(99-1)
        
        # the wage appears in two different ways in test and train data, so we need a total of 4 controls
        wage = line.split(',')[14]
        if wage == " <=50K.\n":
            wage = "0"
        elif wage == " <=50K\n":
            wage = "0"
        elif wage == " >50K.\n":
            wage = "1"
        elif wage == " >50K\n":
            wage = "1"
        output = str(age)+','+education+','+race+','+occupation+','+sex+','+str(hours)+','+wage+'\n'
        if '?' not in output:
            output_file.write(output) 

    output_file.close()
    input_file.close()

# call the functions in the two different databases
normalize("adult.test.txt","adult_test_norm.txt")
normalize("adult.data.txt","adult_norm.txt")
