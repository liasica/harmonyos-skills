---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-673
title: 如何实现根据不同的列表项，弹出不同的上下文菜单
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现根据不同的列表项，弹出不同的上下文菜单
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:00671e4b558c6f159ff5ee6f28fe8f09910b8be76208290a9143b7a4ab346065
---

## 问题现象

给List组件的Item绑定上下文菜单，按条件判断是否显示上下文菜单，且需要根据列表项的不同，弹出不同的上下文菜单，该如何实现？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/scIw7tzMTJOh_mgjkCCggg/zh-cn_image_0000002628554566.gif "点击放大")

## 背景知识

* [List](../harmonyos-references/ts-container-list.md)：列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。
* [bindContextMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu8)：给组件绑定菜单，触发方式为长按或者右键点击，弹出菜单项需要自定义。

## 解决方案

首先对List组件的Item进行判断，使偶数项有菜单弹出，奇数项则无菜单弹出。菜单弹出方式为长按弹出菜单且弹出菜单的内容也不同。

完整示例参考如下：

```ts
@Entry
@Component
struct listDemo {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  @State listData: number[] = [0, 0, 0];

  // @Builder装饰器：构建上下文菜单组件
  @Builder
  MenuBuilder(num: number, flag: boolean) {
    // 根据flag参数决定是否显示菜单
    if (flag) {
      Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
        ForEach(this.listData, (index:number) => {
          Column() {
            Row() {
              Image($r('app.media.startIcon')).width(20).height(20).margin({ right: 5 }) // 可根据具体需要引用资源
              Text(`Menu${num}`).fontSize(20)
            }
            .width('100%')
            .height(30)
            .justifyContent(FlexAlign.Center)
            .align(Alignment.Center)

            // 如果不是最后一个菜单项，显示分隔线
            if (index !== this.listData.length - 1) {
              Divider().height(10).width('80%').color('#ccc')
            }
          }.padding(5).height(40)
        });
      }.width(100)
    }
  };

  build() {
    Column() {
      List({ space: 20, initialIndex: 0 }) {
        ForEach(this.arr, (item: number) => {
          // 根据item奇偶性决定是否绑定上下文菜单
          if (item % 2 === 0) {
            ListItem() {
              Text('' + item)
                .width('100%')
                .height(100)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor(0xFFFFFF) // 绑定上下文菜单，使用MenuBuilder生成菜单，长按触发
                .bindContextMenu(this.MenuBuilder(item, true), ResponseType.LongPress)
            };
          } else {
            ListItem() {
              Text('' + item)
                .width('100%')
                .height(100)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .borderRadius(10)
                .backgroundColor(0xFFFFFF)
                .bindContextMenu(this.MenuBuilder(item, false), ResponseType.LongPress)
            };
          }
        }, (item: string) => item)
      }.width('90%')
      .scrollBar(BarState.Off)
    }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
  }
}
```
