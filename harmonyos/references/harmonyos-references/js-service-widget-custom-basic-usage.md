---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-custom-basic-usage
title: 自定义组件使用说明
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 自定义组件使用说明
category: harmonyos-references
scraped_at: 2026-04-28T08:03:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:65998e5049d04972262e9ae0e921f69750efd5674c351cd7256bd374590d8ad0
---

说明

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

自定义组件是用户根据业务需求，将已有的组件组合，封装成的新组件，可以在工程中多次调用，提高代码的可读性。自定义组件通过element引入到宿主页面，使用方法：

```
1. <element name='comp' src='../../common/component/comp.hml'></element>
2. <div>
3. <comp prop1='xxxx' @child1="bindParentVmMethod"></comp>
4. </div>
```

* name属性指自定义组件名称(非必填)，组件名称对大小写不敏感，默认使用小写。src属性指自定义组件hml文件路径(必填)，若没有设置name属性，则默认使用hml文件名作为组件名。
* 事件绑定：自定义组件中绑定子组件事件使用(on|@)child1语法，子组件中通过{action:"proxy", method: "eventName"}触发事件并进行传值，父组件执行bindParentVmMethod方法并接收子组件传递的参数。

## 自定义组件配置文件标签

PhonePC/2in1TabletTVWearable

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| data | Object | 页面的数据模型，类型是对象。属性名不能以$或\_开头，不要使用保留字for, if, show, tid。 |
| props | Array/Object | props用于组件之间的通信，可以通过<tag xxxx='value'>方式传递给组件；props名称必须用小写，不能以$或\_开头，不要使用保留字for, if, show, tid。目前props的数据类型不支持Function。 |

## 添加自定义事件

PhonePC/2in1TabletTVWearable

自定义组件内支持自定义事件，该事件的标识需要action类型指定为proxy，事件名则通过method指定。使用该自定义组件的卡片页面可以通过该事件名注册相应的事件回调，当自定义组件内该自定义事件触发时，会触发卡片页面上注册的回调事件。

说明

事件名不支持大写字母。

**自定义子组件示例：**

```
1. <!-- comp.hml -->
2. <div class="container">
3. <div class="row-3" if="true">
4. <button onclick="buttonClicked" value="click"></button>
5. </div>
6. </div>
```

```
1. /* comp.css */
2. .container {
3. flex-direction:column;
4. background-color: green;
5. width: 100%;
6. height: 100%;
7. }

9. .row-3 {
10. width: 100%;
11. height: 50px;
12. background-color: orange;
13. font-size:15px;
14. }
```

```
1. {
2. "data": {
3. },
4. "actions": {
5. "buttonClicked": {
6. "action": "proxy",
7. "method":"event_1"
8. }
9. }
10. }
```

**父组件示例：**

```
1. <!-- xxx.hml -->
2. <element name='comp' src='../../common/customComponent/comp.hml'></element>

4. <div class="container">
5. <comp @event_1="click"></comp>
6. <button value="parentClick" @click="buttonClick"></button>
7. </div>
```

```
1. /* xxx.css */
2. .container {
3. background-color: red;
4. height: 500px;
5. width: 500px;
6. }
```

```
1. {
2. "data": {
3. },
4. "actions": {
5. "click": {
6. "action": "message",
7. "params": {
8. "message": "click event"
9. }
10. },
11. "buttonClick": {
12. "action": "message",
13. "params": {
14. "message": "click event 2"
15. }
16. }
17. }
18. }
```

## props

PhonePC/2in1TabletTVWearable

自定义组件可以通过props声明自定义属性，父组件通过设置属性向子组件传递参数。

### 添加默认值

PhonePC/2in1TabletTVWearable

子组件可以通过固定值default设置默认值，当父组件没有设置该属性时，将使用其默认值。此情况下props属性必须为对象形式，不能用数组形式，示例如下：

```
1. <!-- comp.hml -->
2. <div class="container">
3. <div class="row-1">
4. <div class="box-1">
5. <text>xiaoziti</text>
6. </div>
7. <div class="box-2">
8. <text>{{text}}</text>
9. </div>
10. <div class="box-3">
11. <text>{{textdata[0]}}</text>
12. </div>
13. </div>
14. <div class="row-2" if="true">
15. <button value="{{progress}}"></button>
16. </div>
17. <div class="row-3" if="true">
18. <button onclick="buttonClicked" value="click"></button>
19. </div>
20. </div>
```

```
1. {
2. "data": {
3. "progress": {
4. "default": "80"
5. }
6. },
7. "props": {
8. "textdata": {
9. "default": ["a","b"]
10. },
11. "progress": {
12. "default": 60
13. },
14. "text": {
15. "default": "ha"
16. }
17. },
18. "actions": {
19. "buttonClicked": {
20. "action": "proxy",
21. "method": "event_1"
22. }
23. }
24. }
```

引用子组件comp的父组件示例如下：

```
1. <!-- xxx.hml -->
2. <element name='comp' src='../../common/customComponent/comp.hml'></element>

4. <div class="container">
5. <comp progress="{{clicknow}}" textdata="{{texts}}" if="false" @event_1="click"></comp>
6. </div>
```

### 数据单向性

PhonePC/2in1TabletTVWearable

父子组件之间数据的传递是单向的，只能从父组件传递给子组件，子组件不能直接修改父组件传递下来的值，可以将props传入的值用data接收后作为默认值，再对data的值进行修改。

更多说明请参考[Props](js-components-custom-props.md#props)文档。
