from calculatrice_monitoring.models import Indicator
from geonature.utils.env import ma


class IndicatorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Indicator
        include_fk = True
