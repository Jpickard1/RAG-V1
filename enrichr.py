import pandas as pd
import numpy as np
from copy import deepcopy
import os
import sys
from importlib import reload
from scipy.stats import zscore
from scipy.stats import entropy
import scipy.io
import scipy
import textwrap
from scipy import sparse
import importlib
from itertools import product
from datetime import datetime
from IPython.display import display # displaying dataframes
import string
import warnings
import re

# Bioinformatics
import gget


# gene enrichment
def queryEnrichr(chatstatus):
    prompt              = chatstatus['prompt']
    max_p_val           = chatstatus['config']['max_enrichr_pval']
    num_df_rows_display = chatstatus['config']['num_df_rows_display']
    default_enrichr_db  = chatstatus['config']['default_enrichr_db']
    process = {}
    db, save, plot, dbfound = None, False, False, False
    
    # Remove any punctuation except for - and _, which are used in gget database names
    punctuation_to_remove = string.punctuation.replace('-', '').replace('_', '')
    translator = str.maketrans('', '', punctuation_to_remove)
    prompt = prompt.translate(translator)
    
    gene_list = []
    # Get list of gene names
    with open("gene_list.txt", "r") as file:
        g_from_file = [line.strip() for line in file]
    df = pd.read_csv('ggetEnrichrDatabases.tsv', delimiter='\t')
    dbs = list(df['Gene-set Library'].values)
    dbs = [dbi.upper() for dbi in dbs]
    for gene in prompt.split(' '):
        if gene.upper() in g_from_file:
            gene_list.append(gene)
        if gene.upper() in dbs:
            if db is not None:
                warnings.warn('Two potential databases were provided!')
            else:
                db = gene
                dbfound = True
        if gene.upper() == 'SAVE':
            save = True
        if gene.upper() == 'PLOT':
            plot = True
    
    if db is None:
        warnings.warn('warning: setting db to default')
        db = default_enrichr_db
        
    process = {
        'genes'      : str(gene_list),
        'plot'       : plot,
        'save'       : save,
        'database'   : db,
        'default db' : dbfound,
    }
        
    # query GO
    ax = None
    if plot:
        fig, ax = plt.subplots()
    edf = gget.enrichr(gene_list, database=db, plot=plot, ax=ax)
    edf = edf[edf['p_val'] <= max_p_val]
    
    output = 'The following table was generated by quering the gene list against ' + db + ':'
    print(output)
    display(edf[:num_df_rows_display].style)
    if save:
        filepath = 'RAG-gget-' + db + '-' + str(datetime.now()) + '.csv'
        filepath = filepath.replace(" ", "")
        edf.to_csv(filepath)
        saveOutput = 'The table has been saved to: ' + str(filepath)
        output += (' \n ' + saveOutput)
        print(saveOutput)
        process['filepath'] = filepath

    if plot:
        plt.show()
    return output, process
