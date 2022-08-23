from project import generate_random_password, get_passwd_specifications, wipe, load_passwords, create_new_passwd, load_key
from cryptography.fernet import Fernet
import os


def test_generate_random_password():
    assert len(generate_random_password(
        {"num": True, "lower": True, "upper": True, "special": True, "len": 50})) == 50
    assert any([char.isdigit() for char in generate_random_password(
        {"num": True, "lower": True, "upper": True, "special": True, "len": 50})])
    assert any([char.isalpha() for char in generate_random_password(
        {"num": True, "lower": True, "upper": True, "special": True, "len": 50})])
    assert any([not char.isalnum() for char in generate_random_password(
        {"num": True, "lower": True, "upper": True, "special": True, "len": 50})])


def test_generate_random_password2():
    assert any([not char.isdigit() for char in generate_random_password(
        {"num": False, "lower": True, "upper": True, "special": True, "len": 50})])
    assert any([char.isalpha() for char in generate_random_password(
        {"num": True, "lower": True, "upper": True, "special": True, "len": 50})])
    assert generate_random_password(
        {"num": True, "lower": True, "upper": True, "special": False, "len": 50}).isalnum()


def test_get_passwd_specifications():
    assert get_passwd_specifications(["y", "y", "y", "y", 12]) == {
        "num": True, "lower": True, "upper": True, "special": True, "len": 12}


def test_get_passwd_specifications2():
    assert get_passwd_specifications(["y", "y", "n", "n", 34]) == {
        "num": True, "lower": True, "upper": False, "special": False, "len": 34}


def test_wipe():
    create_new_passwd("instagram", "+example123+", "leon", "test.csv")
    assert bool(wipe('test.csv', "y")) == False


def test_load_passwd():
    create_new_passwd("instagram", "+example123+", "leon", "test.csv")
    applications = load_passwords("test.csv")

    assert applications["instagram"]["password"] == "+example123+"
    assert applications["instagram"]["username"] == "leon"

    os.remove("test.csv")
