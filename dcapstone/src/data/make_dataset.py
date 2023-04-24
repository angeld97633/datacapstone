# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

data = pd.read_csv("online_store_customer_data.csv")
cd /Users/angeldurrani/Documents/GitHub/datacapstone/dcapstone/data/raw

@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    data = data.dropna()
    gen_dumm = pd.get_dummies(data['Gender'])
    gen_dumm["Female"] 
    data = pd.concat([data,gen_dumm["Female"]],axis=1)
    data = data.drop(["Gender"],axis=1)
    data.rename(columns = {'Female':'Gender F=1,M=0'}, inplace = True)
    dataNull = data.isnull()
    dataNull.sum()
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
