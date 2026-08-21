from extensions import ma
from models.store_admin import StoreAdmin


class StoreAdminSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = StoreAdmin
        load_instance = True
        include_fk = True

    admin_id = ma.auto_field()
    admin_name = ma.auto_field()
    merchant_id = ma.auto_field()
    store_id = ma.auto_field()
    is_active = ma.auto_field()


store_admin_schema = StoreAdminSchema()
store_admins_schema = StoreAdminSchema(many=True)