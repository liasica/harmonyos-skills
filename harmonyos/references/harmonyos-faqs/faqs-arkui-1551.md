---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1551
title: 如何实现可调高度的下载按钮
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现可调高度的下载按钮
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:74eb1a7c0cd77ba7a69cf5e5c1aecc8103da6fb4f1e144abd4b608de8f9b139e
---

## 问题现象

ProgressButton默认不支持高度调整，如何实现可调高度的下载按钮？

## 背景知识

[Progress](../harmonyos-references/ts-basic-components-progress.md)：进度条组件，用于显示内容加载或操作处理等进度。

## 解决方案

* 方案逻辑：Progress组件可以配置高度，使用Progress的属性可实现与ProgressButton相同的下载效果。
  1. 通过Progress组件的style属性的content参数，实现在Progress组件上显示按钮文字和进度信息。

     ```ts
     Progress({ value: this.progressIndex, total: 100, type: ProgressType.Capsule })
       .width(300)
       .height(100)  // 设置Progress组件的高度
       .color(Color.Blue)
       .margin({top:300})
       .style({
         borderWidth: 1,
         content: this.textState, // 设置按钮文字
         font: { size: 13, style: FontStyle.Normal },
         enableScanEffect: false,
         showDefaultPercentage: false
       })
     ```
  2. 给Progress添加点击事件，控制Progress上显示内容的变化。初始时，显示为“下载”；点击后动态显示下载进度，再次点击后显示“继续”，并且暂停下载进度；进度100%后，显示为“完成”。

     ```ts
     .onClick(() => {
       this.isRunning = !this.isRunning;
       if (this.textState && !this.isRunning && this.progressIndex < 100) {
         this.textState = '继续';
       }
       let timer = setInterval(() => {
         if (this.isRunning && this.progressIndex < 100) {
           this.progressIndex++;
           this.textState = `${this.progressIndex}%`;
           if (this.progressIndex === 100) {
             this.textState = '已完成';
             this.isRunning = false;
           }
         } else {
           clearInterval(timer);
         }
       }, 20);
     })
     ```
  3. 设置Progress组件的高度。

     ```ts
     Progress({ value: this.progressIndex, total: 100, type: ProgressType.Capsule })
       .width(300)
       .height(100)  // 设置Progress组件的高度
     ```

* 完整示例参考如下：

  ```ts
  @Entry
  @Component
  struct PushButton {
    @State progressIndex: number = 0;
    @State textState: string = '下载';
    @State isRunning: boolean = false;

    build() {
      Column({ space: 20 }) {
        Progress({ value: this.progressIndex, total: 100, type: ProgressType.Capsule })
          .width(300)
          .height(100)  // 设置Progress组件的高度
          .color(Color.Blue)
          .margin({top:300})
          .style({
            borderWidth: 1,
            content: this.textState, // 设置按钮文字
            font: { size: 13, style: FontStyle.Normal },
            enableScanEffect: false,
            showDefaultPercentage: false
          })

          .onClick(() => {
            this.isRunning = !this.isRunning;
            if (this.textState && !this.isRunning && this.progressIndex < 100) {
              this.textState = '继续';
            }
            let timer = setInterval(() => {
              if (this.isRunning && this.progressIndex < 100) {
                this.progressIndex++;
                this.textState = `${this.progressIndex}%`;
                if (this.progressIndex === 100) {
                  this.textState = '已完成';
                  this.isRunning = false;
                }
              } else {
                clearInterval(timer);
              }
            }, 20);
          })
      }.alignItems(HorizontalAlign.Center).width('100%').margin({ top: 20 })
    }
  }
  ```
