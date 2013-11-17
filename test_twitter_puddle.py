import logging
import os

import twitter_puddle


logging.basicConfig(
    filename=os.path.join(os.path.dirname(__file__), 'test.log'),
    level=logging.INFO, format='%(asctime)s level=%(levelname)s %(message)s')


def pytest_generate_tests(metafunc):
    metafunc.parametrize('scenario', metafunc.module.scenarios)


def test_twitter_puddle(scenario):
    logging.info('-' * 80)
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
        'walls': [1, 2],
        'expected_volume': 0
    },
    {
        'walls': [-2, -1],
        'expected_volume': 0
    },
    {
        'walls': [2, 1],
        'expected_volume': 0
    },
    {
        'walls': [-1, -2],
        'expected_volume': 0
    },
    {
        'walls': [-3, -2, -1],
        'expected_volume': 0
    },
    {
        'walls': [1, 2, 3],
        'expected_volume': 0
    },
    {
        'walls': [-1, -2, -3],
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
    {
        'walls': [1, 0, -1, -2, -3, -4, -1, -2, -3, -4, -5, -4, 2],
        'expected_volume': 40
    },
    {
        'walls': [1, -2, -1, -3, 1, -2, -1, -3, -2],
        'expected_volume': 11
    },
    {
        'walls': [-5, -6, -4, -5, -3, -4, -2, -3, -1, -2, 0, -1, 1],
        'expected_volume': 6
    },
    {
        'walls': [1, 0, -1, -2, -3, -2],
        'expected_volume': 1
    },
    {
        'walls': [1, -2, -1, -2, -1, 1],
        'expected_volume': 10
    },
]
