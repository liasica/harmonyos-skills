---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-input
title: input
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > input
category: harmonyos-references
scraped_at: 2026-04-28T08:03:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8536def92ff8023e7b72d73053a54c95f994a80cba3ef18aeb50e510718bad14
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

交互式组件，包括单选框，多选框，按钮和单行文本输入框。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | string | text | 否 | input组件类型，可选值为text，email，date，time，number，password，button，checkbox，radio。  其中text，email，date，time，number，password这六种类型之间支持动态切换修改。  button，checkbox，radio不支持动态修改。可选值定义如下：  - button：定义可点击的按钮；  - checkbox：定义多选框；  - radio：定义单选按钮，允许在多个拥有相同name值的选项中选中其中一个；  - text：定义一个单行的文本字段；  - email：定义用于e-mail地址的字段；  - date：定义 date 控件（包括年、月、日，不包括时间）；  - time：定义用于输入时间的控件（不带时区）；  - number：定义用于输入数字的字段；  - password：定义密码字段（字段中的字符会被遮蔽）。 |
| checked | boolean | false | 否 | 当前组件是否选中，仅type为checkbox和radio生效。  true表示选中，false表示未选中。 |
| name | string | - | 否 | input组件的名称。  type为radio时，name为必填。 |
| value | string | - | 否 | input组件的value值，当类型为radio时必填且相同name值的选项该值唯一。 |
| placeholder | string | - | 否 | 设置提示文本的内容，仅在type为text|email|date|time|number|password时生效。 |
| maxlength | number | - | 否 | 输入框可输入的最多字符数量，不填表示不限制输入框中字符数量。 |
| enterkeytype | string | default | 否 | 不支持动态修改。  设置软键盘Enter按钮的类型，可选值为：  - default：默认  - next：下一项  - go：前往  - done：完成  - send：发送  - search：搜索  除“next”外，点击后会自动收起软键盘。 |
| headericon | string | - | 否 | 在文本输入前的图标资源路径，该图标不支持点击事件（button，checkbox和radio不生效），图标格式为jpg，png和svg。 |
| showcounter5+ | boolean | false | 否 | 文本输入框是否显示计数下标，需要配合maxlength一起使用。  true表示显示，false表示不显示。 |
| menuoptions5+ | Array<MenuOption> | - | 否 | 设置文本选择弹框点击更多按钮之后显示的菜单项。 |
| autofocus6+ | boolean | false | 否 | 是否自动获焦。  应用首页中设置不生效，可在onActive中延迟（100-500ms左右）调用focus方法实现输入框在首页中自动获焦。  true表示文本框自动获焦，false表示文本框不自动获焦。 |
| selectedstart6+ | number | -1 | 否 | 开始选择文本时初始选择位置。 |
| selectedend6+ | number | -1 | 否 | 开始选择文本时结尾选择位置。 |
| softkeyboardenabled6+ | boolean | true | 否 | 编辑时是否弹出系统软键盘。  true表示会弹出系统软键盘，false表示不会弹出。 |
| showpasswordicon6+ | boolean | true | 否 | 是否显示密码框末尾的图标（仅type为password时生效）。  true表示显示密码框末尾的图标，false表示不显示。 |

