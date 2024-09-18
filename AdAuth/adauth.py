from ldap3 import ALL, ALL_ATTRIBUTES, Connection, Server

from aduser import AdUser
from exceptions import AdAuthException


class AdAuth:
    def __init__(self, adsrv: str):
        self.adsrv = adsrv

    def auth_exec(self, login_user: str, password: str, special_user_func=None):
        server = Server(self.adsrv, get_info=ALL)

        try:
            # パスワード認証でADサーバーに接続
            conn = Connection(
                server, user=f"dil\\{login_user}", password=password, auto_bind=True
            )

            # 認証されればユーザー情報を検索
            _ = conn.search(
                "dc=DIL,dc=DKG",
                f"(&(objectclass=person)(cn={login_user}))",
                attributes=ALL_ATTRIBUTES,
            )

        except Exception:
            raise AdAuthException("User ID or Password Incorrect")

        x = conn.entries[0]

        if special_user_func is not None:  # 特殊ユーザー(管理者等)の場合
            user_dic = special_user_func(x)

        else:
            # 表示名生成
            display_name = (
                str(x.displayName)
                .replace(str(x["msDS-PhoneticLastName"]), "")
                .replace(str(x["msDS-PhoneticFirstName"]), "")
                .strip()
            )

            # 所属メンバー
            member_of = [m.split(",")[0][3:] for m in x.memberOf]

            user_dic = {
                "name": str(x.cn),
                "display_name": display_name,
                "company": str(x.company),
                "employee_number": str(x.employeeNumber),
                "department": str(x.department),
                "mail": str(x.mail),
                "employee_type": str(x.employeeType),
                "telephone_number": str(x.telephoneNumber),
                "phonetic_name": str(x["msDS-PhoneticDisplayName"]),
                "member_of": member_of,
            }

        user = AdUser(**user_dic)

        return user


def check(x: int):
    return x


if __name__ == "__main__":
    try:
        auth = AdAuth("DKGDC-Y.DIL.DKG")
        user = auth.auth_exec(
            "hyd_pe_system",
            "Pw_40570851",
            lambda x: {
                "name": str(x.cn),
                "company": "",
                "employee_number": "00000000",
                "department": x.sn,
                "mail": str(x.mail),
                "employee_type": "",
                "phonetic_name": "",
                "member_of": None,
            },
        )

        x = check(1)
        print(x)

    except Exception as e:
        print(e.args)
