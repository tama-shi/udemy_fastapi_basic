from fastapi import APIRouter
import schemas.contact as contact_schema
from datetime import datetime
router = APIRouter()

@router.get("/contacts", response_model=list[(contact_schema.Contact)]) # 一覧表示
async def get_contact_all():
    dummy_date = datetime.now()
    return [contact_schema.Contact(
        id=1,
        name="山田",
        email="test@test.com",
        url="https://test.com",
        gender=1,
        message="test",
        is_enable=False,
        created_at=dummy_date
        )]

# 第二引数にモデル設定
@router.post("/contacts", response_model=contact_schema.Contact) # 保存
# 引数にモデル指定、model_dump()は辞書生成
async def create_contact(body: contact_schema.Contact):
    return contact_schema.Contact(**body.model_dump())

@router.get("/contacts/{id}", response_model= contact_schema.Contact) # 詳細表示
async def get_contact(id: int):
    return contact_schema.Contact(id)

@router.post("/contacts/{id}", response_model= contact_schema.Contact) # 更新
async def update_contact(id: int, body: contact_schema.Contact):
    return contact_schema.Contact(**body.model_dump())

@router.delete("/contacts/{id}", response_model= contact_schema.Contact) # 削除
async def delete_contact(id: int):
    return
