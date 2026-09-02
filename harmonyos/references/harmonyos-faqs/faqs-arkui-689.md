---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-689
title: 如何实现含有emoji表情的渐变色文字
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现含有emoji表情的渐变色文字
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5371cdb39da52aeac222cd4bf4b165edccd0c61b37e227bdc0da387bcf6f4716
---

## 问题现象

在输入框组件上直接设置文字渐变色会影响emoji的展示，是否有其他方案实现含有emoji表情的渐变色文字？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/dI9iNzTHQ3S_LHDxR4pKXA/zh-cn_image_0000002628554748.png "点击放大")

## 背景知识

* [linearGradient](../harmonyos-references/ts-universal-attributes-gradient-color.md)：设置组件的颜色渐变效果。可以参照[官网](faqs-arkui-385.md)实现文字渐变色设置。
* [onDidInsert](../harmonyos-references/ts-basic-components-textinput.md#ondidinsert12)：在输入完成时，触发该回调。
* [onDidDelete](../harmonyos-references/ts-basic-components-textinput.md#ondiddelete12)：在删除完成时，触发该回调。

## 解决方案

实现思路：把需要设置渐变色的文字按照类型进行拆分，一类是需要设置渐变色的文字类型，另一类是不需要设置渐变色的emoji表情；在TextInput输入时根据输入的字符判断其类型，放入不同的分类，最后循环展示两类文字即可。

1. 定义文字类型。

   ```screen
   class TextType {
     content: string = '';
     // 1代表普通文字 2代表emoji
     type: number = 1;
   }
   ```
2. 判断单个字符是否是emoji。

   ```screen
   // 判断单个字符是否为emoji
   function isEmojiCharacter(char: string): boolean {
     const codePoint = char.codePointAt(0);
     if (codePoint === undefined) {
       return false;
     }
     // 常见emoji的Unicode范围参考
     return (
       (codePoint >= 0x1F600 && codePoint <= 0x1F64F) || // Emoticons
         (codePoint >= 0x1F300 && codePoint <= 0x1F5FF) || // Misc Symbols and Pictographs
         (codePoint >= 0x1F680 && codePoint <= 0x1F6FF) || // Transport and Map
         (codePoint >= 0x1F700 && codePoint <= 0x1F77F) || // Alchemical Symbols
         (codePoint >= 0x1F780 && codePoint <= 0x1F7FF) || // Geometric Shapes Extended
         (codePoint >= 0x1F800 && codePoint <= 0x1F8FF) || // Supplemental Arrows-C
         (codePoint >= 0x1F900 && codePoint <= 0x1F9FF) || // Supplemental Symbols and Pictographs
         (codePoint >= 0x1FA00 && codePoint <= 0x1FA6F) || // Chess Symbols
         (codePoint >= 0x1FA70 && codePoint <= 0x1FAFF) || // Symbols and Pictographs Extended-A
         (codePoint >= 0x2600 && codePoint <= 0x26FF) || // Misc Symbols
         (codePoint >= 0x2700 && codePoint <= 0x27BF) || // Dingbats
         (codePoint >= 0xFE00 && codePoint <= 0xFE0F) || // Variation Selectors
         (codePoint >= 0x1F1E6 && codePoint <= 0x1F1FF)
     );
   }
   ```
3. 输入框输入根据不同的类型进行处理。

   ```screen
   TextInput({ placeholder: '请输入内容' })
     .margin({ top: 16 })
     .onDidInsert((value: InsertValue) => {
       let tmpType: number = 0;
       if (containsEmoji(value.insertValue)) {
         tmpType = 2;
       } else {
         tmpType = 1;
       }
       if (this.textInputs.length == 0) {
         this.textInputs.push({ 'content': value.insertValue, 'type': tmpType });
       } else {
         let lastInput = this.textInputs[this.textInputs.length - 1];

         if (lastInput.type === tmpType) {
           lastInput = { 'content': lastInput.content + value.insertValue, 'type': tmpType };
           this.textInputs.pop();
           this.textInputs.push(lastInput);
         } else {
           this.textInputs.push({ 'content': value.insertValue, 'type': tmpType });
         }
       }
     })
     .onDidDelete((value: DeleteValue) => {
       if (this.textInputs.length <= 0) {
         return;
       }
       let tmpType: number = 0;
       if (containsEmoji(value.deleteValue)) {
         tmpType = 2;
       } else {
         tmpType = 1;
       }
       let lastInput = this.textInputs[this.textInputs.length - 1];
       let newContent = lastInput.content.substring(0, lastInput.content.length - value.deleteValue.length);
       if (newContent.length > 0) {
         lastInput = { 'content': newContent, 'type': tmpType };
         this.textInputs.pop();
         this.textInputs.push(lastInput);
       } else {
         this.textInputs.pop();
       }
     });
   ```
4. 根据不同的文字类型展示不同的内容。

   ```screen
   ForEach(this.textInputs, (item: TextType) => {
     if (item.type == 1) {
       Row() {
         Text(item.content)
           .fontSize(50)
           .fontWeight(FontWeight.Bold)
           .blendMode(BlendMode.DST_IN, BlendApplyType.OFFSCREEN);
       }
       .linearGradient({
         direction: GradientDirection.Right,
         colors: [['#FFF563FF', 0.0], ['#FF0253EB', 0.2], ['#FF0253EB', 0.5], ['#FF26ECFF', 0.9]]
       })
       .blendMode(BlendMode.SRC_OVER, BlendApplyType.OFFSCREEN);
     } else {
       Row() {
         Text(item.content)
           .fontSize(50)
           .fontWeight(FontWeight.Bold);
       };
     }
   });
   ```

完整示例参考如下：

```screen
@Entry
@Component
struct LinearGradientAndEmoji {
  @State textInputs: TextType[] = [];

  build() {
    Column() {
      Flex({ direction: FlexDirection.Row, wrap: FlexWrap.Wrap }) {
        ForEach(this.textInputs, (item: TextType) => {
          if (item.type == 1) {
            Row() {
              Text(item.content)
                .fontSize(50)
                .fontWeight(FontWeight.Bold)
                .blendMode(BlendMode.DST_IN, BlendApplyType.OFFSCREEN);
            }
            .linearGradient({
              direction: GradientDirection.Right,
              colors: [['#FFF563FF', 0.0], ['#FF0253EB', 0.2], ['#FF0253EB', 0.5], ['#FF26ECFF', 0.9]]
            })
            .blendMode(BlendMode.SRC_OVER, BlendApplyType.OFFSCREEN);
          } else {
            Row() {
              Text(item.content)
                .fontSize(50)
                .fontWeight(FontWeight.Bold);
            };
          }
        });
      };

      TextInput({ placeholder: '请输入内容' })
        .margin({ top: 16 })
        .onDidInsert((value: InsertValue) => {
          let tmpType: number = 0;
          if (containsEmoji(value.insertValue)) {
            tmpType = 2;
          } else {
            tmpType = 1;
          }
          if (this.textInputs.length == 0) {
            this.textInputs.push({ 'content': value.insertValue, 'type': tmpType });
          } else {
            let lastInput = this.textInputs[this.textInputs.length - 1];

            if (lastInput.type === tmpType) {
              lastInput = { 'content': lastInput.content + value.insertValue, 'type': tmpType };
              this.textInputs.pop();
              this.textInputs.push(lastInput);
            } else {
              this.textInputs.push({ 'content': value.insertValue, 'type': tmpType });
            }
          }
        })
        .onDidDelete((value: DeleteValue) => {
          if (this.textInputs.length <= 0) {
            return;
          }
          let tmpType: number = 0;
          if (containsEmoji(value.deleteValue)) {
            tmpType = 2;
          } else {
            tmpType = 1;
          }
          let lastInput = this.textInputs[this.textInputs.length - 1];
          let newContent = lastInput.content.substring(0, lastInput.content.length - value.deleteValue.length);
          if (newContent.length > 0) {
            lastInput = { 'content': newContent, 'type': tmpType };
            this.textInputs.pop();
            this.textInputs.push(lastInput);
          } else {
            this.textInputs.pop();
          }
        });
    }
    .padding(16)
    .width('100%')
    .height('100%');
  }
}

class TextType {
  content: string = '';
  // 1代表普通文字 2代表emoji
  type: number = 1;
}
// 判断单个字符是否为emoji
function isEmojiCharacter(char: string): boolean {
  const codePoint = char.codePointAt(0);
  if (codePoint === undefined) {
    return false;
  }
  // 常见emoji的Unicode范围参考
  return (
    (codePoint >= 0x1F600 && codePoint <= 0x1F64F) || // Emoticons
      (codePoint >= 0x1F300 && codePoint <= 0x1F5FF) || // Misc Symbols and Pictographs
      (codePoint >= 0x1F680 && codePoint <= 0x1F6FF) || // Transport and Map
      (codePoint >= 0x1F700 && codePoint <= 0x1F77F) || // Alchemical Symbols
      (codePoint >= 0x1F780 && codePoint <= 0x1F7FF) || // Geometric Shapes Extended
      (codePoint >= 0x1F800 && codePoint <= 0x1F8FF) || // Supplemental Arrows-C
      (codePoint >= 0x1F900 && codePoint <= 0x1F9FF) || // Supplemental Symbols and Pictographs
      (codePoint >= 0x1FA00 && codePoint <= 0x1FA6F) || // Chess Symbols
      (codePoint >= 0x1FA70 && codePoint <= 0x1FAFF) || // Symbols and Pictographs Extended-A
      (codePoint >= 0x2600 && codePoint <= 0x26FF) || // Misc Symbols
      (codePoint >= 0x2700 && codePoint <= 0x27BF) || // Dingbats
      (codePoint >= 0xFE00 && codePoint <= 0xFE0F) || // Variation Selectors
      (codePoint >= 0x1F1E6 && codePoint <= 0x1F1FF)
  );
}

// 判断字符串是否包含emoji
function containsEmoji(inputString: string): boolean {
  for (let i = 0; i < inputString.length; i++) {
    // 考虑代理对的情况（Surrogate Pairs），emoji可能由两个代码单元组成
    const char = inputString[i];
    // 如果当前字符是高位代理，则与下一个字符（低位代理）组合判断
    if (isHighSurrogate(char.charCodeAt(0)) && i + 1 < inputString.length) {
      const combinedChar = char + inputString[i + 1];
      if (isEmojiCharacter(combinedChar)) {
        return true;
      }
      i++; // 跳过下一个字符，因为已经组合处理
    } else {
      if (isEmojiCharacter(char)) {
        return true;
      }
    }
  }
  return false;
}

// 判断是否为高位代理（High Surrogate）
function isHighSurrogate(codeUnit: number): boolean {
  return codeUnit >= 0xD800 && codeUnit <= 0xDBFF;
}
```
