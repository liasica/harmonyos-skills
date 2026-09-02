---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-695
title: 组件间布局遮挡
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 组件间布局遮挡
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bf25aa4a282a3c541e916e2526e55d58ab460117237d9d2edb1e5c28d1f0da22
---

## 问题现象

打开应用后，出现页面组件间布局遮挡问题，如文本框和图片重叠显示、按钮遮挡文字等异常情况。

## 背景知识

* [layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)设置组件的布局权重，使用该属性的组件在父容器（Row/Column/Flex）的主轴方向按照权重分配尺寸。

  | 参数名 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | value | number /string | 是 | 父容器尺寸确定时，设置了layoutWeight属性的子元素与兄弟元素占主轴尺寸按照权重进行分配，忽略元素本身尺寸设置，表示自适应占满剩余空间。默认值：0。 |
* [margin](../harmonyos-references/ts-universal-attributes-size.md#margin)设置外边距属性。参数：

  | 参数名 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | value | [Margin](../harmonyos-references/ts-types.md#margin) /[Length](../harmonyos-references/ts-types.md#length) / [LocalizedMargin12+](../harmonyos-references/ts-types.md#localizedmargin12) | 是 | 设置组件的外边距。参数为Length类型时，四个方向外边距同时生效。默认值：0，单位：vp 。 |
* [padding](../harmonyos-references/ts-universal-attributes-size.md#padding)设置内边距属性。参数：

  | 参数名 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | value | [Padding](../harmonyos-references/ts-types.md#padding) /[Length](../harmonyos-references/ts-types.md#length) / [LocalizedPadding12+](../harmonyos-references/ts-types.md#localizedpadding12) | 是 | 设置组件的内边距。参数为Length类型时，四个方向内边距同时生效。默认值：0，单位：vp。padding设置百分比时，上下左右内边距均以父容器的width作为基础值。 |

## 问题定位

### 场景一

排查容器布局是否存在约束，即是否使用了Stack堆叠布局。如使用了Stack布局，这种布局子元素默认进行居中堆叠，子元素被约束在Stack下，这会导致组件间布局遮挡，关键代码如下：

```ts
Stack(){
  Image($r('app.media.startIcon'))
    .width('100%')
  TextInput({text:'图片被文本框遮挡'})
    .backgroundColor(Color.Grey)
    .fontSize(24)
    .fontColor(Color.Black)
}
```

### 场景二

排查组件是否使用线性布局，如果线性布局的宽高设置不合理，也会出现遮挡，关键代码如下：

```ts
Column() {
  Column(){
    Text('Test Test')
  }.height('70%').width('100%').backgroundColor('red')
  Row(){
    // 此处的文本被遮挡
    Text('hello world')
  }.height('100%').width('100%').backgroundColor('blue')
}.width('100%').height('100%')
```

### 场景三

排查组件是否有设置内/外边距，以及内/外边距属性设置是否合理，过大/过小的内外边距都会导致组件间布局遮挡，关键代码如下：

```ts
Stack(){
  Image($r('app.media.startIcon'))
    .width('100%')
  TextInput({text:'图片被文本框遮挡'}) 
    .backgroundColor(Color.Grey)
    .fontSize(24)
    .fontColor(Color.Black)
    .margin({top:'-50'})
}
```

## 分析结论

### 场景一

容器存在布局约束，造成组件间堆叠，布局遮挡。

### 场景二

线性布局的宽高设置不合理，造成组件间布局遮挡。

### 场景三

内/外边距属性设置不合理，造成组件间布局遮挡。

## 修改建议

### 场景一

布局约束造成的组件间布局遮挡问题，可以更改为Flex弹性布局，并设置layoutWeight属性来分配剩余空间。

```ts
// 改成Flex布局
Flex(){
  Image($r('app.media.startIcon'))
    .width('100%')
    // 这个页面的占比为1份
    .layoutWeight(1)
  TextInput({text:'图片被文本框遮挡'})
    .backgroundColor(Color.Grey)
    .fontSize(24)
    .fontColor(Color.Black)
    // 整个页面的占比为2份
    .layoutWeight(2)
}
```

### 场景二

线性布局的宽高设置不合理造成的组件间布局遮挡问题，可以根据实际应用场景，动态调整width、height等属性的值。

```ts
Column() {
  Column(){
    Text('Test Test')
  }.height('50%').width('100%').backgroundColor('red')
  Row(){
    // 调整height，此处的文本可正常展示，未被遮挡
    Text('hello world')
  }.height('40%').width('100%').backgroundColor('blue')
}.width('100%').height('100%')
```

### 场景三

组件内/外边距属性设置不合理造成的组件间布局遮挡问题，可以根据实际应用场景，动态调整margin、padding等属性的值。

```ts
Stack(){
  Image($r('app.media.startIcon'))
    .width('100%')
  TextInput({text:'图片被文本框遮挡'})
    .backgroundColor(Color.Grey)
    .fontSize(24)
    .fontColor(Color.Black)
    // 调整了margin的值，可以正常展示，未被遮挡
    .margin({top:'0'})
}
```
