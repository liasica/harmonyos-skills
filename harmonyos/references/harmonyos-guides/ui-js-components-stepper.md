---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-stepper
title: stepper开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 常见组件开发指导 > 容器组件 > stepper开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3b9d5c81d77a7e8225eaa129a6895222ab9ac108a174983387ed84291aea7ad6
---

当一个任务需要多个步骤时，可以使用stepper组件展示当前进展。具体用法请参考[stepper API](../harmonyos-references/js-components-container-stepper.md)。

## 创建stepper组件

在pages/index目录下的hml文件中创建一个stepper组件。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <stepper>
4. <stepper-item>
5. <text>Step 1</text>
6. </stepper-item>
7. <stepper-item>
8. <text>Step 2</text>
9. </stepper-item>
10. </stepper>
11. </div>
```

```
1. /* xxx.css */
2. .container {
3. width:100%;
4. height:100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. background-color: #F1F3F5;
9. }
10. text{
11. width: 100%;
12. height: 100%;
13. text-align: center;
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/HOBF08DyR_SQEo6llzcjZg/zh-cn_image_0000002552798442.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234024Z&HW-CC-Expire=86400&HW-CC-Sign=54855A136B9CFB457BA70E3D5D02E924E93DC617809C58DE4B55DD0EA4125A13)

## 设置index属性

页面默认显示索引值为index的步骤。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <stepper index="2">
4. <stepper-item>
5. <text>stepper-item1</text>
6. </stepper-item>
7. <stepper-item>
8. <text>stepper-item2</text>
9. </stepper-item>
10. <stepper-item>
11. <text>stepper-item3</text>
12. </stepper-item>
13. </stepper>
14. </div>
```

```
1. /* xxx.css */
2. .container {
3. width:100%;
4. height:100%;
5. flex-direction: column;
6. background-color: #F1F3F5;
7. }
8. text{
9. width: 100%;
10. height: 100%;
11. text-align: center;
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/YmFf12aFRDGCbjqiar5cQw/zh-cn_image_0000002583438137.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234024Z&HW-CC-Expire=86400&HW-CC-Sign=A46F5F8D76527EF9B289284EF7497C61FDA8B579F9CA967577690E5EBFBBA668)

通过设置label属性，自定义stepper-item的提示按钮。

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <stepper index="1">
4. <stepper-item label="{{label_1}}">
5. <text>stepper-item1</text>
6. </stepper-item>
7. <stepper-item label="{{label_2}}">
8. <text>stepper-item2</text>
9. </stepper-item>
10. <stepper-item label="{{label_3}}">
11. <text>stepper-item3</text>
12. </stepper-item>
13. <stepper-item>
14. <text>stepper-item4</text>
15. </stepper-item>
16. </stepper>
17. </div>
```

```
1. /* xxx.css */
2. .container {
3. width:100%;
4. height:100%;
5. flex-direction: column;
6. background-color: #F1F3F5;
7. }
8. text{
9. width: 100%;
10. height: 100%;
11. text-align: center;
12. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. label_1:{
5. nextLabel: 'NEXT',
6. status: 'normal'
7. },
8. label_2:{
9. prevLabel: 'BACK',
10. nextLabel: 'NEXT',
11. status: 'normal'
12. },
13. label_3:{
14. prevLabel: 'BACK',
15. nextLabel: 'END',
16. status: 'disabled'
17. },
18. },
19. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/oMfG73iQQLKaEKEY6FzcFg/zh-cn_image_0000002552958092.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234024Z&HW-CC-Expire=86400&HW-CC-Sign=56F78F95DF8AD4C624A41CA44651D2324343953822FE5694510734316AB9E7B5)

## 设置样式

stepper组件默认填充父容器，通过border和background-color设置边框、背景色。

