#*************************************************************************************************************
#*************************************************************************************************************
#                           Code Checker Customly build for Clash Of Code
#
#
#                                  BY: JAINAL GOSALIYA
#                                  DATE: 04 JULY, 2019
#
#
#*************************************************************************************************************  

class Check_Code():
    def getResults(self):
        values = [] # Original Output stored in this list
        fetchedResults = [] # Un Refractored user generated outputs stored here
        fetchedResultsFinal = [] # Final Refactored User Generated Output list
        outputCases = open("output.txt", "r")
        for cases in outputCases:
            values.append(cases)
        """Stores the original output in Values"""
        userOutput = open("stored_output.txt", "r")
        for outputs in userOutput:
            fetchedResults.append(outputs)
        """Unrefractored user outputs """
        for stripers in fetchedResults:
            fetchedResultsFinal.append(stripers.strip())
        """refractored user generated output stored here """
        length = len(fetchedResultsFinal)
        for items in range(length):
                if int(fetchedResultsFinal[items]) == int(values[items]):
                    pass
                else:
                    raise Exception(
                        "Test Case 0 : failed" + "\n"
                        "YOUR OUTPUT: " + str(fetchedResultsFinal[items]) + "\n"
                        "EXPECTED OUTPUT: " + str(values[items])
                    )
        print("Test Case 0: Passed")
    def getResults1(self):
        values1 = [] # Original Output stored in this list
        fetchedResults1 = [] # Un Refractored user generated outputs stored here
        fetchedResultsFinal1 = [] # Final Refactored User Generated Output list
        outputCases = open("output1.txt", "r")
        for cases in outputCases:
            values1.append(cases)
        """Stores the original output in Values"""
        userOutput = open("stored_output1.txt", "r")
        for outputs in userOutput:
            fetchedResults1.append(outputs)
        """Unrefractored user outputs """
        for stripers in fetchedResults1:
            fetchedResultsFinal1.append(stripers.strip())
        """refractored user generated output stored here """
        length = len(fetchedResultsFinal1)
        for items in range(length):
                if int(fetchedResultsFinal1[items]) == int(values1[items]):
                    pass
                else:
                    raise Exception(
                        "Test Case 1 : failed" + "\n"
                        "YOUR OUTPUT: " + str(fetchedResultsFinal1[items]) + "\n"
                        "EXPECTED OUTPUT: " + str(values1[items])
                    )
        print("Test Case 1: Passed")
    def getResults2(self):
        values2 = [] # Original Output stored in this list
        fetchedResults2 = [] # Un Refractored user generated outputs stored here
        fetchedResultsFinal2 = [] # Final Refactored User Generated Output list
        outputCases = open("output2.txt", "r")
        for cases in outputCases:
            values2.append(cases)
        """Stores the original output in Values"""
        userOutput = open("stored_output2.txt", "r")
        for outputs in userOutput:
            fetchedResults2.append(outputs)
        """Unrefractored user outputs """
        for stripers in fetchedResults2:
            fetchedResultsFinal2.append(stripers.strip())
        """refractored user generated output stored here """
        length = len(fetchedResultsFinal2)
        for items in range(length):
                if int(fetchedResultsFinal2[items]) == int(values2[items]):
                    pass
                else:
                    raise Exception(
                        "Test Case 2 : failed" + "\n"
                        "YOUR OUTPUT: " + str(fetchedResultsFinal2[items]) + "\n"
                        "EXPECTED OUTPUT: " + str(values2[items])
                    )
        print("Test Case 2: Passed")
if __name__=='__main__':
   Check_Code().getResults()
   Check_Code().getResults1()
   Check_Code().getResults2()
