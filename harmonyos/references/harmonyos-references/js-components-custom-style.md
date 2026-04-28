---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-custom-style
title: 继承样式
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 自定义组件 > 继承样式
category: harmonyos-references
scraped_at: 2026-04-28T08:03:20+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:779b61fbf6b5a5abab230fd2d949098efee166b7a014320d461b14e2cbb97bbc
---

说明

从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

自定义组件具有inherit-class属性，定义如下：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| inherit-class | string | - | 否 | 从父组件继承的class样式，多个class样式之间用空格分隔。 |

可以通过设置inherit-class属性来继承父组件的样式。

父组件的hml文件，其中自定义组件comp通过inherit-class属性来指定继承其父组件的样式，即parent-class1和parent-class2：

```
1. <!-- xxx.hml -->
2. <element name='comp' src='../../common/component/comp.hml'></element>

4. <div class="container">
5. <comp inherit-class="parent-class1 parent-class2" ></comp>
6. </div>
```

父组件的css文件：

```
1. /* xxx.css */
2. .parent-class1 {
3. background-color:red;
4. border:2px;
5. }
6. .parent-class2 {
7. background-color:green;
8. border:2px;
9. }
```

自定义组件的hml文件，其中parent-class1和parent-class2是从父组件继承的样式：

```
1. <!--comp.hml-->
2. <div class="item">
3. <text class="parent-class1">继承父组件的样式1</text>
4. <text class="parent-class2">继承父组件的样式2</text>
5. </div>
```
