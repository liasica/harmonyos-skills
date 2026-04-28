---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-syntax-hml
title: HML语法参考
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 框架说明 > 语法 > HML语法参考
category: harmonyos-references
scraped_at: 2026-04-28T08:03:23+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:c6f400bfd2677362facb9e31c64b59704492db24c0305d8a57e2266ab29b598b
---

HML是一套类HTML的标记语言，通过组件，事件构建出页面的内容。页面具备数据绑定、事件绑定、列表渲染、条件渲染等高级能力。

## 页面结构

PhonePC/2in1TabletTVWearableLite Wearable

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

PhonePC/2in1TabletTVWearableLite Wearable

```
1. <!-- xxx.hml -->
2. <div onclick="changeText">
3. <text> {{content[1]}} </text>
4. </div>
```

```
1. // xxx.js
2. export default {
3. data: {
4. content: ['Hello World!', 'Welcome to my world!']
5. },
6. changeText: function() {
7. this.content.splice(1, 1, this.content[0]);
8. }
9. }
```

说明

* 针对数组内的数据修改，请使用splice方法生效数据绑定变更。
* HML中的js表达式不支持ES6语法。

## 事件绑定

PhonePC/2in1TabletTVWearableLite Wearable

事件绑定的回调函数接收一个事件对象参数，可以通过访问该事件对象获取事件信息。

```
1. <!-- xxx.hml -->
2. <div>
3. <!-- 通过'@'绑定事件 -->
4. <div @click="clickfunc"></div>
5. <!-- 通过'on'绑定事件  -->
6. <div onclick="clickfunc"></div>
7. <!-- 通过'on'绑定事件，不推荐使用5+ -->
8. <div onclick="clickfunc"></div>
9. <!-- 使用事件冒泡模式绑定事件回调函数。5+ -->
10. <div on:click.bubble="clickfunc"></div>
11. <!-- on:{event}等价于on:{event}.bubble。5+ -->
12. <div on:click="clickfunc"></div>
13. <!-- 绑定事件回调函数，但阻止事件向上传递。5+ -->
14. <div grab:click.bubble="clickfunc"></div>
15. <!-- grab:{event}等价于grab:{event}.bubble。5+ -->
16. <div grab:click="clickfunc"></div>
17. </div>
```

```
1. // xxx.js
2. export default {
3. data: {
4. obj: '',
5. },
6. clickfunc: function(e) {
7. this.obj = 'Hello World';
8. console.info(e);
9. },
10. }
```

说明

事件冒泡机制从API version 5开始支持。升级SDK后，运行存量JS应用，采用旧写法（onclick）的事件绑定还是按事件不冒泡进行处理。但如果使用新版本SDK重新打包JS应用，将旧写法按事件冒泡进行处理。为了避免业务逻辑错误，建议将旧写法（如onclick）改成新写法（grab:click）。

**示例：**

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text class="title">{{count}}</text>
4. <div class="box">
5. <input type="button" class="btn" value="increase" onclick="increase" />
6. <input type="button" class="btn" value="decrease" @click="decrease" />
7. <!-- 传递额外参数 -->
8. <input type="button" class="btn" value="double" @click="multiply(2)" />
9. <input type="button" class="btn" value="decuple" @click="multiply(10)" />
10. <input type="button" class="btn" value="square" @click="multiply(count)" />
11. </div>
12. </div>
```

```
1. // xxx.js
2. export default {
3. data: {
4. count: 0
5. },
6. increase() {
7. this.count++;
8. },
9. decrease() {
10. this.count--;
11. },
12. multiply(multiplier) {
13. this.count = multiplier * this.count;
14. }
15. };
```

```
1. /* xxx.css */
2. .container {
3. display: flex;
4. flex-direction: column;
5. justify-content: center;
6. align-items: center;
7. left: 0px;
8. top: 0px;
9. width: 454px;
10. height: 454px;
11. }
12. .title {
13. font-size: 30px;
14. text-align: center;
15. width: 200px;
16. height: 100px;
17. }
18. .box {
19. width: 454px;
20. height: 200px;
21. justify-content: center;
22. align-items: center;
23. flex-wrap: wrap;
24. }
25. .btn {
26. width: 200px;
27. border-radius: 0;
28. margin-top: 10px;
29. margin-left: 10px;
30. }
```

## 列表渲染

PhonePC/2in1TabletTVWearableLite Wearable

```
1. <!-- xxx.hml -->
2. <div class="array-container">
3. <!-- div列表渲染 -->
4. <!-- 默认$item代表数组中的元素, $idx代表数组中的元素索引 -->
5. <div class="item-container" for="{{array}}" tid="id" onclick="changeText">
6. <text>{{$idx}}.{{$item.name}}</text>
7. </div>
8. <!-- 自定义元素变量名称 -->
9. <div class="item-container" for="{{value in array}}" tid="id" onclick="changeText">
10. <text>{{$idx}}.{{value.name}}</text>
11. </div>
12. <!-- 自定义元素变量、索引名称 -->
13. <div class="item-container" for="{{(index, value) in array}}" tid="id" onclick="changeText">
14. <text>{{index}}.{{value.name}}</text>
15. </div>
16. </div>
```

```
1. // xxx.js
2. export default {
3. data: {
4. array: [
5. {id: 1, name: 'jack', age: 18},
6. {id: 2, name: 'tony', age: 18},
7. ],
8. },
9. changeText: function() {
10. if (this.array[1].name === "tony"){
11. this.array.splice(1, 1, {id:2, name: 'Isabella', age: 18});
12. } else {
13. this.array.splice(2, 1, {id:3, name: 'Bary', age: 18});
14. }
15. },
16. }
```

```
1. .array-container {
2. width: 100%;
3. height: 100%;
4. justify-content: center;
5. align-items: center;
6. flex-direction: column;
7. }

