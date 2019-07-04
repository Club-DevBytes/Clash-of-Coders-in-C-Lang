#*************************************************************************************************************
#*************************************************************************************************************
#                           Code Checker Customly build for Clash Of Code
#
#
#                                  BY: JAINAL GOSALIYA
#                                  DATE: 04 JULY, 2019
#
#
#**************************************************************************************************************  

class Check_Code():
    def getResults(self):
        values = [] # Un Refactored Original Output stored in this list
        valuesFinal = [] # Refactored Original Output stored in this list
        fetchedResults = [] # Un Refractored user generated outputs stored here
        fetchedResultsFinal = [] # Final Refactored User Generated Output list
        outputCases = open("output.txt", "r")
        for cases in outputCases:
            """Stores the original output in Values"""
            values.append(cases)
        for bitches in values:
            """refactored stored output"""
            valuesFinal.append(bitches.strip())
        userOutput = open("stored_output.txt", "r")
        for outputs in userOutput:
            """Unrefractored user outputs """
            fetchedResults.append(outputs)
        for stripers in fetchedResults:
            """refractored user generated output stored here """
            fetchedResultsFinal.append(stripers.strip())
        length = len(fetchedResultsFinal)
        for items in range(length):
                if fetchedResultsFinal[items] == valuesFinal[items]:
                    pass
                else:
                    raise Exception(
                        "Test Case 0 : failed" + "\n"
                        "YOUR OUTPUT: " + fetchedResultsFinal[items] + "\n"
                        "EXPECTED OUTPUT: " + valuesFinal[items]
                    )
        print("Test Case 0: Passed")
    def getResults1(self):
        values = [] # Original Output stored in this list
        valuesFinal = [] # Refactored Original Output stored in this list
        fetchedResults = [] # Un Refractored user generated outputs stored here
        fetchedResultsFinal = [] # Final Refactored User Generated Output list
        outputCases = open("output1.txt", "r")
        for cases in outputCases:
            """Stores the original output in Values"""
            values.append(cases)
        for bitches in values:
            """refactored stored output"""
            valuesFinal.append(bitches.strip())
        userOutput = open("stored_output1.txt", "r")
        for outputs in userOutput:
            """Unrefractored user outputs """
            fetchedResults.append(outputs)
        for stripers in fetchedResults:
            """refractored user generated output stored here """
            fetchedResultsFinal.append(stripers.strip())
        length = len(fetchedResultsFinal)
        for items in range(length):
                if fetchedResultsFinal[items] == valuesFinal[items]:
                    pass
                else:
                    raise Exception(
                        "Test Case 0 : failed" + "\n"
                        "YOUR OUTPUT: " + fetchedResultsFinal[items] + "\n"
                        "EXPECTED OUTPUT: " + valuesFinal[items]
                    )
        print("Test Case 1: Passed")
    def getResults2(self):
        values = [] # Original Output stored in this list
        valuesFinal = [] # Refactored Original Output stored in this list
        fetchedResults = [] # Un Refractored user generated outputs stored here
        fetchedResultsFinal = [] # Final Refactored User Generated Output list
        outputCases = open("output2.txt", "r")
        for cases in outputCases:
            """Stores the original output in Values"""
            values.append(cases)
        for bitches in values:
            """refactored stored output"""
            valuesFinal.append(bitches.strip())
        userOutput = open("stored_output2.txt", "r")
        for outputs in userOutput:
            """Unrefractored user outputs """
            fetchedResults.append(outputs)
        for stripers in fetchedResults:
            """refractored user generated output stored here """
            fetchedResultsFinal.append(stripers.strip())
        length = len(fetchedResultsFinal)
        for items in range(length):
                if fetchedResultsFinal[items] == valuesFinal[items]:
                    pass
                else:
                    raise Exception(
                        "Test Case 0 : failed" + "\n"
                        "YOUR OUTPUT: " + fetchedResultsFinal[items] + "\n"
                        "EXPECTED OUTPUT: " + valuesFinal[items]
                    )
        print("Test Case 2: Passed")
if __name__=='__main__':
   Check_Code().getResults()
   Check_Code().getResults1()
   Check_Code().getResults2()
