---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1628
title: 弹窗重复打开问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 弹窗重复打开问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:547996c87fd76e394819e3fc5c85b15efa68011d1e8406eb4e5f2caf2ceda7d1
---

## 问题现象

多次点击字母排序侧边栏，屏幕中间出现弹窗，弹窗的背景不断叠加，背景色加深。

## 背景知识

[弹出框](../harmonyos-guides/arkts-base-dialog-overview.md)是一种模态窗口，通常用于在保持当前上下文环境的同时，临时展示用户需关注的信息或待处理的操作。用户需在模态弹出框内完成相关交互任务之后，才能退出模态模式。弹出框可以不与任何组件绑定，其内容通常由多种组件组成，如文本、列表、输入框、图片等，以实现布局。ArkUI当前提供了自定义和固定样式两类弹出框组件。

[不依赖UI组件的全局自定义弹出框 (openCustomDialog)](../harmonyos-guides/arkts-uicontext-custom-dialog.md)：在广告、中奖、警告、软件更新等与用户交互响应操作的场景下，可以使用UIContext中获取到的PromptAction对象提供的openCustomDialog接口来实现自定义弹出框。相较于CustomDialogController优势点在于页面解耦，支持动态刷新。

## 问题定位

1. 使用DevEco Testing的UIViewer工具查看页面UI结构，对比正常时和异常时UI结构，确认页面中多出了多个Dialog组件，导致出现后面的背景叠加异常显示效果。
2. 排查代码中拉起弹窗的方法触发的位置。确认多个组件绑定了可以拉起弹窗的点击事件。

   ```ts
   @CustomDialog
   struct CustomDialogExample {
     controller: CustomDialogController;

     build() {
       Column() {
         Text('我是内容')
           .fontSize(20)
       }.height(60).justifyContent(FlexAlign.Center)
     }
   }

   @Entry
   @Component
   struct CustomDialogUser {
     showDialog() {
       let dialogController: CustomDialogController = new CustomDialogController({
         builder: CustomDialogExample(),
       });
       dialogController.open();
       setTimeout(()=>{ dialogController.close(); }, 1000);
     }

     build() {
       Column() {
         Text('click me').onTouch(()=>{this.showDialog();}).width(100).backgroundColor(Color.Blue);
         Text('click me').onTouch(()=>{this.showDialog();}).width(100).backgroundColor(Color.Blue);
         Text('click me').onTouch(()=>{this.showDialog();}).width(100).backgroundColor(Color.Blue);
         Text('click me').onTouch(()=>{this.showDialog();}).width(100).backgroundColor(Color.Blue);
         Text('click me').onTouch(()=>{this.showDialog();}).width(100).backgroundColor(Color.Blue);
         Text('click me').onTouch(()=>{this.showDialog();}).width(100).backgroundColor(Color.Blue);
         Text('click me').onTouch(()=>{this.showDialog();}).width(100).backgroundColor(Color.Blue);
         Text('click me').onTouch(()=>{this.showDialog();}).width(100).backgroundColor(Color.Blue);
         Text('click me').onTouch(()=>{this.showDialog();}).width(100).backgroundColor(Color.Blue);
         Text('click me').onTouch(()=>{this.showDialog();}).width(100).backgroundColor(Color.Blue);
         Text('click me').onTouch(()=>{this.showDialog();}).width(100).backgroundColor(Color.Blue);
         Text('click me').onTouch(()=>{this.showDialog();}).width(100).backgroundColor(Color.Blue);
         Text('click me').onTouch(()=>{this.showDialog();}).width(100).backgroundColor(Color.Blue);
         Text('click me').onTouch(()=>{this.showDialog();}).width(100).backgroundColor(Color.Blue);
         Text('click me').onTouch(()=>{this.showDialog();}).width(100).backgroundColor(Color.Blue);
       }.width('100%').margin({ top: 5 })
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/s-TzLPQMQ5-m8bn7sio9EQ/zh-cn_image_0000002628617580.png "点击放大")

## 分析结论

多次点击字母排序侧边栏，一直弹出新的Dialog，未及时销毁前面Dialog，导致图层堆叠，显示异常。

## 修改建议

使用同一个Dialog组件，后续滑动过程中复用同一个Dialog组件，更新其中的文字，[使用openCustomDialog动态刷新Dialog示例。](../harmonyos-guides/arkts-uicontext-custom-dialog.md#完整示例)
