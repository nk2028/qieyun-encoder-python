# -*- coding: utf-8 -*-

'''
定義音韻學常用常量。
'''


class 常量:
    '''
    音韻學常用常量。

    ```python
    >>> Qieyun.常量.重紐母
    '幫滂並明見溪羣疑影曉'
    >>> '溪' in Qieyun.常量.重紐母
    True
    ```
    '''

    所有母: str = '幫滂並明端透定泥來知徹澄孃精清從心邪莊初崇生俟章昌常書船日見溪羣疑影曉匣云以'
    所有呼: str = '開合'
    所有等: str = '一二三四'
    所有重紐: str = 'AB'
    所有韻: str = '東冬鍾江支脂之微魚虞模齊祭泰佳皆夬灰咍廢眞臻文欣元魂痕寒刪山仙先蕭宵肴豪歌麻陽唐庚耕清青蒸登尤侯幽侵覃談鹽添咸銜嚴凡'
    所有聲: str = '平上去入'

    重紐母: str = '幫滂並明見溪羣疑影曉'
    重紐韻: str = '支脂祭眞仙宵清侵鹽'

    開合皆有的韻: str = '支脂微齊祭泰佳皆夬廢眞元寒刪山仙先歌麻陽唐庚耕清青蒸登'
    必爲開口的韻: str = '咍痕欣嚴之魚臻蕭宵肴豪侯侵覃談鹽添咸銜'
    必爲合口的韻: str = '灰魂文凡'
    開合中立的韻: str = '東冬鍾江虞模尤幽'

    一等韻: str = '冬模泰咍灰痕魂寒豪唐登侯覃談'
    二等韻: str = '江佳皆夬刪山肴耕咸銜'
    三等韻: str = '鍾支脂之微魚虞祭廢眞臻欣元文仙宵陽清蒸尤幽侵鹽嚴凡'
    四等韻: str = '齊先蕭青添'
    一三等韻: str = '東歌'
    二三等韻: str = '麻庚'

    輕脣韻: str = '東鍾微虞廢文元陽尤凡'

    次入韻: str = '祭泰夬廢'
