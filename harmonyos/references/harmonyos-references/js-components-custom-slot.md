---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-custom-slot
title: slot插槽
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 自定义组件 > slot插槽
category: harmonyos-references
scraped_at: 2026-09-02T15:01:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f51dbd3074037c1c7a7c68e1adfda4b386bf278cf7ae6f4c2c903ac8a1d838f1
---

**说明** 

从API version 7 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 默认插槽

自定义组件中通过slot标签来承载父组件中定义的内容，使用slot标签可以更加灵活地控制自定义组件的内容元素，使用方式如下：

```html
<!-- comp.hml -->
<div class="item">  
   <text class="text-style">下面使用父组件定义的内容</text> 
   <slot></slot> 
</div>
```

引用该自定义组件方式如下：

```html
<!-- xxx.hml --> 
 <element name='comp' src='../common/component/comp.hml'></element>  
 <div class="container">  
   <comp>
     <text class="text-style">父组件中定义的内容</text> 
   </comp>  
 </div>
```

## 具名插槽

当自定义组件中需要使用多个插槽时，可通过对插槽命名的方式进行区分，当填充插槽内容时，通过声明插槽名称，将内容加到对应的插槽中。

```html
<!-- comp.hml -->
<div class="item">  
   <text class="text-style">下面使用父组件定义的内容</text> 
   <slot name="first"></slot>
   <slot name="second"></slot> 
</div>
```

引用该自定义组件方式如下：

```html
<!-- xxx.hml --> 
 <element name='comp' src='../common/component/comp.hml'></element>  
 <div class="container">  
   <comp>
     <text class="text-style" slot="second">插入第二个插槽中</text> 
     <text class="text-style" slot="first">插入第一个插槽中</text>
   </comp>  
 </div>
```

**说明** 

name 和 slot 属性不支持绑定动态数据。
