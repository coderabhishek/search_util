# search_util
An intelligent search utility for big e-libraries based on ranking mechanism

Run shas.py to search through files in test_data folder.
You need to first index all files by running page_break.py once on dataset

Indexing Mechanism:
  It stems each word using porter stemmer algorithm and then stores count of each word in each file and based on length of line it gives importance like short lines are more probable to be a heading and so more importance.
  
Searching Mechanism:
  It uses 
   [product_over_all_i (1+lambda*ai)] formula to calculate where ai is importance of ith word in a page and lambda is just a constant so that when product expands as a polynmial the file containing all the words that is no ai=0 will have highest power of lambda thus giving relatively higher weightage.
   