9. .item-container {
10. margin-top: 10px;
11. width: 200px;
12. height: 50px;
13. flex-direction: column;
14. }
```

tid属性主要用于优化for循环的重渲染性能，在列表数据变更时提高重渲染效率。tid属性是用来指定数组中每个元素的唯一标识，如果未指定，数组中每个元素的索引为该元素的唯一id。例如上述tid="id"表示数组中的每个元素的id属性为该元素的唯一标识。for循环支持的写法如下：

* for="array"：其中array为数组对象，array的元素变量默认为$item。
* for="v in array"：其中v为自定义的元素变量，元素索引默认为$idx。
* for="(i, v) in array"：其中元素索引为i，元素变量为v，遍历数组对象array。

说明

* 数组中的每个元素必须存在tid指定的数据属性，否则运行时可能会导致异常。
* 数组中被tid指定的属性要保证唯一性，如果不是则会造成性能损耗。比如，示例中只有id和name可以作为tid字段，因为它们属于唯一字段。
* tid不支持表达式。

## 条件渲染

PhonePC/2in1TabletTVWearableLite Wearable

条件渲染分为2种：if/elif/else和show。两种写法的区别在于：第一种写法里if为false时，组件不会在vdom中构建，也不会渲染，而第二种写法里show为false时虽然也不渲染，但会在vdom中构建；另外，当使用if/elif/else写法时，节点必须是兄弟节点，否则编译无法通过。实例如下：

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <button class="btn" type="capsule" value="toggleShow" onclick="toggleShow"></button>
4. <button class="btn" type="capsule" value="toggleDisplay" onclick="toggleDisplay"></button>
5. <text if="{{show}}"> Hello-One </text>
6. <text elif="{{display}}"> Hello-Two </text>
7. <text else> Hello-World </text>
8. </div>
```

```
1. /* xxx.css */
2. .container{
3. flex-direction: column;
4. align-items: center;
5. }
6. .btn{
7. width: 280px;
8. font-size: 26px;
9. margin: 10px 0;
10. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. show: false,
5. display: true,
6. },
7. toggleShow: function() {
8. this.show = !this.show;
9. },
10. toggleDisplay: function() {
11. this.display = !this.display;
12. }
13. }
```

渲染优化：show方法。当show为真时，节点正常渲染；当为假时，仅仅设置display样式为none。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <button class="btn" type="capsule" value="toggle" onclick="toggle"></button>
4. <text show="{{visible}}" > Hello World </text>
5. </div>
```

```
1. /* xxx.css */
2. .container{
3. flex-direction: column;
4. align-items: center;
5. }
6. .btn{
7. width: 280px;
8. font-size: 26px;
9. margin: 10px 0;
10. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. visible: false,
5. },
6. toggle: function() {
7. this.visible = !this.visible;
8. },
9. }
```

说明

禁止在同一个元素上同时设置for和if属性。
