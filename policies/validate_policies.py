"""
This python script validates policies in the policies directory according
to schema.yml.
"""

import pathlib

from pykwalify.core import Core as Kwalify
import ruamel.yaml
import pytest

directory = pathlib.Path(__file__).parent

with directory.joinpath('schema.yml').open() as read_file:
    schema = ruamel.yaml.safe_load(read_file)

paths = [
    directory.joinpath('template.yml'),
] + list(directory.glob('policies/*.yml'))
paths = [str(x) for x in paths]


@pytest.mark.parametrize('path', paths)
def test_policies(path, caplog):
    """
    Triggers test failure by looking for any logged warnings.
    """
    kwalify = Kwalify(
        source_file=path,
        schema_data=schema,
        strict_rule_validation=True,
    )
    data = kwalify.validate(raise_exception=False)
    n_log_captures = len(caplog.records)
    assert n_log_captures == 0
