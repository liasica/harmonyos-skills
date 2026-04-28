---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-input
title: input开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 基础组件 > input开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:27+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:5c5fcddb3f11ffc286875929ae216d76982efe0434e324c9951f5fc12d8f1151
---

input是交互式组件，用于接收用户数据。其类型可设置为日期、多选框和按钮等。具体用法请参考[input API](../harmonyos-references/js-components-basic-input.md)。

## 创建input组件

在pages/index目录下的hml文件中创建一个input组件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <input type="text">
4. Please enter the content
5. </input>
6. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/zBgnCxAwQ8yVehiAp71KaA/zh-cn_image_0000002552798452.png?HW-CC-KV=V1&HW-CC-Date=20260427T234025Z&HW-CC-Expire=86400&HW-CC-Sign=40B460CAF3E422DCE2AD5ED9611651E7B521E5FC24451232B0E9149A1BB730C6)

## 设置input类型

通过设置type属性来定义input类型，如将input设置为button、date等。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="div-button">
4. <dialog class="dialogClass" id="dialogId">
5. <div class="content">
6. <text>this is a dialog</text>
7. </div>
8. </dialog>
9. <input class="button" type="button" value="click" onclick="btnclick"></input>
10. </div>
11. <div class="content">
12. <input onchange="checkboxOnChange" checked="true" type="checkbox"></input>
13. </div>
14. <div class="content">
15. <input type="date" class="flex" placeholder="Enter date"></input>
16. </div>
17. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. align-items: center;
6. flex-direction: column;
7. justify-content: center;
8. background-color: #F1F3F5 ;
9. }
10. .div-button {
11. flex-direction: column;
12. align-items: center;
13. }
14. .dialogClass{
15. width:80%;
16. height: 200px;
17. }
18. .button {
19. margin-top: 30px;
20. width: 50%;
21. }
22. .content{
23. width: 90%;
24. height: 150px;
25. align-items: center;
26. justify-content: center;
27. }
28. .flex {
29. width: 80%;
30. margin-bottom:40px;
31. }
```

```
1. // xxx.js
2. export default {
3. btnclick(){
4. this.$element('dialogId').show()
5. },
6. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/jVmgVrqHTPao3kKWscVcBA/zh-cn_image_0000002583438147.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234025Z&HW-CC-Expire=86400&HW-CC-Sign=4C8B9B1F56569E2628159637A7A190BD38780685587BDF6FFB94432145763C17)

说明

仅当input类型为checkbox或radio时，当前组件选中的属性是checked才生效，默认值为false。

## 事件绑定

向input组件添加translate事件。

```
1. <!-- xxx.hml -->
2. <div class="content">
3. <text style="margin-left: -7px;">
4. <span>Enter text and then touch and hold what you've entered</span>
5. </text>
6. <input class="input" type="text" ontranslate="translate" placeholder="translate"> </input>
7. </div>
```

```
1. /* xxx.css */
2. .content {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color: #F1F3F5;
9. }
10. .input {
11. margin-top: 50px;
12. width: 60%;
13. placeholder-color: gray;
14. }
15. text{
16. width:100%;
17. font-size:25px;
18. text-align:center;
19. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction'

4. export default {
5. translate(e) {
6. promptAction.showToast({
7. message: e.value,
8. duration: 3000,
9. });
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/IHDEQhlOSnGyNV7d6X2mTg/zh-cn_image_0000002552958102.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234025Z&HW-CC-Expire=86400&HW-CC-Sign=05D1A3E6528EBA0ED0B27279C8E8781238C9CCD513A100863F63608E86B5E6D9)

## 设置输入提示

通过对input组件添加showError方法来提示输入的错误原因。

```
1. <!-- xxx.hml -->
2. <div class="content">
3. <input id="input" class="input" type="text"  maxlength="20" placeholder="Please input text" onchange="change">
4. </input>
5. <input class="button" type="button" value="Submit" onclick="buttonClick"></input>
6. </div>
```

```
1. /* xxx.css */
2. .content {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color: #F1F3F5;
9. }
10. .input {
11. width: 80%;
12. placeholder-color: gray;
13. }
14. .button {
15. width: 30%;
16. margin-top: 50px;
17. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction'
3. export default {
4. data:{
5. value:'',
6. },
7. change(e){
8. this.value = e.value;
9. promptAction.showToast({
10. message: "value: " + this.value,
11. duration: 3000,
12. });
13. },
14. buttonClick(e){
15. if(this.value.length > 6){
16. this.$element("input").showError({
17. error:  'Up to 6 characters are allowed.'
18. });
19. }else if(this.value.length == 0){
20. this.$element("input").showError({
21. error:this.value + 'This field cannot be left empty.'
22. });
23. }else{
24. promptAction.showToast({
25. message: "success "
26. });
27. }
28. },
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/MiDVzfjcQROmaFIzGdMdfQ/zh-cn_image_0000002583478103.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234025Z&HW-CC-Expire=86400&HW-CC-Sign=C4363806989F27FD0EDFE5CB5C964780B819AA3EA516897350A0445BA4002F6C)

说明

showError方法仅在input类型为text、email、date、time、number和password时生效。

## 场景示例

根据场景选择不同类型的input输入框，完成信息录入。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="label-item">
4. <label>memorandum</label>
5. </div>
6. <div class="label-item">
7. <label class="lab" target="input1">content:</label>
8. <input class="flex" id="input1" placeholder="Enter content" />
9. </div>
10. <div class="label-item">
11. <label class="lab" target="input3">date:</label>
12. <input class="flex" id="input3" type="date" placeholder="Enter date" />
13. </div>
14. <div class="label-item">
15. <label class="lab" target="input4">time:</label>
16. <input class="flex" id="input4" type="time" placeholder="Enter time" />
17. </div>
18. <div class="label-item">
19. <label class="lab" target="checkbox1">Complete:</label>
20. <input class="flex" type="checkbox" id="checkbox1" style="width: 100px;height: 100px;" />
21. </div>
22. <div class="label-item">
23. <input class="flex" type="button" id="button" value="save" onclick="btnclick"/>
24. </div>
25. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. background-color: #F1F3F5;
5. }
6. .label-item {
7. align-items: center;
8. border-bottom-width: 1px;border-color: #dddddd;
9. }
10. .lab {
11. width: 400px;}
12. label {
13. padding: 30px;
14. font-size: 30px;
15. width: 320px;
16. font-family: serif;
17. color: #9370d8;
18. font-weight: bold;
19. }
20. .flex {
21. flex: 1;
22. }
23. .textareaPadding {
24. padding-left: 100px;
25. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. data: {
5. },
6. onInit() {
7. },
8. btnclick(e) {
9. promptAction.showToast({
10. message:'Saved successfully!'
11. })
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/7cOZpFE3TwSqcShfVsu4AQ/zh-cn_image_0000002552798454.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234025Z&HW-CC-Expire=86400&HW-CC-Sign=3262551E09D1DE2F01B9BE940D0C9CB4DEE19F480AA9B8C8FAA1B76D5CDA29E0)
