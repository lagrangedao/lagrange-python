from lagrange.lagrange_client import LagrangeClient
import pytest


def test_get_dataset():
    lagrange_client = LagrangeClient()
    dataset = lagrange_client.get_dataset("charles-hello")
    assert dataset.name == "charles-hello"


def test_dataset_not_found():
    lagrange_client = LagrangeClient()
    dataset = lagrange_client.get_dataset("charles-hell")
    assert dataset is None
