---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1580
title: 如何对SelectDialog的单选项进行增减
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何对SelectDialog的单选项进行增减
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e99e884a00c7c631116ae6738f0870cb31b1aaf085c3e242ad256bcad2a18c3d
---

## 问题现象

如图所示，[纯列表弹出框](../harmonyos-references/ohos-arkui-advanced-dialog.md#示例2纯列表弹出框)提供如下的示意图，如何自定义单选项的数量，使得弹窗属性title的内容是从string数组foreach遍历获取？

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/xDuRdR7nSYSO52dOQrvIyQ/zh-cn_image_0000002658969515.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/3Ejc15GRREKm7UL1o2Yk8A/zh-cn_image_0000002628610296.gif "点击放大")

## 背景知识

[SelectDialog](../harmonyos-references/ohos-arkui-advanced-dialog.md#selectdialog)：选择类弹出框，弹框中以列表或网格的形式提供可选的内容。

## 解决方案

在aboutToAppear中使用for循环动态初始化SelectDialog的radioContent。

```ts
import { SelectDialog } from '@kit.ArkUI';

@Entry
@Component
struct SelectDialogDemo {
  // title数组
  titleList: string[] = [];
  // SelectDialog的radioContent进行初始化
  radioContent: Array<SheetInfo> = [];
  // 设置默认选中radio的index
  radioIndex = 0;
  dialogControllerList: CustomDialogController = new CustomDialogController({
    builder: SelectDialog({
      title: '文本标题',
      selectedIndex: this.radioIndex,
      confirm: {
        value: '取消',
        action: () => {
        },
      },
      // 将初始化后的radioContent赋值给SelectDialog的radioContent属性
      radioContent: this.radioContent
    }),
  });

  build() {
    Row() {
      Stack() {
        Column() {
          Button('纯列表弹出框')
            .width(96)
            .height(40)
            .onClick(() => {
              this.titleList.push('文本');
              this.titleList.push('文本文本');
              this.titleList.push('文本文本文本');
              this.titleList.push('文本文本文本文本');
              this.titleList.push('文本文本文本文本文本');
              this.titleList.push('文本文本文本文本文本文本');

              // 赋值给radioContent
              this.titleList.forEach((value: string, index: number) => {
                let sheetInfo: SheetInfo = {
                  title: value,
                  action: () => {
                    this.radioIndex = index;
                  }
                };
                this.radioContent.push(sheetInfo);
              });
              this.dialogControllerList.open();
            });
        }.margin({ bottom: 300 });
      }
      .align(Alignment.Bottom)
      .width('100%')
      .height('100%');
    }
    .backgroundImageSize({ width: '100%', height: '100%' })
    .height('100%');
  }
}
```
