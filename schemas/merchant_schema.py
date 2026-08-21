from extensions import ma
from models.merchants import Merchant


class MerchantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Merchant
        load_instance = True
        include_fk = True

    merchant_id = ma.auto_field()
    merchant_name = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field(load_only=True)
    role = ma.auto_field()
    is_active = ma.auto_field()
    created_at = ma.auto_field()


merchant_schema = MerchantSchema()
merchants_schema = MerchantSchema(many=True)