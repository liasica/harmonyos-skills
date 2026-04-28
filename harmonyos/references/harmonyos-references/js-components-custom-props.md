---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-custom-props
title: 数据传递与处理
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 自定义组件 > 数据传递与处理
category: harmonyos-references
scraped_at: 2026-04-28T08:03:20+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:77165aeb472b345f30ac0d5dc7177691b28d17c4fc36244338dfc440ef6ed746
---

## Props

PhonePC/2in1TabletTVWearable

自定义组件可以通过props声明属性，父组件通过设置属性向子组件传递参数，props支持类型包括：String，Number，Boolean，Array，Object，Function。camelCase (驼峰命名法) 的 prop 名，在外部父组件传递参数时需要使用 kebab-case (短横线分隔命名) 形式，即当属性compProp在父组件引用时需要转换为comp-prop。给自定义组件添加props，通过父组件向下传递参数的示例如下：

```
1. <!-- comp.hml -->
2. <div class="item">
3. <text class="title-style">{{compProp}}</text>
4. </div>
```

```
1. // comp.js
2. export default {
3. props: ['compProp'],
4. }
```

```
1. <!-- xxx.hml -->
2. <element name='comp' src='../common/component/comp/comp.hml'></element>
3. <div class="container">
4. <comp comp-prop="{{title}}"></comp>
5. </div>
```

说明

自定义属性命名时禁止以on、@、on:、grab: 等保留关键字为开头。

### 添加默认值

PhonePC/2in1TabletTVWearable

子组件可以通过固定值default设置默认值，当父组件没有设置该属性时，将使用其默认值。此情况下props属性必须为对象形式，不能用数组形式，示例如下：

```
1. <!-- comp.hml -->
2. <div class="item">
3. <text class="title-style">{{title}}</text>
4. </div>
```

```
1. // comp.js
2. export default {
3. props: {
4. title: {
5. default: 'title',
6. },
7. },
8. }
```

本示例中加入了一个text组件显示标题，标题的内容是一个自定义属性，显示用户设置的标题内容，当用户没有设置时显示默认值title。在引用该组件时添加该属性的设置：

```
1. <!-- xxx.hml -->
2. <element name='comp' src='../common/component/comp/comp.hml'></element>
3. <div class="container">
4. <comp title="自定义组件"></comp>
5. </div>
```

### 数据单向性

PhonePC/2in1TabletTVWearable

父子组件之间数据的传递是单向的，只能从父组件传递给子组件，子组件不能直接修改父组件传递下来的值，可以将props传入的值用data接收后作为默认值，再对data的值进行修改。

```
1. // comp.js
2. export default {
3. props: ['defaultCount'],
4. data() {
5. return {
6. count: this.defaultCount,
7. };
8. },
9. onClick() {
10. this.count = this.count + 1;
11. },
12. }
```

### $watch感知数据改变

PhonePC/2in1TabletTVWearable

如果需要观察组件中属性变化，可以通过$watch方法增加属性变化回调。使用方法如下：

```
1. // comp.js
2. export default {
3. props: ['title'],
4. onInit() {
5. this.$watch('title', 'onPropertyChange');
6. },
7. onPropertyChange(newV, oldV) {
8. console.info('title 属性变化 ' + newV + ' ' + oldV);
9. },
10. }
```

## computed

PhonePC/2in1TabletTVWearable

自定义组件中经常需要在读取或设置某个属性时进行预先处理，提高开发效率，此种情况就需要使用computed计算属性。computed字段中可通过设置属性的getter和setter方法在属性读写的时候进行触发，使用方式如下：

```
1. // comp.js
2. export default {
3. props: ['title'],
4. data() {
5. return {
6. objTitle: this.title,
7. time: 'Today',
8. };
9. },
10. computed: {
11. message() {
12. return this.time + ' ' + this.objTitle;
13. },
14. notice: {
15. get() {
16. return this.time;
17. },
18. set(newValue) {
19. this.time = newValue;
20. },
21. },
22. },
23. onClick() {
24. console.info('get click event ' + this.message);
25. this.notice = 'Tomorrow';
26. },
27. }
```

这里声明的第一个计算属性message默认只有getter函数，message的值会取决于objTitle的值的变化。getter函数只能读取不能改变参数值，例如data中初始化定义的time，当需要赋值给计算属性的时候可以提供一个setter函数，如示例中的notice。
