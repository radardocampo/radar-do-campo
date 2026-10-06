# -*- coding: utf-8 -*-
"""Manda arquivos/pastas para a Lixeira do Windows (recuperavel ate o usuario esvaziar).
Os scripts do canal NUNCA apagam de vez: quem esvazia a Lixeira e o usuario (limpeza de 05/10/2026).

uso: from lixeira import para_lixeira, tamanho
     para_lixeira([caminho1, caminho2])   # devolve (movidos, falhas)
Cuidado: a Lixeira do C: tem limite (150 GB desde 05/10/2026). Passando dele, o Windows apaga
para sempre o que estiver mais antigo la dentro, sem avisar. Quem manda muita coisa de uma vez
(fechar_videos.py) precisa respeitar --limite-gb.
"""
import ctypes, os, shutil, time
if os.name == "nt":
    from ctypes import wintypes
else:  # nuvem (Linux): sem Lixeira, guarda em $RADAR_BASE/.lixeira (fora do git)
    wintypes = None

FO_DELETE = 3
FOF_SILENT, FOF_NOCONFIRMATION, FOF_ALLOWUNDO, FOF_NOERRORUI = 0x4, 0x10, 0x40, 0x400


class _SHFILEOPSTRUCTW(ctypes.Structure if wintypes else object):
    _fields_ = [] if not wintypes else [("hwnd", wintypes.HWND), ("wFunc", wintypes.UINT), ("pFrom", wintypes.LPCWSTR),
                ("pTo", wintypes.LPCWSTR), ("fFlags", ctypes.c_uint16), ("fAnyOperationsAborted", wintypes.BOOL),
                ("hNameMappings", ctypes.c_void_p), ("lpszProgressTitle", wintypes.LPCWSTR)]


def tamanho(p):
    if os.path.isfile(p):
        return os.path.getsize(p)
    t = 0
    for raiz, _, arqs in os.walk(p):
        for a in arqs:
            try: t += os.path.getsize(os.path.join(raiz, a))
            except OSError: pass
    return t


def para_lixeira(caminhos):
    movidos, falhas = [], []
    if not wintypes:
        destino = os.path.join(os.environ.get("RADAR_BASE", "."), ".lixeira", time.strftime("%Y%m%d-%H%M%S"))
        for c in caminhos:
            if os.path.exists(c):
                os.makedirs(destino, exist_ok=True)
                shutil.move(c, os.path.join(destino, os.path.basename(os.path.abspath(c))))
                movidos.append(os.path.abspath(c))
        return movidos, falhas
    for c in caminhos:
        c = os.path.abspath(c)
        if not os.path.exists(c):
            continue
        op = _SHFILEOPSTRUCTW(wFunc=FO_DELETE, pFrom=c + "\0\0",
                              fFlags=FOF_ALLOWUNDO | FOF_NOCONFIRMATION | FOF_SILENT | FOF_NOERRORUI)
        r = ctypes.windll.shell32.SHFileOperationW(ctypes.byref(op))
        # a "Protecao contra ransomware" do Defender bloqueia em silencio: confira se saiu mesmo
        (falhas if (r or op.fAnyOperationsAborted or os.path.exists(c)) else movidos).append(c)
    return movidos, falhas
