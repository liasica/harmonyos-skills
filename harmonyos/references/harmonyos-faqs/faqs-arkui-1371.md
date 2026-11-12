---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1371
title: 如何解决Checkbox组件无法全部选中的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Checkbox组件无法全部选中的问题
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:a38b8a4179df8e0ccc95e3071dba73ac6666d3a748df6626ee826b74ee2aa7c2
---

## 问题现象

List中有Checkbox组件，全选只能选中屏幕中的选项，超出屏幕的选项不能被选中。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/j11oEnCKSI-BBkyLVcMf-w/zh-cn_image_0000002658961253.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233152Z&HW-CC-Expire=31536000000&HW-CC-Sign=4442557927F1A43A7D6D8CA0804B7297EA5B16C451D50AA4A7C3FFD2071E425F "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/VHjMCKHZSs6kdmPLoSsghg/zh-cn_image_0000002658841305.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233152Z&HW-CC-Expire=31536000000&HW-CC-Sign=6BFF4EAF1A1407768C4837C3FBEBD7D58DC0B489D1E60A554B4F6D456DA00D05 "点击放大")

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