```
1. <!-- xxx.hml -->
2. <div class="container" >
3. <div class="stepperContent">
4. <stepper class="stepperClass">
5. <stepper-item>
6. <text>stepper-item1</text>
7. </stepper-item>
8. </stepper>
9. </div>
10. </div>
```

```
1. /* xxx.css */
2. .container {
3. width:100%;
4. height:100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. background-color:#F1F3F5;
9. }
10. .stepperContent{
11. width: 300px;
12. height: 300px;
13. }
14. .stepperClass{
15. border:1px solid silver ;
16. background-color: white;
17. }
18. text{
19. width: 100%;
20. height: 100%;
21. text-align: center;
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/ZBriUQ4iR6yh6gbrz3T6Og/zh-cn_image_0000002583478093.png?HW-CC-KV=V1&HW-CC-Date=20260427T234024Z&HW-CC-Expire=86400&HW-CC-Sign=7938D33552299269123FC196D2162883862AAFEAC9500C5BC921A0E291109D46)

## 添加事件

stepper分别添加finish，change，next，back，skip事件。

* 当change与next或back同时存在时，会先执行next或back事件再去执行change事件。
* 重新设置index属性值时要先清除index的值再重新设置，否则检测不到值的改变。

```
1. <!-- xxx.hml -->
2. <div class="container"  style="background-color:#F1F3F5;">
3. <div >
4. <stepper onfinish="stepperFinish" onchange="stepperChange" onnext="stepperNext" onback="stepperBack" onskip="stepperSkip" id="stepperId" index="{{index}}">
5. <stepper-item>
6. <text>stepper-item1</text>
7. <button value="skip" onclick="skipClick"></button>
8. </stepper-item>
9. <stepper-item>
10. <text>stepper-item2</text>
11. <button value="skip" onclick="skipClick"></button>
12. </stepper-item>
13. <stepper-item>
14. <text>stepper-item3</text>
15. </stepper-item>
16. </stepper>
17. </div>
18. </div>
```

```
1. /* xxx.css */
2. .doc-page {
3. width:100%;
4. height:100%;
5. flex-direction: column;
6. align-items: center;
7. justify-content: center;
8. }
9. stepper-item{
10. width: 100%;
11. flex-direction: column;
12. align-self: center;
13. justify-content: center;
14. }
15. text{
16. margin-top: 45%;
17. justify-content: center;
18. align-self: center;
19. margin-bottom: 50px;
20. }
21. button{
22. width: 80%;
23. height: 60px;
24. margin-top: 20px;
25. }
```

```
1. // xxx.js
2. import promptAction from '@ohos.promptAction';
3. export default {
4. data: {
5. index:0,
6. },
7. stepperSkip(){
8. this.index=2;
9. },
10. skipClick(){
11. this.$element('stepperId').setNextButtonStatus({status: 'skip', label: 'SKIP'});
12. },
13. stepperFinish(){
14. promptAction.showToast({
15. message: 'All Finished'
16. })
17. },
18. stepperChange(e){
19. console.info("stepperChange"+e.index)
20. promptAction.showToast({
21. // index表示当前步骤的序号
22. message: 'Previous step: '+e.prevIndex+"-------Current step:"+e.index
23. })
24. },
25. stepperNext(e){
26. console.info("stepperNext"+e.index)
27. promptAction.showToast({
28. // pendingIndex表示将要跳转的序号
29. message: 'Current step:'+e.index+"-------Next step:"+e.pendingIndex
30. })
31. var index = {pendingIndex:e.pendingIndex }
32. return index;
33. },
34. stepperBack(e){
35. console.info("stepperBack"+e.index)
36. var index = {pendingIndex: e.pendingIndex }
37. return index;
38. }
39. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/9sZnLetbTqygyp9bJkDyJQ/zh-cn_image_0000002552798444.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234024Z&HW-CC-Expire=86400&HW-CC-Sign=5E1A9F06D89CDC6FEDDCC33E11920E1DF7D8990D64A0BDA7167F9D9D34476EB1)
