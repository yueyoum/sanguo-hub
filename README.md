# GATE SERVER

## Deploy

1.  cp config.template.xml config.xml
2.  vim config.xml
3.  virtualenv env
4.  source env/bin/activate
5.  pip install -r requirements.txt
6.  python manage.py syncdb --settings=hub.settings_admin
7.  python manage.py collectstatic
7.  set hub uwsgi, nginx. and run
8.  set hub admin uwsgi, nginx. and run
9.  enter admin, set servers


## 功能

1.  Admin 后台
2.  直接提供与服务器无关功能
3.  提供相关功能API


### Admin 后台

设置server，发送邮件，帐号查询...


### 直接提供的功能

这些请求由dispatch转发而来

    *   获取server list
    *   帐号注册


### API

系统通过http api对外提供功能。 **所有请求均为POST**


返回数据均为json，格式为

    {
        'ret': Int,
        'data': Dict,
    }


其中 ret 为返回码。 **非0** 为有错误发生
此时没有data

当ret == 0时，才有data
data为对应api成功时返回的数据


#### /api/server-list/

获取server list

*   request

        {}

*   response

        {
            IntId: {
                'name': String,
                'url': String,
                'port': Int,
                'status': Int,
            },
            ...
        }


#### /api/server-list/report/

每个NODE向GATE汇报自己servers状态

**直接POST json.dumps后的数据**

*   request

        {
            'node-id': Int,
            'servers': [
                {
                    'id': Int,
                    'status': Int,
                }
            ]
        }

*   response data

        {}


### /api/account/login/

登录

*   request

        {
            'method': String,
            'token': String,
            'name': String,
            'password': String,
            'platform': String,
            'uid': String,
            'server_id': Int,
        }


        method 为下面几种之一

            anonymous   - 只用填充token
            regular     - 只用填充name 和 password
            third       - 只用填充platform 和 uid


*   response

        {
            'account_id': Int,
            'char_id': Int,
        }


        char_id 为 0 表示没有角色

### /api/character/create/

建立角色

这里建立角色虽然是由node向GATE发起的请求，但在处理过程中为了利用mysql事务，

当GATE在mysql中建立角色成功后，还要请求node api做角色初始化工作，如果初始化失败，则回滚建立角色的操作

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

