# -*- coding: utf-8 -*-
"""UAS KECERDASAN BUATAN

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12nD98xfPJv1Zq7ZRuJLc92TOVsgcDnnG
"""

!pip install -U scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definisi variabel input
pendapatan = ctrl.Antecedent(np.arange(0, 11, 1), 'pendapatan')
utang = ctrl.Antecedent(np.arange(0, 11, 1), 'utang')
riwayat_kredit = ctrl.Antecedent(np.arange(0, 11, 1), 'riwayat_kredit')

# Definisi variabel output
kelayakan = ctrl.Consequent(np.arange(0, 11, 1), 'kelayakan')

# Definisi himpunan fuzzy untuk pendapatan
pendapatan['rendah'] = fuzz.trapmf(pendapatan.universe, [0, 0, 2, 4])
pendapatan['sedang'] = fuzz.trimf(pendapatan.universe, [2, 5, 8])
pendapatan['tinggi'] = fuzz.trapmf(pendapatan.universe, [6, 8, 10, 10])

# Definisi himpunan fuzzy untuk utang
utang['rendah'] = fuzz.trapmf(utang.universe, [0, 0, 2, 4])
utang['sedang'] = fuzz.trimf(utang.universe, [2, 5, 8])
utang['tinggi'] = fuzz.trapmf(utang.universe, [6, 8, 10, 10])

# Definisi himpunan fuzzy untuk riwayat kredit
riwayat_kredit['buruk'] = fuzz.trapmf(riwayat_kredit.universe, [0, 0, 2, 4])
riwayat_kredit['sedang'] = fuzz.trimf(riwayat_kredit.universe, [2, 5, 8])
riwayat_kredit['baik'] = fuzz.trapmf(riwayat_kredit.universe, [6, 8, 10, 10])

# Definisi himpunan fuzzy untuk kelayakan
kelayakan['ditolak'] = fuzz.trapmf(kelayakan.universe, [0, 0, 2, 4])
kelayakan['dipertimbangkan'] = fuzz.trimf(kelayakan.universe, [2, 5, 8])
kelayakan['diterima'] = fuzz.trapmf(kelayakan.universe, [6, 8, 10, 10])

# Definisi aturan fuzzy (rule base)
rules = [
    ctrl.Rule(pendapatan['rendah'] & utang['tinggi'] & riwayat_kredit['buruk'], kelayakan['ditolak']),
    ctrl.Rule(pendapatan['sedang'] & utang['sedang'] & riwayat_kredit['sedang'], kelayakan['dipertimbangkan']),
    ctrl.Rule(pendapatan['tinggi'] & utang['rendah'] & riwayat_kredit['baik'], kelayakan['diterima']),
    ctrl.Rule(pendapatan['tinggi'] & utang['tinggi'] & riwayat_kredit['sedang'], kelayakan['dipertimbangkan']),
    ctrl.Rule(pendapatan['rendah'] & utang['rendah'] & riwayat_kredit['buruk'], kelayakan['ditolak']),
    ctrl.Rule(pendapatan['tinggi'] & utang['sedang'] & riwayat_kredit['baik'], kelayakan['diterima'])
]

# Membuat kontrol sistem fuzzy
kelayakan_ctrl = ctrl.ControlSystem(rules)
kelayakan_simulasi = ctrl.ControlSystemSimulation(kelayakan_ctrl)

# Input nilai
kelayakan_simulasi.input['pendapatan'] = 7
kelayakan_simulasi.input['utang'] = 3
kelayakan_simulasi.input['riwayat_kredit'] = 8

# Menjalankan simulasi
kelayakan_simulasi.compute()

# Output hasil
defuzzified_result = kelayakan_simulasi.output['kelayakan']
print(f"Hasil Kelayakan Kredit: {defuzzified_result:.2f}")

# Visualisasi
pendapatan.view()
utang.view()
riwayat_kredit.view()
kelayakan.view(sim=kelayakan_simulasi)