---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-528
title: 如何监听ListItemGroup的Header吸顶状态
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何监听ListItemGroup的Header吸顶状态
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9cc29ebbd5a6c944dd19fe645060a653220f634f421f344bb7502f49a575d854
---

## 问题现象

是否有API能够返回当前ListItemGroup的Header吸顶的状态？

## 背景知识

* [ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)：用来展示列表item分组，宽度默认充满[List](../harmonyos-references/ts-container-list.md)组件，必须配合List组件来使用。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)：组件区域变化时触发该回调。组件区域变化事件指组件显示的尺寸、位置等发生变化时触发的事件。

## 解决方案

原理说明：

1. sticky属性设置：通过.sticky(StickyStyle.Header)启用列表的头部吸顶特性。
2. 组件区域变化监听：在自定义Header组件中，使用onAreaChange事件监听组件位置变化。
3. 坐标判断逻辑：通过判断事件参数中的oldValue.position.y === 0 && newValue.position.y === 0时表示未吸顶。

```ts
@Entry
@Component
struct StickyHeaderExample {
  private arr: number[] = [0, 1];

  @Builder
  CustomHeader() {
    Text('分组标题')
      .height(50)
      .width('100%')
      .backgroundColor(Color.Gray)
      .onAreaChange((oldValue: Area, newValue: Area) => {
        if (oldValue.position.y === 0 && newValue.position.y === 0) {
          console.info('没吸顶');
        } else {
          console.info(`吸顶了 ${oldValue.position.y}`);
        }
      });
  }

  build() {
    Column() {
      List({ space: 10 }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Text(item.toString())
              .width('100%')
              .height(50)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF);
          };
        }, (item: string) => item);
        ListItemGroup({
          header: this.CustomHeader,
          space: 10
        }) {
          ForEach(Array.from({ length: 20 }), (item: void, index: number) => {
            ListItem() {
              Text(`列表项 ${index}`)
                .height(80)
                .width('100%')
                .backgroundColor('#FFF');
            };
          });
        };
      }
      .sticky(StickyStyle.Header)
      .width('100%')
      .height('100%');
    };
  }
}
```
