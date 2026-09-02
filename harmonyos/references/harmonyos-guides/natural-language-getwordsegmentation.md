---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/natural-language-getwordsegmentation
title: 分词
breadcrumb: 指南 > AI > Natural Language Kit（自然语言理解服务） > 分词
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2cdca70ed949405405c60184c7129ce63a7b9c55575f5e3ebefb8c311c63749a
---

## 适用场景

分词的目的是让文本文件的中文、英文、数字内容变成一个一个的单词或者词组，从而为后续的转变为词向量提供基础。使用场景例如搜索引擎会将用户输入的文本分词处理后提取关键词送搜索。

## 约束与限制

该能力当前不支持模拟器。

| AI能力 | 约束 |
| --- | --- |
| 分词 | - 支持的语言：简体中文、英文、繁体中文。  - 文本长度：不超过1000字符。 |

## 开发步骤

1. 引用相关类添加至工程。

   ```typescript
   import { textProcessing } from '@kit.NaturalLanguageKit';
   ```
2. 配置输入文本框和按钮，调用分词[textProcessing.getWordSegment](../harmonyos-references/natural-language-text-processing-api.md#textprocessinggetwordsegment)接口。

   ```typescript
   private inputText: string = '';
   @State outputText: string = '';

   TextInput({ placeholder: '请输入文本' })
     .height(40)
     .fontSize(16)
     .width('90%')
     .margin(10)
     .onChange((value: string) => {
       this.inputText = value;
     })

   Button('获取分词结果')
     .type(ButtonType.Capsule)
     .fontColor(Color.White)
     .width('45%')
     .margin(10)
     .onClick(async () => {
       try {
         let result = await textProcessing.getWordSegment(this.inputText);
         this.outputText = this.formatWordSegmentResult(result);
       } catch (err) {
         console.error(`getWordSegment errorCode: ${err.code}, errorMessage: ${err.message}`);
       }
     })
   ```
3. 在界面上展示分词结果[WordSegment](../harmonyos-references/natural-language-text-processing-api.md#wordsegment)。

   ```typescript
   private formatWordSegmentResult(segments: textProcessing.WordSegment[]): string {
     let output = 'Word Segments:\n';
     segments.forEach((segment, index) => {
       output += `Word[${index}]: ${segment.word}, Tag: ${segment.wordTag}\n`;
     });
     return output;
   }
   ```

## 开发实例

```typescript
import { textProcessing } from '@kit.NaturalLanguageKit';

@Entry
@Component
struct Index {
  private inputText: string = '';
  @State outputText: string = '';

  build() {
    Column() {
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

      // 调用分词接口
      Row() {
        Button('获取分词结果')
          .type(ButtonType.Capsule)
          .fontColor(Color.White)
          .width('45%')
          .margin(10)
          .onClick(async () => {
            try {
              let result = await textProcessing.getWordSegment(this.inputText);
              this.outputText = this.formatWordSegmentResult(result);
            } catch (err) {
              console.error(`getWordSegment errorCode: ${err.code}, errorMessage: ${err.message}`);
            }
          })
      }
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  // 分词结果转义
  private formatWordSegmentResult(segments: textProcessing.WordSegment[]): string {
    let output = 'Word Segments:\n';
    segments.forEach((segment, index) => {
      output += `Word[${index}]: ${segment.word}, Tag: ${segment.wordTag}\n`;
    });
    return output;
  }
}
```
