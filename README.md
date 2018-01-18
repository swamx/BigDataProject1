# BigDataProject1
AMOD Big Data Course Data Collection Project 1: Collecting commits from git repository

The project aims to collect commits made on a GITHUB repository and be able to store those commits for analysis. 
This allows dataset users to analyse the information of message and conclude the importance of a commit.
For a large scale Open Source project thousands of commits are made everyday, the central body adopting certain branches for merge into master branch would want to view which brach has novel implementations that have been commited.
The term novel implementation includes code optimizations, introduction of new features, debugging, error corrections, and other minor or major changes.
The commit messages contains such information, as presented in a human language. 
Since, there is no sentiment or sarcasm to detect, iIt becomes clear that the only relevant details in the commit message are terms and not the organization of the terms.
Hence, we wish to populate the dataset initially with commit sha (as a unique identifier) and commit message. 
The storage solution used for storing commit is MongoDB because of the scalability and stability it offers. 
