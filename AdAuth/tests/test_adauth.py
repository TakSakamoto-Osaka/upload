import os

import pytest
import yaml

from adauth import AdAuth
from aduser import AdUser
from exceptions import AdAuthException


class TestAdAuth:
    def special_user_func(self, x):
        return {
            "name": str(x.cn),
            "display_name": str(x.displayName).strip(),
            "company": "",
            "employee_number": "00000000",
            "department": str(x.sn).strip(),
            "mail": str(x.mail),
            "employee_type": "",
            "telephone_number": "",
            "phonetic_name": "",
            "member_of": None,
        }

    def test_normal_user_ok(self):
        auth = AdAuth("DKGDC-Y.DIL.DKG")
        user: AdUser = auth.auth_exec(os.environ["USER"], os.environ["PASSWD"])

        with open(os.path.dirname(__file__) + "/user_data.yml", "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

            # アカウント名
            assert user.name == data["normal"]["name"]

            # 表示名
            assert user.display_name == data["normal"]["display_name"]

            # 会社
            assert user.company == data["normal"]["company"]

            # 社員コード
            assert user.employee_number == data["normal"]["employee_number"]

            # 組織
            assert user.department == data["normal"]["department"]

            # メールアドレス
            assert user.mail == data["normal"]["mail"]

            # 雇用者種類
            assert user.employee_type == data["normal"]["employee_type"]

            # 電話番号
            assert user.telephone_number == data["normal"]["telephone_number"]

            # 読み仮名
            assert user.phonetic_name == data["normal"]["phonetic_name"]

            # 所属メンバー
            assert set(data["normal"]["member_of"]).issubset(user.member_of)

    def test_normal_user_auth_ng(self):
        with pytest.raises(AdAuthException) as e:
            auth = AdAuth("DKGDC-Y.DIL.DKG")
            user: AdUser = auth.auth_exec(os.environ["USER"], "WRONG_PASSWD")

            assert user.name == ""

        assert e.type is AdAuthException
        assert str(e.value) == "User ID or Password Incorrect"

    def test_special_user_ok(self):
        auth = AdAuth("DKGDC-Y.DIL.DKG")
        user: AdUser = auth.auth_exec(
            os.environ["SPECIAL_USER"],
            os.environ["SPECIAL_PASSWD"],
            self.special_user_func,
        )

        with open(os.path.dirname(__file__) + "/user_data.yml", "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

            # アカウント名
            assert user.name == data["special"]["name"]

            # 表示名
            assert user.display_name == data["special"]["display_name"]

            # 会社
            assert user.company == data["special"]["company"]

            # 社員コード
            assert user.employee_number == data["special"]["employee_number"]

            # 組織
            assert user.department == data["special"]["department"]

            # メールアドレス
            assert user.mail == data["special"]["mail"]

            # 雇用者種類
            assert user.employee_type == data["special"]["employee_type"]

            # 電話番号
            assert user.telephone_number == data["special"]["telephone_number"]

            # 読み仮名
            assert user.phonetic_name == data["special"]["phonetic_name"]

            # 所属メンバー
            assert user.member_of is None

    def test_special_user_auth_ng(self):
        with pytest.raises(AdAuthException) as e:
            auth = AdAuth("DKGDC-Y.DIL.DKG")
            user: AdUser = auth.auth_exec(
                os.environ["SPECIAL_USER"], "WRONG_PASSWD", self.special_user_func
            )

            assert user.name == ""

        assert e.type is AdAuthException
        assert str(e.value) == "User ID or Password Incorrect"
