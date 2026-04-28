---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-mutablebuilder
title: mutableBuilder：实现全局@Builder动态更新
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 组件扩展 > mutableBuilder：实现全局@Builder动态更新
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:58+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:eccb6177e21508fa33a6779e5ff19127ea32ec220efb60435c1f9c204b11c0ba
---

当在一个自定义组件内使用多个全局[@Builder](arkts-builder.md)函数实现UI的不同效果时，代码维护将变得非常困难，且页面不够整洁。此时，可以使用[wrapBuilder](arkts-wrapbuilder.md)封装全局@Builder。但是wrapBuilder不支持动态切换@Builder，引入[mutableBuilder](../harmonyos-references/ts-universal-mutablebuilder.md)实现全局@Builder的动态切换。

说明

从API version 22开始，开发者可以使用mutableBuilder实现全局@Builder的动态切换。

从API version 22开始，mutableBuilder支持在元服务中使用。

## wrapBuilder不支持动态全局@Builder

当前wrapBuilder不支持二次赋值， 更改@Builder，UI不会发生变化。

```
1. class TextContent {
2. text: string = '';
3. }

5. @Builder
6. function textBuilder(p: TextContent) {
7. Text(p.text)
8. }

10. @Builder
11. function buttonBuilder(p: TextContent) {
12. Button(p.text)
13. }

15. @Entry
16. @Component
17. struct Index {
18. @State message: string = 'init';
19. @State text: WrappedBuilder<[TextContent]> = wrapBuilder(textBuilder); // 使用textBuilder初始化

21. build() {
22. Column() {
23. this.text.builder({ text: this.message })
24. Button().onClick(() => {
25. this.text = wrapBuilder(buttonBuilder); // 点击Button，将textBuilder替换为buttonBuilder进行二次赋值
26. })
27. }
28. }
29. }
```

在上述代码中，使用textBuilder初始化wrapBuilder，点击Button的onClick事件，使用buttonBuilder再次初始化wrapBuilder，不会触发对应的@Builder的更新。

