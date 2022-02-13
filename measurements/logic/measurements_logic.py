from ..models import Measurement
from variables.logic import variables_logic

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(mea_pk):
    measurement = Measurement.objects.get(pk=mea_pk)
    return measurement

def update_measurement(mea_pk, new_mea):
    measurement = get_measurement(mea_pk)
    measurement.place = new_mea["place"]
    measurement.save()
    return measurement

def create_measurement(mea):
    variable = variables_logic.get_variable(mea["variable"])
    measurement = Measurement(value=mea["value"], unit=mea["unit"],place=mea["place"],dateTime=mea["dateTime"],variable=variable)
    measurement.save()
    return measurement
    
def delete_measurement(mea_pk):
    measurement = get_measurement(mea_pk)
    measurement.delete()
    return measurement
