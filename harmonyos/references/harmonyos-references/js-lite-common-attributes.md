---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-common-attributes
title: 通用属性
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 组件通用信息 > 通用属性
category: harmonyos-references
scraped_at: 2026-04-28T08:03:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:61a43581c393d68ac1acefd9be52c446828a0770c811d988cbfbadf62f19cd2e
---

## 常规属性

PhonePC/2in1TabletTVWearableLite Wearable

常规属性指的是组件普遍支持的用来设置组件基本标识和外观显示特征的属性。

| 名称 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| id | string | 否 | 组件的唯一标识。 |
| style | string | 否 | 组件的样式声明。 |
| class | string | 否 | 组件的样式类，用于引用样式表。 |
| ref | string | 否 | 用来指定指向子元素的引用信息，该引用将注册到父组件的$refs 属性对象上。 |

## 渲染属性

PhonePC/2in1TabletTVWearableLite Wearable

组件普遍支持的用来设置组件是否渲染的属性。

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| for | Array | 根据设置的数据列表，展开当前元素。 |
| if | boolean | 根据设置的boolean值，添加或移除当前元素。 |
| show | boolean | 根据设置的boolean值，显示或隐藏当前元素。 |

说明

属性和样式不能混用，不能在属性字段中进行样式设置。
