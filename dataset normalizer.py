def normalize(in_filename, out_filename):

    input_file = open(in_filename,"r")
    output_file = open(out_filename,"w")
    
    for line in input_file:

        age = (int(line.split(',')[0])-17)/(90-17)
        education = str((int(line.split(',')[4])-1)/15)
        occupation = line.split(',')[6]
        
        sex = line.split(',')[9]
        if sex == " Male":
            sex = "0"
        elif sex == " Female":
            sex = "1"
            
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
        hours = (int(line.split(',')[12])-1)/(99-1)
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

normalize("adult.test.txt","adult_test_norm.txt")
normalize("adult.data.txt","adult_norm.txt")
