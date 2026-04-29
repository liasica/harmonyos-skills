---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-syntax-hml
title: HML语法参考
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 框架说明 > 语法 > HML语法参考
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:42+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8851791e32aee07c3850385df11079de091cae11c0375b4f22e4c3306b37d005
---

HML是一套类HTML的标记语言，通过组件，事件构建出页面的内容。页面具备数据绑定、事件绑定、列表渲染、条件渲染和逻辑控制等高级能力。

## 页面结构

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

```
1. <!-- xxx.hml -->
2. <div class="container" onclick="changeText">
3. <text> {{content[1]}} </text>
4. </div>
```

```
1. /*xxx.css*/
2. .container{
3. margin: 200px;
4. }
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
* hml文件中的js表达式不支持ES6语法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/hSp3Y9nIQaSBMvTIJiM4zQ/zh-cn_image_0000002558604910.png?HW-CC-KV=V1&HW-CC-Date=20260429T052840Z&HW-CC-Expire=86400&HW-CC-Sign=34E07EC94546DDCA47B266C3B396F3AA3954557D1B4F0CA56D44B82343EBE55A)

## 普通事件绑定

事件通过'on'或者'@'绑定在组件上，当组件触发事件时会执行JS文件中对应的事件处理函数。

事件支持的写法有：

* "funcName"：funcName为事件回调函数名（在JS文件中定义相应的函数实现）。
* "funcName(a,b)"：函数参数例如a，b可以是常量，或者是在JS文件中的data中定义的变量（前面不用写this.）。
* 示例

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/KKBg75EbSkCgONZGKd9F1Q/zh-cn_image_0000002589324435.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052840Z&HW-CC-Expire=86400&HW-CC-Sign=28CF500132471A61E8C31689118DADE3F86641290C11C58C60DBAA378D16CF74)

## 冒泡事件绑定5+

冒泡事件绑定包括：

* 绑定冒泡事件：on:{event}.bubble。on:{event}等价于on:{event}.bubble。
* 绑定并阻止冒泡事件向上冒泡：grab:{event}.bubble。grab:{event}等价于grab:{event}.bubble。

  说明

  冒泡事件是指多个组件嵌套时，组件之间会有层次关系，当这些组件注册了相同的事件时，这个事件会首先运行在该元素上的处理程序，然后运行其父元素上的处理程序，一直向上到其他祖先上的处理程序。如果当一个组件触发了这个事件，它会首先触发该组件的回调函数，然后触发其父元素上的回调函数，然后触发其他祖先上的处理程序。

  详细冒泡事件说明参见[通用事件](../harmonyos-references/js-components-common-events.md)章节。
* 示例

  ```
  1. <!-- xxx.hml -->
  2. <div>
  3. <!-- 使用事件冒泡模式绑定事件回调函数。5+ -->;
  4. <div on:touchstart.bubble="touchstartfunc" style="background-color: red; width: 10%; height: 100%"></div>
  5. <div on:touchstart="touchstartfunc" style="background-color: orange; width: 10%; height: 100%"></div>
  6. <!-- 绑定事件回调函数，但阻止事件向上传递。5+ -->
  7. <div grab:touchstart.bubble="touchstartfunc" style="background-color: yellow; width: 10%; height: 100%"></div>
  8. <div grab:touchstart="touchstartfunc" style="background-color: greenyellow; width: 10%; height: 100%"></div>
  9. <!-- 使用事件冒泡模式绑定事件回调函数。6+ -->
  10. <div on:click.bubble="clickfunc" style="background-color: lightskyblue; width: 10%; height: 100%"></div>
  11. <div on:click="clickfunc" style="background-color: cornflowerblue; width: 10%; height: 100%"></div>
  12. <!-- 绑定事件回调函数，但阻止事件向上传递。6+ -->
  13. <div grab:click.bubble="clickfunc" style="background-color: mediumslateblue; width: 10%; height: 100%"></div>
  14. <div grab:click="clickfunc" style="background-color: purple; width: 10%; height: 100%"></div>
  15. </div>
  ```

  ```
  1. // xxx.js
  2. export default {
  3. clickfunc: function(e) {
  4. console.info(e);
  5. },
  6. touchstartfunc: function(e) {
  7. console.info(e);
  8. },
  9. }
  ```

说明

采用旧写法(onclick)的事件绑定在最小API版本6以下时采用不冒泡处理，在最小API版本为6及6以上时采用冒泡处理。

## 捕获事件绑定5+

Touch触摸类事件支持捕获，捕获阶段位于冒泡阶段之前，捕获事件先到达父组件然后到达子组件。

捕获事件绑定包括：

* 绑定捕获事件：on:{event}.capture。
* 绑定并阻止事件向下传递：grab:{event}.capture。
* 示例

  ```
  1. <!-- xxx.hml -->
  2. <div>
  3. <!-- 使用事件捕获模式绑定事件回调函数。5+ -->
  4. <div on:touchstart.capture="touchstartfunc"></div>
  5. <!-- 绑定事件回调函数，但阻止事件向下传递。5+ -->
  6. <div grab:touchstart.capture="touchstartfunc"></div>
  7. </div>
  ```

  ```
  1. // xxx.js
  2. export default {
  3. touchstartfunc: function(e) {
  4. console.info(e);
  5. },
  6. }
  ```

## 列表渲染

```
1. <!-- xxx.hml -->
2. <div class="array-container" style="flex-direction: column;margin: 200px;">
3. <!-- div列表渲染 -->
4. <!-- 默认$item代表数组中的元素, $idx代表数组中的元素索引 -->
5. <div for="{{array}}" tid="id" onclick="changeText">
6. <text>{{$idx}}.{{$item.name}}</text>
7. </div>
8. <!-- 自定义元素变量名称 -->
9. <div for="{{value in array}}" tid="id" onclick="changeText">
10. <text>{{$idx}}.{{value.name}}</text>
11. </div>
12. <!-- 自定义元素变量、索引名称 -->
13. <div for="{{(index, value) in array}}" tid="id" onclick="changeText">
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

