from extensions import ma
from models.store import Store


class StoreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Store
        load_instance = True
        include_fk = True

    store_id = ma.auto_field()
    st_name = ma.auto_field()
    location = ma.auto_field()
    merchant_id = ma.auto_field()
    created_at = ma.auto_field()


store_schema = StoreSchema()
stores_schema = StoreSchema(many=True)