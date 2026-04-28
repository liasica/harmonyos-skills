---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-custom-basic-usage
title: 自定义组件的基本用法
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 自定义组件 > 自定义组件的基本用法
category: harmonyos-references
scraped_at: 2026-04-28T08:03:21+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:ff92cfc1cbfb9c2b87e21b0a9c146ae38a6abc4568677e1926c51727284ac3db
---

自定义组件是用户根据业务需求，将已有的组件组合，封装成的新组件，可以在工程中多次调用，从而提高代码的可读性。自定义组件通过element引入到宿主页面，使用方法如下：

```
1. <element name='comp' src='../common/component/comp.hml'></element>
2. <div>
3. <comp prop1='xxxx' @child1="bindParentVmMethod"></comp>
4. </div>
```

结合if-else使用自定义组件的示例，showComp1为true时显示自定义组件comp1，否则显示comp2：

```
1. <element name='comp1' src='../common/component/comp1/comp1.hml'></element>
2. <element name='comp2' src='../common/component/comp2/comp2.hml'></element>
3. <div>
4. <comp1 if="{{showComp1}}" prop1='xxxx' @child1="bindParentVmMethodOne"></comp1>
5. <comp2 else prop1='xxxx' @child1="bindParentVmMethodTwo"></comp2>
6. </div>
```

自定义组件的name属性指自定义组件名称(非必填)，组件名称对大小写不敏感，默认使用小写。src属性指自定义组件hml文件路径(必填)，若没有设置name属性，则默认使用hml文件名作为组件名。

## 自定义事件

PhonePC/2in1TabletTVWearable

父组件中绑定自定义子组件的事件使用(on|@)event-name="bindParentVmMethod"语法，子组件中通过this.$emit('eventName', { params: '传递参数' })触发事件并向上传递参数，父组件执行bindParentVmMethod方法并接收子组件传递的参数。

说明

子组件中使用驼峰命名法命名的事件，在父组件中绑定时需要使用短横线分隔命名形式，例如：@children-event表示绑定子组件的childrenEvent事件。

**示例1：无参数传递**

子组件comp定义如下：

```
1. <!-- comp.hml -->
2. <div class="item">
3. <text class="text-style" onclick="childClicked">点击这里查看隐藏文本</text>
4. <text class="text-style" if="{{showObj}}">hello world</text>
5. </div>
```

```
1. /* comp.css */
2. .item {
3. width: 700px;
4. flex-direction: column;
5. height: 300px;
6. align-items: center;
7. margin-top: 100px;
8. }
9. .text-style {
10. font-weight: 500;
11. font-family: Courier;
12. font-size: 40px;
13. }
```

```
1. // comp.js
2. export default {
3. data: {
4. showObj: false,
5. },
6. childClicked () {
7. this.$emit('eventType1');
8. this.showObj = !this.showObj;
9. },
10. }
```

引入子组件comp的父组件示例如下：

```
1. <!-- xxx.hml -->
2. <element name='comp' src='../common/component/comp.hml'></element>
3. <div class="container">
4. <comp @event-type1="textClicked"></comp>
5. </div>
```

```
1. /* xxx.css */
2. .container {
3. background-color: #f8f8ff;
4. flex: 1;
5. flex-direction: column;
6. align-content: center;
7. }
```

```
1. // xxx.js
2. export default {
3. textClicked () {}
4. }
```

**示例2：有参数传递**

子组件comp定义如下：

```
1. <!-- comp.hml -->
2. <div class="item">
3. <text class="text-style" onclick="childClicked">点击这里查看隐藏文本</text>
4. <text class="text-style" if="{{ showObj }}">hello world</text>
5. </div>
```

```
1. // comp.js
2. export default {
3. childClicked () {
4. this.$emit('eventType1', { text: '收到子组件参数' });
5. this.showObj = !this.showObj;
6. },
7. }
```

子组件向上传递参数text，父组件接收时通过e.detail来获取该参数：

```
1. <!-- xxx.hml -->
2. <element name='comp' src='../common/comp/comp.hml'></element>
3. <div class="container">
4. <text>父组件：{{text}}</text>
5. <comp @event-type1="textClicked"></comp>
6. </div>
```

```
1. // xxx.js
2. export default {
3. data: {
4. text: '开始',
5. },
6. textClicked (e) {
7. this.text = e.detail.text;
8. },
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/ROf9gPowT8e7WxhMIxEQtA/zh-cn_image_0000002552960256.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000320Z&HW-CC-Expire=86400&HW-CC-Sign=9650322421538BE99183AC1608800B3FA98B5DA59DE75F9ADCD2822481078A95)

## 自定义组件数据

PhonePC/2in1TabletTVWearable

自定义组件的js文件中可以通过声明data、props、computed等字段完成数据的定义、传递与处理，其中props与computed的具体使用请参考[数据传递与处理](js-components-custom-props.md)章节。

**表1** 自定义组件数据

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| data | Object | Function | 页面的数据模型，类型是对象或者函数，如果类型是函数，返回值必须是对象。属性名不能以$或\_开头，不要使用保留字for, if, show, tid。  在使用data时，不能同时使用private或public修饰符。 |
| props | Array | Object | props用于组件之间的数据通信，可以通过<tag xxxx='value'>方式传递给组件；props名称必须用小写，不能以$或\_开头，不要使用保留字for, if, show, tid。目前props的数据类型不支持Function。 |
| computed | Object | 计算属性，用于在读取或设置参数时，进行预先处理，其结果会被缓存。计算属性名不能以$或\_开头，不要使用保留字。 |
