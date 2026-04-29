---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-ui-component-encapsulation
title: 组件封装
breadcrumb: 最佳实践 > 组件封装与复用 > 组件封装
category: best-practices
scraped_at: 2026-04-29T14:10:18+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:3925efc22ae22bcba6a10da1a3173d1ef52d652aeabe1e1d98dfdc8806a2f1d5
---

## 概述

在ArkUI应用开发中，常常需要对UI组件或样式进行封装。封装是为了复用相同或相似的代码功能，提高开发效率，同时也便于工程维护和团队协作。

通常组件封装包含以下典型场景：

* [组件公共样式封装](bpta-ui-component-encapsulation.md#section16593152733118)
* [自定义组件封装](bpta-ui-component-encapsulation.md#section299514487282)
* [组件工厂类封装](bpta-ui-component-encapsulation.md#section178216212105)

## 组件公共样式封装

### 场景描述

在开发不同的业务功能时，可能需要使用相同样式的组件。例如，登录页面的登录按钮与购物页面的结算按钮，二者在同一应用中且表示确认操作，可能会采用相同的UI样式。这时可以抽取按钮Button组件的公共样式，封装后实现全局复用。下图是一个在默认态、按压态两种不同情况下的Button按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/d3wLmaQERKmqPkZrcV7lnA/zh-cn_image_0000002362705992.png?HW-CC-KV=V1&HW-CC-Date=20260429T061017Z&HW-CC-Expire=86400&HW-CC-Sign=C8ED4B1C19B4F8FFABC3A1815CC81ED5D8890C22A655945877BC83DD26AB48B9)

### 实现原理

组件的公共样式通过设置组件的属性实现，ArkUI可以使用[AttributeModifier属性修改器](../harmonyos-guides/arkts-user-defined-extension-attributemodifier.md)，将属性封装在同一个AttributeModifier实现类中，在需要复用样式的组件中应用AttributeModifier实例对象。

### 开发步骤

1. 提供方定义AttributeModifier接口的实现类，封装公共样式属性。

   ```
   1. // The provider creates a custom Class that implements the system's AttributeModifier interface.
   2. export class MyButtonModifier implements AttributeModifier<ButtonAttribute> {
   3. private buttonType: ButtonType = ButtonType.Normal;

   5. constructor() {
   6. }

   8. applyNormalAttribute(instance: ButtonAttribute): void {
   9. instance.type(this.buttonType);
   10. instance.width(200);
   11. instance.height(50);
   12. instance.fontSize(20);
   13. instance.fontColor('#0A59F7')
   14. instance.backgroundColor('#0D000000')
   15. }

   17. applyPressedAttribute(instance: ButtonAttribute): void {
   18. instance.fontColor('#0A59F7')
   19. instance.backgroundColor('#26000000')
   20. }

   22. type(type: ButtonType): MyButtonModifier {
   23. this.buttonType = type;
   24. return this;
   25. }
   26. }
   ```

   [AttributeStylePage.ets](https://gitcode.com/harmonyos_samples/ComponentEncapsulation/blob/master/entry/src/main/ets/pages/AttributeStylePage.ets#L18-L43)
2. 使用方创建AttributeModifier实例，将其作为参数传入到系统组件的attributeModifier()方法中，封装的样式会应用到该组件上。

   ```
   1. @Entry
   2. @Component
   3. struct AttributeStylePage {
   4. modifier = new MyButtonModifier()
   5. .type(ButtonType.Capsule)

   7. build() {
   8. NavDestination() {
   9. Column() {
   10. Button('Capsule Button')
   11. .attributeModifier(this.modifier)
   12. }
   13. .margin({ top: $r('app.float.margin_top') })
   14. .justifyContent(FlexAlign.Start)
   15. .alignItems(HorizontalAlign.Center)
   16. .width('100%')
   17. .height('100%')
   18. }
   19. .title(getResourceString($r('app.string.common_style_extract'), this))
   20. }
   21. }
   ```

   [AttributeStylePage.ets](https://gitcode.com/harmonyos_samples/ComponentEncapsulation/blob/master/entry/src/main/ets/pages/AttributeStylePage.ets#L52-L72)

   说明

   AttributeModifier应用在系统组件上，暂不支持修改自定义组件的属性。

   AttributeModifier实例可以跨文件导出复用，支持多态样式下的属性/事件修改。

   更多参考[AttributeModifier使用说明](../harmonyos-guides/arkts-user-defined-extension-attributemodifier.md#使用说明)。

## 自定义组件封装

### 场景描述

应用开发中，除了UI样式，布局、逻辑等也可能需要复用，这时可以考虑将相同功能或样式的UI内容封装成一个自定义组件。例如，下图是一个包含图片文字的自定义组件，由Image组件和Text组件纵向排列实现，其中Image和Text的样式可由使用方修改。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/erQmamhDR9GkMccjAFDUiA/zh-cn_image_0000002396385773.png?HW-CC-KV=V1&HW-CC-Date=20260429T061017Z&HW-CC-Expire=86400&HW-CC-Sign=2F2CD31FEDCC80E1265960E53158FD83DEB98B7115BB938BBCCC0571A3EE7E68 "点击放大")

### 实现原理

使用@Component封装[自定义组件](../harmonyos-guides/arkts-create-custom-components.md)，将不变的部分实现在组件内部，将可能发生变化的部分，使用参数变量暴露出去。

当前场景下，添加变量设置子组件的attributeModifier()方法，外部使用方通过参数传入AttributeModifier实例，从而实现内部子组件的样式修改。

### 开发步骤

1. 提供方封装默认属性样式：分别实现Image组件和Text组件的AttributeModifier接口实现类，提供方法设置可能发生变化的属性，例如width、height等。

   ```
   1. // The AttributeModifier interface implementation class for the Image component.
   2. export class CustomImageModifier implements AttributeModifier<ImageAttribute> {
   3. private imageWidth: Length = 0;
   4. private imageHeight: Length = 0;

   6. constructor(width: Length, height: Length) {
   7. this.imageWidth = width;
   8. this.imageHeight = height;
   9. }

   11. width(width: Length) {
   12. this.imageWidth = width;
   13. return this;
   14. }

   16. height(height: Length) {
   17. this.imageHeight = height;
   18. return this;
   19. }

   21. applyNormalAttribute(instance: ImageAttribute): void {
   22. instance.width(this.imageWidth);
   23. instance.height(this.imageHeight);
   24. instance.borderRadius($r('app.float.border_radius'))

   26. }
   27. }

   29. // Text component's AttributeModifier interface implementation class.
   30. export class CustomTextModifier implements AttributeModifier<TextAttribute> {
   31. constructor() {
   32. }

   34. applyNormalAttribute(instance: TextAttribute): void {
   35. instance.fontSize($r('app.float.font_size_l'));
   36. }
   37. }
   ```

   [CustomImageText.ets](https://gitcode.com/harmonyos_samples/ComponentEncapsulation/blob/master/entry/src/main/ets/view/CustomImageText.ets#L18-L54)
2. 提供方封装自定义组件CustomImageText，添加相关变量，使用默认AttributeModifier对象设置Image、Text。

   ```
   1. @Component
   2. export struct CustomImageText {
   3. @Prop imageAttribute: AttributeModifier<ImageAttribute> = new CustomImageModifier(100, 100);
   4. @Prop textAttribute: AttributeModifier<TextAttribute> = new CustomTextModifier();
   5. @Prop imageSrc: PixelMap | ResourceStr | DrawableDescriptor;
   6. @Prop text: string;
   7. onClickEvent?: () => void;

   9. build() {
   10. Column({ space: 12 }) {
   11. Image(this.imageSrc)
   12. .attributeModifier(this.imageAttribute)
   13. Text(this.text)
   14. .attributeModifier(this.textAttribute)
   15. }.onClick(() => {
   16. if (this.onClickEvent !== undefined) {
   17. this.onClickEvent();
   18. }
   19. })
   20. }
   21. }
   ```

   [CustomImageText.ets](https://gitcode.com/harmonyos_samples/ComponentEncapsulation/blob/master/entry/src/main/ets/view/CustomImageText.ets#L58-L78)
3. 使用方在布局中添加自定义组件CustomImageText，可以选择创建Image、Text组件的AttributeModifier实现类实例，传参到CustomImageText组件中修改属性样式。

   ```
   1. @Component
   2. struct CommonComponent {
   3. imageAttribute: CustomImageModifier = new CustomImageModifier(330, 330);

   5. build() {
   6. NavDestination() {
   7. Column() {
   8. CustomImageText({
   9. imageAttribute: this.imageAttribute,
   10. imageSrc: $r('app.media.image'),
   11. text: 'Scenery',
   12. onClickEvent: () => {
   13. this.getUIContext().getPromptAction().showToast({ message: 'Clicked' })
   14. }
   15. })
   16. }
   17. .margin({ top: $r('app.float.margin_top') })
   18. .justifyContent(FlexAlign.Start)
   19. .alignItems(HorizontalAlign.Center)
   20. .width('100%')
   21. .height('100%')
   22. }
   23. .title(getResourceString($r('app.string.common'), this))
   24. }
   25. }
   ```

   [CommonComponent.ets](https://gitcode.com/harmonyos_samples/ComponentEncapsulation/blob/master/entry/src/main/ets/pages/CommonComponent.ets#L26-L50)

## 组件工厂类封装

### 场景描述

如下图所示，团队A实现了一个组件工厂类，其中封装了多个组件。业务团队B在不同的开发场景下，希望通过组件名从工厂类实例中获取对应的组件。例如，当B团队向实例中传入参数"TextInput"或"Radio"，可以分别获取TextInput或Radio组件模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/Sua1J9XQQCunMPqfdp4OlQ/zh-cn_image_0000002362865888.png?HW-CC-KV=V1&HW-CC-Date=20260429T061017Z&HW-CC-Expire=86400&HW-CC-Sign=FB0DBE39659AE4C7AAF4420877B70C2B4B71CF39B090638A56D5C0F2912569EA "点击放大")

### 实现原理

系统提供了[@Builder装饰器](../harmonyos-guides/arkts-builder.md)，其装饰的方法遵循自定义组件build()函数语法规则。将@Builder装饰的方法传入[wrapBuilder](../harmonyos-guides/arkts-wrapbuilder.md)后，会返回[WrappedBuilder](../harmonyos-guides/arkts-wrapbuilder.md)对象，该对象支持赋值和传递。

借助wrapBuilder函数，组件工厂可以使用Map结构存入各种组件，其中key为组件名，value为WrappedBuilder对象，使用时可以通过key值获取相应的组件。

### 开发步骤

1. 在组件工厂实现方，将需要工厂化的组件通过全局@Builder方法封装。

   ```
   1. @Builder
   2. function myRadio() {
   3. Text($r('app.string.radio'))
   4. .width('100%')
   5. .fontColor($r('sys.color.mask_secondary'))
   6. Row() {
   7. Radio({ value: '1', group: 'radioGroup' })
   8. .margin({ right: $r('app.float.margin_right') })
   9. Text('man')
   10. }
   11. .width('100%')

   13. Row() {
   14. Radio({ value: '0', group: 'radioGroup' })
   15. .margin({ right: $r('app.float.margin_right') })
   16. Text('woman')
   17. }
   18. .width('100%')
   19. }

   21. @Builder
   22. function myCheckBox() {
   23. Text($r('app.string.checkbox'))
   24. .width('100%')
   25. .fontColor($r('sys.color.mask_secondary'))
   26. Row() {
   27. CheckboxGroup({ group: 'checkboxGroup' })
   28. .checkboxShape(CheckBoxShape.ROUNDED_SQUARE)
   29. Text('all')
   30. .margin({ left: $r('app.float.margin_right') })
   31. }
   32. .width('100%')

   34. Row() {
   35. Checkbox({ name: '1', group: 'checkboxGroup' })
   36. .shape(CheckBoxShape.ROUNDED_SQUARE)
   37. .margin({ right: $r('app.float.margin_right') })
   38. Text('text1')
   39. }
   40. .width('100%')

   42. Row() {
   43. Checkbox({ name: '0', group: 'checkboxGroup' })
   44. .shape(CheckBoxShape.ROUNDED_SQUARE)
   45. .margin({ right: $r('app.float.margin_right') })
   46. Text('text2')
   47. }
   48. .width('100%')
   49. }
   ```

   [FactoryMap.ets](https://gitcode.com/harmonyos_samples/ComponentEncapsulation/blob/master/entry/src/main/ets/view/FactoryMap.ets#L17-L65)
2. 在组件工厂实现方，将封装好的全局@Builder方法使用wrapBuilder函数包裹，并将返回值作为组件工厂Map的value值存入。全部组件存入后，将组件工厂导出供外部使用。

   ```
   1. // Define the component factory Map.
   2. let factoryMap: Map<string, object> = new Map();

   4. // The components that need to be factory stored in the component factory.
   5. factoryMap.set('Radio', wrapBuilder(myRadio));
   6. factoryMap.set('Checkbox', wrapBuilder(myCheckBox));

   8. // Export assembly factory
   9. export { factoryMap };
   ```

   [FactoryMap.ets](https://gitcode.com/harmonyos_samples/ComponentEncapsulation/blob/master/entry/src/main/ets/view/FactoryMap.ets#L69-L77)
3. 在使用方，引入组件工厂并通过key值获取对应的WrappedBuilder对象。

   ```
   1. // Import the component factory. The path must be based on the actual location.
   2. import { factoryMap } from '../view/FactoryMap';
   3. // ...
   4. // Get the corresponding WrappedBuilder object from the key value of the component factory Map.
   5. let myRadio: WrappedBuilder<[]> = factoryMap.get('Radio') as WrappedBuilder<[]>;
   6. let myCheckbox: WrappedBuilder<[]> = factoryMap.get('Checkbox') as WrappedBuilder<[]>;
   ```

   [ComponentFactory.ets](https://gitcode.com/harmonyos_samples/ComponentEncapsulation/blob/master/entry/src/main/ets/pages/ComponentFactory.ets#L16-L23)
4. 在使用方，build()函数中调用WrappedBuilder对象的builder()方法应用具体组件。

   ```
   1. @Component
   2. struct ComponentFactory {
   3. build() {
   4. NavDestination() {
   5. Column({ space: 12 }) {
   6. // myRadio and myCheckbox are WrappedBuilder objects obtained from the component factory.
   7. myRadio.builder();
   8. myCheckbox.builder();
   9. }
   10. .width('100%')
   11. .padding($r('app.float.padding'))
   12. }
   13. .title(getResourceString($r('app.string.factory'), this))
   14. }
   15. }
   ```

   [ComponentFactory.ets](https://gitcode.com/harmonyos_samples/ComponentEncapsulation/blob/master/entry/src/main/ets/pages/ComponentFactory.ets#L32-L46)

说明

使用wrapBuilder方法有以下限制：

1. wrapBuilder方法只支持传入全局@Builder方法。
2. wrapBuilder方法返回的WrappedBuilder对象的builder属性方法只能在struct内部使用。

## 常见问题

### 如何调用子组件中的方法

主要有以下方法：

* **方法一****：****使用Controller类**
  1. 定义Controller类，添加一个方法变量。
  2. 在子组件中封装具体方法，添加Controller变量，在aboutToAppear()时将方法赋值。
  3. 父组件中创建Controller实例，并传递给子组件。当父组件执行Controller实例中的方法，会间接调用子组件中的方法。

     ```
     1. export class Controller {
     2. action = () => {
     3. };
     4. }

     6. @Component
     7. export struct ChildComponent {
     8. @State bgColor: ResourceColor = Color.White;
     9. controller: Controller | undefined = undefined;
     10. private switchColor = () => {
     11. if (this.bgColor === Color.White) {
     12. this.bgColor = Color.Red;
     13. } else {
     14. this.bgColor = Color.White;
     15. }
     16. }

     18. aboutToAppear(): void {
     19. if (this.controller) {
     20. this.controller.action = this.switchColor;
     21. }
     22. }

     24. build() {
     25. Column() {
     26. Text('Child Component')
     27. }.backgroundColor(this.bgColor).borderWidth(1)
     28. }
     29. }

     31. @Entry
     32. @Component
     33. struct Index {
     34. private childRef = new Controller();

     36. build() {
     37. Column() {
     38. ChildComponent({ controller: this.childRef })

     40. Button('Switch Color')
     41. .onClick(() => {
     42. this.childRef.action();
     43. })
     44. .margin({ top: 16 })
     45. }
     46. .width('100%')
     47. .alignItems(HorizontalAlign.Center)
     48. }
     49. }
     ```

     [ControllerCallPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ComponentEncapsulation/entry/src/main/ets/pages/ControllerCallPage.ets#L16-L65)

* **方法二：****使用@Watch**

  使用[@Watch](../harmonyos-guides/arkts-watch.md)监听状态变量，当父组件修改此变量时，@Watch的回调方法将被执行，即实现了子组件中的方法调用。

  ```
  1. @Component
  2. export struct ChildComponent {
  3. @State bgColor: ResourceColor = Color.White;
  4. @Link @Watch('switchColor') checkFlag: boolean;

  6. private switchColor() {
  7. if (this.checkFlag) {
  8. this.bgColor = Color.Red;
  9. } else {
  10. this.bgColor = Color.White;
  11. }
  12. }

  14. build() {
  15. Column() {
  16. Text('Child Component')
  17. }.backgroundColor(this.bgColor)
  18. .borderWidth(1)
  19. }
  20. }

  22. @Entry
  23. @Component
  24. struct Index {
  25. @State childCheckFlag: boolean = false;

  27. build() {
  28. Column() {
  29. ChildComponent({ checkFlag: this.childCheckFlag })

  31. Button('Switch Color')
  32. .onClick(() => {
  33. this.childCheckFlag = !this.childCheckFlag;
  34. })
  35. .margin({ top: 16 })
  36. }
  37. .width('100%')
  38. .alignItems(HorizontalAlign.Center)
  39. }
  40. }
  ```

  [WatchCallPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ComponentEncapsulation/entry/src/main/ets/pages/WatchCallPage.ets#L16-L56)
* **方法三：使用事件通信**

  使用[Emitter](../harmonyos-guides/itc-with-emitter.md)通信机制，在子组件中添加事件监听，在父组件emit发布对应事件，监听的事件被执行，即实现了子组件中的方法调用。

  ```
  1. @Component
  2. export struct ChildComponent {
  3. public static readonly EVENT_ID_SWITCH_COLOR = 'SWITCH_COLOR';
  4. @State bgColor: ResourceColor = Color.White;
  5. private switchColor = () => {
  6. if (this.bgColor === Color.White) {
  7. this.bgColor = Color.Red;
  8. } else {
  9. this.bgColor = Color.White;
  10. }
  11. }

  13. aboutToAppear(): void {
  14. emitter.on(ChildComponent.EVENT_ID_SWITCH_COLOR, this.switchColor);
  15. }

  17. aboutToDisappear(): void {
  18. emitter.off(ChildComponent.EVENT_ID_SWITCH_COLOR, this.switchColor);
  19. }

  21. build() {
  22. Column() {
  23. Text('Child Component')
  24. }.backgroundColor(this.bgColor)
  25. .borderWidth(1)
  26. }
  27. }

  29. @Entry
  30. @Component
  31. struct Index {
  32. build() {
  33. Column() {
  34. ChildComponent()

  36. Button('Switch Color')
  37. .onClick(() => {
  38. emitter.emit(ChildComponent.EVENT_ID_SWITCH_COLOR);
  39. })
  40. .margin({ top: 16 })
  41. }
  42. .width('100%')
  43. .alignItems(HorizontalAlign.Center)
  44. }
  45. }
  ```

  [EmitterCallPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ComponentEncapsulation/entry/src/main/ets/pages/EmitterCallPage.ets#L18-L63)

### 如何调用父组件中的方法

在子组件中添加一个回调方法，当父组件在使用子组件时，将父组件中的方法做为参数传递进去即可。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Component
5. export struct ChildComponent {
6. call = () => {
7. };

9. build() {
10. Column() {
11. Button('Child Component')
12. .onClick(() => {
13. this.call();
14. })
15. }
16. }
17. }

19. @Entry
20. @Component
21. struct Index {
22. parentAction() {
23. try {
24. this.getUIContext().getPromptAction().showToast({ message: 'Parent Action' });
25. } catch (error) {
26. let err = error as BusinessError;
27. hilog.warn(0x000, 'testTag', `showToast failed, code=${err.code}, message=${err.message}`);
28. }
29. }

31. build() {
32. Column() {
33. ChildComponent({ call: this.parentAction })
34. }
35. .width('100%')
36. .alignItems(HorizontalAlign.Center)
37. }
38. }
```

[ParentCallPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ComponentEncapsulation/entry/src/main/ets/pages/ParentCallPage.ets#L16-L54)

### 如何将UI的可变部分提取出来，实现类似插槽的功能

使用[@BuilderParam参数](../harmonyos-guides/arkts-builderparam.md#参数初始化组件)或[@BuilderParam尾随闭包](../harmonyos-guides/arkts-builderparam.md#尾随闭包初始化组件)的方法，在封装的子组件中，将可变的UI内容做为变量开放出去，当父组件在应用子组件时实现具体的UI内容。

```
1. @Component
2. export struct ChildComponent {
3. @Builder
4. customBuilder() {
5. }

7. @BuilderParam customBuilderParam: () => void = this.customBuilder;

9. build() {
10. Column() {
11. Text('Text in Child')
12. this.customBuilderParam();
13. }
14. }
15. }

17. @Entry
18. @Component
19. struct Index {
20. @Builder
21. componentBuilder() {
22. Text(`Parent builder`)
23. }

25. build() {
26. Column() {
27. ChildComponent() {
28. this.componentBuilder();
29. }
30. }
31. .width('100%')
32. .alignItems(HorizontalAlign.Center)
33. }
34. }
```

[BuilderParamPage.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ComponentEncapsulation/entry/src/main/ets/pages/BuilderParamPage.ets#L16-L50)

### 如何传递UI组件数组，实现ForEach循环渲染

先将UI组件包装成全局@Builder，然后使用[wrapBuilder](../harmonyos-guides/arkts-wrapbuilder.md)依次封装每个@Builder，这样得到的WrappedBuilder对象/数组可以用于参数传递，可以使用ForEach对传递的数组进行渲染。

参考：[builder方法赋值给变量在ui语法中使用](../harmonyos-guides/arkts-wrapbuilder.md#builder方法赋值给变量在ui语法中使用)

## 示例代码

* [实现组件的封装](https://gitcode.com/harmonyos_samples/ComponentEncapsulation)
