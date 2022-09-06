import json
import pandas as pd
from decimal import Decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)


def renderdata(queryobject):
    # function used to render data from database to JSON data by passing through some steps

    dataframe = pd.DataFrame(list(queryobject))
    data = data_selection(dataframe)
    data_result = data.values.tolist()
    data_result.insert(0, data.columns.tolist())
    columns_labels = data.columns.values.tolist()
    row_list = data['rubrique'].values.tolist()
    data_result = json.dumps({'data_title': " Donnee du Ministere de l'education Nationale",
                              'data_subtitle': "Education Nationale",
                              'data_result': data_result,
                              'columns_labels': columns_labels,
                              'row_list': row_list}, cls=DecimalEncoder)
    return data_result


def cleaning_df(dataframe):
    if isinstance(dataframe, pd.DataFrame) and dataframe is not None:
        dataframe = dataframe.dropna(how="all")  # remove missing values
        dataframe = dataframe.fillna(0)  # filling empty values with 0
        dataframe = dataframe.sort_values()
        # dataframe = dataframe.drop_duplicates()
        return dataframe
    return "Error in dataset"


def data_selection1(df):
    df.drop('filename', axis=1, inplace=True)
    code_dict = {}

    for code in df['code'].unique():
        code_dict[code] = df[df['code'] == code].groupby(['annee']).mean().reset_index()
        code_dict[code]['annee'] = code_dict[code]['annee'].astype(str)
        code_dict[code] = code_dict[code].set_index('annee')
        code_dict[code] = code_dict[code].transpose()

    return code_dict


def renderdata1(query='SELECT * FROM "BD_DATABASE"."BD_DATABASE_PRESIDENCE".transport;'):
    # function used to render data from database to JSON data by passing through some steps
    con = getconnection()
    dataframe = pd.read_sql_query(query, con)  # execute query
    data = data_selection1(dataframe)
    data = data['TRANS_AER_FRETAER']

    data = data.reset_index()
    data.rename(columns={'index': 'mois'}, inplace=True)
    data_result = data.values.tolist()
    data_result.insert(0, data.columns.tolist())
    columns_labels = data.columns.values.tolist()
    row_list = data['mois'].values.tolist()
    data_result = json.dumps({'data_title': " Données du Ministere du Transport",
                              'data_subtitle': "Fret Aérien Domestiques",
                              'data_result': data_result,
                              'columns_labels': columns_labels,
                              'row_list': row_list})
    return data_result


def data_selection(df):  # education table
    # Select specifics data from the dataframe in argument
    # This only works for Education table
    if isinstance(df, pd.DataFrame) and df is not None:
        # Primary data

        # select rows from rubric column data that contains specifics information;

        # Select rows from the table where rubrique contains word primaire
        primaire = df[df['rubrique'].str.lower().str.contains('primaire')]
        # Select rows among the past result (primaire) containing word nombre
        primaire_nb = primaire[primaire['rubrique'].str.lower().str.contains('nombre')]
        # classify the result from the primaire_nb by 'public', 'prive' and 'communautaire'
        primaire_nb_public = primaire_nb[(primaire_nb['rubrique'].str.lower().str.contains('publi'))]
        primaire_nb_prive = primaire_nb[(primaire_nb['rubrique'].str.lower().str.contains('privé'))]
        primaire_nb_commu = primaire_nb[(primaire_nb['rubrique'].str.lower().str.contains('communautaire'))]
        # Select rows from the table that don't contain any of word privé, public and communautaire
        # and select the total values
        primaire_nb_total = primaire_nb.drop(primaire_nb_commu['rubrique'].index) \
            .drop(primaire_nb_prive['rubrique'].index) \
            .drop(primaire_nb_public['rubrique'].index)

        # transform the resulting data into plottable table for json
        # Then gather the result in a single dictionary
        result = {"primaire_nb_total": data_transformation(primaire_nb_total),
                  "primaire_nb_commu": data_transformation(primaire_nb_commu),
                  "primaire_nb_prive": data_transformation(primaire_nb_prive),
                  "primaire_nb_public": data_transformation(primaire_nb_public),
                  }

        # print(primaire_nb.describe())
        primaire_nb = primaire_nb.drop(columns='code', axis=1)

        return primaire_nb

    return 0


def data_transformation(df):  # education table

    # this function transform the dataframe in the argument into plottable datatable
    # The education table is used for our case and works only with such table
    if isinstance(df, pd.DataFrame) and df is not None:  # verify dataframe exist and not empty

        df = df.drop(columns=['code'], axis=1)  # remove the 'code' column
        # use rubrique rows as column after transposition
        df = df.set_index('rubrique')
        df = df.transpose()
        # convert index values to integer
        index = df.index.str.replace('_', '')
        index = [int(i, base=10) for i in index]
        # add new column year with numeric values
        df['annee'] = index
        # set annee column to index
        df = df.set_index('annee')
        df = df.reset_index()
        # \
        # df['annee'] = pd.to_datetime(df['annee'], format='%Y-%m-%d').dt.year

        # generate new ordered index and create new column annee

        return df
    return 0
