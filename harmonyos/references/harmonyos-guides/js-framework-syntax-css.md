---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-syntax-css
title: CSS语法参考
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 框架说明 > 语法 > CSS语法参考
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:03157565d99ec2964df002935bc2e2d743a8dabe1e22541a8aa3ce247b1fa734
---

CSS是描述[HML](js-framework-syntax-hml.md)页面结构的样式语言。所有组件均存在系统默认样式，也可在页面CSS样式文件中对组件、页面自定义不同的样式。请参考[通用样式](../harmonyos-references/js-components-common-styles.md)了解兼容JS的类Web开发范式支持的组件样式。

## 尺寸单位

* 逻辑像素px（文档中以<length>表示）：

  + 默认屏幕具有的逻辑宽度为720px（配置见[js标签配置](js-framework-js-tag.md)中的window小节），实际显示时会将页面布局缩放至屏幕实际宽度，如100px在实际宽度为1440物理像素的屏幕上，实际渲染为200物理像素（从720px向1440物理像素，所有尺寸放大2倍）。
  + 额外配置autoDesignWidth为true时（配置见[js标签配置](js-framework-js-tag.md)中的window小节），逻辑像素px将按照屏幕密度进行缩放，如100px在屏幕密度为3的设备上，实际渲染为300物理像素。应用需要适配多种设备时，建议采用此方法。
* 百分比（文档中以<percentage>表示）：表示该组件占父组件尺寸的百分比，如组件的width设置为50%，代表其宽度为父组件的50%。

## 样式导入

为了模块化管理和代码复用，CSS样式文件支持 @import 语句，导入css文件。

## 声明样式

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
2. 文件导入，合并外部样式文件。例如，在common目录中定义样式文件style.css，并在index.css文件首行中进行导入：

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

css选择器用于选择需要添加样式的元素，支持的选择器如下表所示：

| 选择器 | 样例 | 样例描述 |
| --- | --- | --- |
| .class | .container | 用于选择class="container"的组件。 |
| #id | #titleId | 用于选择id="titleId"的组件。 |
| tag | text | 用于选择text组件。 |
| , | .title, .content | 用于选择class="title"和class="content"的组件。 |
| #id .class tag | #containerId .content text | 非严格父子关系的后代选择器，选择具有id="containerId"作为祖先元素，class="content"作为次级祖先元素的所有text组件。如需使用严格的父子关系，可以使用“>”代替空格，如：#containerId>.content。 |

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
2. .container {
3. width: 100%;
4. height: 100%;
5. justify-content: center;
6. align-items: center;
7. }
8. /* 对所有div组件设置样式 */
9. div {
10. flex-direction: column;
11. }
12. /* 对class="title"的组件设置样式 */
13. .title {
14. font-size: 30px;
15. }
16. /* 对id="contentId"的组件设置样式 */
17. #contentId {
18. font-size: 20px;
19. }
20. /* 对所有class="title"以及class="content"的组件都设置padding为5px */
21. .title, .content {
22. padding: 5px;
23. }
24. /* 对class="container"的组件下的所有text设置样式 */
25. .container text {
26. color: #007dff;
27. }
28. /* 对class="container"的组件下的直接后代text设置样式 */
29. .container > text {
30. color: #fa2a2d;
31. }
```

以上样式运行效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/cuQUeH-NSn2GwqurH5-Yug/zh-cn_image_0000002589244377.png?HW-CC-KV=V1&HW-CC-Date=20260429T052840Z&HW-CC-Expire=86400&HW-CC-Sign=44839D2CDC7FFE70B8221BEE85D4376955F59F89489F0725ABFC51151DDF0FC2)

其中“.container text”将“标题”和“内容”设置为蓝色，而“.container > text”直接后代选择器将“标题”设置为红色。2者优先级相同，但直接后代选择器声明顺序靠后，将前者样式覆盖（优先级计算见[选择器优先级](js-framework-syntax-css.md#选择器优先级)）。

## 选择器优先级

选择器的优先级计算规则与w3c规则保持一致（只支持：内联样式，id，class，tag，后代和直接后代），其中内联样式为在元素style属性中声明的样式。

当多条选择器声明匹配到同一元素时，各类选择器优先级由高到低顺序为：内联样式 > id > class > tag。

## 伪类

css伪类是选择器中的关键字，用于指定要选择元素的特殊状态。例如，:disabled状态可以用来设置元素的disabled属性变为true时的样式。

除了单个伪类之外，还支持伪类的组合，例如，:focus:checked状态可以用来设置元素的focus属性和checked属性同时为true时的样式。支持的单个伪类如下表所示，按照优先级降序排列：

| 名称 | 支持组件 | 描述 |
| --- | --- | --- |
| :disabled | 支持disabled属性的组件 | 表示disabled属性变为true时的元素（不支持动画样式的设置）。 |
| :active | 支持click事件的组件 | 表示被用户激活的元素，如：被用户按下的按钮、被激活的tab-bar页签（不支持动画样式的设置）。 |
| :waiting | button | 表示waiting属性为true的元素（不支持动画样式的设置）。 |
| :checked | input[type="checkbox"、type="radio"]、 switch | 表示checked属性为true的元素（不支持动画样式的设置）。 |

伪类示例如下，设置按钮的:active伪类可以控制被用户按下时的样式：

```
1. <!-- index.hml -->
2. <div class="container">
3. <input type="button" class="button" value="Button"></input>
4. </div>
```

```
1. /* index.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. justify-content: center;
6. align-items: center;
7. }

9. .button:active {
10. background-color: #888888;/*按钮被激活时，背景颜色变为#888888 */
11. }
```

说明

针对弹窗类组件及其子元素不支持伪类效果，包括popup、dialog、menu、option、picker。

## 样式预编译

预编译提供了利用特有语法生成css的程序，可以提供变量、运算等功能，令开发者更便捷地定义组件样式，目前支持less、sass和scss的预编译。使用样式预编译时，需要将原css文件后缀改为less、sass或scss，如index.css改为index.less、index.sass或index.scss。

* 当前文件使用样式预编译，例如将原index.css改为index.less：

  ```
  1. /* index.less */
  2. /* 定义变量 */
  3. @colorBackground: #000000;
  4. .container {
  5. background-color: @colorBackground; /* 使用当前less文件中定义的变量 */
  6. }
  ```
* 引用预编译文件，例如common中存在style.scss文件，将原index.css改为index.scss，并引入style.scss：

  ```
  1. /* style.scss */
  2. /* 定义变量 */
  3. $colorBackground: #000000;
  ```

  在index.scss中引用：

  ```
  1. /* index.scss */
  2. /* 引入外部scss文件 */
  3. @import '../../common/style.scss';
  4. .container {
  5. background-color: $colorBackground; /* 使用style.scss中定义的变量 */
  6. }
  ```

  说明

  引用的预编译文件建议放在common目录进行管理。

## CSS样式继承6+

css样式继承提供了子节点继承父节点样式的能力，继承下来的样式在多选择器样式匹配的场景下，优先级排最低，当前支持以下样式的继承：

* font-family
* font-weight
* font-size
* font-style
* text-align
* line-height
* letter-spacing
* color
* visibility
