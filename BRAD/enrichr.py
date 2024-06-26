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
import matplotlib.pyplot as plt

# Bioinformatics
import gget

from BRAD import utils
from BRAD import log

# gene enrichment
def queryEnrichr(chatstatus, gene_list):
    """
    Performs gene enrichment analysis using the Enrichr service and updates the chat status with the results.

    :param chatstatus: The current status of the chat, including the prompt, configuration, and process details.
    :type chatstatus: dict

    :raises FileNotFoundError: If the gene list or Enrichr databases file is not found.
    :raises ValueError: If the gene list or prompt contains invalid entries.
    :raises Warning: If multiple potential databases are provided or no database is specified.

    :return: The updated chat status dictionary containing the enrichment results and process details.
    :rtype: dict
    """
    prompt              = chatstatus['prompt']
    max_p_val           = chatstatus['config']['max_enrichr_pval']
    num_df_rows_display = chatstatus['config']['num_df_rows_display']
    default_enrichr_db  = chatstatus['config']['default_enrichr_db']
    
    process = {'MODULE' : 'ENRICHR'}
    db, save, plot, dbfound = None, True, True, False

    # Remove any punctuation except for - and _, which are used in gget database names
    punctuation_to_remove = string.punctuation.replace('-', '').replace('_', '')
    translator = str.maketrans('', '', punctuation_to_remove)
    prompt = prompt.translate(translator)
    
    # Get list of gene names
    current_script_path = os.path.abspath(__file__)
    current_script_dir = os.path.dirname(current_script_path)
    file_path = os.path.join(current_script_dir, 'helperData', 'gene_list.txt')
    with open(file_path, "r") as file:
        g_from_file = [line.strip() for line in file]
    file_path = os.path.join(current_script_dir, 'helperData', 'ggetEnrichrDatabases.tsv')
    df = pd.read_csv(file_path, delimiter='\t')
    dbs = list(df['Gene-set Library'].values)
    dbs = [dbi.upper() for dbi in dbs]
    for gene in prompt.split(' '):
        if gene.upper() in dbs:
            if db is not None:
                warnings.warn('Two potential databases were provided!')
            else:
                db = gene
                dbfound = True
        if gene.upper() == 'PLOT':
            plot = True
    save = True
    if db is None:
        warnings.warn('warning: setting db to default')
        db = default_enrichr_db
        
    process = {
        'module'     : 'ENRICHR',
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
    chatstatus = log.userOutput(output, chatstatus=chatstatus)
    display(edf[:num_df_rows_display].style)
    if save:
        chatstatus = utils.save(chatstatus, edf, 'ENRICHR-' + db + '.csv')

    if plot:
        chatstatus = utils.savefig(chatstatus, ax, 'ENRICHR-' + db + '.png')
        plt.show()
    
    if chatstatus['process'] is None:
        chatstatus['process'] = process
    else:
        chatstatus['process']['steps'].append(process)
    
    chatstatus['output']  = output
    return chatstatus
