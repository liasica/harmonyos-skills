---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-610
title: 实现可展开的首页缩略图
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现可展开的首页缩略图
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:48cb0615628833490b96662f4e2d1e86ac02fdf2fe10281c9f415396b32d4a42
---

## 问题现象

如何在新闻等列表页面中实现可展开的缩略图？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/fJNDPG3BTfOVUm94yJb2Pw/zh-cn_image_0000002658911939.png "点击放大")

## 背景知识

* [UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)提供[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)接口，用于在因闭包代码引起的状态变化时，插入过渡动画，从而实现平滑的界面状态转换效果。
* [Flex](../harmonyos-references/ts-container-flex.md)是以弹性方式布局子组件的容器组件，能够高效地排列、对齐子元素并分配剩余空间。

## 解决方案

1. 创建一个名为scrollItems的自定义组件。在build函数中，先用Text显示标题，再通过Flex布局展示内容。当flag为true时，Flex使用横向排列；当flag为false时，改为纵向排列。
2. 为Flex添加点击事件onClick，点击时调用animateTo方法触发动画效果，并将flag的值取反，从而实现布局方向的切换动画。
3. 在父组件中使用ForEach对scrollItems进行循环渲染，传入不同的数据，实现多个模块的复用展示。每个scrollItems都可以独立切换布局。

```ts
@Entry
@Component
struct ExpandableThumbnailDemo {
  @State arr: string[] = ['国内新闻', '国际新闻', '生活娱乐', '信息世界'];

  build() {
    Scroll() {
      Column() {
        ForEach(this.arr, (item: string, index: number) => {
          scrollItems({ text: item, colorID: index }).transition({ type: TransitionType.All });
        }, (value: string) => value);
      };
    }
    .width('100%')
    .height('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
    .align(Alignment.Top);
  }
}

@Component
struct scrollItems {
  @State flag: boolean = true;
  text: string = '';
  colorID: number = 0;
  color: string = ((index: number): string => {
    const colors: string[] = ['255,0,0', '255,0,0', '255,0,0', '255,0,0'];
    return colors[index];
  })(this.colorID);

  build() {
    Column() {
      Text(this.text)
        .width('100%')
        .height(25)
        .margin({ bottom: 3 })
        .fontColor(this.color);
      Flex({
        direction: this.flag ? FlexDirection.Row : FlexDirection.Column, // 横向布局和纵向布局切换
        justifyContent: FlexAlign.Start,
        alignItems: ItemAlign.Start
      }) {
        Column() {
          Image($r('app.media.startIcon')); // 此处仅为样例，请开发者更换为可用图片
        }
        .width(this.flag ? 80 : '100%')
        .height(this.flag ? 80 : 240)
        .borderRadius(4)
        .backgroundColor('#ffadcfff')
        .margin({ right: 7, bottom: 7 });

        Column() {
          Row() {
            Text('国内发生重大新闻');
          }
          .width('100%')
          .height(20)
          .backgroundColor('#ffadcfff')
          .borderRadius(4)
          .padding({ left: 10 });

          Row() {
            Text('国外发生重大新闻');
          }
          .width('70%')
          .height(20)
          .backgroundColor('#FFE8F0FF')
          .borderRadius(4)
          .padding({ left: 10 })
          .margin({ top: 10 });

          Row() {
            Text('国外发生了重大新闻');
          }
          .width('75%')
          .height(20)
          .backgroundColor('#FFE8F0FF')
          .padding({ left: 10 })
          .borderRadius(4)
          .margin({ top: 10 });

          if (!this.flag) {
            Row() {
              Text('国内发生了重大新闻');
            }
            .width('70%')
            .height(20)
            .backgroundColor('#FFE8F0FF')
            .borderRadius(4)
            .padding({ left: 10 })
            .margin({ top: 10 });

            Row() {
              Text('国外发生大新闻');
            } // 最小每行内容
            .width('75%')
            .height(20)
            .backgroundColor('#FFE8F0FF')
            .padding({ left: 10 })
            .borderRadius(4)
            .margin({ top: 10 });

            Row() {
              Text('国内发生大新闻');
            } // 最小每行内容
            .width('75%')
            .height(20)
            .backgroundColor('#FFE8F0FF')
            .padding({ left: 10 })
            .borderRadius(4)
            .margin({ top: 10 });
          }
        }
        .alignItems(HorizontalAlign.Start);
      }
      .width('100%')
      .height(this.flag ? 95 : 430)
      .padding({
        top: 7,
        left: 7,
        bottom: 7,
        right: 7
      })
      .margin({ bottom: 5 })
      .borderRadius(8)
      .shadow({ radius: 10, color: 'rgba(0,0,0,1)' })
      .onClick(() => {
        // 布局切换动画效果
        this.getUIContext().animateTo({ duration: 500, curve: Curve.FastOutSlowIn }, () => {
          this.flag = !this.flag;
        });
      });
    }
    .width('100%')
    .padding({ left: 20, right: 20 })
    .margin({ top: 20 });
  }
}
```
