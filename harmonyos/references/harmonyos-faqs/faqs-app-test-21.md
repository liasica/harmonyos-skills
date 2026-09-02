---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-21
title: 自定义UI组件无类型、无id，UI测试该如何操作
breadcrumb: FAQ > DevEco Studio > 应用测试 > 自定义UI组件无类型、无id，UI测试该如何操作
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6254e7e789ee72754d06427c1708b94526799fd49aed66a7f1301ddd45d31064
---

## 问题现象

组件测试，UI测试，自定义UI组件无法通过类型找到，也无id属性，应该怎么操作？

## 背景知识

UiTest框架从API version 9开始，通过On类提供了丰富的控件特征描述API，用于进行控件筛选来匹配/查找出目标控件。

On提供的API能力具有以下几个特点:

1. 支持单属性匹配和多属性组合匹配，例如同时指定目标控件text和id。
2. 控件属性支持多种匹配模式。
3. 支持控件绝对定位，相对定位，可通过ON.isBefore和ON.isAfter等API限定邻近控件特征进行辅助定位。

On类提供的所有API均为同步接口，建议使用者通过静态构造器ON来链式创建On对象。

UiTest API文档：[UI Test](../harmonyos-references/js-apis-uitest.md#on9)。

## 解决方案

如果不能通过类型或id找到，可以尝试通过text、描述、组件的位置关系等进行定位。

```screen
async function test() {
  let driver: Driver = Driver.create();
  let on: On = ON.text('456').isBefore(ON.text('123')); // 查找text为123之前的第一个text为456的组件
  let button: Component = await driver.findComponent(on);
  await button.click()
}
```
