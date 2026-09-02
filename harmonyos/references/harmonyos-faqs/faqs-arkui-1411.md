---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1411
title: 如何解决顶部图片延伸场景存在留白问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决顶部图片延伸场景存在留白问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ce358466ff0ffdb8ed5e0598a7656c68877d5ea1c14c2fdd8127cfdca614913a
---

## 问题现象

当图片扩展到安全区域时，图片上下会出现空白。

问题代码示例参考如下：

```ts
@Entry
@Component
struct page1 {
  build() {
    Column() {
      Image($r('app.media.startIcon')) // 资源文件需自行替换
        .width('100%')
        .objectFit(ImageFit.Contain)
        .backgroundColor(Color.Blue)
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP]);
    }
    .height('100%')
    .width('100%');
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/ShMEkPzQSmyxHu-Tx3VjQQ/zh-cn_image_0000002658962479.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/zo0ZCV6xSiq91IT2Q4s8eA/zh-cn_image_0000002628603268.png "点击放大")

## 背景知识

* [height](../harmonyos-references/ts-universal-attributes-size.md#height)('auto')：将组件高度设置为auto时，组件会根据自身内容（如文本、子组件等）自动调整高度，无需手动指定固定值。
* 扩展其安全区域：[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)控制组件扩展其安全区域，实现屏幕整体一致，达成沉浸式体验。
* [ImageFit](../harmonyos-references/ts-appendix-enums.md#imagefit)：不同尺寸图片在固定容器中的适配问题。具体区别如下：

  | 模式 | 保持比例 | 是否裁剪 | 放大策略 | 应用场景 |
  | --- | --- | --- | --- | --- |
  | Contain | 是 | 否 | 允许放大 | 完整展示图片 |
  | Cover | 是 | 是 | 允许放大 | 全屏背景 |
  | Fill | 否 | 否 | 强制拉伸 | 图形填充 |
  | ScaleDown | 是 | 否 | 仅缩小 | 保护图片质量 |
  | Auto | 是 | 是 | 动态调整 | 响应式布局场景 |

## 解决方案

* 方案一：Image组件加载图片的填充效果为Cover，保持宽高比进行缩小或者放大，使得图片两边都大于或等于显示边界，可通过为Image组件设置宽高值来约束其显示范围。

  示例代码如下：

  ```ts
  @Entry
  @Component
  struct page4 {
    build() {
      Column() {
        Image($r('app.media.startIcon')) // 资源文件需自行替换
          .width('100%')
          .height('300')
          .objectFit(ImageFit.Cover)
          .backgroundColor(Color.Blue)
          .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP]);
      }
      .height('100%')
      .width('100%');
    }
  }
  ```
* 方案二：使用ImageFit.Fill让图片填满容器（会改变图片宽高比）。

  示例代码如下：

  ```ts
  @Entry
  @Component
  struct page2 {
    build() {
      Column() {
        Image($r('app.media.startIcon')) // 资源文件需自行替换
          .width('100%')
          .objectFit(ImageFit.Fill)
          .backgroundColor(Color.Blue)
          .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP]);
      }
      .height('100%')
      .width('100%');
    }
  }
  ```
* 方案三：给图片设置height('auto')，让其自动适应内容高度（确保图片原始尺寸）。

  示例代码如下：

  ```ts
  @Entry
  @Component
  struct page3 {
    build() {
      Column() {
        Image($r('app.media.startIcon')) // 资源文件需自行替换
          .width('100%')
          .objectFit(ImageFit.Contain)
          .height('auto')
          .backgroundColor(Color.Blue)
          .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP]);
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

## 总结

在使用ImageFit时，建议如下：

* 优先使用Cover/Contain保持视觉一致性。
* 涉及文字/图形展示时绝对避免Fill模式。
* 需要防止图片放大模糊时选择ScaleDown。
* 在复杂响应式布局可以选择Auto。
