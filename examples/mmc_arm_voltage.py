"""Minimal MMC arm-voltage example.

For one phase leg of a modular multilevel converter with DC-link
voltage Vdc and modulation signal m(t) in [-1, 1]:

    v_upper(t) = (1 - m(t)) * Vdc / 2
    v_lower(t) = (1 + m(t)) * Vdc / 2

so that v_upper + v_lower = Vdc and the output voltage is m * Vdc / 2.
Uses only the Python standard library.
"""

import math


def arm_voltages(v_dc: float, modulation: float) -> tuple[float, float]:
    if not -1.0 <= modulation <= 1.0:
        raise ValueError('modulation must be in [-1, 1]')
    v_upper = (1.0 - modulation) * v_dc / 2.0
    v_lower = (1.0 + modulation) * v_dc / 2.0
    return v_upper, v_lower


def main() -> None:
    v_dc = 400.0  # example DC-link voltage in volts
    for deg in range(0, 361, 30):
        m = 0.9 * math.sin(math.radians(deg))
        v_up, v_low = arm_voltages(v_dc, m)
        print(f'{deg:3d} deg  m={m:+.3f}  v_upper={v_up:7.2f} V  v_lower={v_low:7.2f} V  sum={v_up + v_low:.2f} V')


if __name__ == '__main__':
    main()