为了解决这一问题，引入mutableBuilder作为动态全局@Builder封装函数。mutableBuilder返回MutableBuilder对象，用于[全局@Builder](arkts-builder.md#全局自定义构建函数)的动态刷新。

## 接口说明

mutableBuilder是一个模板函数，返回一个[MutableBuilder](../harmonyos-references/ts-universal-mutablebuilder.md#mutablebuilder-2)对象。相比[WrappedBuilder](../harmonyos-references/ts-universal-wrapbuilder.md#wrappedbuilder)，MutableBuilder可以实现动态切换全局@Builder。

```
1. declare function mutableBuilder<Args extends Object[]>(builder: BuilderCallback): MutableBuilder<Args>;
```

同时MutableBuilder对象是一个模板类，继承自[WrappedBuilder](arkts-wrapbuilder.md#接口说明)。

```
1. declare class MutableBuilder<Args extends Object[]> extends WrappedBuilder<Args> {
2. }
```

说明

模板参数Args extends Object[]需要匹配@Builder函数参数的类型。

使用方法：

```
1. let builderVar: MutableBuilder<[string, number]> = mutableBuilder(MyBuilder);
2. let builderArr: MutableBuilder<[string, number]>[] = [mutableBuilder(MyBuilder)]; // mutableBuilder支持放入数组中
```

## 限制条件

1. mutableBuilder方法只能传入[全局@Builder](arkts-builder.md#全局自定义构建函数)方法，传入局部@Builder方法编译时报错。

   ```
   1. class TextContent {
   2. text: string = '';
   3. }

   5. @Builder
   6. function globalBuilder(p: TextContent) {
   7. Text(p.text)
   8. }

   10. @ComponentV2
   11. struct MyApp {
   12. @Local message: string = 'init';
   13. // 正确用法，使用全局@Builder
   14. @Local switchingBuilder: MutableBuilder<[TextContent]> = mutableBuilder(globalBuilder);
   15. // 错误用法，使用局部@Builder，编译报错
   16. @Local localBuilderObject: MutableBuilder<[TextContent]> = mutableBuilder(this.localBuilder);

   18. @Builder
   19. localBuilder(p: TextContent) {
   20. Text(p.text)
   21. }
   22. build() {
   23. Column() {
   24. this.switchingBuilder.builder({ text: this.message })
   25. }
   26. }
   27. }
   ```
2. MutableBuilder对象的builder属性方法仅限在自定义组件内部使用，在自定义组件外面使用会导致程序运行时崩溃。

   ```
   1. class TextContent {
   2. text: string = '';
   3. }

   5. @Builder
   6. function globalBuilder(p: TextContent) {
   7. Text(p.text)
   8. }

   10. // 错误用法，MutableBuilder对象的builder属性方法在自定义组件外面使用，运行时崩溃
   11. let outSideBuilder: MutableBuilder<[TextContent]> = mutableBuilder(globalBuilder);
   12. outSideBuilder.builder({ text: 'message' });

   14. @ComponentV2
   15. struct MyApp {
   16. @Local message: string = 'init';
   17. @Local switchingBuilder: MutableBuilder<[TextContent]> = mutableBuilder(globalBuilder);
   18. build() {
   19. Column() {
   20. // 正确用法，MutableBuilder对象的builder属性方法在自定义组件中使用
   21. this.switchingBuilder.builder({ text: this.message })
   22. }
   23. }
   24. }
   ```
3. 不建议与wrapBuilder混合使用，因为mutableBuilder创建的对象类型是MutableBuilder类型，会导致不符合预期的更新。

   如下为不推荐的用法：

   ```
   1. // 在实例化MutableBuilder对象时，建议使用mutableBuilder(builderName)方法
   2. @State switchingBuilder: MutableBuilder<[MutableBinding]> = mutableBuilder(textBuilder);
   3. // 不支持将MutableBuilder类型的变量赋值为undefined或null，会导致运行时crash
   4. @State switchingBuilder: MutableBuilder<[MutableBinding]> | undefined | null = null;
   5. Button(`MutableBuilder`).onClick(() => {
   6. // 不建议将wrapBuilder创建的对象赋值给MutableBuilder类型的对象，赋值后会将textBuilder动态切换成buttonBuilder
   7. this.switchingBuilder = wrapBuilder(buttonBuilder);
   8. })
   ```

   如下为推荐用法：

   ```
   1. // 在实例化MutableBuilder对象时，建议使用mutableBuilder(builderName)方法
   2. @State switchingBuilder: MutableBuilder<[MutableBinding]> = mutableBuilder(textBuilder);

   4. Button(`MutableBuilder`).onClick(() => {
   5. // 赋值会将wrapBuilder中textBuilder中动态切换成buttonBuilder
   6. this.switchingBuilder = mutableBuilder(buttonBuilder); // 推荐用法
   7. })
   ```

## 动态更改全局@Builder实例

使用@Builder装饰器装饰的方法textBuilder作为mutableBuilder的参数，然后将mutableBuilder的返回值赋值给变量switchingBuilder，在Button的点击事件中，使用@Builder装饰器装饰的方法buttonBuilder作为mutableBuilder的参数，将mutableBuilder的返回值再次赋值给变量switchingBuilder，可实现textBuilder 更新为buttonBuilder，以解决wrapBuilder不支持二次赋值的问题。

```
1. class TextContent {
2. text: string = '';
3. }

5. @Builder
6. function textBuilder(p: TextContent) {
7. Text(p.text).margin(20)
8. }

10. @Builder
11. function buttonBuilder(p: TextContent) {
12. Button(p.text).margin(20)
13. }

15. let counter: number = 1;
16. @Entry
17. @ComponentV2
18. struct MyApp {
19. @Local message: string = 'init';
20. @Local switchingBuilder: MutableBuilder<[TextContent]> = mutableBuilder(textBuilder);
21. build() {
22. Column() {
23. this.switchingBuilder.builder({ text: this.message })
24. Button('Click to change')
25. .onClick(() => {
26. counter++; // 每次点击按钮修改counter来动态改变全局@Builder
27. if(counter % 2 === 0) {
28. this.message += 'B';
29. this.switchingBuilder = mutableBuilder(buttonBuilder); // textBuilder--->buttonBuilder
30. } else {
31. this.message += 'T';
32. this.switchingBuilder = mutableBuilder(textBuilder); // buttonBuilder--->textBuilder
33. }
34. })
35. }.position({x: 120, y: 60})
36. }
37. }
```

点击Button，可将textBuilder动态更改为buttonBuilder，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/9W6NvrJHTqSQq299YvxN2w/zh-cn_image_0000002583437627.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233856Z&HW-CC-Expire=86400&HW-CC-Sign=61EF283409F2952CC879391FB6F0DB268B8F7EA611E9DDA1B87D271E8D1AEBEF)

## 使用mutableBuilder显示弹出菜单

由于MutableBuilder继承自WrappedBuilder，故mutableBuilder对应的@Builder具有跟WrappedBuilder同等能力，如下示例，mutableBuilder对应的@Builder方法可作为bindMenu入参，支持点击弹出菜单。

```
1. @Builder
2. function overBuilder() {
3. Row() {
4. Text('全局 Builder')
5. .fontSize(30)
6. .fontWeight(FontWeight.Bold)
7. }
8. }

10. @Entry
11. @Component
12. struct Index {
13. @State arr: number[] = [1,2,3,4,5];

15. mutableBuilderMenu: MutableBuilder<[]> = mutableBuilder<[]>(overBuilder);
16. build() {
17. Column() {
18. List({ space: 10 }) {
19. ForEach(this.arr, (item: number) => {
20. ListItem() {
21. Text(`${item}`)
22. .width('100%')
23. .height(100)
24. .fontSize(16)
25. .textAlign(TextAlign.Center)
26. .borderRadius(10)
27. .backgroundColor(0xFFFFFF)
28. }
29. .bindMenu(this.mutableBuilderMenu.builder)
30. }, (item: number) => JSON.stringify(item))
31. }
32. }
33. }
34. }
```

## 观察mutableBuilder中@Builder的变化

mutableBuilder对应的@Builder函数中可使用[MutableBinding](../harmonyos-references/js-apis-statemanagement.md#mutablebindingt20)进行包裹来观察状态变量的变化，同时可通过[@Monitor](arkts-new-monitor.md)或[addMonitor](arkts-new-addmonitor-clearmonitor.md)监听mutableBuilder中@Builder的变化。

```
1. import { UIUtils, MutableBinding } from '@kit.ArkUI';

3. @Builder
4. function textBuilder(p: MutableBinding<string>) {
5. Text(p.value)
6. .margin(20)
7. .onClick(() => {
8. p.value += 't';
9. })
10. }

12. @Builder
13. function buttonBuilder(p: MutableBinding<string>) {
14. Button(p.value)
15. .margin(20)
16. .onClick(() => {
17. p.value += 'b';
18. })
19. }

21. let counter: number = 1;

23. @Entry
24. @ComponentV2
25. struct MyApp {
26. @Local message: string = 'init';
27. @Local switchingBuilder: MutableBuilder<[MutableBinding<string>]> = mutableBuilder(textBuilder);

29. @Monitor('switchingBuilder') variableChange(m: IMonitor): void {
30. console.info(`Builder changed. is buttonBuilder: ${m.value<MutableBuilder<[MutableBinding<string>]>>()?.now.builder === buttonBuilder}`);
31. }

33. build() {
34. Column() {
35. this.switchingBuilder.builder(UIUtils.makeBinding(()=> this.message, txt => this.message = txt))
36. Button('Click to change')
37. .onClick(() => {
38. counter++;
39. if(counter % 2 === 0) {
40. this.message += 'B';
41. this.switchingBuilder = mutableBuilder(buttonBuilder); // textBuilder--->buttonBuilder，@Monitor会触发回调
42. } else {
43. this.message += 'T';
44. this.switchingBuilder = mutableBuilder(textBuilder); // buttonBuilder--->textBuilder，@Monitor会触发回调
45. }
46. })
47. }.position({x: 120, y: 60})
48. }
49. }
```

点击Button，可将textBuilder动态切换为buttonBuilder。点击buttonBuilder，this.message会自动加B，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/yes9N6XGSmiUSywX_RwoRw/zh-cn_image_0000002552957582.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233856Z&HW-CC-Expire=86400&HW-CC-Sign=DB37A565BCFFF7FB6AE8124B84D4A7840F92359C188D84806C332F04C5059FB3)

点击Button将textBuilder动态切换为buttonBuilder时，@Monitor会监听到全局@Builder的变化，并打印日志@Builder change. is buttonBuilder: true。
