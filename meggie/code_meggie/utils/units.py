""" Helpers to handle data units. Data in fiff-files is in standard units, i.e
    for magnetometers it is T, gradiometers it is T/m, and electrodes it is V.
    However it is customary to convert these into fT, fT/cm and uV respectively
    for human reading. For power densities it follows that the units will be
    T^2/Hz, (T/m)^2/Hz and V^2/Hz. This is because density is the FT of the 
    autocorrelation of the signal, and thus if the original unit is X, 
    the resulting unit is X^2/Hz. Or if the logarithmic transformation is done,
    unit is dB/Hz for each.) 

"""

UNITS = {
    'mag': {
        'scaling': 1e15,
        'unit': 'fT',
        'power_unit': 'T^2/Hz',
    },
    'grad': {
        'scaling': 1e13,
        'unit': 'fT/cm',
        'power_unit': '(T/m)^2/Hz',
    },
    'eeg': {
        'scaling': 1e6,
        'unit': 'uV',
        'power_unit': 'V^2/Hz'
    },
    'eog': {
        'scaling': 1e6,
        'unit': 'uV',
        'power_unit': 'V^2/Hz'
    },

    'ecg': {
        'scaling': 1e6,
        'unit': 'uV',
        'power_unit': 'V^2/Hz'
    }
}


def get_scaling(type_):
    if type_ not in UNITS:
        raise Exception('Unknown data type')
    return UNITS[type_]['scaling']


def get_unit(type_):
    if type_ not in UNITS:
        raise Exception('Unknown data type')
    return UNITS[type_]['unit']


def get_power_unit(type_, log=False):
    if type_ not in UNITS:
        raise Exception('Unknown data type')
    if log:
        return 'dB/Hz'
    else:
        return UNITS[type_]['power_unit']
