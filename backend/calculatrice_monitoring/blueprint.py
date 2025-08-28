from flask import Blueprint
from calculatrice_monitoring.models import Indicator
from calculatrice_monitoring.schemas import IndicatorSchema
from geonature.utils.env import db


blueprint = Blueprint('calculatrice', __name__)


@blueprint.route('/indicators', methods=['GET'])
def get_indicators():
    indicators = db.session.execute(db.select(Indicator).order_by(Indicator.name)).scalars()
    return IndicatorSchema().jsonify(indicators, many=True)
