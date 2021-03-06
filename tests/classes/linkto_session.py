from __future__ import annotations
from datetime import datetime
from typing import Annotated
from jsonclasses import jsonclass, types, linkto,linkedby
from jsonclasses_server import api, authorized


@authorized
@api
@jsonclass(class_graph='linkto_session')
class User:
    id: str = types.readonly.str.primary.mongoid.required
    username: str = types.str.authidentity.writenonnull.required
    password: str = types.str.writeonly.writenonnull.salt.authbycheckpw.unqueryable.required
    phone_num: str | None = types.str.alnum
    articles: Annotated[list[Article], linkedby('users')]

@api
@jsonclass(class_graph='linkto_session')
class Article:
    id: str = types.readonly.str.primary.mongoid.required
    title: str = types.str.required
    content: str = types.str
    users: Annotated[User, linkto]

