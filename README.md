# Duplicate Aricles Remover
this tool was developed by python to reduce the number of duplicate articles in the imported from news feed
note in order to work the template of the sheet should be similar to the one used and must include title [TITLE] , summary[SUMMARY] and other field. I have included a template 
the code can also be modified to work on diffrent templates and sheets.

how the algorithm works?  
first it loops over all the articles removing the identicals ones - (the ones with same url and or title)
then it removed the ones the have identical company name, round amount and round curreny.
Final stage is applying SpaCy's similarity method to compare how two text content are similar if similarity is high enough 
the it will be considered duplicated and removed.



#python #Spacy #pandas #NLP #TextAnalysis
