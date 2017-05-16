#!/usr/bin/env Rscript

# Copyright 2017 Complex Systems, Analytics, and Visualization Institute

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Authors: Chris Gropp and Alex Herzog
# Date: March 31, 2017
# Purpose: Generate Synthetic Data from an LDA Model

rm(list = ls())

args = commandArgs(trailingOnly=TRUE)
if(length(args) < 6)
{
	stop("Proper usage: <topics_filename> <mixtures_filename> <output_filename> <seed> <num_docs> <avg_doc_size>\n")
}

#generate_data("time-all.dat","mixtures-smaller.dat","synthetic_test_corpus.txt",42,10,15)
generate_data(args[1],args[2],args[3],args[4],args[5],args[6])

generate_data <- function(TOPICS_FILENAME, MIXTURES_FILENAME, OUTPUT_FILENAME, RANDOM_SEED, NUM_DOCS, AVG_DOC_SIZE)
{
set.seed(RANDOM_SEED)

m <- read.csv(TOPICS_FILENAME, sep=" ", header=FALSE, stringsAsFactors=FALSE)
N.topics <- ncol(m)-1

vocab <- m[,1]
topics <- m[,2:(N.topics+1)]

topic.mixtures <- read.csv(MIXTURES_FILENAME, sep=" ", header=FALSE)
N.docs <- nrow(topic.mixtures)

numdocs <- NUM_DOCS # number of documents
avg.doc.size <- AVG_DOC_SIZE # average doc size (i.e., avg number of words in a doc)

# loop to generate data
corpus <- rep("",numdocs)
for (doc.index in 1:numdocs) {
    # Sample length of document by pulling a random number from the
    # poisson distribtuon with mean avg.doc.size
    docwords <- rpois(1, avg.doc.size)

    # Pick a random document from topic.mixtures and use its mixture
    # for the current document
    mixture <- topic.mixtures[sample(N.docs,1),]

    # Build the document
    doc.strings <- rep("", docwords)
    for (word.index in 1:docwords) {
        # Sample a column from the topics matrix weighted by the current mixture
        col.index <- sample(N.topics, 1, prob=mixture)
        topic <- topics[,col.index]

        # Sample word from the topic
        word <- sample(vocab, 1, prob=topic)
        
        # Plug into document
        doc.strings[word.index] <- word
    }
    # Plug document into corpus
    corpus[doc.index] <- paste(doc.strings, collapse=" ")
}

# Write corpus to file
write(corpus, file=OUTPUT_FILENAME)

}
