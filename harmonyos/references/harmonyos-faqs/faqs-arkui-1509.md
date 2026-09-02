---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1509
title: 通过isShown状态控制bindContextMenu实现菜单随点击位置弹出
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 通过isShown状态控制bindContextMenu实现菜单随点击位置弹出
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:55e0451e09f285625a191492f3c231e1081ba21cc32600485b03238b58afda76
---

## 问题现象

使用bindContextMenu时，通过长按触发，菜单能够准确跟随点击位置弹出。然而，当通过绑定的isShown状态变量触发菜单显示时，菜单无法覆盖在绑定组件上方，且无法直接跟随点击位置弹出。如何实现通过isShown控制时，菜单仍能跟随点击位置弹出呢？

## 背景知识

* [bindContextMenu⁸](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu8)：给组件绑定菜单，控制菜单显隐的触发方式为长按或者通过[bindContextMenu¹²](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu12)给组件绑定菜单，菜单的显隐通过控制绑定的isShown触发。
* [ContextMenuOptions](../harmonyos-references/ts-universal-attributes-menu.md#contextmenuoptions10)：配置弹出菜单的参数。

## 解决方案

通过isShown状态变量触发bindContextMenu时，控制菜单显隐的组件与实际绑定菜单的组件可以分离。具体实现方案如下：

1. 将一个不可见的组件（如高度宽度为0的组件）用于绑定bindContextMenu菜单。
2. 由实际接收点击事件的组件控制isShown状态，并在点击时通过事件对象获取当前点击位置的屏幕坐标。
3. 将获取的坐标值通过菜单配置参数（如ContextMenuOptions中的offset属性）动态设置菜单弹出位置，从而实现菜单跟随点击位置弹出。

   ```ts
   @Entry
   @Component
   struct BindMenu {
     @State isShown: boolean = false;
     private clickX: number = 0;
     private clickY: number = 0;

     @Builder
     MyMenu() {
       Menu() {
         MenuItem({ content: '菜单选项' });
         MenuItem({ content: '菜单选项' });
         MenuItem({ content: '菜单选项' });
       }
     }

     build() {
       Column() {
         // 绑定菜单的不显示组件，置于屏幕左上角
         Row() {
         }.width('0%')
         .height('0%')
         .bindContextMenu(this.isShown, this.MyMenu,
           {
             placement: Placement.BottomRight,
             // 根据点击屏幕位置设置菜单偏移
             offset: {
               x: this.clickX,
               y: this.clickY
             }
           });

         // 控制isShown的组件，同时获取点击屏幕位置
         Column() {
           Text('preview-builder')
             .width(200)
             .height(100)
             .textAlign(TextAlign.Center)
             .margin(100)
             .fontSize(30)
         }.width('100%')
         .height('100%')
         .onClick((event?: ClickEvent) => {
           if (!this.isShown) {
             this.clickX = event!.windowX;
             this.clickY = event!.windowY;
             this.isShown = true;
           } else {
             this.isShown = false;
           }
         });
       }
     }
   }
   ```