tid属性主要用来加速for循环的重渲染，旨在列表中的数据有变更时，提高重新渲染的效率。tid属性是用来指定数组中每个元素的唯一标识，如果未指定，数组中每个元素的索引为该元素的唯一id。例如上述tid="id"表示数组中的每个元素的id属性为该元素的唯一标识。for循环支持的写法如下：

* for="array"：其中array为数组对象，array的元素变量默认为$item。
* for="v in array"：其中v为自定义的元素变量，元素索引默认为$idx。
* for="(i, v) in array"：其中元素索引为i，元素变量为v，遍历数组对象array。

说明

* 数组中的每个元素必须存在tid指定的数据属性，否则运行时可能会导致异常。
* 数组中被tid指定的属性要保证唯一性，如果不是则会造成性能损耗。比如，示例中只有id和name可以作为tid字段，因为它们属于唯一字段。
* tid不支持表达式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/vD8VCq6zQzCIv6mik19wIA/zh-cn_image_0000002589244375.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052840Z&HW-CC-Expire=86400&HW-CC-Sign=D485E262EDA30BF13B2376EF6D5E0778424BBBCE3B795B8AC13201DDE5AFD5CD)

## 条件渲染

条件渲染分为2种：if/elif/else和show。两种写法的区别在于：第一种写法里if为false时，组件不会在vdom中构建，也不会渲染，而第二种写法里show为false时虽然也不渲染，但会在vdom中构建；另外，当使用if/elif/else写法时，节点必须是兄弟节点，否则编译无法通过。实例如下：

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <button class="btn" type="capsule" value="toggleShow" onclick="toggleShow"></button>
4. <button class="btn" type="capsule" value="toggleDisplay" onclick="toggleDisplay"></button>
5. <text if="{{visible}}"> Hello-world1 </text>
6. <text elif="{{display}}"> Hello-world2 </text>
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
4. visible: false,
5. display: true,
6. },
7. toggleShow: function() {
8. this.visible = !this.visible;
9. },
10. toggleDisplay: function() {
11. this.display = !this.display;
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/HP18Wve4QA6H0kVByQkctw/zh-cn_image_0000002558764568.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052840Z&HW-CC-Expire=86400&HW-CC-Sign=562B03B38DE8FC03868901A0330F4EC24D884901BD545826636000552B9B2DCD)

优化渲染：show方法。当show为true时，节点正常渲染；当为false时，仅仅设置display样式为none。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/iRi1NczVTCy3zWaiJ0ENhA/zh-cn_image_0000002558604912.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052840Z&HW-CC-Expire=86400&HW-CC-Sign=95CCBF946C2CB9958A1BC5A4F99596F345088B540ACC4639AE224C3C0BB0B325)

## 逻辑控制块

<block>控制块使得循环渲染和条件渲染变得更加灵活；block在构建时不会被当作真实的节点编译。注意block标签只支持for和if属性。

```
1. <!-- xxx.hml -->
2. <list>
3. <block for="glasses">
4. <list-item type="glasses">
5. <text>{{$item.name}}</text>
6. </list-item>
7. <block for="$item.kinds">
8. <list-item type="kind">
9. <text>{{$item.color}}</text>
10. </list-item>
11. </block>
12. </block>
13. </list>
```

```
1. // xxx.js
2. export default {
3. data: {
4. glasses: [
5. {name:'sunglasses', kinds:[{name:'XXX',color:'XXX'},{name:'XXX',color:'XXX'}]},
6. {name:'nearsightedness mirror', kinds:[{name:'XXX',color:'XXX'}]},
7. ],
8. },
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/ObakUOEMRMuwkbEJ8pzNAw/zh-cn_image_0000002589324437.png?HW-CC-KV=V1&HW-CC-Date=20260429T052840Z&HW-CC-Expire=86400&HW-CC-Sign=6D41F69DAC74F8C6E2C1FFBE2B28F4E31C390803E312C2D0F0490B35458B7ACE)

## 模板引用

HML可以通过element引用模板文件，详细介绍可参考[自定义组件的基本用法](../harmonyos-references/js-components-custom-basic-usage.md)章节。

```
1. <!-- template.hml -->
2. <div class="item">
3. <text>Name: {{name}}</text>
4. <text>Age: {{age}}</text>
5. </div>
```

```
1. <!-- index.hml -->
2. <element name='comp' src='../../common/template.hml'></element>
3. <div>
4. <comp name="Tony" age="18"></comp>
5. </div>
```
