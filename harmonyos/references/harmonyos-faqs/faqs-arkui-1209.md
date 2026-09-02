---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1209
title: 开启“高对比度文字”时文字显示异常如何解决
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 开启“高对比度文字”时文字显示异常如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:45+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:05506ad9270aa27c587c021fb2d6c5163ec85bb3a731dbf9f57b50947f34cac6
---

## 问题现象

* 场景一：开启“高对比度文字”时应用文字显示模糊。

  图一：未开启“高对比度文字”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/eQpeHK07TqaiKZt0-kRcsg/zh-cn_image_0000002675223403.png "点击放大")

  图二：开启“高对比度文字”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/zSPU0jQwT_6jTswNshUZew/zh-cn_image_0000002675343279.png "点击放大")
* 场景二：使用Text组件和MutableStyledString设置描边文字大标题（白字黑描边+黄色底）时，预览效果与实际效果不同，异常文本出现外黑内白的现象。

## 背景知识

* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)组件为单行文本输入框组件。其[placeholderColor](../harmonyos-references/ts-basic-components-textinput.md#placeholdercolor)属性可设置placeholder文本颜色。
* 设备依据字体的三原色来判断应用是希望字体为浅色还是深色，从而在高对比度模式下将字体作为外黑内白（或是外白内黑）来增加对比度效果。三原色之和大于594（#C6C6C6），才会显示为外黑内白，否则为外白内黑。
* [Text](../harmonyos-references/ts-basic-components-text.md)组件和[MutableStyledString](../harmonyos-references/ts-universal-styled-string.md#mutablestyledstring)用于设置富文本和描边文字样式，开启“高对比度文字”后系统会自动调整文字显示效果。

## 问题定位

### 场景一

1. 使用DevEco Testing查看问题组件，该组件为TextInput组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Jlj0ATcySV2vnE8UPWX5sA/zh-cn_image_0000002675343137.png "点击放大")
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

### 场景二

1. 检查设备设置，进入设置>关怀和无障碍，发现“高对比度文字”开关处于开启状态。
2. 开启“高对比度文字”后，系统会将白色描边文字自动转换为外黑内白效果以增加对比度，导致预览效果（白字黑描边+黄色底）与实际效果不一致。
3. 关闭“高对比度文字”设置后，文字恢复正常的白字黑描边+黄色底显示效果。

## 分析结论

* 场景一：placeholder文本颜色设置为#d6d6d6，三原色之和大于594，开启“高对比度文字”时显示为外黑内白，导致文字颜色与背景色相近，显示模糊。
* 场景二：设备开启了“高对比度文字”设置，系统自动将浅色文字转换为外黑内白效果以增加对比度，导致描边文字的预览效果与实际显示效果不一致。

## 修改建议

### 场景一：合理设置文字颜色

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

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/hoS5HsRyTsWXe9dyUyvasw/zh-cn_image_0000002645183290.png "点击放大")

### 场景二：关闭高对比度文字设置

进入设备设置>关怀和无障碍，关闭“高对比度文字”开关，描边文字即可恢复正常显示效果。
