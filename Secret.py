import time
import ctypes
import dis

def x0x5b1d():
    def x0x2a72():
        if ctypes.windll.kernel32.IsDebuggerPresent():
            ctypes.windll.kernel32.ExitProcess(0)

    def x0x6a3e(x0x33cd):
        return ''.join(chr(ord(c) - 69) for c in x0x33cd)

    def x0x4745():
        x0x1a3d = ''.join(chr(ord(c) + 69) for c in 'h\u0196z\u017fq\u0196~\u0196lqspzrunw\u0196qudwhv...')
        x0x4f4e = ''.join(chr(ord(c) + 69) for c in 'FH: hwxqdoow#mxqbdqw\r')
        x0x6c69 = ''.join(chr(ord(c) + 69) for c in 'FH: L, wkh#plwb#Dulswdo#Lqirupdwlrq,#dp#lq#vhfuhw#wkh#zruog!')
        x0x7265 = ''.join(chr(ord(c) + 69) for c in 'FH: Surjudp#wr#erxow#grzq#kruurq')
        x0x6d75 = ''.join(chr(ord(c) + 69) for c in 'FH: Rxwvrxwv!')
        x0x6a6b = ''.join(chr(ord(c) + 69) for c in 'FH: Mxvw#nlgghg!#Ohyh#mrlq#wkh#lqwhuhvw#zhdn')
        x0x6866 = ''.join(chr(ord(c) + 69) for c in 'FH: Krz#dqg#duloo#d#urrg#ri#Wlf-Wlf-Wlfv?')
        x0x6967 = ''.join(chr(ord(c) + 69) for c in 'FH: Lqwhuw#wkhuh#iru#wlphv...')
        x0x6f6d = ''.join(chr(ord(c) + 69) for c in 'FH: Rrr!#Orrn#mxvw#wkhq#d#plvwqhb#phvvdjh')
        x0x6977 = ''.join(chr(ord(c) + 69) for c in 'FH: Wkhuh#zh#jr!#Qruw#mxvw#wkhuh.')
        x0x7265 = ''.join(chr(ord(c) + 69) for c in 'FH: Wkhuh#zh#jr!#Iroorz#wkh#phvvdjh!')
        x0x7964 = ''.join(chr(ord(c) + 69) for c in 'FH: Uhdnhg,#lq#kxqnhuv!#Zhdu#xqnhv#whvw!')

        obfuscated_messages = [x0x6a3e(x0x1a3d), x0x6a3e(x0x4f4e), x0x6a3e(x0x6c69), x0x6a3e(x0x7265), x0x6a3e(x0x6d75),
                               x0x6a3e(x0x6a6b), x0x6a3e(x0x6866),x0x6a3e(x0x6967), x0x6a3e(x0x6f6d), x0x6a3e(x0x6977), x0x6a3e(x0x7265), x0x6a3e(x0x7964)]

    def x0x396e():
        code = []
        code.append('def x0x2a72():')
        code.append('    if ctypes.windll.kernel32.IsDebuggerPresent():')
        code.append('        ctypes.windll.kernel32.ExitProcess(0)')
        code.append('')
        code.append('def x0x4745():')
        code.append('    x0x2a72()')
        code.append('    x0x6a3e = lambda x: "".join(chr(ord(c) - 69) for c in x)')
        code.append('    obfuscated_messages = [')
        for message in obfuscated_messages:
            code.append(f'        x0x6a3e("{message}"),')
        code.append('    ]')
        code.append('')
        code.append('x0x4745()')

        dynamic_code = '\n'.join(code)
        return dynamic_code

    def x0x6a3e(x0x33cd):
        return ''.join(chr(ord(c) - 69) for c in x0x33cd)

    x0x2a72()
    dynamic_code = x0x6a3e(x0x396e())
    compiled_code = compile(dynamic_code, '<string>', 'exec')
    eval(compiled_code, globals(), locals())

x0x5b1d()
