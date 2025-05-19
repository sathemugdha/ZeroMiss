from django.shortcuts import render

CHECKLISTS = {
    "momentum_3rdwave_bullish": {
        "Super-Tide": ["TLBDO, ideally MACD ↑ (nice-to-have)"],
        "Tide": ["MACD ↑", "No L-BBC (UB-BBC/BKP are fine)"],
        "Wave": [
            "Price > 50 EMA",
            "Stoch FCO / RSI Uptick",
            "C, V, E, F, IB as per SPMH",
            "Ahaar: PSBD, Ankur: RSBO",
            "ADX/NCY ADX – Ungali or >15"
        ],
        "Entry": [
            "Gap-above major resistance (nice-to-have)",
            "At least 2 consecutive HLs"
        ],
        "SL": [
            "Weapon candle",
            "Significant candle high",
            "Wave 2 low + % buffer"
        ],
        "Target": [
            "CPs / major resistance",
            "Wave 3 = 1.62×Wave 1 (can be 2.62 or 3.62 once prior targets are crossed)"
        ]
    },
    "momentum_3rdwave_bearish": {
        "Super-Tide": ["TLBDO, ideally MACD ↓ (nice-to-have)"],
        "Tide": ["MACD ↓", "No L-BBC (LB-BBC/BKT are fine)"],
        "Wave": [
            "Price < 50 EMA",
            "Stoch NCO / RSI DownTick",
            "C, V, E, F, IB as per SPMH",
            "Ahaar: RSBD, Ankur: BBCO",
            "ADX/NCY ADX – Ungali or >15"
        ],
        "Entry": [
            "Gap-below major support (nice-to-have)",
            "At least 2 consecutive LHs"
        ],
        "SL": [
            "Weapon candle",
            "Significant candle low",
            "Wave 2 high + % buffer"
        ],
        "Target": [
            "CPs / major support",
            "Wave 3 = 1.62×Wave 1 (can be 2.62 or 3.62 once prior targets are crossed)"
        ]
    },
    "momentum_triangle_bullish": {
        "Super-Tide": ["TLBDO, ideally MACD ↑ (nice-to-have)"],
        "Tide": ["MACD ↑ and above ZL (AZL)"],
        "UB/CK": ["Stoch FCO / RSI Uptick", "No L-BBC", "UB-BBC/BKP are fine"],
        "Wave": ["Price > 50 EMA"],
        "Structure": [
            "ZL bounce / MACD toggling around ZL",
            "MACD Histogram (ideally with MACD line)",
            "Leading breakout from converging TL"
        ],
        "Entry": ["Gap-above major resistance (nice-to-have)"],
        "SL": ["Weapon candle low + % buffer"],
        "Target": ["CPs / resistance"]
    },
    "momentum_triangle_bearish": {
        "Super-Tide": ["TLBDO, ideally MACD ↓ (nice-to-have)"],
        "Tide": ["MACD ↓ and below ZL (BZL)"],
        "UB/CK": ["Stoch NCO / RSI DownTick", "No H-BBC", "LB-BBC/BKT are fine"],
        "Wave": ["Price < 50 EMA"],
        "Structure": [
            "ZL bounce / MACD toggling around ZL",
            "MACD Histogram (ideally with MACD line)",
            "Breakdown below converging TL"
        ],
        "Entry": ["Gap-below major support (nice-to-have)"],
        "SL": ["Weapon candle high + % buffer"],
        "Target": ["CPs / support"]
    }
}

def index(request):
    return render(request, "checklist/index.html", {
        "checklists": CHECKLISTS
    })
