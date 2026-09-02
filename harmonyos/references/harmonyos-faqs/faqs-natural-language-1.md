---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-natural-language-1
title: Natural Language Kit获取Entity中缺少rrule字段
breadcrumb: FAQ > AI功能开发 > 机器学习 > 自然语言理解（Natural Language） > Natural Language Kit获取Entity中缺少rrule字段
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:3e89547cbb343396d628c00aa771f9a7637e611f431e56a70654f5937249e3bb
---

## 问题现象

在5.0.1.130版本上使用[getEntity](../harmonyos-references/natural-language-text-processing-api.md#textprocessinggetentity)接口，返回回来的[jsonObject](../harmonyos-references/natural-language-json-object-api.md)少了一个rrule字段。

问题代码示例参考如下：

```screen
import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';

@Entry
@Component
struct Index {
  private inputText: string = '';
  @State outputText: string = '';

  build() {
    Column() {
      // 每周四晚上10点
      TextInput({ placeholder: '请输入文本' })
        .height(40)
        .fontSize(16)
        .width('90%')
        .margin(10)
        .onChange((value: string) => {
          this.inputText = value;
        })
      Scroll() {
        Text(this.outputText)
          .fontSize(16)
          .width('90%')
          .margin(10)
      }
      .height('40%')

      // 调用实体抽取接口
      Row() {
        Button('获取实体结果')
          .type(ButtonType.Capsule)
          .fontColor(Color.White)
          .width('45%')
          .margin(10)
          .onClick(async () => {
            try {
              let result = await textProcessing.getEntity(this.inputText, { entityTypes: [EntityType.DATETIME] });
              this.outputText = this.formatEntityResult(result);
            } catch (err) {
              console.error(`getEntity errorCode: ${err.code}, errorMessage: ${err.message}`);
              this.outputText = 'Error occurred while getting entities.';
            }
          })
      }
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  // 实体结果转义
  private formatEntityResult(entities: textProcessing.Entity[]): string {
    if (!entities || !entities.length) {
      return 'No entities found.';
    }
    let output = 'Entities:\n';
    for (let i = 0; i < entities.length; i++) {
      let entity = entities[i];
      output += `Entity[${i}]:\n`;
      output += `oriText: ${entity.text}\n`;
      output += `charOffset: ${entity.charOffset}\n`;
      output += `entityType: ${entity.type}\n`;
      output += `jsonObject: ${entity.jsonObject}\n\n`;
    }
    return output;
  }
}
```

输出结果如下：

```screen
{
  "containFuzzySection": "E",
  "inferType": "ABSOLUTE",
  "isChangedIllegal": false,
  "isContainFuzzyTime": true,
  "isFestival": false,
  "isIllegal": false,
  "isLunarTime": false,
  "isPlusTwelveHour": false,
  "isSolarTerm": false,
  "minSection": "P",
  "oriFestival": "",
  "originTimestamp": 1750684503227,
  "rangeDecoration": "POINT",
  "rangeText": "每周四晚上10点",
  "repeat": "W4",
  "sequence": 1,
  "start": "T22:00:00",
  "startTimestamp": 1750946400000,
  "timestampZone": "Asia/Shanghai"
}
```

## 解决方案

从5.0.1.130版本开始，rrule字段以后不会输出了，请使用repeat字段替代，repeat字段的使用规范如下：

| repeat | 说明 |
| --- | --- |
| Y | 每年 |
| Y3 | 每年3月 |
| Y3.6 | 每年3月6日 |
| Y3.6-Y5.2 | 每年3月6日到5月2日 |
| M | 每月 |
| M2 | 每月2日 |
| M2-M5 | 每月2日到5日 |
| W | 每周 |
| W3 | 每周三 |
| W3-W5 | 每周三到每周五 |
| workingDay | 法定工作日 |
| holiday | 节假日 |
