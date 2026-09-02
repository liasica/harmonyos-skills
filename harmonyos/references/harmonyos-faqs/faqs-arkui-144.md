---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-144
title: ArkUI组件的字符串中如何实现字符串变量拼接
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > ArkUI组件的字符串中如何实现字符串变量拼接
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:6deccb18ef8db89bb4e0eca75325da0c2bebabe25f3c3ef2e96e0215aa932857
---

**问题现象**

ArkUI组件的字符串中如何实现字符串变量拼接，结合限定词目录的资源文件，例如语言切换时候，字符串内容自动跟随切换。例如Text()组件如何实现字符串变量的拼接功能？

```typescript
Text($r('app.string.EntryAbility_desc', 'Hello'))
```

**解决措施**

可以通过资源文件结合`%d`和`%s`的方式实现。使用样例如下所示。

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
2. 在页面组件中，使用$r(xx)拼接变量。

   ```screen
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
3. 切换中英文语言时，自动带入对应变量信息。

**参考链接**

[资源分类与访问](../harmonyos-guides/resource-categories-and-access.md)
