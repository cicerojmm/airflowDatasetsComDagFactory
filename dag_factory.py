from airflow import DAG
from dagfactory import load_yaml_dags


load_yaml_dags(globals_dict=globals(), suffix=['dags_*.yml', 'dags_*.yaml'])