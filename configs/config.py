import os
import pathlib


# Diretório raíz
PACKAGE_ROOT = pathlib.Path('.').resolve()

# Caminhos para os diretórios dos dados
DATADIR = os.path.join(PACKAGE_ROOT, 'data')
DATADIR_RAW = os.path.join(DATADIR, 'raw')
DATADIR_INTERIM = os.path.join(DATADIR, 'interim')
DATADIR_PREPROCESSED = os.path.join(DATADIR, 'preprocessed')

# Files raw Data
FILE_TRAIN = os.path.join(DATADIR_RAW,'train.csv')
FILE_STORE = os.path.join(DATADIR_RAW,'store.csv')
FILE_TEST = os.path.join(DATADIR_RAW,'test.csv')


# Files interim Data


# logging Messages



