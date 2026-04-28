---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-custom-components
title: 自定义组件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 自定义组件
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a3262909b208746604ea8b8c5ef99a05efd83198a865c462fdb1c1dc68cfd80f
---

使用兼容JS的类Web开发范式的方舟开发框架支持自定义组件，用户可根据业务需求将已有的组件进行扩展，增加自定义的私有属性和事件，封装成新的组件，方便在工程中多次调用，提高页面布局代码的可读性。具体的封装方法示例如下：

* 构建自定义组件

  ```
  1. <!-- comp.hml -->
  2. <div class="item">
  3. <text class="title-style">{{title}}</text>
  4. <text class="text-style" onclick="childClicked" focusable="true">点击这里查看隐藏文本</text>
  5. <text class="text-style" if="{{showObj}}">hello world</text>
  6. </div>
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
  10. width: 100%;
  11. text-align: center;
  12. font-weight: 500;
  13. font-family: Courier;
  14. font-size: 36px;
  15. }
  16. .title-style {
  17. font-weight: 500;
  18. font-family: Courier;
  19. font-size: 50px;
  20. color: #483d8b;
  21. }
  ```

  ```
  1. // comp.js
  2. export default {
  3. props: {
  4. title: {
  5. default: 'title',
  6. },
  7. showObject: {},
  8. },
  9. data() {
  10. return {
  11. showObj: this.showObject,
  12. };
  13. },
  14. childClicked () {
  15. this.$emit('eventType1', {text: '收到子组件参数'});
  16. this.showObj = !this.showObj;
  17. },
  18. }
  ```
* 引入自定义组件

  ```
  1. <!-- xxx.hml -->
  2. <element name='comp' src='../../common/component/comp.hml'></element>
  3. <div class="container">
  4. <text>父组件：{{text}}</text>
  5. <comp title="自定义组件" show-object="{{isShow}}" @event-type1="textClicked"></comp>
  6. </div>
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
  3. data: {
  4. text: '开始',
  5. isShow: false,
  6. },
  7. textClicked (e) {
  8. this.text = e.detail.text;
  9. },
  10. }
  ```

本示例中父组件通过添加自定义属性向子组件传递了名称为title的参数，子组件在props中接收。同时子组件也通过事件绑定向上传递了参数text，接收时通过e.detail获取。要绑定子组件事件，父组件事件命名必须遵循事件绑定规则，详见[自定义组件的基本用法](../harmonyos-references/js-components-custom-basic-usage.md)。自定义组件效果如下图所示：

**图1** 自定义组件的效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/QQPr3GGMTBmdA-BmKjntQg/zh-cn_image_0000002552798502.png?HW-CC-KV=V1&HW-CC-Date=20260427T234034Z&HW-CC-Expire=86400&HW-CC-Sign=11F4392CCEA95A5E1EFE20D539726EAAF7EF59949881C72E67A7A59C14629192)
