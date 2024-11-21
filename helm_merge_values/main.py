import copy
from typing import Dict

import click
from deepmerge import Merger, always_merger
import yaml

HELM_DEFAULT_MERGE_STRATEGY = Merger(
    [
        (set, ["override"]),
        (list, ["override"]),
        (dict, ["merge"]),
    ],
    ["override"],
    ["override"]
)

FULL_DEEP_MERGE_STRATEGY = always_merger

OVERRIDE_MERGE_STRATEGY = Merger(
    [
        (set, ["override"]),
        (list, ["override"]),
        (dict, ["override"]),
    ],
    ["override"],
    ["override"]
)

merge_options: Dict[str, Merger] = {
    "default-helm": HELM_DEFAULT_MERGE_STRATEGY,
    "full-deep": FULL_DEEP_MERGE_STRATEGY,
    "override": OVERRIDE_MERGE_STRATEGY,  # TODO fix OVERRIDE doesn't work for some reason
}

@click.command()
@click.option('--strategy',
              type=click.Choice(list(merge_options.keys()), case_sensitive=False), default='default-helm', show_default=True,
              help='The strategy to use when merging'
              )
@click.option('-f', '--values', 'file_names',
              type=click.Path(exists=True), multiple=True, default=[], required=True,
              help='The values file name')
def merge_values(strategy, file_names):
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
        merge_options[strategy].merge(merged_values_dict, copy.deepcopy(values_file))
    click.echo(yaml.dump(merged_values_dict, sort_keys=False))

if __name__ == '__main__':
    merge_values()