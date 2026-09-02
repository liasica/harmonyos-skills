---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-818
title: padding边距显示不准确
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > padding边距显示不准确
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6fc873c82822f3c4740f67094275ed85094ca3ae15a7efee287571031214eac7
---

## 问题现象

Row组件内包含Image和Text组件，当Text内容为多行时，Row组件设置的内边距显示不准确。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Frhk9B7oTmyOqzn35MD0IQ/zh-cn_image_0000002628398432.png "点击放大")

## 背景知识

[Text组件](../harmonyos-references/ts-basic-components-text.md)是显示一段文本的组件，可以设置属性[constraintSize](../harmonyos-references/ts-securitycomponent-attributes.md#constraintsize11)，在组件布局时，进行尺寸范围限制。

## 解决方案

通过添加constraintSize属性来限制Text文本显示的最大长度，使内边距显示准确。

```ts
@Entry
@Component
struct constraintSizeExample {
  build() {
    Column({ space: 30 }) {
      Row() {
        Text('添加constraintSize属性下的状态，右padding样式添加正常').constraintSize({ maxWidth: '90%' });
        Image($r('app.media.startIcon'))   // 开发者需自行替换图片
          .width(18)
          .height(18)
      }
      .rowStyle('#77ceeb')

      Row() {
        Text('没有添加constraintSize属性下的状态，右padding添加未生效');
        Image($r('app.media.startIcon'))  // 开发者需自行替换图片
          .width(18)
          .height(18)
      }
      .rowStyle('#f3f5f7')
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

@Extend(Row)
function rowStyle(color: string) {
  .padding({
    left: 16,
    top: 10,
    right: 16,
    bottom: 10
  })
  .width('50%')
  .borderRadius(20)
  .backgroundColor(color)
  .justifyContent(FlexAlign.SpaceBetween);
}
```

## 常见FAQ

Q：特定场景下constraintSize属性不生效？

A：在使用constraintSize属性来限制组件的尺寸时，当子组件设置了百分比宽度后，会导致组件被撑大，从而使constraintSize的设置失效。为了解决这个问题，可以在外层使用一个Scroll组件，并在该组件上设置constraintSize，以确保子组件即使占用了过多空间，也会显示滚动条。

Q：设置了constraintSize后，组件的宽高失效了。

A：constraintSize的优先级高于Width和Height。

Q：如何解决TextInput设置高度和padding后，输入内容底部被截断？

A：查看padding设置的top和bottom值，减少或设置为0。
