---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/servicecollaboration-richeditor-title
title: 跨设备互通（RichEditor控件）
breadcrumb: 指南 > 系统 > 网络 > Service Collaboration Kit（协同服务） > 跨设备互通（RichEditor控件）
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a63ecce9a48844c6eb6d66acf1a13616d98ea137f9ab8516c7f8db25f3f51048
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/2Y7H-g_DSYyntiO_UYqkKw/zh-cn_image_0000002589324807.png?HW-CC-KV=V1&HW-CC-Date=20260429T053302Z&HW-CC-Expire=86400&HW-CC-Sign=AC93C687F4EF8CBDCFFB58CF630F9B44D57303A0EA3FEAEC328947ED5E528AC5)

2.选择想要使用的能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/Y1l16z9kT6CSD7mhlsvGuQ/zh-cn_image_0000002589244745.png?HW-CC-KV=V1&HW-CC-Date=20260429T053302Z&HW-CC-Expire=86400&HW-CC-Sign=AB0F67B6EE14F80E00F92735EB0A5F58A722284DD3EC660BC9C37F0FA7621A6F)

3.等待对端设备拍照回传。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/v8uBfXT5T1qYY8qJOyvIHw/zh-cn_image_0000002558764940.png?HW-CC-KV=V1&HW-CC-Date=20260429T053302Z&HW-CC-Expire=86400&HW-CC-Sign=4506531A87078FC5233E0BD85E1B15902D05E852422EA7D8D7D5E915B00C1942)

4.图片回传后，在光标后面已嵌入一张图片。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/ul3ilMP6RcKGOgmE5LUekA/zh-cn_image_0000002558605284.png?HW-CC-KV=V1&HW-CC-Date=20260429T053302Z&HW-CC-Expire=86400&HW-CC-Sign=BFFD192A67C8D1097DE4108E044DEB2DE5328A595679FFE0D70A2563D4511137)

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
