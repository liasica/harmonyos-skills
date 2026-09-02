---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-14
title: 平板页面局部图片被截断
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板页面局部图片被截断
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:549d58cc83392088030fd5a2973c30af38b55f76d04ab7aff53cc7bd55ab3d76
---

## 问题现象

平板打开应用，页面内的部分图片被截断，只能显示一部分，存在体验问题。

## 背景知识

[objectFit](../harmonyos-references/ts-basic-components-image.md#objectfit)是[Image](../harmonyos-references/ts-basic-components-image.md)组件用来设置图片的填充效果的属性，将Image组件的objectFit属性的值设置为[ImageFit](../harmonyos-references/ts-appendix-enums.md#imagefit).Cover可保证Image组件锁定宽高比进行缩放。

## 问题定位

1. 检查被截断图片组件，图片和父组件的宽高比是否一致。
2. 检查代码中不同宽高比的父组件引用的图片是否是同一资源路径的图片，如果是同一路径，则引用了同一张图片，例如下面代码。

```ts
@Entry
@Component
export default struct Index {
  build() {
    Column() {
      Row() {
        Image($r('app.media.startIcon'))
          .objectFit(ImageFit.Cover);
      }
      // 此处用aspectRatio模拟宽高比，也可以是具体的宽度和高度属性
      .aspectRatio(1.5);

      Row() {
        Image($r('app.media.startIcon'))
          .objectFit(ImageFit.Cover);
      }
      // 此处用aspectRatio模拟宽高比，也可以是具体的宽度和高度属性
      .aspectRatio(1);
    }
    .width('100%')
    .height('100%');
  }
}
```

## 分析结论

ImageFit.Cover使得图片两边都大于或等于显示边界，对齐方式为水平居中。当图片延长至状态栏，宽度也会超出屏幕外，因此当Image组件引用的图片资源的宽高比与父组件宽高比不一致时，显示出来的图片就会被截断。应用中不同宽高比父组件引用了同一张图片，与图片宽高比不一致的父组件在页面上显示出来的图片就会被截断。

## 修改建议

1. 准备图片内容一致，宽高比不一致的图片，放在对应的宽高比组件内。

   ```ts
   @Entry
   @Component
   struct ImagePage {
     build() {
       Column() {
         Row() {
           // 这里引用的资源图片宽高比为1.5，该资源只是示例，使用时可更改为已有资源
           Image($r('app.media.test'))
             .objectFit(ImageFit.Cover)
         }
         // 此处用aspectRatio模拟宽高比，也可以是具体的宽度和高度属性
         .aspectRatio(1.5)
         .margin(10)
       }
       .width('100%')
       .height('100%')
     }
   }
   ```
2. 使用objectFit设置图片的缩放类型，保证图片能够正常显示。
