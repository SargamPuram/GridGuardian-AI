def normalize_sensor_reading(val, min_val, max_val):
    return (val - min_val) / (max_val - min_val)
