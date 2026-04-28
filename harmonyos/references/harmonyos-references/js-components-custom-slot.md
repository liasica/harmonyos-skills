---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-custom-slot
title: slot插槽
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 自定义组件 > slot插槽
category: harmonyos-references
scraped_at: 2026-04-28T08:03:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:08c0c40a3acf1dfd34700080439a50628238524c9521200f784a0bb7a326532e
---

说明

从API version 7 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 默认插槽

PhonePC/2in1TabletTVWearable

自定义组件中通过slot标签来承载父组件中定义的内容，使用slot标签可以更加灵活的控制自定义组件的内容元素，使用方式如下：

```
1. <!-- comp.hml -->
2. <div class="item">
3. <text class="text-style">下面使用父组件定义的内容</text>
4. <slot></slot>
5. </div>
```

引用该自定义组件方式如下：

```
1. <!-- xxx.hml -->
2. <element name='comp' src='../common/component/comp.hml'></element>
3. <div class="container">
4. <comp>
5. <text class="text-style">父组件中定义的内容</text>
6. </comp>
7. </div>
```

## 具名插槽

PhonePC/2in1TabletTVWearable

当自定义组件中需要使用多个插槽时，可通过对插槽命名的方式进行区分，当填充插槽内容时，通过声明插槽名称，将内容加到对应的插槽中。

```
1. <!-- comp.hml -->
2. <div class="item">
3. <text class="text-style">下面使用父组件定义的内容</text>
4. <slot name="first"></slot>
5. <slot name="second"></slot>
6. </div>
```

引用该自定义组件方式如下：

```
1. <!-- xxx.hml -->
2. <element name='comp' src='../common/component/comp.hml'></element>
3. <div class="container">
4. <comp>
5. <text class="text-style" slot="second">插入第二个插槽中</text>
6. <text class="text-style" slot="first">插入第一个插槽中</text>
7. </comp>
8. </div>
```

说明

name 和 slot 属性不支持绑定动态数据。
