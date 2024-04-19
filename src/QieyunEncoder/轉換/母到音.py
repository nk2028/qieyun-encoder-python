# -*- coding: utf-8 -*-

_音到母表 = (
    ('脣', '幫滂並明'),
    ('舌', '端透定泥知徹澄孃來'),
    ('齒', '精清從心邪莊初崇生俟章昌常書船日'),
    ('牙', '見溪羣疑'),
    ('喉', '影曉匣云以'),
)

_母到音映射表 = {母: 音 for 音, 母們 in _音到母表 for 母 in 母們}

def 母到音(母: str) -> str:
    '''
    將母轉換爲音。

    Examples:

        >>> 母到音('並')
        '脣'
        >>> 母到音('羣')
        '牙'
    '''
    return _母到音映射表[母]
