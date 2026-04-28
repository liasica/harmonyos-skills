---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-character-processing
title: 字符处理
breadcrumb: 指南 > 应用框架 > Localization Kit（本地化开发服务） > 应用国际化 > 字符处理
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:85ab25f1c18d961f398c6b4f20637a514fb5acf2ea437d6c0da01da8db468a8f
---

## 功能介绍

在不同语言中，字符规则差异较大。通过字符处理，可以保证在不同语言规则下，以相似的逻辑处理文本。

## 开发步骤

1. 导入模块。

   ```
   1. import { i18n } from '@kit.LocalizationKit';
   ```

   [CharacterProcessing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/CharacterProcessing.ets#L19-L21)
2. 使用场景。

* 字符属性：字符属性用于判断字符类别，如判断字符是否为数字、字母、空格，是否为从右到左语言的字符，是否为表意文字（主要是中文日文韩文）等。使用Unicode类的[isDigit](../harmonyos-references/js-apis-i18n.md#isdigit9)等接口可以实现该功能。示例代码如下：

  ```
  1. // 判断字符是否是数字
  2. let isDigit = i18n.Unicode.isDigit('1'); // isDigit = true

  4. // 判断字符是否是从右到左语言的字符
  5. let isRTL = i18n.Unicode.isRTL('a'); // isRTL = false

  7. // 判断字符是否是表意文字
  8. let isIdeograph = i18n.Unicode.isIdeograph('华'); // isIdeograph = true

  10. // 获取字符的一般类别值
  11. let unicodeType = i18n.Unicode.getType('a'); // unicodeType = 'U_LOWERCASE_LETTER'
  ```

  [CharacterProcessing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/CharacterProcessing.ets#L33-L45)
* 音译：是指将采用某个文字系统或字母表表示的文本转换为发音相同的采用另一个文字系统或字母表表示的文本的过程，并不等同于翻译。使用Transliterator类的[transform](../harmonyos-references/js-apis-i18n.md#transform9)接口可以实现音译功能。示例代码如下：

  说明

  本模块支持中文汉字转拼音，但当中文文本中包含多音字时，可能出现部分多音字无法按照正确的发音转换为拼音的问题。

  ```
  1. // 音译成Latn格式
  2. let transliterator: i18n.Transliterator = i18n.Transliterator.getInstance('Any-Latn');
  3. let translatedText = transliterator.transform('中国'); // translatedText = 'zhōng guó'

  5. // 汉语音译去声调
  6. let toneLessTransliterator: i18n.Transliterator = i18n.Transliterator.getInstance('Any-Latn;Latin-Ascii');
  7. let toneLessTranslatedText = toneLessTransliterator.transform('中国'); // toneLessTranslatedText = 'zhong guo'

  9. // 汉语姓氏读音
  10. let nameTransliterator: i18n.Transliterator = i18n.Transliterator.getInstance('Han-Latin/Names');
  11. let nameTranslatedText = nameTransliterator.transform('单老师'); // nameTranslatedText = 'shàn lǎo shī'

  13. // 获取音译支持的转换ID列表
  14. let ids = i18n.Transliterator.getAvailableIDs(); // ids = ['ASCII-Latin', 'Accents-Any', ...]
  ```

  [CharacterProcessing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/CharacterProcessing.ets#L59-L74)
* 文本标准化：是指按指定的范式标准化文本。文本标准化的范式包括NFC、NFD、NFKC和NFKD，范式的详细介绍请参考[国际标准](https://www.unicode.org/reports/tr15/#Norm_Forms)。使用Normalizer类的[normalize](../harmonyos-references/js-apis-i18n.md#normalize10)接口可以实现文本标准化。示例代码如下：

  ```
  1. // 按照NFC范式对文本进行标准化处理
  2. let normalizer: i18n.Normalizer = i18n.Normalizer.getInstance(i18n.NormalizerMode.NFC);
  3. let normalizedText = normalizer.normalize('\u1E9B\u0323'); // normalizedText = 'ẛ̣'
  ```

  [CharacterProcessing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/CharacterProcessing.ets#L86-L90)
* 获取文本的可换行点：使用[BreakIterator](../harmonyos-references/js-apis-i18n.md#breakiterator8)类的接口可以根据设定的区域获取文本的可换行点。示例代码如下：

  ```
  1. // 创建获取文本可换行点的对象，该对象将按照指定区域的规则计算文本中的可换行点的位置
  2. let iterator: i18n.BreakIterator  = i18n.getLineInstance('en-GB');

  4. // 设置处理文本
  5. iterator.setLineBreakText('Apple is my favorite fruit.');

  7. // 将换行迭代器移动到文本起始位置
  8. let firstPos = iterator.first(); // firstPos = 0

  10. // 将换行迭代器向后移动2个可换行点，nextPos为移动后在文本中的位置，如果超出文本的长度范围，返回-1
  11. let nextPos = iterator.next(2); // nextPos = 9

  13. // 获取换行迭代器在当前所处理文本中的位置
  14. let currentPos = iterator.current(); // currentPos = 9

  16. // 判断某个位置是否是可换行点
  17. let isBoundary = iterator.isBoundary(9); // isBoundary = true

  19. // 获取BreakIterator对象处理的文本
  20. let breakText = iterator.getLineBreakText(); // breakText = 'Apple is my favorite fruit.'
  ```

  [CharacterProcessing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/CharacterProcessing.ets#L113-L134)
* 文件路径镜像处理：是指传入镜像语言时，对文件路径字符串进行本地化处理，实现镜像语言下文件路径的镜像显示效果。使用I18NUtil类的[getUnicodeWrappedFilePath](../harmonyos-references/js-apis-i18n.md#getunicodewrappedfilepath20)接口可以实现文件路径镜像处理。示例代码如下：

  ```
  1. let mirrorPath = '';
  2. let unMirrorPath = '';

  4. // 传入镜像语言，对路径进行镜像处理
  5. let path = 'data/out/tmp';

  7. try {
  8. let delimiter = '/';
  9. let locale: Intl.Locale = new Intl.Locale('ar');
  10. // mirrorPath = 'tmp/out/data/'
  11. mirrorPath = i18n.I18NUtil.getUnicodeWrappedFilePath(path, delimiter, locale);

  13. // 传入非镜像语言，不处理路径
  14. let localeZh: Intl.Locale = new Intl.Locale('zh');
  15. // unMirrorPath = '/data/out/tmp'
  16. unMirrorPath = i18n.I18NUtil.getUnicodeWrappedFilePath(path, delimiter, localeZh);
  17. } catch (error) {
  18. console.error(`call I18NUtil.getUnicodeWrappedFilePath failed, error code: ${error.code}, message: ${error.message}.`);
  19. }
  ```

  [CharacterProcessing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/CharacterProcessing.ets#L144-L164)

## 示例代码

* [国际化-字符处理](https://gitcode.com/harmonyos_samples/international)
