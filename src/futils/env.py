import logging
import os
import subprocess
from os.path import join

from prefect import task


@task()
def save_conda_env(output_dir: str, logger=logging):
    """
    Save conda environment to conda-environment.yaml.

    :param output_dir:
    :param logger:
    :return:
    """
    conda_prefix = os.environ["CONDA_PREFIX"]
    outpath = join(output_dir, "conda-environment.yaml")
    cmd = f"conda list -p {conda_prefix} > {outpath}"
    result = subprocess.run(cmd, shell=True, check=True)
    result.check_returncode()

    logger.info(f"Saved conda-environment to {outpath}.")
