---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-common-events
title: 通用事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 组件通用信息 > 通用事件
category: harmonyos-references
scraped_at: 2026-04-28T08:03:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d3c8884f2be58e16f91a39915eef393acf6774b1cfc3f182c35d865a24d97fe0
---

相对于私有事件，大部分组件都可以绑定如下事件。

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| click | - | 点击动作触发该事件。 |
| longpress | - | 长按动作触发该事件。 |
| swipe5+ | SwipeEvent | 组件上快速滑动后触发。 |

SwipeEvent 基础事件对象属性列表（继承BaseEvent）

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| direction | string | 滑动方向，可能值有：  1. left：向左滑动；  2. right：向右滑动；  3. up：向上滑动；  4. down：向下滑动。 |
