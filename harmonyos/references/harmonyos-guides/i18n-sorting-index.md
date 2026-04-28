---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-sorting-index
title: 创建索引
breadcrumb: 指南 > 应用框架 > Localization Kit（本地化开发服务） > 应用国际化 > 多语言排序 > 创建索引
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cc9be3aeeeb5f39c1dfb3536ca91bd512e45c5ffec937b37c4d19f6683f2944b
---

## 功能介绍

当列表选项过多时，用户需要滑动窗口查找目标选项。为了提高查找效率，可以使用创建索引的方法。创建索引方式实质是打标签。例如，在联系人页面右侧通常会有“ABCD”的英文标记与联系人姓名首字母对应。若需寻找王同学，点击“W”可直接跳转到目标项范围。诸如“ABCD”的英文标记称为索引，通过创建索引的方式快速让窗口滑动到相应范围，找到目标选项。

## 开发步骤

接口具体使用方法和说明请参考[IndexUtil](../harmonyos-references/js-apis-i18n.md#indexutil8)的API文档。

1. 导入模块。

   ```
   1. import { i18n } from '@kit.LocalizationKit';
   ```

   [MultilingualSorting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/MultilingualSorting.ets#L19-L21)
2. 获取索引列表和索引值。

   ```
   1. // 创建索引
   2. let indexUtil: i18n.IndexUtil = i18n.getInstance('zh-CN');
   3. let indexList = indexUtil.getIndexList(); // indexList = ['…', 'A', 'B', 'C', ... 'X', 'Y', 'Z', '…']

   5. // 多语言index混排
   6. indexUtil.addLocale('ru-RU');
   7. // indexList = ['…', 'A', 'B', 'C', ... 'X', 'Y', 'Z', '…', 'А', 'Б', 'В', ... 'Э', 'Ю', 'Я', '…']
   8. indexList = indexUtil.getIndexList();

   10. // 获取字符串的索引值
   11. let index = indexUtil.getIndex('你好'); // index = 'N'
   ```

   [MultilingualSorting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/MultilingualSorting.ets#L32-L44)