**表1** MenuOption5+

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| icon | string | 菜单选项中的图标路径。 |
| content | string | 菜单选项中的文本内容。 |

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-components-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | <color> | #e6000000 | 否 | 单行输入框或者按钮的文本颜色。 |
| font-size | <length> | 16px | 否 | 单行输入框或者按钮的文本尺寸。 |
| allow-scale | boolean | true | 否 | 单行输入框或者按钮的文本尺寸是否跟随系统设置字体缩放尺寸进行放大缩小。true表示跟随，false表示不跟随。  如果在config描述文件中针对ability配置了fontSize的config-changes标签，则应用不会重启而直接生效。 |
| placeholder-color | <color> | #99000000 | 否 | 单行输入框的提示文本的颜色，type为text | email | date | time | number | password时生效。 |
| font-weight | number | string | normal | 否 | 单行输入框或者按钮的字体粗细，见[text组件font-weight的样式属性](js-components-basic-text.md#样式)。 |
| caret-color6+ | <color> | - | 否 | 设置输入光标的颜色。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

* 当input类型为text、email、date、time、number、password时，支持如下事件：

  | 名称 | 参数 | 描述 |
  | --- | --- | --- |
  | change | {  value: inputValue  } | 输入框输入内容发生变化时触发该事件，返回用户当前输入值。  改变value属性值不会触发该回调。 |
  | enterkeyclick | {  value: enterKey  } | 软键盘enter键点击后触发该事件，返回enter按钮的类型，enterKey类型为number，可选值为：  - 2：设置enterkeytype属性为go时生效。  - 3：设置enterkeytype属性为search时生效。  - 4：设置enterkeytype属性为send时生效。  - 5：设置enterkeytype属性为next时生效。  - 6：不设置enterkeytype或者设置enterkeytype属性为default、done时生效。 |
  | translate5+ | {  value: selectedText  } | 设置此事件后，进行文本选择操作后文本选择弹窗会出现翻译按钮，点击翻译按钮之后，触发该回调，返回选中的文本内容。 |
  | share5+ | {  value: selectedText  } | 设置此事件后，进行文本选择操作后文本选择弹窗会出现分享按钮，点击分享按钮之后，触发该回调，返回选中的文本内容。 |
  | search5+ | {  value: selectedText  } | 设置此事件后，进行文本选择操作后文本选择弹窗会出现搜索按钮，点击搜索按钮之后，触发该回调，返回选中的文本内容。 |
  | optionselect5+ | {  index: optionIndex,  value: selectedText  } | 文本选择弹窗中设置menuoptions属性后，用户在文本选择操作后，点击菜单项后触发该回调，返回点击的菜单项序号和选中的文本内容。 |
  | selectchange6+ | {  start: number,  end: number  } | 文本选择变化时触发事件。 |
* 当input类型为checkbox、radio时，支持如下事件：

  | 名称 | 参数 | 描述 |
  | --- | --- | --- |
  | change | {  checked:true | false  } | checkbox多选框或radio单选框的checked状态发生变化时触发该事件。 |

## 方法

PhonePC/2in1TabletTVWearable

除支持[通用方法](js-components-common-methods.md)外，还支持如下方法：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| focus | {  focus: true|false  }，  focus不传值时默认为true。 | 使组件获得或者失去焦点，type为text | email | date | time | number | password时，可弹出或收起软键盘。 |
| showError | {  error: string  } | 展示输入错误提示，type为text | email | date | time | number | password时生效。 |
| delete6+ | - | type为text | email | date | time | number | password时，根据当前光标位置删除文本内容，如果当前输入组件没有光标，默认删除最后一个字符并展示光标。 |

## 示例

PhonePC/2in1TabletTVWearable

1. type为text

   ```
   1. <!-- xxx.hml -->
   2. <div class="content">
   3. <input id="input" class="input" type="text" value="" maxlength="20" enterkeytype="send"
   4. headericon="/common/search.svg" placeholder="Please input text" onchange="change"
   5. onenterkeyclick="enterkeyClick">
   6. </input>
   7. <input class="button" type="button" value="Submit" onclick="buttonClick" style="color: blue"></input>
   8. </div>
   ```

   ```
   1. /* xxx.css */
   2. .content {
   3. width: 100%;
   4. flex-direction: column;
   5. align-items: center;
   6. }
   7. .input {
   8. width: 60%;
   9. placeholder-color: gray;
   10. }
   11. .button {
   12. width: 60%;
   13. background-color: gray;
   14. margin-top: 20px;
   15. }
   ```

   ```
   1. // xxx.js
   2. import promptAction from '@ohos.promptAction';
   3. export default {
   4. change(e){
   5. promptAction.showToast({
   6. message: "value: " + e.value,
   7. duration: 3000,
   8. });
   9. },
   10. enterkeyClick(e){
   11. promptAction.showToast({
   12. message: "enterkey clicked",
   13. duration: 3000,
   14. });
   15. },
   16. buttonClick(e){
   17. this.$element("input").showError({
   18. error: 'error text'
   19. });
   20. },
   21. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/FWpkGo0hQMas5pWy38vf3Q/zh-cn_image_0000002583480191.png?HW-CC-KV=V1&HW-CC-Date=20260428T000300Z&HW-CC-Expire=86400&HW-CC-Sign=4FDC95FBA2122CABC9D6BDF37616507D274CD3DF59123BA6274EB0D8512F49D6)
2. type为button

   ```
   1. <!-- xxx.hml -->
   2. <div class="div-button">
   3. <input class="button" type="button" value="Input-Button"></input>
   4. </div>
   ```

   ```
   1. /* xxx.css */
   2. .div-button {
   3. flex-direction: column;
   4. align-items: center;
   5. }
   6. .button {
   7. margin-top: 30px;
   8. width: 280px;
   9. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/3FqJFyO4RBavzsFCeC_d-w/zh-cn_image_0000002552800542.png?HW-CC-KV=V1&HW-CC-Date=20260428T000300Z&HW-CC-Expire=86400&HW-CC-Sign=7765CFDA7BCC5F7F0E65F4939A786CFB4AFE0F77E72BA2A878312044F45FDDC7)
3. type为checkbox

   ```
   1. <!-- xxx.hml -->
   2. <div class="content">
   3. <input onchange="checkboxOnChange" checked="true" type="checkbox"></input>
   4. </div>
   ```

   ```
   1. /* xxx.css */
   2. .content{
   3. width: 100%;
   4. height: 200px;
   5. align-items: center;
   6. justify-content: center;
   7. }
   ```

   ```
   1. // xxx.js
   2. import promptAction from '@ohos.promptAction';
   3. export default {
   4. checkboxOnChange(e) {
   5. promptAction.showToast({
   6. message:'checked: ' + e.checked,
   7. duration: 3000,
   8. });
   9. }
   10. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/RqYowiKwRVWRfSSXAXzP6A/zh-cn_image_0000002583440237.png?HW-CC-KV=V1&HW-CC-Date=20260428T000300Z&HW-CC-Expire=86400&HW-CC-Sign=00C5744493D7458737F691EBC9A5013408F4F9CB358147BCDC737F2D88CC6A6A)
4. type为radio

   ```
   1. <!-- xxx.hml -->
   2. <div class="content">
   3. <input type="radio" checked='true' name="radioSample" value="radio1" onchange="onRadioChange('radio1')"></input>
   4. <input type="radio" checked='false' name="radioSample" value="radio2" onchange="onRadioChange('radio2')"></input>
   5. <input type="radio" checked='false' name="radioSample" value="radio3" onchange="onRadioChange('radio3')"></input>
   6. </div>
   ```

   ```
   1. /* xxx.css */
   2. .content{
   3. width: 100%;
   4. height: 200px;
   5. justify-content: center;
   6. align-items: center;
   7. }
   ```

   ```
   1. // xxx.js
   2. import promptAction from '@ohos.promptAction';
   3. export default {
   4. onRadioChange(inputValue, e) {
   5. if (inputValue === e.value) {
   6. promptAction.showToast({
   7. message: 'The chosen radio is ' + e.value,
   8. duration: 3000,
   9. });
   10. }
   11. }
   12. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/JFI1qe2kRyCPZEokxoNXhg/zh-cn_image_0000002552960192.png?HW-CC-KV=V1&HW-CC-Date=20260428T000300Z&HW-CC-Expire=86400&HW-CC-Sign=75C10BD640BA27923B93FFC00EB5C8CFC3B6E746B7FDD4F02C08C867622F8B5C)
