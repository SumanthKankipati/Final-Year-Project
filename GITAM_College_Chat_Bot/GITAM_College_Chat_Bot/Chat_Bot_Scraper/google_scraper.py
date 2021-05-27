from search_engine_parser import GoogleSearch
import asyncio

def google(query):

    asyncio.set_event_loop(asyncio.new_event_loop())

    final_result = ''

    try:
        linkIndex = 0
        search_args = (query, 2)
        gsearch = GoogleSearch()
        gresults = gsearch.search(*search_args)
        queryResult = gresults[linkIndex]["descriptions"]
        length_result = len(queryResult)
        final_result = ''

        if length_result >= 400:
            result = queryResult[:350]
            final_result = find_dot(result)

        elif length_result >= 300:
            result = queryResult[:250]
            final_result = find_dot(result)

        else:
            final_result = queryResult

    except Exception as e:
        print("Data Not Found, "+str(e))

    return final_result


def find_dot(data):
    dot_index = data.rfind(".")
    print(dot_index)
    if dot_index != -1:
        return data[:dot_index+1]
    else:
        return data


#query = input("enter question:")
#print(google(query))
