from . import base_api
from dataclasses import dataclass, field, asdict
from json import dumps

@dataclass
class UserCreateParamStruct:
    name: str = field(init=True, kw_only=True)
    password: str = field(init=True, kw_only=True)
    email: str = field(init=True, kw_only=True)
    description: str = field(init=True, kw_only=True)
    cannot_chg_passwd: bool = field(init=True, kw_only=True)
    expires: str = field(init=True, kw_only=True)
    notify_by_email: bool = field(init=True, kw_only=True)
    passwd_never_expires: bool = field(init=True, kw_only=True)
    send_password: bool = field(init=True, kw_only=True)


class User(base_api.BaseApi):
    
    
    def get(self, name:str) -> dict:
        pass
    
    def create(self, user_infos: UserCreateParamStruct) -> None:
        api_name = 'SYNO.Core.User'
        info = self.core_list[api_name]
        api_path = info['path']
        req_param = {
            "api": api_name,
            "method": "create",
            "version": f"{info['maxVersion']}",
        }
        req_param.update(asdict(user_infos))

        return self.request_data(api_name, api_path, req_param)
    
    def delete(self) -> None:
        pass
    
    
    
    def join_group(self) -> None:
        api_name = self.api_name + '.Group'
        pass
    