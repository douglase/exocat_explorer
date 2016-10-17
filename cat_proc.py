import astroquery
import pandas as pd
from astroquery.simbad import Simbad
import numpy as np
def get_names(target_name,catalog="HIP",all_cats=False):
    """
    use astroquery to resolve the target's catalog value via simbad. 
    
    Parameters
    -------------
    
    target_name: str
    name of the target to query
    
    catalog: str
    the simbad appreviation of the catalog, e.g. HIP, HD, BD, Gliese. Defaults to HIP (Hipparchus).
    
    all_cats: bool
    return a list of all the catalog values.
    """
    result_table=Simbad.query_objectids(target_name)
    if result_table is None:
         return target_name
    if all_cats:
        result_table = pd.Series([j.as_void()[0].decode('utf-8') for j in result_table])
        return result_table
    if target_name.find(catalog) != -1:
        return target_name
    else:
        result_table = pd.Series([j.as_void()[0].decode('utf-8') for j in result_table])
    result_val=result_table[result_table.str.contains(catalog)].values
    if np.shape(result_val)[0] ==0:
        result_val = ["NaN"]
    #if only one value, drop the list brackets:
    if np.shape(result_val)[0] ==1:  
        result_val=result_val[0]

    return result_val