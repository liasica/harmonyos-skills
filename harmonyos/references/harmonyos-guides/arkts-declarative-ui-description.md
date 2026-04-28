---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-declarative-ui-description
title: 声明式UI描述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 声明式UI描述
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2129414b06cdad455fffde6797ebd327431b3dafb551fd725b9877b09e31c056
---

ArkTS以声明方式组合和扩展组件来描述应用程序的UI，同时还提供了基本的属性、事件和子组件配置方法，帮助开发者实现应用交互逻辑。

## 创建组件

根据组件构造方法的不同，创建组件包含有参数和无参数两种方式。

说明

创建组件不需要使用new关键字。

### 无参数

如果组件接口定义中不包含必选构造参数，则组件后面的“()”不需要配置任何内容。例如：Divider组件不包含构造参数。

```
1. Column() {
2. // ...
3. Divider()
4. // ...
5. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DeclarativeUIDescription/entry/src/main/ets/pages/Index.ets#L48-L55)

### 有参数

如果组件接口定义包含构造参数，则在组件后的“()”中配置相应参数。

* Image组件的必选参数src。

  ```
  1. Image('https://xyz/test.jpg')
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DeclarativeUIDescription/entry/src/main/ets/pages/Index.ets#L57-L59)
* Text组件的非必选参数content。

  ```
  1. // string类型的参数
  2. Text('test')
  3. // $r形式引入应用资源，可应用于多语言场景
  4. Text($r('app.string.title_value'))
  5. // 无参数形式
  6. Text()
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DeclarativeUIDescription/entry/src/main/ets/pages/Index.ets#L61-L68)
* 变量或表达式可以用于参数赋值，表达式结果类型必须符合参数要求。

  例如，设置变量或表达式来构造Image和Text组件的参数。

  ```
  1. Image(this.imagePath)
  2. // 此处需要替换为开发者所需的正确url
  3. Image('https://' + this.imageUrl)
  4. Text(`count: ${this.count}`)
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DeclarativeUIDescription/entry/src/main/ets/pages/Index.ets#L70-L75)

## 配置属性

属性方法以“.”链式调用配置组件样式和其他属性，建议每个属性方法单独一行。

* 配置Text组件的字体大小。

  ```
  1. Text('test')
  2. .fontSize(12)
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DeclarativeUIDescription/entry/src/main/ets/pages/Index.ets#L77-L80)
* 配置组件的多个属性。

  ```
  1. Image('test.jpg')
  2. .alt('error.jpg')
  3. .width(100)
  4. .height(100)
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DeclarativeUIDescription/entry/src/main/ets/pages/Index.ets#L82-L87)
* 除了直接传递常量参数，还可以传递变量或表达式。

  ```
  1. Text('hello')
  2. .fontSize(this.fontSize)
  3. Image('test.jpg')
  4. .width(this.count % 2 === 0 ? 100 : 200)
  5. .height(this.offsetNum + 100)
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DeclarativeUIDescription/entry/src/main/ets/pages/Index.ets#L89-L95)
* 对于系统组件，ArkUI还为其属性预定义了一些枚举类型供开发者调用，枚举类型可以作为参数传递，但必须满足参数类型要求。

  例如，可以按以下方式配置Text组件的颜色和字体样式。

  ```
  1. Text('hello')
  2. .fontSize(20)
  3. .fontColor(Color.Red)
  4. .fontWeight(FontWeight.Bold)
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DeclarativeUIDescription/entry/src/main/ets/pages/Index.ets#L97-L102)

## 配置事件

事件方法以“.”链式调用的方式配置系统组件支持的事件，建议每个事件方法单独写一行。

* 使用箭头函数配置组件的事件方法。

  ```
  1. Button('Click me')
  2. .onClick(() => {
  3. this.myText = 'ArkUI';
  4. })
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DeclarativeUIDescription/entry/src/main/ets/pages/Index.ets#L104-L109)
* 使用箭头函数表达式配置组件的事件方法，要求使用“() => {...}”，以确保函数与组件绑定，同时符合ArkTS语法规范。

  ```
  1. Button('add counter')
  2. .onClick(() => {
  3. this.counter += 2;
  4. })
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DeclarativeUIDescription/entry/src/main/ets/pages/Index.ets#L111-L116)
* 使用组件的成员函数配置组件的事件方法，需要bind this。ArkTS语法不建议使用成员函数配合bind this来配置组件的事件方法。

  ```
  1. myClickHandler(): void {
  2. this.counter += 2;
  3. }

  5. // ···
  6. Button('add counter')
  7. .onClick(this.myClickHandler.bind(this))
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DeclarativeUIDescription/entry/src/main/ets/pages/Index.ets#L30-L121)
* 使用声明的箭头函数时可以直接调用，不需要bind this。

  ```
  1. fn = () => {
  2. hilog.info(0x0000, 'Declarative UI Description', `counter: ${this.counter}`);
  3. this.counter++;
  4. };

  6. // ···
  7. Button('add counter')
  8. .onClick(this.fn)
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DeclarativeUIDescription/entry/src/main/ets/pages/Index.ets#L37-L126)

说明

箭头函数内部的this是词法作用域，由上下文确定。匿名函数可能会出现this指向不明确的问题，因此在ArkTS中不允许使用。

## 配置子组件

如果组件支持子组件配置，则需在尾随闭包"{...}"中为组件添加子组件的UI描述。Column、Row、Stack、Grid、List等组件都是容器组件。

* 以下是简单的Column组件配置子组件的示例。

  ```
  1. Column() {
  2. Text('Hello')
  3. .fontSize(100)
  4. Divider()
  5. Text(this.myText)
  6. .fontSize(100)
  7. .fontColor(Color.Red)
  8. }
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DeclarativeUIDescription/entry/src/main/ets/pages/Index.ets#L128-L138)
* 容器组件均支持子组件配置，可以实现相对复杂的多级嵌套。

  ```
  1. Column() {
  2. Row() {
  3. Image('test1.jpg')
  4. .width(100)
  5. .height(100)
  6. Button('click +1')
  7. .onClick(() => {
  8. hilog.info(0x0000, 'Declarative UI Description', '+1 clicked!');
  9. })
  10. }
  11. }
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DeclarativeUIDescription/entry/src/main/ets/pages/Index.ets#L140-L153)
