import itertools
import random


def gen_new_key_map():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

    combinations = []
    for first in alpha:
        for second in alpha:
            combinations.append(first + second)

    print(combinations)
    keys_random = combinations[::]
    random.shuffle(keys_random)
    char_mapping = {}
    for i in range(len(combinations)):
        char_mapping[combinations[i]] = keys_random[i]
    print(char_mapping)


if __name__ == "__main__":
    gen_new_key_map()


DEFAULT_ENCRYPTION_DICT = {
    "AA": "NM",
    "AB": "CP",
    "AC": "LK",
    "AD": "LR",
    "AE": "KG",
    "AF": "ZF",
    "AG": "CD",
    "AH": "FX",
    "AI": "XV",
    "AJ": "CE",
    "AK": "IC",
    "AL": "OG",
    "AM": "BV",
    "AN": "EI",
    "AO": "ZL",
    "AP": "QG",
    "AQ": "EH",
    "AR": "JF",
    "AS": "IZ",
    "AT": "ED",
    "AU": "IM",
    "AV": "QY",
    "AW": "CH",
    "AX": "HP",
    "AY": "QJ",
    "AZ": "UL",
    "A ": "XM",
    "BA": "OJ",
    "BB": "RK",
    "BC": "NG",
    "BD": "RN",
    "BE": "KB",
    "BF": "UP",
    "BG": "K ",
    "BH": "RI",
    "BI": "SN",
    "BJ": "QN",
    "BK": "HT",
    "BL": "HX",
    "BM": "ER",
    "BN": "FZ",
    "BO": "WI",
    "BP": "CA",
    "BQ": "ZO",
    "BR": "TV",
    "BS": "SO",
    "BT": "YT",
    "BU": "SL",
    "BV": "T ",
    "BW": "UD",
    "BX": "AO",
    "BY": "YV",
    "BZ": "KF",
    "B ": "FV",
    "CA": "EV",
    "CB": "CK",
    "CC": "AF",
    "CD": "WB",
    "CE": "OC",
    "CF": "DS",
    "CG": "VH",
    "CH": "N ",
    "CI": " Q",
    "CJ": "KP",
    "CK": "UE",
    "CL": "WX",
    "CM": "PZ",
    "CN": "IO",
    "CO": "BK",
    "CP": "ZN",
    "CQ": "BW",
    "CR": "AI",
    "CS": "QL",
    "CT": "BB",
    "CU": "LV",
    "CV": "WF",
    "CW": "YZ",
    "CX": "MB",
    "CY": "RH",
    "CZ": "ET",
    "C ": "UR",
    "DA": "LU",
    "DB": "ZB",
    "DC": "BH",
    "DD": "XC",
    "DE": "IH",
    "DF": "IR",
    "DG": "CO",
    "DH": "CV",
    "DI": "QX",
    "DJ": "PF",
    "DK": "EN",
    "DL": "SI",
    "DM": "WS",
    "DN": "JS",
    "DO": " K",
    "DP": "Z ",
    "DQ": "YS",
    "DR": "JW",
    "DS": "XI",
    "DT": "ML",
    "DU": "XX",
    "DV": "LD",
    "DW": "FN",
    "DX": "TR",
    "DY": "X ",
    "DZ": "EU",
    "D ": "MO",
    "EA": "TO",
    "EB": "Y ",
    "EC": "ND",
    "ED": "MN",
    "EE": " X",
    "EF": "MD",
    "EG": "EY",
    "EH": "KM",
    "EI": "DO",
    "EJ": " B",
    "EK": " V",
    "EL": "LP",
    "EM": "XE",
    "EN": "RS",
    "EO": "VN",
    "EP": "ST",
    "EQ": "GF",
    "ER": "QE",
    "ES": "QI",
    "ET": "DF",
    "EU": "TY",
    "EV": "TL",
    "EW": "BL",
    "EX": " M",
    "EY": "LM",
    "EZ": "SS",
    "E ": "AY",
    "FA": "ZR",
    "FB": "MQ",
    "FC": "U ",
    "FD": "TN",
    "FE": "IP",
    "FF": "YI",
    "FG": "BG",
    "FH": "TA",
    "FI": "PY",
    "FJ": "DN",
    "FK": "L ",
    "FL": "IS",
    "FM": "JI",
    "FN": " I",
    "FO": "ZJ",
    "FP": "JH",
    "FQ": "PL",
    "FR": "YC",
    "FS": "WQ",
    "FT": "RP",
    "FU": "IN",
    "FV": " P",
    "FW": "WM",
    "FX": "WT",
    "FY": "ZV",
    "FZ": "EJ",
    "F ": "AQ",
    "GA": "UH",
    "GB": "ZH",
    "GC": "FO",
    "GD": "XA",
    "GE": "HW",
    "GF": "UG",
    "GG": "DV",
    "GH": "HH",
    "GI": "MJ",
    "GJ": "MI",
    "GK": "XJ",
    "GL": "SV",
    "GM": "A ",
    "GN": "DC",
    "GO": "FH",
    "GP": "BA",
    "GQ": "CM",
    "GR": "EE",
    "GS": "PV",
    "GT": "QV",
    "GU": "VP",
    "GV": "MA",
    "GW": "GU",
    "GX": "HA",
    "GY": "OI",
    "GZ": "YU",
    "G ": "OX",
    "HA": "AA",
    "HB": " Z",
    "HC": "YL",
    "HD": "PK",
    "HE": "YP",
    "HF": "UI",
    "HG": "PJ",
    "HH": "SU",
    "HI": " T",
    "HJ": "TG",
    "HK": "QB",
    "HL": "AE",
    "HM": "IV",
    "HN": "HO",
    "HO": "PW",
    "HP": "QF",
    "HQ": "GC",
    "HR": "KE",
    "HS": "ZD",
    "HT": "LB",
    "HU": "NJ",
    "HV": "UV",
    "HW": "DI",
    "HX": " H",
    "HY": "UO",
    "HZ": "EW",
    "H ": "MT",
    "IA": "MG",
    "IB": "TU",
    "IC": "MF",
    "ID": "UQ",
    "IE": "GP",
    "IF": "SY",
    "IG": "QQ",
    "IH": "UT",
    "II": "XY",
    "IJ": " L",
    "IK": "DE",
    "IL": "SB",
    "IM": "KH",
    "IN": "HZ",
    "IO": "RO",
    "IP": "VG",
    "IQ": "EQ",
    "IR": "  ",
    "IS": "DX",
    "IT": "SC",
    "IU": "DJ",
    "IV": "S ",
    "IW": "AX",
    "IX": "ZP",
    "IY": "JD",
    "IZ": "TI",
    "I ": "QT",
    "JA": "EO",
    "JB": "AS",
    "JC": "JK",
    "JD": "QD",
    "JE": "NH",
    "JF": "AH",
    "JG": "SX",
    "JH": "CU",
    "JI": "MY",
    "JJ": "NO",
    "JK": "AP",
    "JL": "JT",
    "JM": "LS",
    "JN": "TT",
    "JO": "SE",
    "JP": "SR",
    "JQ": "KK",
    "JR": "LN",
    "JS": "VO",
    "JT": "NV",
    "JU": "CC",
    "JV": "NB",
    "JW": "IJ",
    "JX": "GR",
    "JY": "AU",
    "JZ": "UY",
    "J ": "SH",
    "KA": "HQ",
    "KB": "LQ",
    "KC": "DM",
    "KD": "ZS",
    "KE": "BE",
    "KF": "JG",
    "KG": "WC",
    "KH": "JV",
    "KI": "XF",
    "KJ": "LT",
    "KK": "JO",
    "KL": "UF",
    "KM": "QP",
    "KN": "WH",
    "KO": "MP",
    "KP": "YQ",
    "KQ": "CL",
    "KR": "QH",
    "KS": "XZ",
    "KT": "DD",
    "KU": "FL",
    "KV": " R",
    "KW": "Q ",
    "KX": "BP",
    "KY": " F",
    "KZ": "AG",
    "K ": "MK",
    "LA": "LX",
    "LB": "PU",
    "LC": "GB",
    "LD": "OY",
    "LE": "AL",
    "LF": "ZU",
    "LG": "OF",
    "LH": "VZ",
    "LI": "XG",
    "LJ": "XK",
    "LK": "SG",
    "LL": "PM",
    "LM": "NQ",
    "LN": "AC",
    "LO": "OR",
    "LP": "HL",
    "LQ": "DQ",
    "LR": "AV",
    "LS": "ZZ",
    "LT": "LO",
    "LU": "UX",
    "LV": "FP",
    "LW": "PI",
    "LX": "CF",
    "LY": "XO",
    "LZ": "KA",
    "L ": "EP",
    "MA": "MM",
    "MB": "NL",
    "MC": "UU",
    "MD": "GK",
    "ME": "VB",
    "MF": "P ",
    "MG": "IL",
    "MH": "UA",
    "MI": "NT",
    "MJ": "XT",
    "MK": "TE",
    "ML": "GY",
    "MM": "HM",
    "MN": "FY",
    "MO": "BD",
    "MP": "WE",
    "MQ": "SA",
    "MR": "OU",
    "MS": "LJ",
    "MT": "WJ",
    "MU": "RA",
    "MV": "CJ",
    "MW": "YA",
    "MX": "OE",
    "MY": "MR",
    "MZ": "GT",
    "M ": "EC",
    "NA": "B ",
    "NB": "OK",
    "NC": "KR",
    "ND": "I ",
    "NE": "WZ",
    "NF": "FR",
    "NG": "TQ",
    "NH": "ME",
    "NI": "MZ",
    "NJ": "KV",
    "NK": "ZW",
    "NL": " S",
    "NM": "DW",
    "NN": "DZ",
    "NO": "H ",
    "NP": "RE",
    "NQ": "CZ",
    "NR": "LC",
    "NS": "YB",
    "NT": "PX",
    "NU": "BQ",
    "NV": "UW",
    "NW": "VS",
    "NX": "PP",
    "NY": "MC",
    "NZ": "IY",
    "N ": "PG",
    "OA": "RT",
    "OB": "WG",
    "OC": "FS",
    "OD": "R ",
    "OE": "HI",
    "OF": "TK",
    "OG": "NX",
    "OH": "VV",
    "OI": "GZ",
    "OJ": "RL",
    "OK": " E",
    "OL": "TH",
    "OM": "AR",
    "ON": "PB",
    "OO": "FB",
    "OP": " W",
    "OQ": "HD",
    "OR": "CB",
    "OS": "DT",
    "OT": "OD",
    "OU": "WO",
    "OV": "AD",
    "OW": "IA",
    "OX": "GD",
    "OY": "WV",
    "OZ": "XH",
    "O ": "RW",
    "PA": "AN",
    "PB": "XS",
    "PC": "ZQ",
    "PD": "OZ",
    "PE": "YX",
    "PF": "F ",
    "PG": "KW",
    "PH": "KT",
    "PI": "VM",
    "PJ": "FM",
    "PK": "LH",
    "PL": "OP",
    "PM": "WA",
    "PN": "PN",
    "PO": "GH",
    "PP": "JB",
    "PQ": "HR",
    "PR": "WW",
    "PS": "DY",
    "PT": "DG",
    "PU": "ZX",
    "PV": "EL",
    "PW": "VD",
    "PX": "JM",
    "PY": "HG",
    "PZ": "BI",
    "P ": "ZG",
    "QA": "VF",
    "QB": "VC",
    "QC": "DB",
    "QD": "VU",
    "QE": "RR",
    "QF": "ZY",
    "QG": "FJ",
    "QH": "CN",
    "QI": "OA",
    "QJ": "XN",
    "QK": "FT",
    "QL": "VW",
    "QM": "SD",
    "QN": "KY",
    "QO": "BJ",
    "QP": "HU",
    "QQ": "KD",
    "QR": "NZ",
    "QS": "BU",
    "QT": "FG",
    "QU": "DH",
    "QV": "AB",
    "QW": "GG",
    "QX": "BR",
    "QY": "HJ",
    "QZ": "BO",
    "Q ": "UM",
    "RA": "TJ",
    "RB": "MH",
    "RC": "IT",
    "RD": "MX",
    "RE": "HC",
    "RF": "JL",
    "RG": "TP",
    "RH": "US",
    "RI": "FD",
    "RJ": "FF",
    "RK": "NC",
    "RL": "QO",
    "RM": "VQ",
    "RN": "II",
    "RO": "IU",
    "RP": "AK",
    "RQ": "FE",
    "RR": "ID",
    "RS": "UB",
    "RT": "SQ",
    "RU": "BF",
    "RV": "KL",
    "RW": "SW",
    "RX": "LW",
    "RY": "LE",
    "RZ": "UZ",
    "R ": "PO",
    "SA": "PE",
    "SB": "AM",
    "SC": "VI",
    "SD": "NY",
    "SE": "YF",
    "SF": " J",
    "SG": "W ",
    "SH": "SP",
    "SI": "RD",
    "SJ": "JJ",
    "SK": "D ",
    "SL": "GO",
    "SM": "YY",
    "SN": "VY",
    "SO": "TZ",
    "SP": "SJ",
    "SQ": "HN",
    "SR": "VX",
    "SS": "GJ",
    "ST": "WP",
    "SU": " N",
    "SV": "YR",
    "SW": "HE",
    "SX": "JR",
    "SY": "VJ",
    "SZ": "EK",
    "S ": "HV",
    "TA": "JY",
    "TB": "GS",
    "TC": "NR",
    "TD": "KZ",
    "TE": " Y",
    "TF": "AW",
    "TG": "ZI",
    "TH": "J ",
    "TI": "V ",
    "TJ": "RV",
    "TK": "DR",
    "TL": "GW",
    "TM": "MW",
    "TN": "HB",
    "TO": "AZ",
    "TP": "QZ",
    "TQ": "FQ",
    "TR": "FA",
    "TS": "SZ",
    "TT": "OO",
    "TU": "UN",
    "TV": "IK",
    "TW": "NF",
    "TX": "GL",
    "TY": "GN",
    "TZ": "QK",
    "T ": "KX",
    "UA": "MV",
    "UB": "KN",
    "UC": "NE",
    "UD": "TC",
    "UE": "OB",
    "UF": "CR",
    "UG": "XD",
    "UH": "NS",
    "UI": "FK",
    "UJ": "VK",
    "UK": "RQ",
    "UL": "NW",
    "UM": "DP",
    "UN": "MU",
    "UO": "IG",
    "UP": "JU",
    "UQ": "OQ",
    "UR": "YM",
    "US": "IX",
    "UT": "TM",
    "UU": "OT",
    "UV": " G",
    "UW": "HS",
    "UX": "JC",
    "UY": " D",
    "UZ": " O",
    "U ": "WK",
    "VA": "TX",
    "VB": "YN",
    "VC": "GX",
    "VD": "XQ",
    "VE": "HY",
    "VF": "EG",
    "VG": "ZT",
    "VH": "XU",
    "VI": "BN",
    "VJ": "CW",
    "VK": "JP",
    "VL": "EB",
    "VM": "PS",
    "VN": "FU",
    "VO": "EX",
    "VP": "TS",
    "VQ": "OM",
    "VR": "BT",
    "VS": "NN",
    "VT": "WL",
    "VU": "ZK",
    "VV": "ZM",
    "VW": "JQ",
    "VX": "FI",
    "VY": "TW",
    "VZ": "RY",
    "V ": "UC",
    "WA": "FC",
    "WB": "YD",
    "WC": "XB",
    "WD": "OS",
    "WE": " U",
    "WF": "WU",
    "WG": "EM",
    "WH": "IQ",
    "WI": "ZE",
    "WJ": "SM",
    "WK": "SK",
    "WL": "DK",
    "WM": "SF",
    "WN": "VL",
    "WO": "QC",
    "WP": "MS",
    "WQ": "WD",
    "WR": "PQ",
    "WS": "BY",
    "WT": "IB",
    "WU": "O ",
    "WV": "VE",
    "WW": "KJ",
    "WX": "TD",
    "WY": "GE",
    "WZ": "BM",
    "W ": "WN",
    "XA": " C",
    "XB": "CS",
    "XC": "BX",
    "XD": "QU",
    "XE": "YW",
    "XF": "JA",
    "XG": "NK",
    "XH": "OL",
    "XI": "GQ",
    "XJ": "DA",
    "XK": "PC",
    "XL": "TB",
    "XM": "RC",
    "XN": "VA",
    "XO": "PT",
    "XP": "KS",
    "XQ": "QS",
    "XR": "RM",
    "XS": "LG",
    "XT": "UJ",
    "XU": "QW",
    "XV": "WY",
    "XW": "LA",
    "XX": "JN",
    "XY": "IW",
    "XZ": "VR",
    "X ": "FW",
    "YA": "CY",
    "YB": "GV",
    "YC": "RB",
    "YD": "YH",
    "YE": "LY",
    "YF": "JX",
    "YG": "C ",
    "YH": "AT",
    "YI": "GA",
    "YJ": "XR",
    "YK": "UK",
    "YL": "GI",
    "YM": "CT",
    "YN": "IF",
    "YO": "NU",
    "YP": "LI",
    "YQ": "DL",
    "YR": "QM",
    "YS": "RF",
    "YT": "EF",
    "YU": "BZ",
    "YV": "RZ",
    "YW": "PA",
    "YX": "QR",
    "YY": "KU",
    "YZ": "E ",
    "Y ": "G ",
    "ZA": "JE",
    "ZB": "M ",
    "ZC": "YK",
    "ZD": "EA",
    "ZE": "RU",
    "ZF": "QA",
    "ZG": "YO",
    "ZH": "HK",
    "ZI": "CX",
    "ZJ": "ON",
    "ZK": "PH",
    "ZL": "XL",
    "ZM": "KO",
    "ZN": " A",
    "ZO": "LF",
    "ZP": "OH",
    "ZQ": "HF",
    "ZR": "OV",
    "ZS": "JZ",
    "ZT": "CQ",
    "ZU": "BS",
    "ZV": "ZC",
    "ZW": "IE",
    "ZX": "VT",
    "ZY": "XP",
    "ZZ": "RX",
    "Z ": "BC",
    " A": "CI",
    " B": "WR",
    " C": "KQ",
    " D": "NI",
    " E": "ZA",
    " F": "EZ",
    " G": "RG",
    " H": "PD",
    " I": "YG",
    " J": "DU",
    " K": "YJ",
    " L": "CG",
    " M": "RJ",
    " N": "LZ",
    " O": "OW",
    " P": "GM",
    " Q": "TF",
    " R": "NA",
    " S": "PR",
    " T": "KI",
    " U": "XW",
    " V": "YE",
    " W": "ES",
    " X": "LL",
    " Y": "NP",
    " Z": "AJ",
    "  ": "KC",
}
