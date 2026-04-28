---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-div
title: div
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 容器组件 > div
category: harmonyos-references
scraped_at: 2026-04-28T08:02:56+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:556f2f027d478e8bfd77efde300bd089af63a1214bd776bbb1ab7502e028f5fa
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

基础容器，用作页面结构的根节点或将内容进行分组。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

支持。

## 属性

PhonePC/2in1TabletTVWearable

支持[通用属性](js-components-common-attributes.md)。

## 样式

PhonePC/2in1TabletTVWearable

除支持组件[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| flex-direction | string | row | 否 | flex容器主轴方向。可选项有：  - column：垂直方向从上到下。  - row：水平方向从左到右。 |
| flex-wrap | string | nowrap | 否 | flex容器是单行还是多行显示，该值暂不支持动态修改。可选项有：  - nowrap：不换行，单行显示。  - wrap：换行，多行显示。 |
| justify-content | string | flex-start | 否 | flex容器当前行的主轴对齐格式。可选项有：  - flex-start：项目位于容器的开头。  - flex-end：项目位于容器的结尾。  - center：项目位于容器的中心。  - space-between：项目位于各行之间留有空白的容器内。  - space-around：项目位于各行之前、之间、之后都留有空白的容器内。  - space-evenly5+: 均匀排列每个元素，每个元素之间的间隔相等。 |
| align-items | string | stretch | 否 | flex容器当前行的交叉轴对齐格式，可选值为：  - stretch：弹性元素在交叉轴方向被拉伸到与容器相同的高度或宽度。  - flex-start：元素向交叉轴起点对齐。  - flex-end：元素向交叉轴终点对齐。  - center：元素在交叉轴居中。  - baseline：如Flex布局纵向排列，则该值与’flex-start‘等效。横向布局时，内容元素存在文本时按照文本基线对齐，否则底部对齐。 |
| align-content | string | flex-start | 否 | 交叉轴中有额外的空间时，多行内容对齐格式，可选值为：  - flex-start：所有行从交叉轴起点开始填充。第一行的交叉轴起点边和容器的交叉轴起点边对齐。接下来的每一行紧跟前一行。  - flex-end：所有行从交叉轴末尾开始填充。最后一行的交叉轴终点和容器的交叉轴终点对齐。同时所有后续行与前一个对齐。  - center：所有行朝向容器的中心填充。每行互相紧挨，相对于容器居中对齐。容器的交叉轴起点边和第一行的距离相等于容器的交叉轴终点边和最后一行的距离。  - space-between：所有行在容器中平均分布。相邻两行间距相等。容器的交叉轴起点边和终点边分别与第一行和最后一行的边对齐。  - space-around：所有行在容器中平均分布，相邻两行间距相等。容器的交叉轴起点边和终点边分别与第一行和最后一行的距离是相邻两行间距的一半。 |
| grid-template-[columns | rows] | string | 1行1列 | 否 | 用于设置当前网格布局行和列的数量，不设置时默认1行1列，仅当display为grid时生效。  示例：如设置grid-template-columns为：  - 50px 100px 60px：分三列，第一列50px，第二列100px，第三列60px；  - 1fr 1fr 2fr：分三列，将父组件允许的宽分为4等份，第一列占1份，第二列占一份，第三列占2份；  - 30% 20% 50%：分三列，将父组件允许的宽为基准，第一列占30%，第二列占20%，第三列占50%；  - repeat(2,100px)：分两列，第一列100px，第二列100px；  - repeat(auto-fill,100px)5+：按照每列100px的大小和交叉轴大小计算最大正整数重复次数，按照该重复次数布满交叉轴；  - auto 1fr 1fr：分三列，第一列自适应内部子组件所需宽度，剩余空间分为两等份，第二列占一份，第三列占一份。 |
| grid-[columns | rows]-gap | <length> | 0 | 否 | 用于设置行与行的间距或者列与列的间距，也可以支持通过grid-gap设置相同的行列间距，仅当display为grid时生效。 |
| grid-row-[start | end] | number | - | 否 | 用于设置当前元素在网格布局中的起止行号，仅当父组件display样式为grid时生效（仅div支持display样式设置为grid）。 |
| grid-column-[start | end] | number | - | 否 | 用于设置当前元素在网格布局中的起止列号，仅当父组件display样式为grid时生效（仅div支持display样式设置为grid）。 |
| grid-auto-flow5+ | string | - | 否 | 使用框架自动布局算法进行网格的布局，可选值为：  - row：逐行填充元素，如果行空间不够，则新增行；  - column：逐列填充元素，如果列空间不够，则新增列。 |
| overflow6+ | string | visible | 否 | 设置元素内容区超过元素本身大小时的表现形式。  - visible：多个子元素内容超过元素大小时，显示在元素外面；  - hidden：元素内容超过元素大小时，进行裁切显示；  - scroll：元素内容超过元素大小时，进行滚动显示并展示滚动条（当前只支持纵向）。  overflow: scroll样式需要元素设置固定的大小，默认滚动方向与容器方向一致。 |
| align-items6+ | string | - | 否 | 设置容器中元素交叉轴上的对齐方式：  - stretch：Flex容器内容在交叉轴方向被拉伸到与容器相同的高度或宽度；  - flex-start：Flex布局容器内元素向交叉轴起点对齐；  - flex-end：Flex布局容器内元素向交叉轴终点对齐；  - center：Flex布局容器内元素在交叉轴居中对齐；  - baseline：如Flex布局纵向排列，则该值与'flex-start'等效。横向布局时，内容元素存在文本时按照文本基线对齐，否则底部对齐。 |
| scrollbar-color6+ | <color> | - | 否 | 设置滚动条的颜色。 |
| scrollbar-width6+ | <length> | - | 否 | 设置滚动条的宽度。 |
| overscroll-effect6+ | string | - | 否 | 设置滚动边缘效果，可选值为：  - spring：弹性物理动效，滑动到边缘后可以根据初始速度或通过触摸事件继续滑动一段距离，松手后回弹。  - fade：渐隐物理动效，滑动到边缘后展示一个波浪形的渐隐，根据速度和滑动距离的变化渐隐也会发生一定的变化。  - none：滑动到边缘后无效果。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| reachstart6+ | - | 当页面滑动到最开始的点时触发的事件回调，需要设置flex-direction为row时才会触发。 |
| reachend6+ | - | 当页面滑动到最末尾的点时触发的事件回调，需要设置flex-direction为row时才会触发。 |
| reachtop6+ | - | 当页面滑动到最上部的点时触发的事件回调，需要设置flex-direction为column时才会触发。 |
| reachbottom6+ | - | 当页面滑动到最下部的点时触发的事件回调，需要设置flex-direction为column时才会触发。 |

## 方法

PhonePC/2in1TabletTVWearable

除支持[通用方法](js-components-common-methods.md)外，还支持如下方法：

| 名称 | 参数 | 返回值 | 描述 |
| --- | --- | --- | --- |
| getScrollOffset6+ | - | ScrollOffset | 获取元素内容的滚动偏移。  需要设置overflow样式为scroll。 |
| scrollBy6+ | ScrollParam | - | 指定元素内容的滚动偏移。  需要设置overflow样式为scroll。 |

**表1** ScrollOffset6+

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 在x轴方向的偏移，单位为px。 |
| y | number | 在y轴方向的偏移，单位为px。 |

**表2** ScrollParam6+

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| dx | number | 水平方向滑动的偏移量，单位px。 |
| dy | number | 垂直方向滑动的偏移量，单位px。 |
| smooth | boolean | 是否平滑处理。设置为true时表示平滑处理，设置为false时表示不平滑处理。 |

## 示例

PhonePC/2in1TabletTVWearable

1. Flex样式

   ```
   1. <!-- xxx.hml -->
   2. <div class="container">
   3. <div class="flex-box">
   4. <div class="flex-item color-primary"></div>
   5. <div class="flex-item color-warning"></div>
   6. <div class="flex-item color-success"></div>
   7. </div>
   8. </div>
   ```

   ```
   1. /* xxx.css */
   2. .container {
   3. flex-direction: column;
   4. justify-content: center;
   5. align-items: center;
   6. width: 454px;
   7. height: 454px;
   8. }
   9. .flex-box {
   10. justify-content: space-around;
   11. align-items: center;
   12. width: 400px;
   13. height: 140px;
   14. background-color: #ffffff;
   15. }
   16. .flex-item {
   17. width: 120px;
   18. height: 120px;
   19. border-radius: 16px;
   20. }
   21. .color-primary {
   22. background-color: #007dff;
   23. }
   24. .color-warning {
   25. background-color: #ff7500;
   26. }
   27. .color-success {
   28. background-color: #41ba41;
   29. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/vaPaLE_PRNCCCSO9dPYsyQ/zh-cn_image_0000002583480179.png?HW-CC-KV=V1&HW-CC-Date=20260428T000255Z&HW-CC-Expire=86400&HW-CC-Sign=AE3D131EE61036A4A5B90ADD5F9FB09FF200B2A3035E5523C7F498D44314D1E4)
2. Flex Wrap样式

   ```
   1. <!-- xxx.hml -->
   2. <div class="container">
   3. <div class="flex-box">
   4. <div class="flex-item color-primary"></div>
   5. <div class="flex-item color-warning"></div>
   6. <div class="flex-item color-success"></div>
   7. </div>
   8. </div>
   ```

   ```
   1. /* xxx.css */
   2. .container {
   3. flex-direction: column;
   4. justify-content: center;
   5. align-items: center;
   6. width: 454px;
   7. height: 454px;
   8. }
   9. .flex-box {
   10. justify-content: space-around;
   11. align-items: center;
   12. flex-wrap: wrap;
   13. width: 300px;
   14. height: 250px;
   15. background-color: #ffffff;
   16. }
   17. .flex-item {
   18. width: 120px;
   19. height: 120px;
   20. border-radius: 16px;
   21. }
   22. .color-primary {
   23. background-color: #007dff;
   24. }
   25. .color-warning {
   26. background-color: #ff7500;
   27. }
   28. .color-success {
   29. background-color: #41ba41;
   30. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/PNnNH-YUSk2Wh_9MVdEH-Q/zh-cn_image_0000002552800530.png?HW-CC-KV=V1&HW-CC-Date=20260428T000255Z&HW-CC-Expire=86400&HW-CC-Sign=BB889069B24F6D46A34651924B9C52C5FDC43258CBBE3F52C0D1DC13AADEB4E2)
3. Grid样式

   ```
   1. <!-- xxx.hml -->
   2. <div class="common grid-parent">
   3. <div class="grid-child grid-left-top"></div>
   4. <div class="grid-child grid-left-bottom"></div>
   5. <div class="grid-child grid-right-top"></div>
   6. <div class="grid-child grid-right-bottom"></div>
   7. </div>
   ```

   ```
   1. /* xxx.css */
   2. .common {
   3. width: 400px;
   4. height: 400px;
   5. background-color: #ffffff;
   6. align-items: center;
   7. justify-content: center;
   8. margin: 24px;
   9. }
   10. .grid-parent {
   11. display: grid;
   12. grid-template-columns: 35% 35%;
   13. grid-columns-gap: 24px;
   14. grid-rows-gap: 24px;
   15. grid-template-rows: 35% 35%;
   16. }
   17. .grid-child {
   18. width: 100%;
   19. height: 100%;
   20. border-radius: 8px;
   21. }
   22. .grid-left-top {
   23. grid-row-start: 0;
   24. grid-column-start: 0;
   25. grid-row-end: 0;
   26. grid-column-end: 0;
   27. background-color: #3f56ea;
   28. }
   29. .grid-left-bottom {
   30. grid-row-start: 1;
   31. grid-column-start: 0;
   32. grid-row-end: 1;
   33. grid-column-end: 0;
   34. background-color: #00aaee;
   35. }
   36. .grid-right-top {
   37. grid-row-start: 0;
   38. grid-column-start: 1;
   39. grid-row-end: 0;
   40. grid-column-end: 1;
   41. background-color: #00bfc9;
   42. }
   43. .grid-right-bottom {
   44. grid-row-start: 1;
   45. grid-column-start: 1;
   46. grid-row-end: 1;
   47. grid-column-end: 1;
   48. background-color: #47cc47;
   49. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/pjRD39q1Q7y1T28UwJptPA/zh-cn_image_0000002583440225.png?HW-CC-KV=V1&HW-CC-Date=20260428T000255Z&HW-CC-Expire=86400&HW-CC-Sign=86393C52E48181E726354193577CF5C9970462EDE2255954FB007158F5155115)
4. 拖拽7+

   ```
   1. <!-- xxx.hml -->
   2. <div class="container">
   3. <div class="content" ondragstart="dragstart" ondrag="drag" ondragend="dragend" style="position: absolute;left: {{left}};top: {{top}};">
   4. </div>
   5. </div>
   ```

   ```
   1. /* xxx.css */
   2. .container {
   3. flex-direction: column;
   4. width: 100%;
   5. height: 100%;
   6. }
   7. .content {
   8. width: 200px;
   9. height: 200px;
   10. background-color: red;
   11. }
   ```

   ```
   1. // xxx.js
   2. import promptAction from '@ohos.promptAction';
   3. export default {
   4. data:{
   5. left:0,
   6. top:0,
   7. },
   8. dragstart(e){
   9. promptAction.showToast({
   10. message: 'Start to be dragged'
   11. })
   12. },
   13. drag(e){
   14. this.left = e.globalX;
   15. this.top = e.globalY;
   16. },
   17. dragend(e){
   18. promptAction.showToast({
   19. message: 'End Drag'
   20. })
   21. }
   22. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/K29Zx3wdSnG2WimxIJ-dyQ/zh-cn_image_0000002552960180.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000255Z&HW-CC-Expire=86400&HW-CC-Sign=6182F869E932218990578F88F99EB54F21EB084FB422119D355629680AAEE1CD)

   ```
   1. <!-- xxx.hml -->
   2. <div class="container">
   3. <div class="content" ondrag="drag" style="position: absolute;left: {{left}};top: {{top}};"></div>
   4. <div style="width: 500px; height: 500px; background-color: yellow; position: fixed; left: 15%; top: 30%; opacity:0.3"
   5. ondragenter="dragenter" ondragover="dragover" ondragleave="dragleave" ondrop="drop">
   6. </div>
   7. </div>
   ```

   ```
   1. /* xxx.css */
   2. .container {
   3. flex-direction: column;
   4. width: 100%;
   5. position: relative;
   6. max-width: 100%;
   7. }
   8. .content{
   9. width: 200px;
   10. height: 200px;
   11. background-color: red;
   12. position: absolute;
   13. }
   ```

   ```
   1. // xxx.js
   2. import promptAction from '@ohos.promptAction';
   3. export default {
   4. data:{
   5. left:0,
   6. top:0,
   7. },
   8. drag(e){
   9. this.left = e.globalX;
   10. this.top = e.globalY;
   11. },
   12. dragenter(e){
   13. promptAction.showToast({
   14. message: 'enter'
   15. })
   16. },
   17. dragover(e){
   18. promptAction.showToast({
   19. message: 'over'
   20. })
   21. },
   22. dragleave(e){
   23. promptAction.showToast({
   24. message: 'leave'
   25. })
   26. },
   27. drop(e){
   28. promptAction.showToast({
   29. message: 'drop'
   30. })
   31. }
   32. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/SWfZiuvITrmoXEbg_gZuVw/zh-cn_image_0000002583480181.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000255Z&HW-CC-Expire=86400&HW-CC-Sign=6008773DBD6D2D64D13F7E37F9D75DB80F90521ADE90F15A51F08BF37652A744)
5. 手指捏合7+

   ```
   1. <!-- xxx.hml -->
   2. <div class="container">
   3. <div class="content" onpinchstart="pinchstart" onpinchend="pinchend" onpinchupdate="pinchupdate"
   4. onpinchcancel="pinchcancel">
   5. </div>
   6. </div>
   ```

   ```
   1. /* xxx.css */
   2. .container {
   3. flex-direction: column;
   4. justify-content: center;
   5. align-items: center;
   6. width: 454px;
   7. height: 454px;
   8. }
   9. .content {
   10. width: 400px;
   11. height: 400px;
   12. background-color: aqua;
   13. margin: 30px;
   14. }
   ```

   ```
   1. // xxx.js
   2. import promptAction from '@ohos.promptAction';
   3. export default {
   4. pinchstart(e){
   5. promptAction.showToast({
   6. message: 'pinchstart!!!'
   7. })
   8. },
   9. pinchupdate(e){
   10. promptAction.showToast({
   11. message: 'Two-finger pinch update'
   12. })
   13. },
   14. pinchend(e){
   15. promptAction.showToast({
   16. message: 'Finished with two fingers pinching'
   17. })
   18. },
   19. pinchcancel(e){
   20. promptAction.showToast({
   21. message: 'Finger pinching is interrupted'
   22. })
   23. }
   24. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/t37b2jDeRcW7zfv4L5dISA/zh-cn_image_0000002552800532.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000255Z&HW-CC-Expire=86400&HW-CC-Sign=3A50DFF9B69505662DF449542966652B016A0E8ED2BEB23535CA45E6A280F3B0)
