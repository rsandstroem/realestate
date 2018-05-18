# -*- coding: utf-8 -*-
import logging
from pathlib import Path

import click
import pandas as pd

from dotenv import find_dotenv, load_dotenv


def create_data_frame(input_filepath):
    """Creates a pandas data frame from a json file.

    Args:
        input_filepath: relative file path of a single json file

    Returns:
        A pandas.DataFrame without any conversion or processing.
    """
    df = pd.read_json(input_filepath)
    logger = logging.getLogger(__name__)
    logger.info('Imported dataframe:')
    logger.info(df.info())
    logger.info(df.describe())
    logger.info(df.head())
    return df


def process_columns(df):
    """Process select columns of a dataframe

    The column names, and how they should be processed,
    are hard coded. As such, care should be taken if
    modifying the input format/source.

    Args:
        df: A pandas dataframe which will be modified.

    Returns:
        None
    """
    logger = logging.getLogger(__name__)
    # Strip units and convert numerical columns to float.
    # Many columns have numbers with separators for thousand,
    # e.g., 2,062 for 2062.0.
    num_cols = [
        'living_space',
        'volume',
        'lot_size',
        'price'
    ]
    for col in num_cols:
        logger.debug(col)
        df[col] = df[col].str.replace('[^\w\s]', '')
        df[col] = df[col].str.split(' ').str.get(0)
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # The location column contains "postal_code commune"
    # df['commune'] = df.location.str.extract(r'([A-Z]\w{0,})', expand=False)
    df['commune'] = df.location.str.split(' ', 1).str.get(1)
    df['postal_code'] = df.location.str.extract(r'(\d{0,})', expand=True)
    df.drop(['location'], axis=1, inplace=True)


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).

    Args:
        input_filepath: relative file path of a single json file
        output_filepath: relative file path of the output file

    Returns:
        None
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    df = create_data_frame(input_filepath)
    process_columns(df)
    logger.info(df.head())
    df.to_csv(output_filepath, index=False)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
