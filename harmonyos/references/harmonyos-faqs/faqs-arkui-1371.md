---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1371
title: 如何解决Checkbox组件无法全部选中的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Checkbox组件无法全部选中的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:daacec15409543999ff82b73da8ee657e4bd38616eab14e9c11dcccb99859cde
---

## 问题现象

List中有Checkbox组件，全选只能选中屏幕中的选项，超出屏幕的选项不能被选中。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/v7wRW_ntRJa6_y6Db4YPIA/zh-cn_image_0000002658961253.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/vOjdVTJ0To-DmK9JK9G5XQ/zh-cn_image_0000002658841305.gif "点击放大")

## 背景知识

* [Checkbox](../harmonyos-references/ts-basic-components-checkbox.md)是一种常见且实用的交互元素，它允许用户从一系列选项中选择多个项。无论是电子商务网站上的商品筛选，还是在线表单的数据收集，Checkbox都发挥着重要作用。
* [List组件](../harmonyos-guides/arkts-layout-development-create-list.md)只加载和渲染当前屏幕可视区域内的列表项，这被称为按需加载。当用户滚动列表时，List组件会动态加载和卸载列表项，以确保只渲染当前可见的项，从而提高性能。

## 解决方案

List组件按需加载的特性使得每次只有当前可见项被渲染，导致全选时无法选中所有组件，可以在List组件外再套一层Scroll组件，确保所有组件可以被渲染。

```ts
@Entry
@Component
struct SelectAllCheckBoxSample {
  @State dataArray: string[] = [];

  aboutToAppear(): void {
    for (let i = 0; i < 50; i++) {
      this.dataArray.push(i + '');
    }
  }

  build() {
    Row() {
      Column() {
        Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
          CheckboxGroup({ group: 'checkboxGroup' })
            .checkboxShape(CheckBoxShape.ROUNDED_SQUARE)
            .selectedColor('FF0858F8')
            .onChange((itemName: CheckboxGroupResult) => {
              console.info(`checkbox group content ${JSON.stringify(itemName)} `);
            })
            .mark({
              strokeColor: Color.White,
              size: 40,
              strokeWidth: 5
            })
            .unselectedColor(Color.Gray)
            .width(30)
            .height(30)
          Text('Select All').fontSize(20);
        }.margin({ right: 40 })

        Scroll() { // 在外面套一层scroll
          List() {
            ForEach(this.dataArray,
              (item: string, index: number) => {
                ListItem() {
                  Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
                    Checkbox({ name: 'checkbox' + index, group: 'checkboxGroup' })
                      .selectedColor('FF0858F8')
                      .shape(CheckBoxShape.ROUNDED_SQUARE)
                      .onChange((value: boolean) => {
                        console.info(`Checkbox${index}change is${value}`);
                      })
                      .mark({
                        strokeColor: Color.White,
                        size: 50,
                        strokeWidth: 5
                      })
                      .unselectedColor(Color.Gray)
                      .width(30)
                      .height(30)
                    Text(`Checkbox${index}`).fontSize(20);
                  }
                  .width(160)
                }.backgroundColor(Color.White)
              }
            )
          }
          .alignListItem(ListItemAlign.Center)
          .width('100%')

        }
      }.layoutWeight(1)
      .width(300)
      .height('100%')
    }
    .height('100%')
    .margin({ top: '16PX' })

  }
}
```
