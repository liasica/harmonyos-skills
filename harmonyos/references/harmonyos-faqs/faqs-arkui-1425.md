---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1425
title: 输入框光标闪烁效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 输入框光标闪烁效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a6a3e7d1a64868f6a62bfb13b7b6264cfc8abdf3d562946bd7b23feb12abbef9
---

## 问题现象

如何实现输入框在未输入时光标闪烁的效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/tN4XvCEBTlKNx3_TAzcBpQ/zh-cn_image_0000002658843011.png "点击放大")

## 背景知识

[visibility](../harmonyos-references/ts-universal-attributes-visibility.md)：控制组件的显示或隐藏。当未设置visibility时，组件默认为显示。通过设置属性值Hidden（隐藏，但参与布局进行占位）、Visible（显示）与None（隐藏，但不参与布局，不进行占位）控制组件是否可见。

## 解决方案

实现输入框在未输入时光标闪烁的效果可通过使用[setInterval](../harmonyos-references/js-apis-timer.md#setinterval)定时器切换元素的visibility属性来控制组件的显隐，模拟出光标闪烁的效果。

```screen
@Entry
@Component
struct TextInputPage {
  @State isShowPoint: boolean = true;
  private setIntervalB: number = -1;
  @State isFirstCLick: boolean = true;

  aboutToDisappear(): void {
    // 页面销毁，关闭定时器
    clearInterval(this.setIntervalB);
  }

  aboutToAppear(): void {
    this.carbetFire();
  }

  carbetFire() {
    if (this.isFirstCLick) {
      this.isFirstCLick = false;
      this.setIntervalB = setInterval(() => {
        this.isShowPoint = !this.isShowPoint;
      }, 800);
    }
  }

  build() {
    RelativeContainer() {
      Stack() {
        Row() {
          Row()
            .width(2)
            .height(18)
            .backgroundColor('#0A59F7')
            .margin({ left: 16 });
          Blank()
            .height('100%');
        }
        .width('100%')
        .height('100%')
        // 控制组件的显示隐藏
        .visibility(this.isShowPoint ? Visibility.Visible : Visibility.None);

        TextInput()
          .margin({left:16,right:16})
          .width('100%')
          .onEditChange((status: boolean) => {
            if (status) {
              clearInterval(this.setIntervalB);
              this.isShowPoint = false;
              this.isFirstCLick = true;
            } else {
              this.isShowPoint = true;
              this.carbetFire();
            }
          });
      }
      .alignRules({
        center: { anchor: '__container__', align: VerticalAlign.Center },
        middle: { anchor: '__container__', align: HorizontalAlign.Center }
      })
      .width('95%')
      .height(40)
      .margin({ left: 16, right: 16 });
    }
    .height('100%')
    .width('100%');
  }
}
```
