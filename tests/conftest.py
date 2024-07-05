"""Fixtures for bw_simapro_csv"""

from copy import deepcopy

import pytest
from bw2data.tests import bw2test
from fixtures.basic import DATA as BASIC_DATA


@pytest.fixture
@bw2test
def basic():
    from multifunctional import MultifunctionalDatabase

    db = MultifunctionalDatabase("basic")
    db.write(deepcopy(BASIC_DATA), process=False)
    db.metadata["dirty"] = True
    return db
