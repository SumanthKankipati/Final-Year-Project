from Chat_Bot_Scraper import google_scratch_scraper
from Chat_Bot_Scraper import google_scraper
from Chat_Bot_Scraper import wiki_scraper
import concurrent.futures
import asyncio


def get_scraper_result(query):
    global user_query_answer
    global google_result

    asyncio.set_event_loop(asyncio.new_event_loop())

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(wiki_scraper.search_summary_on_wiki, query)
        wiki_result = future.result()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(google_scratch_scraper.fetch_data_from_google, query)
        google_scratch_result = future.result()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(google_scraper.google, query)
        google_result = future.result()

    # wiki_result = wiki_scraper.search_summary_on_wiki(query)

    if wiki_result != "Data Not Found":
        user_query_answer = wiki_result

    elif google_scratch_result != "Data Not Found":
        user_query_answer = google_scratch_result

    elif google_result != "Data Not Found":
        user_query_answer = google_result



    else:
        user_query_answer = "Unable to find answer of your question please try again !!"

    return user_query_answer





