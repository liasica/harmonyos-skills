---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-syntax-hml
title: HML语法参考
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 框架说明 > 语法 > HML语法参考
category: harmonyos-references
scraped_at: 2026-04-28T08:03:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5c5b82518043b3066afd1cc207fb6be5b8dae1f98bdb3ec1045260c123274e7d
---

HML是一套类HTML的标记语言，通过组件，事件构建出页面的内容。页面具备数据绑定、事件绑定、条件渲染和逻辑控制等高级能力。

## 页面结构

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="item-container">
3. <text class="item-title">Image Show</text>
4. <div class="item-content">
5. <image src="/common/xxx.png" class="image"></image>
6. </div>
7. </div>
```

## 数据绑定

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="item-container">
3. <text>{{content}}</text>            <!-- 输出：Hello World！-->
4. <text>{{key1}} {{key2}}</text>       <!-- 输出：Hello World-->
5. <text>key1 {{key1}}</text>           <!-- 输出：key1 Hello-->
6. <text>{{flag1 && flag2}}</text>      <!-- 输出：false-->
7. <text>{{flag1 || flag2}}</text>      <!-- 输出：true-->
8. <text>{{!flag1}}</text>              <!-- 输出：false-->
9. </div>
```

卡片hml文件中的变量需要在json文件的data字段下进行声明：

```
1. {
2. "data": {
3. "content": "Hello World!",
4. "key1": "Hello",
5. "key2": "World",
6. "flag1": true,
7. "flag2": false
8. }
9. }
```

说明

* key值支持对象操作符和数组操作符，如{{key.value}}、{{key[0]}}。
* 支持字符串拼接、逻辑运算和三元表达式。
* 字符串拼接：

  + 支持变量跟变量：{{key1}}{{key2}}等
  + 支持常量跟变量： "my name is {{name}}， i am from {{city}}." "key1 {{key1}}"
* 逻辑运算：

  + 与：{{flag1 && flag2}}（仅支持两个boolean变量间的与逻辑运算）
  + 或：{{flag1 || flag2}} （仅支持两个boolean变量间的或逻辑运算）
  + 非：{{!flag1}} （仅支持boolean变量的非逻辑运算）
* 三元表达式

  + {{flag? key1:key2}}（flag为boolean变量，key1和key2可以是变量，也可以是常量）
* 注意事项

  + 非boolean类型值进行bool运算默认为false
  + 以上所有变量解析跟运算解析均不支持嵌套

## 事件绑定

PhonePC/2in1TabletTVWearable

卡片的事件需要在json文件的actions字段下进行声明。卡片仅支持click通用事件，事件的定义只能是直接命令式，事件定义必须包含action字段，用以说明事件类型。卡片支持两种事件类型：跳转事件(router)和消息事件(message)。跳转事件可以跳转到卡片提供方的应用，消息事件可以将开发者自定义信息传递给卡片提供方。事件参数支持变量，变量以"{{}}"修饰。跳转事件中若定义了params字段，则在被拉起应用的onStart的intent中，可用"params"作为key将跳转事件定义的params字段的值取到。

* 跳转事件格式

  通过定义ability名称和携带的参数字段params直接跳转，可用"params"作为key提取到跳转事件定义的params字段值。

  | 选择器 | 样例 | 默认值 | 样例描述 |
  | --- | --- | --- | --- |
  | action | string | "router" | 事件类型。  - "router"：用于应用跳转。  - "message"：自定义点击事件。 |
  | abilityName | string | - | 跳转ability名。 |
  | params | Object | - | 跳转应用携带的额外参数。 |

  ```
  1. {
  2. "data": {
  3. "mainAbility": "xxx.xxx.xxx"
  4. },
  5. "actions": {
  6. "routerEvent": {
  7. "action": "router",
  8. "abilityName": "{{mainAbility}}",
  9. "params":{}
  10. }
  11. }
  12. }
  ```
