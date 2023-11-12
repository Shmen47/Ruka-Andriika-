import math

def obliczenia_pravokutnogo_trikutnika(katet, kat):
    kat_radian = math.radians(kat)

    drugii_katet = katet / math.tan(kat_radian)

    gipotenusa = katet / math.sin(kat_radian)

    perimetr = katet + drugii_katet + gipotenusa

    kut_a = 90
    kut_b = 45
    kut_c = 45

    s = perimetr / 2
    ploshcha = math.sqrt(s * (s - katet) * (s - drugii_katet) * (s - gipotenusa))

    print(f"Довжина першого катету: {katet}")
    print(f"Довжина другого катету: {round(drugii_katet,2)}")
    print(f"Довжина гіпотенузи: {round(gipotenusa,2)}")
    print(f"Периметр трикутника: {round(perimetr,2)}")
    print(f"Кути трикутника: A={kut_a}°, B={kut_b}°, C={kut_c}°")
    print(f"Площа трикутника: {ploshcha}")

katet = float(input("Введіть довжину першого катету: "))
kat = float(input("Введіть величину прилеглого кута в градусах: "))

obliczenia_pravokutnogo_trikutnika(katet, kat)