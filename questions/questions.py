import nltk
import sys
import os
import string
import math 

FILE_MATCHES = 1
SENTENCE_MATCHES = 1
nltk.download('punkt')
nltk.download('stopwords')

def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])

    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)
    
    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files = {}
    for filename in os.listdir(directory+os.sep):
        with open(directory+os.sep+filename) as f:
            contents = f.read()
        files[filename] = contents
    return files

def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    stopwords = nltk.corpus.stopwords.words("english")
    s = string.punctuation
    list_words = nltk.tokenize.word_tokenize(document.lower())
    return [word for word in list_words if word not in stopwords and word not in s]


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    
    num_doc = len(documents)
    idfs = {}
    for doc in documents.values():
        for word in doc:
            if word not in idfs.keys():
                num_occ = len([True for d in documents.values() if word in d])           
                idfs[word] = math.log(num_doc/num_occ)
    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    top_files = {filename:0 for filename in files.keys()}
    for word in query:
        for file in files.keys():
            if word in files[file]:
                top_files[file] += files[file].count(word) * idfs[word]
    return sorted(top_files.keys(), key=top_files.__getitem__, reverse=True)[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    top_sentences = {sentence:[0,0] for sentence in sentences.keys()}
    for word in query:
        for sentence in sentences.keys():
            if word in sentences[sentence]:
                top_sentences[sentence][0] += idfs[word]
                top_sentences[sentence][1] += sentences[sentence].count(word) / len(sentences[sentence])
    
    return sorted(top_sentences.keys(), key=top_sentences.__getitem__, reverse=True)[:n]
    


if __name__ == "__main__":
    main()