* 消息事件格式

  | 选择器 | 样例 | 默认值 | 样例描述 |
  | --- | --- | --- | --- |
  | action | string | message | 表示事件类型。 |
  | params | Object | - | 跳转应用携带的额外参数。 |

  ```
  1. {
  2. "actions": {
  3. "activeEvent": {
  4. "action": "message",
  5. "params": {}
  6. }
  7. }
  8. }
  ```
* 绑定路由事件和消息事件

  ```
  1. <!-- xxx.hml -->
  2. <div>
  3. <!-- 正常格式 -->
  4. <div onclick="activeEvent"></div>
  5. <!-- 缩写 -->
  6. <div @click="activeEvent"></div>
  7. </div>
  ```

## 列表渲染

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="array-container">
3. <!-- div列表渲染 -->
4. <!-- 默认$item代表数组中的元素, $idx代表数组中的元素索引 -->
5. <div for="{{array}}" tid="id">
6. <text>{{$item.name}}</text>
7. </div>
8. <!-- 自定义元素变量名称 -->
9. <div for="{{value in array}}" tid="id">
10. <text>{{value.name}}</text>
11. </div>
12. <!-- 自定义元素变量、索引名称 -->
13. <div for="{{(index, value) in array}}" tid="id">
14. <text>{{value.name}}</text>
15. </div>
16. </div>
```

```
1. {
2. "data": {
3. "array": [
4. {"id": 1, "name": "jack", "age": 18},
5. {"id": 2, "name": "tony", "age": 18}
6. ]
7. }
8. }
```

tid属性主要用来加速for循环的重渲染，旨在列表中的数据有变更时，提高重新渲染的效率。tid属性是用来指定数组中每个元素的唯一标识，如果未指定，数组中每个元素的索引为该元素的唯一id。例如上述tid="id"表示数组中的每个元素的id属性为该元素的唯一标识。for循环支持的写法如下：

* for="array"：其中array为数组对象，array的元素变量默认为$item。
* for="v in array"：其中v为自定义的元素变量，元素索引默认为$idx。
* for="(i, v) in array"：其中元素索引为i，元素变量为v，遍历数组对象array。

说明

* 数组中的每个元素必须存在tid指定的数据属性，否则运行时可能会导致异常。
* 数组中被tid指定的属性要保证唯一性，如果不是则会造成性能损耗。比如，示例中只有id和name可以作为tid字段，因为它们属于唯一字段。
* tid不支持表达式。
* 不支持for嵌套使用。
* for对应的变量数组，当前要求数组中的object是相同类型，不支持多种object类型混合写在一个数组中。

## 条件渲染

PhonePC/2in1TabletTVWearable

条件渲染分为2种：if/elif/else和show。

当使用if/elif/else写法时，节点必须是兄弟节点，否则编译无法通过。实例如下：

```
1. <!-- xxx.hml -->
2. <div>
3. <text if="{{show}}"> Hello-TV </text>
4. <text elif="{{display}}"> Hello-Wearable </text>
5. <text else> Hello-World </text>
6. </div>
```

```
1. {
2. "data": {
3. "show": false,
4. "display": true
5. }
6. }
```

当show为真时，节点正常渲染；当show为假时，节点不渲染，效果等同display样式为none。

```
1. <!-- xxx.hml -->
2. <text show="{{visible}}"> Hello World </text>
```

```
1. {
2. "data": {
3. "visible": false
4. }
5. }
```

## 逻辑控制块

PhonePC/2in1TabletTVWearable

<block>控制块使得循环渲染和条件渲染变得更加灵活；block在构建时不会被当作真实的节点编译。block标签只支持if属性。

```
1. <!-- xxx.hml -->
2. <div>
3. <block if="{{show}}">
4. <text>Hello</text>
5. <text>World</text>
6. </block>
7. </div>
```

```
1. {
2. "data": {
3. "show": true
4. }
5. }
```
