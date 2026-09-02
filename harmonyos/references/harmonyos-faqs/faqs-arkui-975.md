---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-975
title: 如何实现图片透明度渐变动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现图片透明度渐变动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cc90316b3c7cfe2688022bef3a37de592ec63e34af859f31eaeeae61f4b421da
---

## 问题现象

如何在Image组件切换时，形成透明度由高到低的动画效果？

## 背景知识

* [关键帧动画 (keyframeAnimateTo)](../harmonyos-references/ts-keyframeanimateto.md)：在UIContext中提供keyframeAnimateTo接口来指定若干个关键帧状态，实现分段的动画。
* [opacity](../harmonyos-references/ts-universal-attributes-opacity.md#opacity)：设置组件的不透明度，取值范围为0到1，1表示不透明，0表示完全透明。

## 解决方案

可以利用if条件语句来控制Image的展示，配合关键帧动画修改图片的透明度，从而达成透明度渐变动画，示例代码参考如下：

```ts
@Entry
@Component
struct ImageOpacityAnimate {
  @State showOpacity: number = 1;
  @State showIndex: number = 0;
  data: ResourceStr[] = [];

  aboutToAppear() {
    // 图片资源需自行替换
    this.data.push($r('app.media.img1'));
    this.data.push($r('app.media.img2'));
    this.data.push($r('app.media.startIcon'));
  }

  build() {
    Column({ space: 5 }) {
      Column() {
        ForEach(this.data, (item: ResourceStr, index: number) => {
          if (this.showIndex === index) {
            Image(item)
              .width(200)
              .height(200)
              .opacity(this.showOpacity);
          }
        });
      };

      Button('click').onClick(() => {
        this.show();
      });
    }
    .width('100%');
  }

  show() {
    this.getUIContext().keyframeAnimateTo({
      iterations: 1,
      onFinish: () => {
        // 递归调用
        this.show();
      }
    },
      [
        {
          duration: 1000,
          event: () => {
            // 第一段动画把图片透明度从1变成0
            this.showOpacity = 0;
          }
        },
        {
          duration: 500,
          event: () => {
            // 第二段动画完成图片切换
            this.showIndex = (this.showIndex + 1) % this.data.length;
          }
        },
        {
          duration: 1000,
          event: () => {
            // 第三段动画把图片透明度从0变成1
            this.showOpacity = 1;
          }
        }
      ]);
  }
}
```
