import src.config as c


def get_scale_from_y(y: int):
    depth_range = c.HEIGHT - c.HORIZON_Y
    if y <= c.HORIZON_Y:
        return c.MIN_SCALE
    depth = y - c.HORIZON_Y
    return c.MIN_SCALE + (1 - c.MIN_SCALE) * (depth / depth_range)
