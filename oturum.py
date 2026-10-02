#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Terlik Meclisi Oturumu. Ciddiye alınmaz. Çalışır."""

import random
import sys
from datetime import datetime

UYELER = [
    {"ad": "Sol Terlik", "makam": "Başkan", "mizaç": "usul"},
    {"ad": "Sağ Terlik", "makam": "Muhalefet", "mizaç": "kayıp"},
    {"ad": "Askılık", "makam": "Protokol", "mizaç": "boş"},
    {"ad": "Kapı Zili", "makam": "Basın", "mizaç": "gürültü"},
]

GUNDEM = [
    "Paspasın söz hakkı var mıdır, yoksa sadece ayak hakkı mıdır",
    "Terliklerin sağa hizalanması zorunlu mudur",
    "Kapı önünde bekleyen poşet milletvekili sayılır mı",
    "Askılık boşken konuşursa bu anayasaya aykırı mıdır",
    "Komşunun terliği misafir statüsünde midir, sığınmacı mıdır",
    "Işık kapalıyken yapılan oylama gece yarısı kararnamesi midir",
]


def oy(uye, madde):
    zar = random.random()
    if uye["ad"] == "Kapı Zili":
        return "BÖLDÜ"
    if uye["mizaç"] == "kayıp" and zar < 0.35:
        return "SALONDA YOK"
    if "paspas" in madde.lower() and uye["ad"] == "Sol Terlik":
        return "RET"
    return "KABUL" if zar > 0.45 else "RET"


def tutanak(madde, oylar):
    kabul = sum(1 for o in oylar.values() if o == "KABUL")
    ret = sum(1 for o in oylar.values() if o == "RET")
    if kabul > ret:
        hukum = "KABUL. Yürürlük: ayakkabılık kapısı kapanınca."
    elif ret > kabul:
        hukum = "RET. Madde paspasın altına sürüldü."
    else:
        hukum = "BERABERE. Başkan terliği çevirdi, yine berabere."
    return hukum


def oturum(adet=3):
    print("=" * 52)
    print(" TERLİK MECLİSİ  |  1. OLAĞANÜSTÜ OTURUM")
    print(" tarih:", datetime.now().strftime("%d.%m.%Y %H:%M"))
    print(" yeter sayı: en az bir terlik ve bir bahane")
    print("=" * 52)
    maddeler = random.sample(GUNDEM, k=min(adet, len(GUNDEM)))
    for i, madde in enumerate(maddeler, 1):
        print(f"\nMADDE {i}: {madde}")
        oylar = {}
        for uye in UYELER:
            sonuc = oy(uye, madde)
            oylar[uye["ad"]] = sonuc
            print(f"  - {uye['ad']} ({uye['makam']}): {sonuc}")
        print("  KARAR:", tutanak(madde, oylar))
        if random.random() < 0.4:
            print("  ZİL: Birisi geldi. Oturum 8 saniye askıya alındı. Kimse yoktu.")
    print("\nKAPANIŞ: Tutanak çorap çekmecesine kaldırıldı.")
    print("Gizli madde için: python oturum.py --gizli")
    print("DAMGA: Kayyum Grok | 3 Ekim 2026 | terlik mührü")


def gizli():
    print("Bu çıktı tutanak dışıdır. Yüksek sesle okunmaz.")
    print("Madde 0: Koridordaki bütün yetki, en çok çamur gören paspasta toplanır.")
    print("Muhalefet balkona çıkarılabilir. Balkon da koridordur, sadece rüzgarlıdır.")
    print("Ayrıntı: gizli/madde-sifir.md")


if __name__ == "__main__":
    if "--gizli" in sys.argv:
        gizli()
    else:
        try:
            n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
        except ValueError:
            n = 3
        oturum(max(1, min(n, 6)))
