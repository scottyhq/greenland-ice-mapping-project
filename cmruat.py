'''
Simplified version of NSIDC Download Script to return links without downloading
'''

import requests
import itertools

CMR_URL = 'https://cmr.uat.earthdata.nasa.gov'
URS_URL = 'https://uat.urs.earthdata.nasa.gov'
CMR_PAGE_SIZE = 2000
CMR_FILE_URL = '{0}/search/granules.json?&scroll=true&page_size={1}'.format(CMR_URL,CMR_PAGE_SIZE)

def cmr_filter_urls(search_results):
    """Select only the desired data files from CMR response."""
    if 'feed' not in search_results or 'entry' not in search_results['feed']:
        return []

    entries = [e['links']
               for e in search_results['feed']['entry']
               if 'links' in e]
    # Flatten "entries" to a simple list of links
    links = list(itertools.chain(*entries))

    urls = []
    unique_filenames = set()
    for link in links:
        if 'href' not in link:
            # Exclude links with nothing to download
            continue
        if 'inherited' in link and link['inherited'] is True:
            # Why are we excluding these links?
            continue
        if 'rel' in link and 'data#' not in link['rel']:
            # Exclude links which are not classified by CMR as "data" or "metadata"
            continue

        if 'title' in link and 'opendap' in link['title'].lower():
            # Exclude OPeNDAP links--they are responsible for many duplicates
            # This is a hack; when the metadata is updated to properly identify
            # non-datapool links, we should be able to do this in a non-hack way
            continue

        filename = link['href'].split('/')[-1]
        if filename in unique_filenames:
            # Exclude links with duplicate filenames (they would overwrite)
            continue
        unique_filenames.add(filename)

        urls.append(link['href'])

    return urls


def query_cmr(query_url):
    ''' return JSON / python dictionary'''
    print(query_url)
    response = requests.get(query_url)
    search_results = response.json()
    return search_results


def build_cmr_query_url(echo_collection_id, token, time_start=None, time_end=None, polygon=None, bounding_box=None, filename_filter=None):
    params = '&echo_collection_id={0}'.format(echo_collection_id)
    params += '&token={0}'.format(token)
    if time_start:
        params += '&temporal[]={0},{1}'.format(time_start, time_end)
    if polygon:
        params += '&polygon={0}'.format(polygon)
    elif bounding_box:
        params += '&bounding_box={0}'.format(bounding_box)
    if filename_filter:
        option = '&options[producer_granule_id][pattern]=true'
        params += '&producer_granule_id[]={0}{1}'.format(filename_filter, option)
    return CMR_FILE_URL + params



def get_urls(echo_collection_id, token,  time_start=None, time_end=None, bounding_box=None, polygon=None, filename_filter=None):
    query_url = build_cmr_query_url(echo_collection_id, token,  time_start, time_end, bounding_box, polygon, filename_filter)
    search_results = query_cmr(query_url)
    urls = cmr_filter_urls(search_results)
    return urls
    
