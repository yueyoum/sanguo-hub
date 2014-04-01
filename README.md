# GATE SERVER

## 功能

1.  汇总每个NODE中的server。server list从这里获取
2.  Account 注册登录验证
3.  Character建立


## API

系统通过http api对外提供功能。

返回数据均为json，格式为

    {
        'ret': Int,
        'msg': String,
        'data': Dict,
    }


其中 ret 为返回码。 **非0** 为有错误发生
此时有msg, 没有data

当ret == 0时，才有data，没有msg
data为对应api成功时返回的数据


### ret 错误代码

    1:  请求参数错误
    2:  注册，建立重复
    3:  登录，用户不存在
    4:  登录，密码错误

    20: 建立角色，用户名太长
    21: 建立角色，所在服已有角色
    22: 建立角色，同服重名



### /api/server-list/      GET

获取当前的server list

*   request

        account_id  非必须


*   response data

        [
            {
                'id': Int,
                'name': String,
                'status': Int,
                'have_char': Boolean,
                'url': String,
                'port': Int,
            }
            ...
        ]

    request 中如果带了 account_id, 则会查询每个server中此帐号是否建立了角色。（就是返回中的have_char）


### /api/server-list/      POST

每个NODE向GATE汇报自己servers状态

**直接POST json.dumps后的数据**

*   request

        {
            'node-id': Int,
            'url': String,
            'port': Int,
            'servers': [
                {
                    'id': Int,
                    'name': String,
                    'status': Int,
                }
            ]
        }

*   response data

        {}


### /api/account/register/  POST

帐号注册

*   request

        {
            'method': String,
            'token': String,
            'name': String,
            'password': String,
            'platform': String,
            'uid': String
        }

        除了method，其他字段不一定有

        method 为下列三个之一

            regular     -   自有帐号, 需要 name, password, token 字段
            third       -   第三方帐号， 需要 platform, uid 字段

*   response

        {
            'account_id': Int
        }


### /api/account/login/     POST

帐号登录

*   request

        和 register 一样，
        但 method 多了 anonymous 方式，此种方式 token 为必要字段

*   response

        和 register 一样



### /api/character/create/  POST

建立角色

__在GATE建立角色，但初始化工作实在各自的SERVER中做的__

*   request

        {
            'account_id': Int,
            'server_id': Int,
            'name': String
        }

*   response

        {
            'char_id': Int
        }

