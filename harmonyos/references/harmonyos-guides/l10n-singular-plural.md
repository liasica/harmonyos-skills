---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/l10n-singular-plural
title: 支持单复数
breadcrumb: 指南 > 应用框架 > Localization Kit（本地化开发服务） > 应用本地化 > 提升可翻译性 > 支持单复数
category: harmonyos-guides
scraped_at: 2026-10-15T07:04:25+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:2eb219a581a7ca54687a10374b57fdad2b04c80b9d3089b79a256f53d914f3fd
---

翻译过程中，不同语言对于名词或单位表达式的单复数格式要求各不相同。有些语言不区分单复数，有些语言有两种形式，还有一些语言有多种形式。例如，在英语中，名词支持两种单复数形式；对于中文，名词不分单复数，通过量词表达数量的不同。

国际上常通过如下类别区分单复数：

* zero：0或者0结尾
* one：单数或者1结尾
* two：2结尾
* few：数值较小的数
* many：数值较大的数
* other：其他情况

例如，在阿拉伯语中，单复数规则如下：

* zero：0
* one：1
* two：2
* few：3~10、103~110，1003...
* many：11~26、111，1011...
* other：100~102、200~202、1000、10000...

## 开发步骤

接口具体使用方法请参考[getIntPluralStringValueSync](../harmonyos-references/js-apis-resource-manager.md#getintpluralstringvaluesync18)的API文档。
