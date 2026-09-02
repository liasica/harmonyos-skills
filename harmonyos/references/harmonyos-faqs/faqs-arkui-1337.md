---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1337
title: Span组件响应组件外点击事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Span组件响应组件外点击事件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7644a81bfb291f162b66d31745ba95c9cefb379e5cf843af8482cf5109563a60
---

## 问题现象

由于Span组件不支持宽高属性设置，因此在其文字内容外部无法触发点击事件。目前有一组包含联系人的数据，需要点击每个联系人能够跳转到对应的联系人详情信息页面（联系人所在行也都能响应点击事件），Span组件如何实现该功能？

## 背景知识

[Span组件](../harmonyos-references/ts-basic-components-span.md)目前仅支持继承的属性包括：fontColor、fontSize、fontStyle、fontWeight、decoration、letterSpacing、textCase、fontfamily、textShadow，但不支持通用属性，因此即使设置了通用属性，如：width、height，但并不会生效。

## 解决方案

[点击事件](../harmonyos-references/ts-universal-events-click.md)可以获取点击位置相对于被点击元素原始区域左上角的Y坐标，可以通过给出的Y坐标和对象显示区域计算出对应Span组件。

以下为具体步骤：

1. 通过点击事件获取组件高度、当前点击的Y坐标值。
2. 基于Span组件总数，计算出单个Span高度值。
3. 使用点击的Y坐标值对Span高度值整除，计算出被点击的对应Span组件区域。

   ```screen
   import hilog from '@ohos.hilog';

   @Entry
   @Component
   export struct Index {
     private contacts: string[] = ['张三', '李四', '王五', '赵六'];

     onClicked(event: ClickEvent) {
       const height: number = event.target.area.height as number; // 组件总高度
       const avgHeight: number = height / this.contacts.length; // 分配到每个Span的平均高度

       let index: number = Math.floor(event.y / avgHeight); // 计算点击位置所在编号，取整，忽略小数部分
       if (index >= this.contacts.length) {
         index = this.contacts.length - 1;
       }

       this.getUIContext().getPromptAction().showDialog({
         title: '联系人信息',
         message: this.contacts[index]
       }).catch(() => {
         hilog.error(0x0, 'Index', 'Show dialog error.');
       });
     }

     build() {
       Column() {
         Text() {
           ForEach(this.contacts, (item: string, index: number) => {
             Span(item)
             if (index < this.contacts.length - 1) {
               Span('\n')
             }
           })
         }
         .width('100%')
         .fontSize(20)
         .fontFamily('HarmonyOS Sans')
         .textAlign(TextAlign.Center)
         .onClick((event: ClickEvent) => {
           this.onClicked(event);
         })
       }
       .padding(12)
     }
   }
   ```
