---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-syntax-css
title: CSS语法参考
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 框架说明 > 语法 > CSS语法参考
category: harmonyos-references
scraped_at: 2026-04-28T08:03:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:97abf8e22e418aff75ac8f4c9f920c0a4973950296bde4c1813c2634b24a57b0
---

CSS是描述HML页面结构的样式语言。所有组件均存在系统默认样式，也可在页面CSS样式文件中对组件、页面自定义不同的样式。

## 样式导入

PhonePC/2in1TabletTVWearableLite Wearable

为了模块化管理和代码复用，CSS样式文件支持 @import 语句，导入 CSS 文件。

## 声明样式

PhonePC/2in1TabletTVWearableLite Wearable

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

PhonePC/2in1TabletTVWearableLite Wearable

css选择器用于选择需要添加样式的元素，支持的选择器如下表所示：

| 选择器 | 样例 | 样例描述 |
| --- | --- | --- |
| .class | .container | 用于选择class="container"的组件。 |
| #id | #titleId | 用于选择id="titleId"的组件。 |
| , | .title, .content | 用于选择class="title"和class="content"的组件。 |

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
10. /* 对所有class="title"以及class="content"的组件都设置padding为5px */
11. .title, .content {
12. padding: 5px;
13. }
```

## 伪类

PhonePC/2in1TabletTVWearableLite Wearable

css伪类是选择器中的关键字，用于指定要选择元素的特殊状态。

| 名称 | 支持组件 | 描述 |
| --- | --- | --- |
| :active | input[type="button"] | 表示被用户激活的元素，如：被用户按下的按钮。轻量级智能穿戴上伪类选择器上仅支持background-color 和background-image 的样式设置。 |
| :checked | input[type="checkbox"、type="radio"] | 表示checked属性为true的元素。轻量级智能穿戴上伪类选择器上仅支持background-color 和background-image 的样式设置。 |

伪类示例如下，设置按钮的:active伪类可以控制被用户按下时的样式：

```
1. <!-- index.hml -->
2. <div class="container">
3. <input type="button" class="button" value="Button"></input>
4. </div>
```

```
1. /* index.css */
2. .button:active {
3. background-color: #888888;/*按钮被激活时，背景颜色变为#888888 */
4. }
```

## 样式预编译

PhonePC/2in1TabletTVWearableLite Wearable

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
