---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-richtext
title: richtext
category: harmonyos-references
scraped_at: 2026-04-28T08:03:04+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5a1035f5eca9bc493b9d03ad4217be8d8fba64a15ce71e800934f724ef2f3560
---

说明

* 该组件从API version 6开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 富文本内容需要写在元素标签内。

富文本组件，用于展示富文本信息。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 属性

PhonePC/2in1TabletTVWearable

仅支持[通用属性](js-components-common-attributes.md)中的id、style和class属性。

## 样式

PhonePC/2in1TabletTVWearable

仅支持[通用样式](js-components-common-styles.md)中的display和visibility样式。

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](js-components-common-events.md)外，还支持如下事件：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| start | - | 开始加载时触发。 |
| complete | - | 加载完成时触发。 |

说明

* 不支持focus、blur、key事件。
* 不支持无障碍事件。
* 包含richtext的页面返回时richtext显示区域不会跟随页面的转场动效。
* richtext内容不建议超过一个屏幕高度，超出部分不会显示。
* 不支持设置宽度，默认撑开全屏。

## 方法

PhonePC/2in1TabletTVWearable

不支持。

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div style="flex-direction: column;width: 100%;">
3. <richtext @start="onLoadStart" @complete="onLoadEnd">{{content}}</richtext>
4. </div>
```

```
1. // xxx.js
2. export default {
3. data: {
4. content: `
5. <div class="flex-direction: column; background-color: #ffffff; padding: 30px; margin-bottom: 30px;">
6. <style>h1{color: yellow;}</style>
7. <p class="item-title">h1</p>
8. <h1>文本测试(h1测试)</h1>
9. <p class="item-title">h2</p>
10. <h2>文本测试(h2测试)</h2>
11. </div>
12. `,
13. },
14. onLoadStart() {
15. console.error("start load rich text")
16. },
17. onLoadEnd() {
18. console.error("end load rich text")
19. }
20. }
```
