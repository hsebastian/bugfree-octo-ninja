import csv

import twitter_puddle


def pytest_generate_tests(metafunc):
    metafunc.parametrize('scenario', metafunc.module.scenarios)


def test_twitter_puddle(scenario):
    actual_volume = twitter_puddle.compute_volume(scenario['walls'])
    assert actual_volume == scenario['expected_volume']


scenarios = [
    {
        'walls': [2, 5, 1, 2, 3, 4, 7, 7, 6],
        'expected_volume': 10
    },
    {
        'walls': [],
        'expected_volume': 0
    },
    {
        'walls': [-1],
        'expected_volume': 0
    },
    {
        'walls': [1],
        'expected_volume': 0
    },
    {
        'walls': [-3, -2, -1],
        'expected_volume': 0
    },
    {
        'walls': [3, 2, 1],
        'expected_volume': 0
    },
    {
        'walls': [1, -2, 1],
        'expected_volume': 3
    },
    {
        'walls': [1, -2, 1, -2],
        'expected_volume': 3
    },
    {
        'walls': [1, -2, 1, -2, 1],
        'expected_volume': 6
    },
    {
        'walls': [1, -2, 1, -2, 10],
        'expected_volume': 6
    },
    {
        'walls': [10, -2, 1],
        'expected_volume': 3
    },
    {
        'walls': [1, 1, 1],
        'expected_volume': 0
    },
    {
        'walls': [1, 2, 1],
        'expected_volume': 0
    },
    {
        'walls': [1, 0, 1],
        'expected_volume': 1
    },
]
