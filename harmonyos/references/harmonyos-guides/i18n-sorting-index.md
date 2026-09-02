---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-sorting-index
title: 创建索引
breadcrumb: 指南 > 应用框架 > Localization Kit（本地化开发服务） > 应用国际化 > 多语言排序 > 创建索引
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:57d95e4b2317c482268e9df4e7e35ff6a28b24d8c9a977650a19072ff0986755
---

## 功能介绍

当列表选项过多时，用户需要滑动窗口查找目标选项。为了提高查找效率，可以使用创建索引的方法。创建索引方式实质是打标签。例如，在联系人页面右侧通常会有“ABCD”的英文标记与联系人姓名首字母对应。若需寻找王同学，点击“W”可直接跳转到目标项范围。诸如“ABCD”的英文标记称为索引，通过创建索引的方式快速让窗口滑动到相应范围，找到目标选项。

## 开发步骤

接口具体使用方法和说明请参考[IndexUtil](../harmonyos-references/js-apis-i18n.md#indexutil8)的API文档。

1. 导入模块。

   ```typescript
   import { i18n } from '@kit.LocalizationKit';
   ```
2. 获取索引列表和索引值。

   ```typescript
   // 创建索引
   let indexUtil: i18n.IndexUtil = i18n.getInstance('zh-CN');
   let indexList = indexUtil.getIndexList(); // indexList = ['…', 'A', 'B', 'C', ... 'X', 'Y', 'Z', '…']

   // 多语言index混排
   indexUtil.addLocale('ru-RU');
   // indexList = ['…', 'A', 'B', 'C', ... 'X', 'Y', 'Z', '…', 'А', 'Б', 'В', ... 'Э', 'Ю', 'Я', '…']
   indexList = indexUtil.getIndexList();

   // 获取字符串的索引值
   let index = indexUtil.getIndex('你好'); // index = 'N'
   ```
