---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-376
title: 如何实现ArkUI组件字符串变量拼接
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现ArkUI组件字符串变量拼接
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:050acf7b2b1a34174dc89c733f04f53d1c76e0460596a6b5f30c7a3b2875514c
---

**问题现象**

例如：在Text组件中如何实现字符串与变量的拼接功能？

```typescript
Text($r('app.string.EntryAbility_desc', 'Hello'))
```

**解决措施**

可以通过资源文件结合%d、%s的方式进行实现。

示例如下所示：

1. 修改"src/main/resources/zh\_CN/element/string.json"文件，对其中的一个需要变量拼接内容增加%d拼接。

   ```json
   { 
     "string": [ 
       { 
         "name": "module_desc", 
         "value": "模块描述%d" 
       }, 
       { 
         "name": "EntryAbility_desc", 
         "value": "description" 
       }, 
       { 
         "name": "EntryAbility_label", 
         "value": "label" 
       } 
     ] 
   }
   ```

   修改"src/main/resources/en\_US/element/string.json"文件，对其中的一个需要变量拼接内容增加%d拼接。

   ```json
   { 
     "string": [ 
       { 
         "name": "module_desc", 
         "value": "module description%d" 
       }, 
       { 
         "name": "EntryAbility_desc", 
         "value": "description%d" 
       }, 
       { 
         "name": "EntryAbility_label", 
         "value": "label" 
       } 
     ] 
   }
   ```
2. 在页面组件中使用$r()方法拼接变量（示例代码如下）。

   ```typescript
   @Entry
   @Component
   struct Page1 {
     @State num1: number = 100;

     build() {
       Row() {
         Column() {
           Text($r('app.string.module_desc', this.num1))
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
3. 切换中英文语言时，会自动跟随语言的切换代入对应的变量信息。

**参考链接**

[资源访问](../harmonyos-guides/resource-categories-and-access.md#资源访问)
