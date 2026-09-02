---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/natural-language-getentity
title: 实体抽取
breadcrumb: 指南 > AI > Natural Language Kit（自然语言理解服务） > 实体抽取
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dddcf96b3587a6eebc7d799447ee2f35b077f3173c0903a755ebe9e8d533a46c
---

## 适用场景

实体抽取是自然语言处理服务的一项关键能力。通过综合分析上下文信息，从文本中准确识别出多种类型的实体：

1. 日期时间（DATETIME）：提取文本中的具体日期，如“2024年6月18日”等。
2. 电子邮件（EMAIL）：识别文本中的电子邮件地址，如“\*\*\*@example.com”。
3. 快递单号（EXPRESS\_NO）：抽取文本中的快递单号信息。
4. 航班号（FLIGHT\_NO）：定位文本中的航班号，如“CA1234”等。
5. 地址（LOCATION）：从文本中提取详细的地址描述。
6. 人名（NAME）：找出文本中出现的人名信息。
7. 手机号（PHONE\_NO）：识别文本中的手机号码。
8. 网址（URL）：抽取文本中的网址链接。
9. 验证码（VERIFICATION\_CODE）：定位文本中的验证码数字。
10. 身份证号（ID\_NO）：识别文本中的身份证号码信息。

通过准确抽取以上多种类型的实体信息，该项能力可以广泛应用于新闻阅读、信息检索、客户服务、社交聊天、金融运营等多种场景。例如，在新闻阅读场景中，可以对新闻正文进行实体抽取，并对人名、地名、时间、网址等关键实体信息进行高亮标识，帮助读者快速获取文章要点；在客服场景，通过抽取用户留言中的手机号、快递单号、验证码等信息，客服人员能够更高效地定位问题并给出解决方案。实体抽取为各行业的智能化应用提供了坚实的基础支持。

## 约束与限制

该能力当前不支持模拟器。

| AI能力 | 约束 |
| --- | --- |
| 实体抽取 | - 支持的语言：简体中文、英文、繁体中文。  - 支持的实体：时间、地点、邮箱、快递单号、航班号、人名、电话号码、网址链接、验证码、证件号。  - 文本长度：不超过1000字符。 |

## 开发步骤

1. 在使用实体抽取功能时，将实现实体抽取的类添加至工程。

   ```typescript
   import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';
   ```
2. 配置输入文本框。

   ```typescript
   private inputText: string = '张三的电话号码是12345';
   @State outputText: string = '';

   TextInput({ placeholder: '请输入文本', text: this.inputText })
     .height(40)
     .fontSize(16)
     .width('90%')
     .margin(10)
     .onChange((value: string) => {
       this.inputText = value;
     })
   ```
3. 配置按钮，调用实体抽取[textProcessing.getEntity](../harmonyos-references/natural-language-text-processing-api.md#textprocessinggetentity)接口。

   ```typescript
   Button('获取实体结果')
     .type(ButtonType.Capsule)
     .fontColor(Color.White)
     .width('45%')
     .margin(10)
     .onClick(async () => {
       try {
         let result = await textProcessing.getEntity(this.inputText, {entityTypes: [EntityType.NAME, EntityType.PHONE_NO]});
         this.outputText = this.formatEntityResult(result);
       } catch (err) {
         console.error(`getEntity errorCode: ${err.code}, errorMessage: ${err.message}`);
         this.outputText = 'Error occurred while getting entities.';
       }
     })
   ```
4. 在界面上展示实体抽取结果。

   ```typescript
   private formatEntityResult(entities: textProcessing.Entity[]): string {
     if (!entities || !entities.length) {
       return 'No entities found.';
     }

     let output = 'Entities:\n';
     for (let i = 0; i < entities.length; i++) {
       let entity = entities[i];
       output += `Entity[${i}]:\n`;
       output += `  oriText: ${entity.text}\n`;
       output += `  charOffset: ${entity.charOffset}\n`;
       output += `  entityType: ${entity.type}\n`;
       output += `  jsonObject: ${entity.jsonObject}\n\n`;
     }
     return output;
   }
   ```

## 开发实例

```typescript
import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';

@Entry
@Component
struct Index {
  private inputText: string = '张三的电话号码是12345';
  @State outputText: string = '';

  build() {
    Column() {
      TextInput({ placeholder: '请输入文本', text: this.inputText })
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
              let result = await textProcessing.getEntity(this.inputText, {entityTypes: [EntityType.NAME, EntityType.PHONE_NO]});
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
      output += `  oriText: ${entity.text}\n`;
      output += `  charOffset: ${entity.charOffset}\n`;
      output += `  entityType: ${entity.type}\n`;
      output += `  jsonObject: ${entity.jsonObject}\n\n`;
    }
    return output;
  }
}
```
