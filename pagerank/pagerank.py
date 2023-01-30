import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    N = len(corpus)
    n_links = len(corpus[page])
    result = dict()
    
    if n_links != 0:
        for p in corpus:
            if p in corpus[page]:
                result[p] = ((1 - damping_factor) / N) + (damping_factor / n_links)
            else:
                result[p] = (1 - damping_factor) / N
                
    else:
        for p in corpus:
            result[p] = (1 - damping_factor) / N
            
    return result
    

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages = list(corpus)
    sample = random.choice(pages)
    result = dict()
    
    for p in pages:
        result[p] = 0
    
    for i in range(n):
        if n == 1:
            result[sample] += 1
        else:
            pagerank = transition_model(corpus, sample, damping_factor)
            sample = random.choices(pages, list(pagerank.values()))[0]
            result[sample] += 1
    result = {key : value / n for key, value in result.items()}
    return result
    

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages = list(corpus)
    N = len(corpus)
    result = dict()
    
    for p in pages:
        result[p] = 1 / N
        
    links_page = dict()
    for i , p_set in corpus.items():
        links_page[i] = [i_in for i_in , p_set_in in corpus.items() if i in p_set_in]
    
    while True:
        count = 0
        for p in pages:
            prob = damping_factor * sum([ result[i] / len(corpus[i]) for i  in links_page[p] if len(corpus[i]) != 0]) + ((1 - damping_factor) / N)
            if abs(result[p] - prob) < 0.001:
                count += 1
            
            result[p] = prob
        if count == N:
            break
    return result


if __name__ == "__main__":
    main()
