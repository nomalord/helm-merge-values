import copy

import click
from deepmerge import Merger
import yaml

from helm_merge_values.click_custom_classes import OrderedParamsCommand

HELM_DEFAULT_MERGE_STRATEGY = Merger(
    [
        (set, ["override"]),
        (list, ["override"]),
        (dict, ["merge"]),
    ],
    ["override"],
    ["override"]
)

@click.command(cls=OrderedParamsCommand)
@click.option('-f', '--values', 'file_names',
              type=click.Path(exists=True), multiple=True, default=[], required=True,
              help='The values file name')
@click.option('--set', 'file_names',
              type="", multiple=True, default=[], required=True,
              help='The values file name')
def merge_values(file_names):
    """
    Merge values files according to the chosen strategy\n
    Available Strategies:\n
    \tdefault-helm\tmerge dictionaries deeply and override for all other types (helm's strategy)\n
    \tfull-deep\tmerge all available types deeply (lists get appended, dicts deep merge)\n
    \toverride\tmerge all available types by overriding values\b
    """
    merged_values_dict = {}
    loaded_values_files = [yaml.safe_load(click.open_file(file, mode='r')) for file in file_names]
    for values_file in loaded_values_files:
        HELM_DEFAULT_MERGE_STRATEGY.merge(merged_values_dict, copy.deepcopy(values_file))
    click.echo(yaml.dump(merged_values_dict, sort_keys=False))

if __name__ == '__main__':
    merge_values()