import importlib

import pytest

import vw
import vw.config


@vw.tests_only
def method_that_prints__with_tests_only():
    print("Hello, world!")


@vw.no_op
def method_that_prints__with_no_op():
    print("Hello, world!")


@pytest.fixture()
def set_control_vars():
    def reset():
        importlib.reload(vw.config)
        vw.clear_env_cache()

    yield reset
    reset()


@pytest.fixture()
def env_with_vw_ignore_turned_on(monkeypatch: pytest.MonkeyPatch, set_control_vars):
    monkeypatch.setenv("VW_IGNORE", "1")
    set_control_vars()
    yield
    monkeypatch.undo()


@pytest.fixture()
def env_with_vw_ignore_off(monkeypatch: pytest.MonkeyPatch, set_control_vars):
    monkeypatch.setenv("VW_IGNORE", "0")
    set_control_vars()
    yield
    monkeypatch.undo()


@pytest.fixture()
def env_with_vw_always_on(monkeypatch: pytest.MonkeyPatch, set_control_vars):
    monkeypatch.setenv("VW_ALWAYS", "1")
    set_control_vars()
    yield
    monkeypatch.undo()


@pytest.fixture()
def env_with_vw_always_off(monkeypatch: pytest.MonkeyPatch, set_control_vars):
    monkeypatch.setenv("VW_ALWAYS", "0")
    set_control_vars()
    yield
    monkeypatch.undo()


def test___ignore_set___is_test_env(env_with_vw_ignore_turned_on):
    assert vw.is_test_env() is False


def test___ignore_unset___is_test_env(env_with_vw_ignore_off):
    assert vw.is_test_env() is True


def test___ignore_set_and_always_set___is_test_env(
    env_with_vw_ignore_turned_on, env_with_vw_always_on
):
    assert vw.is_test_env() is False
