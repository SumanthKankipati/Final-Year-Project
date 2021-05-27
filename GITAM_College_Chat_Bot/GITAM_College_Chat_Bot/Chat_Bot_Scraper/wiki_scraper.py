import wikipedia

def search_summary_on_wiki(query):
    global final_result
    final_result = ''
    try:
        queryResult = wikipedia.summary(query)
        length_result = len(queryResult)
        final_result = ''

        if (length_result>=500):
            result = queryResult[:400]
            final_result = find_dot(result)

        elif (length_result>=400):
            result = queryResult[:300]
            final_result = find_dot(result)

        elif (length_result<=30):
            final_result = "Data Not Found"

        else:
            final_result = "Data Not Found"

    except Exception as e:
        print("Data Not Found, "+str(e))
        final_result = "Data Not Found"

    return final_result


def find_dot(data):
    dot_index = data.rfind(".")
    print(dot_index)
    if dot_index != -1:
        return data[:dot_index+1]
    else:
        return data



# print(search_summary_on_wiki('what is ml'))
