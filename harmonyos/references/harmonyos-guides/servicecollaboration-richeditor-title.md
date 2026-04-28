---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/servicecollaboration-richeditor-title
title: 跨设备互通（RichEditor控件）
breadcrumb: 指南 > 系统 > 网络 > Service Collaboration Kit（协同服务） > 跨设备互通（RichEditor控件）
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c2c6005ec390a3ee1a0b10a069012de027321deb91aa1fcc917801c6fe9d87ee
---

富文本控件[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)已集成跨设备互通能力。在平板或2in1设备上，用户可通过其右键菜单调用手机的相机、扫描及图库（访问图片）功能。

## 场景介绍

您通过此能力实现跨设备交互，可以使用其他设备的相机、扫描和图库功能。

## 约束与限制

需同时满足以下条件，才能使用该功能：

* **设备限制**

  + 本端设备：HarmonyOS版本为HarmonyOS NEXT及以上的平板或2in1设备。
  + 远端设备：HarmonyOS版本为HarmonyOS NEXT及以上、具有相机能力的手机或平板设备。
* **使用限制**

  + 双端设备需要登录同一华为账号。
  + 跨设备互通API支持根据特定调用策略调用设备。调用策略：2in1设备可以调用平板和手机，平板可以调用手机，同类型设备不可调用。
  + 双端设备需要打开WLAN和蓝牙开关。

    条件允许时，建议双端设备接入同一个局域网，可提升唤醒相机的速度。

## 开发步骤

添加[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)富文本组件，即可在富文本组件中右键中选择其他设备进行导入，通过onWillChange属性对回传的照片进行处理。

```
1. @Entry
2. @Component
3. struct Index {
4. controller: RichEditorController = new RichEditorController()
5. options: RichEditorOptions = { controller: this.controller }

7. build() {
8. Column() {
9. Column() {
10. RichEditor(this.options)
11. .onWillChange((value: RichEditorChangeValue) => {
12. if (value?.replacedImageSpans[0]?.imageStyle?.objectFit != 0) {
13. return true;
14. }
15. for(let item of value.replacedImageSpans) {
16. this.controller.addImageSpan(item.valuePixelMap, {
17. imageStyle: {
18. size: ["500px", "500px"],
19. layoutStyle: {
20. borderRadius: '10px',
21. }
22. }
23. })
24. }
25. return false;
26. })
27. .borderWidth(1)
28. .borderColor(Color.Green)
29. .width("100%")
30. .height("100%")
31. }
32. .borderWidth(1)
33. .borderColor(Color.Red)
34. .width("100%")
35. .height("70%")
36. }
37. }
38. }
```

富文本组件使用流程如下：

1.在富文本区域右键。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/HKplkFEKTAaxEhYgYNEFJg/zh-cn_image_0000002552798790.png?HW-CC-KV=V1&HW-CC-Date=20260427T234410Z&HW-CC-Expire=86400&HW-CC-Sign=F52EF3BAD7E4528B5AA3B9E45C80C2732AAF9FD4C04B2635636125150FED1AA0)

2.选择想要使用的能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/MVNsx5ICRaO1l8iwcaia0w/zh-cn_image_0000002583438485.png?HW-CC-KV=V1&HW-CC-Date=20260427T234410Z&HW-CC-Expire=86400&HW-CC-Sign=BE5941C93137BE677EEA99E75487FCFE5A1A2A881F8F878C19DCD804F764C714)

3.等待对端设备拍照回传。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/3wmiVJUVTc-tXp6v2KYOqw/zh-cn_image_0000002552958440.png?HW-CC-KV=V1&HW-CC-Date=20260427T234410Z&HW-CC-Expire=86400&HW-CC-Sign=F965130193D6C930C8DACF15E79F60AC0E302A7FB839EA8D8C65A36403CF3171)

4.图片回传后，在光标后面已嵌入一张图片。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/I9Dm_6XgQQGhibPTGLqg7Q/zh-cn_image_0000002583478441.png?HW-CC-KV=V1&HW-CC-Date=20260427T234410Z&HW-CC-Expire=86400&HW-CC-Sign=0A7887066F816C0DC4A23E6A7CBA33C97436B6ECB8A07E5C01EF7D4D6FA9E04F)

## 关闭富文本跨设备互通能力

如果需要关闭富文本右键菜单跨设备互通能力，可通过editMenuOptions属性自定义菜单内容去除跨设备互通菜单项，示例如下：

```
1. @Entry
2. @Component
3. struct Index {
4. controller: RichEditorController = new RichEditorController()
5. options: RichEditorOptions = { controller: this.controller }

7. build() {
8. Column() {
9. Column() {
10. RichEditor(this.options)
11. .editMenuOptions({
12. onCreateMenu: (menuItems: Array<TextMenuItem>) => {
13. if (menuItems.length === 0) {
14. return menuItems;
15. }
16. let newMenuItems: TextMenuItem[] = [];
17. menuItems.forEach((item, index) => {
18. if(!item.id.equals(TextMenuItemId.COLLABORATION_SERVICE)) {
19. newMenuItems.push(item);
20. }
21. })
22. return newMenuItems;
23. },
24. onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
25. return false;
26. }
27. })
28. .borderWidth(1)
29. .borderColor(Color.Green)
30. .width("100%")
31. .height("100%")
32. }
33. .borderWidth(1)
34. .borderColor(Color.Red)
35. .width("100%")
36. .height("70%")
37. }
38. }
39. }
```
