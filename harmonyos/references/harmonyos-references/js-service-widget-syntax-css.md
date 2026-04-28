---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-syntax-css
title: CSS语法参考
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 框架说明 > 语法 > CSS语法参考
category: harmonyos-references
scraped_at: 2026-04-28T08:03:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8db71c66e2e489dd3f50f47adc04912c34c0354b94fe6cd64001ffe6e19f1e56
---

CSS是描述HML页面结构的样式语言。所有组件均存在系统默认样式，也可在页面CSS样式文件中对组件、页面自定义不同的样式。

## 尺寸单位

PhonePC/2in1TabletTVWearable

1. 逻辑像素px（文档中以<length>表示）：

   1. 默认卡片具有的逻辑宽度为150px，实际显示时会将页面布局缩放至屏幕实际宽度，如100px在宽度为300的卡片上，实际渲染为200物理像素（从150px向300物理像素，所有尺寸放大2倍）。
   2. 额外配置autoDesignWidth为true时，逻辑像素px将按照屏幕密度进行缩放，如100px在屏幕密度为3的设备上，实际渲染为300物理像素。应用需要适配多种设备时，建议采用此方法。
2. 百分比（文档中以<percentage>表示）：表示该组件占父组件尺寸的百分比，如组件的width设置为50%，代表其宽度为父组件的50%。

## 样式导入

PhonePC/2in1TabletTVWearable

为了模块化管理和代码复用，CSS样式文件支持 @import 语句，导入 CSS 文件。

## 声明样式

PhonePC/2in1TabletTVWearable

每个页面目录下存在一个与布局hml文件同名的css文件，用来描述该hml页面中组件的样式，决定组件应该如何显示。

1. 内部样式，支持使用style、class属性来控制组件的样式。例如：

   ```
   1. <!-- index.hml -->
   2. <div class="container">
   3. <text style="color: red">Hello World</text>
   4. </div>
   ```

   ```
   1. /* index.css */
   2. .container {
   3. justify-content: center;
   4. }
   ```
2. 文件导入，合并外部样式文件。例如，在common目录中定义样式文件style.css，并在index.css中进行导入：

   ```
   1. /* style.css */
   2. .title {
   3. font-size: 50px;
   4. }
   ```

   ```
   1. /* index.css */
   2. @import '../../common/style.css';
   3. .container {
   4. justify-content: center;
   5. }
   ```

## 选择器

PhonePC/2in1TabletTVWearable

css选择器用于选择需要添加样式的元素，支持的选择器如下表所示：

| 选择器 | 样例 | 样例描述 |
| --- | --- | --- |
| .class | .container | 用于选择class="container"的组件。 |
| #id | #titleId | 用于选择id="titleId"的组件。 |

示例：

```
1. <!-- 页面布局xxx.hml -->
2. <div id="containerId" class="container">
3. <text id="titleId" class="title">标题</text>
4. <div class="content">
5. <text id="contentId">内容</text>
6. </div>
7. </div>
```

```
1. /* 页面样式xxx.css */
2. /* 对class="title"的组件设置样式 */
3. .title {
4. font-size: 30px;
5. }
6. /* 对id="contentId"的组件设置样式 */
7. #contentId {
8. font-size: 20px;
9. }
```

## 选择器优先级

PhonePC/2in1TabletTVWearable

选择器的优先级计算规则与w3c规则保持一致（只支持：内联样式，id，class），其中内联样式为在元素style属性中声明的样式。

当多条选择器声明匹配到同一元素时，各类选择器优先级由高到低顺序为：内联样式 > id > class 。
