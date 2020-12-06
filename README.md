# scNLP
Welcome to scNLP, a pipeline for performing deep-learning based Natural Language Processing on large volumes of scientific literature. This originated as a fun project while working from home during COVID, though I believe this will have many applications across scientific disciplines. This is very much a work in progress, so pull requests welcome!

Using a free NCBI API Key (you can get one <a href='https://ncbiinsights.ncbi.nlm.nih.gov/2017/11/02/new-api-keys-for-the-e-utilities/'>here </a>, we are able to query PubMed or PubMedCentral at 10 searches per second, allowing collection and archiving of hundreds or thousands of literature results for any given topic. I then have trained a SpaCy Named Entity Recognition (NER) model to extract meaningful terms, including cell types, neurotransmitters, brain regions, physiologically relevant molecules (e.g. proteins) and functions, and measure term enrichment within a body of literature sampled from a larger corpus (via Fisher's Exact Test, similar to GO Ontology term analysis). By extracting these terms along with the context they are used in, we are then able to train a word vector embedding model (Word2Vec) to quantitatively measure the  similarity between these named entities, and visualize the relationship between topics as they are described in the literature.

My trained model can be found <a href='https://drive.google.com/drive/folders/1B5DBQBiVd1Hso8NN2Yxnzgl7b_j-0awy?usp=sharing'>on Google Drive here</a>

The application I have uploaded code for in this repo is analysis of single-cell sequencing marker gene or differential expression lists, which can be generated using  <a href='https://github.com/alexcwsmith/singleCellTools'>my scanPy single-cell analysis pipeline</a>, but these functions can be easily adapted to search for any keywords in PubMed/PMC. In order to analyze single-cell sequencing data, this model examines gene lists for individual clusters of genes, and performs a series of PMC searches, for each gene plus an additional suffix of interest (e.g. search for 'Gria2 psychiatric disorder'). By gathering 25-100 literature results per gene, for 20-50 genes per cluster, a corpus of between 500-5000 papers are obtained for each cluster. Named entity recognition then extracts meaningful terms, and examines the fequency of each term within a single cluster versus in the entire corpus containing all clusters, and calculates statistical enrichment.

Named entity recognition may be useful for identifying cell types from marker gene lists, or for quickly identifying clusters that show dynamic differential expression of many genes related to pathological states. Applying this code to neuroanatomy or circuitry by searching for brain structures in combination with each other, or with neuropsychiatric disorders, is able to quickly provide novel insights into brain networks.

Finally, this contains a text summarization tool that will produce a short summary (user-defined lenght) of a corpus of literature.
