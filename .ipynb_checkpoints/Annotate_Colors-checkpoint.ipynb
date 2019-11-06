{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 217,
   "metadata": {},
   "outputs": [],
   "source": [
    "import networkx as nx\n",
    "import pandas as pd\n",
    "from functools import partial \n",
    "\n",
    "def to_integer(bitstr):\n",
    "    return int(bitstr, 2)\n",
    "\n",
    "def Rename_Colors(dict_color_ctr_map, color):\n",
    "    return dict_color_ctr_map[color]\n",
    "\n",
    "def Create_Sublineages_Matrix(df):\n",
    "    row_list = []\n",
    "    for i, row in df.iterrows():\n",
    "        K_mer = row['K-Mer']\n",
    "        sub_lin = row['Sublineages'].split(',')\n",
    "        bit_val = [1]*len(sub_lin)\n",
    "        d = dict(zip(sub_lin, bit_val))\n",
    "        d['K_Mer'] = K_mer\n",
    "        row_list.append(d)\n",
    "    df_op = pd.DataFrame(row_list)\n",
    "    df_op.fillna(0, inplace = True)\n",
    "    df_op = df_op.set_index('K_Mer')\n",
    "    df_op.sort_index(axis=1, inplace=True)\n",
    "    df_op = df_op.astype(int).astype(str)\n",
    "    df_op['Bitstring'] = df_op.apply(lambda row: ''.join(row.values.astype(str)), axis=1)\n",
    "    df_op['Color'] = df_op['Bitstring'].apply(to_integer)\n",
    "\n",
    "    color_unique = df_op['Color'].unique()\n",
    "    counter = [i for i in range(len(color_unique))]\n",
    "    color_rename_map = dict(zip(color_unique, counter))\n",
    "    df_op['Color_new'] = df_op['Color'].apply(partial(Rename_Colors, color_rename_map))\n",
    "    return df_op\n",
    "\n",
    "def Return_Lineage_List(row):\n",
    "    op_list = []\n",
    "    keys = list(row.keys())\n",
    "    for k in keys:\n",
    "        if k!='Color' and k!='Color_new' and k!='Bitstring':\n",
    "            if row[k] == \"1\":\n",
    "                op_list.append(k)\n",
    "    return op_list\n",
    "\n",
    "def Prepare_Op_File(df_op):\n",
    "    data = []\n",
    "    for (index, row) in df_op.iterrows():\n",
    "        d = {'Sub_Lineages':Return_Lineage_List(row), 'Color':row['Color_new'], 'K-mer':index}\n",
    "        data.append(d)\n",
    "    df_ret = pd.DataFrame(data)\n",
    "    df_ret.set_index('K-mer', inplace = True)\n",
    "    return df_ret"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('data/HIV_full_Refs_k23_1.kmer_sublineage_info.tsv', sep = '\\t', names = ['K-Mer','Sublineages'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 219,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_op = Create_Sublineages_Matrix(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 220,
   "metadata": {},
   "outputs": [],
   "source": [
    "G = nx.read_gexf('data/HIV_full_Refs_k23_1.gexf')\n",
    "nx.set_node_attributes(G, df_op[['Color_new']].T.to_dict())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_ret = Prepare_Op_File(df_op)\n",
    "df_ret.to_csv('data/HIV_full_Refs_k23_1_Color_Table.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 222,
   "metadata": {},
   "outputs": [],
   "source": [
    "nx.write_gexf(G, \"data/HIV_full_Refs_k23_1_Color_Annotated.gexf\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 223,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Color</th>\n",
       "      <th>Sub_Lineages</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>K-mer</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>AAAAACAGGAAAATATGCCAGAA</th>\n",
       "      <td>0</td>\n",
       "      <td>[01_AE, 15_01B, 33_01B]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>AAAAAGGACAGCACCAAATGGAG</th>\n",
       "      <td>1</td>\n",
       "      <td>[01_AE, 15_01B, CPZ]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>AAAAATCTTAGAGCCCTTTAGAA</th>\n",
       "      <td>2</td>\n",
       "      <td>[01_AE, 02_AG, 04_cpx, 05_DF, 06_cpx, 09_cpx, ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>AAAACTGGATGACAGAAACCTTG</th>\n",
       "      <td>3</td>\n",
       "      <td>[01_AE, 02_AG, 05_DF, 15_01B, 25_cpx, 34_01B, F2]</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>AAAAGCAGGGTATGTCACTGACA</th>\n",
       "      <td>4</td>\n",
       "      <td>[01_AE, 02_AG, 11_cpx, 15_01B, 25_cpx, 27_cpx,...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                         Color  \\\n",
       "K-mer                            \n",
       "AAAAACAGGAAAATATGCCAGAA      0   \n",
       "AAAAAGGACAGCACCAAATGGAG      1   \n",
       "AAAAATCTTAGAGCCCTTTAGAA      2   \n",
       "AAAACTGGATGACAGAAACCTTG      3   \n",
       "AAAAGCAGGGTATGTCACTGACA      4   \n",
       "\n",
       "                                                              Sub_Lineages  \n",
       "K-mer                                                                       \n",
       "AAAAACAGGAAAATATGCCAGAA                            [01_AE, 15_01B, 33_01B]  \n",
       "AAAAAGGACAGCACCAAATGGAG                               [01_AE, 15_01B, CPZ]  \n",
       "AAAAATCTTAGAGCCCTTTAGAA  [01_AE, 02_AG, 04_cpx, 05_DF, 06_cpx, 09_cpx, ...  \n",
       "AAAACTGGATGACAGAAACCTTG  [01_AE, 02_AG, 05_DF, 15_01B, 25_cpx, 34_01B, F2]  \n",
       "AAAAGCAGGGTATGTCACTGACA  [01_AE, 02_AG, 11_cpx, 15_01B, 25_cpx, 27_cpx,...  "
      ]
     },
     "execution_count": 223,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_ret.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
