---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-troubleshooting-0006
title: 开启“高对比度文字”时应用文字显示模糊
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 故障排查 > 开启“高对比度文字”时应用文字显示模糊
category: harmonyos-faqs
scraped_at: 2026-11-21T09:17:49+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:7a237c4ae0a0e731d3b0a96a89fb86bc2bc667853c8cdd916a51d1b9515d838a
---

## 开启高对比度文字时文字显示模糊

### 问题现象

开启“高对比度文字”时应用文字显示模糊。

### 定位过程

1. 使用DevEco Testing查看问题组件，该组件为TextInput组件。
2. 查看该TextInput组件的设置，placeholder文本颜色设置为#d6d6d6，三原色之和大于594，开启“高对比度文字”时显示为外黑内白。且组件背景色设置为#f1f3f5灰色，导致文字颜色与背景色相近，显示模糊。

   ```ts
       @Entry
       @Component
       struct Index {
         build() {
           Column() {
             TextInput({ placeholder: '请输入搜索内容' })
               .fontSize(14)
               .placeholderColor('#d6d6d6') // 三原色之和大于594
               .fontWeight(FontWeight.Bold)
               .backgroundColor('#f1f3f5') // 组件背景色较浅
               .placeholderFont({
                 size: 14,
                 weight: 400
               })
               .caretColor('#000000')
               .height(40)
               .enableKeyboardOnFocus(true)
               .width('80%')
               .margin({ top: 20 });
           }
           .height('100%')
           .width('100%');
         }
       }
   ```

### 分析结论

placeholder文本颜色设置为#d6d6d6，三原色之和大于594，开启“高对比度文字”时显示为外黑内白，导致文字颜色与背景色相近，显示模糊。

### 修改建议

合理设置文字颜色。

组件背景色较浅时文字三原色之和小于等于594，组件背景色较深时文字三原色之和大于594。

```ts
@Entry
@Component
struct TextinputExample {
  build() {
    Column() {
      TextInput({ placeholder: '请输入搜索内容' })
        .fontSize(14)
        .placeholderColor('#c5c5c5') // 三原色之和小于等于594
        .fontWeight(FontWeight.Bold)
        .backgroundColor('#f1f3f5') // 组件背景色较浅
        .placeholderFont({
          size: 14,
          weight: 400
        })
        .caretColor('#000000')
        .height(40)
        .enableKeyboardOnFocus(true)
        .width('80%')
        .margin({ top: 20 });
    }
    .height('100%')
    .width('100%');
  }
}
```

## 描边文字预览与实际效果不一致

### 问题现象

使用Text组件和MutableStyledString设置描边文字大标题（白字黑描边+黄色底）时，预览效果与实际效果不同，异常文本出现外黑内白的现象。

### 定位过程

1. 检查设备设置，进入设置>关怀和无障碍，发现“高对比度文字”开关处于开启状态。
2. 开启“高对比度文字”后，系统会将白色描边文字自动转换为外黑内白效果以增加对比度，导致预览效果（白字黑描边+黄色底）与实际效果不一致。
3. 关闭“高对比度文字”设置后，文字恢复正常的白字黑描边+黄色底显示效果。

### 分析结论

设备开启了“高对比度文字”设置，系统自动将浅色文字转换为外黑内白效果以增加对比度，导致描边文字的预览效果与实际显示效果不一致。

### 修改建议

关闭高对比度文字设置。

进入设备设置>关怀和无障碍，关闭“高对比度文字”开关，描边文字即可恢复正常显示效果。
