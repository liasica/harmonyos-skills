---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-previewer-operating-4
title: 预览告警“There are properties not initialized”
breadcrumb: FAQ > DevEco Studio > 界面预览 > 预览告警“There are properties not initialized”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ee491566e45092bebb69d01f60c915df550e4dacc5476175c937a7ea409e72ed
---

**问题现象**

启动预览后，预览窗口白屏，并显示错误信息：“Preview failed. View details in the PreviewerLog window.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/2uvQOuqZSdKVwafCxMaejw/zh-cn_image_0000002194317976.png?HW-CC-KV=V1&HW-CC-Date=20260429T062017Z&HW-CC-Expire=86400&HW-CC-Sign=AD532E37755565C2FAC77693E03EC211BBD3EDB8FBA43148E9A974B95499DD75 "点击放大")

此时下方PreviewLog窗口出现告警信息：“There are properties not initialized.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/JxaYAw2LTOOUnSBG5WLkWQ/zh-cn_image_0000002194158356.png?HW-CC-KV=V1&HW-CC-Date=20260429T062017Z&HW-CC-Expire=86400&HW-CC-Sign=8214017C7830EA266DEE1610F55346CBB4BE8E0AC8C91F2A710D0F14CB023AEA)

**解决措施**

预览页面或组件中存在未初始化成功的成员变量，调用这些成员变量的属性或方法时会导致错误，预览界面显示空白。导致该问题的常见原因包括：

场景一：使用AppStorage等方法设置全局变量。

场景二：使用router.getParams()获取路由参数。

使用自定义的Mock。

1. 在 oh-package.json5 中添加以下依赖。

   ```
   1. "dependencies": {
   2. // The version number needs to be modified according to the relationship between hvigor and the SDK
   3. "@ohos/hamock": "1.0.0"
   4. }
   ```

   [oh-package.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/InterfacePreviewKit/entry/oh-package.json5#L11-L14)
2. 预览页面中导入mock依赖。

   ```
   1. import { MockSetup } from '@ohos/hamock';
   ```

   [GlobalData.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/InterfacePreviewKit/entry/src/main/ets/pages/GlobalData.ets#L22-L22)
3. 设置mock数据。

   ```
   1. @MockSetup
   2. mock(){
   3. this.fruit = new Fruit("apple");
   4. }
   ```

   [GlobalData.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/InterfacePreviewKit/entry/src/main/ets/pages/GlobalData.ets#L44-L47)

场景一：使用AppStorage等方法设置的全局变量，修改后的示例代码如下：

```
1. import { MockSetup } from '@ohos/hamock';

3. export default class Fruit{
4. public name: string;

6. getName(): string{
7. return this.name;
8. }

10. constructor(name: string) {
11. this.name = name;
12. }

14. }

16. @Entry
17. @Component
18. struct GlobalData {
19. @State fruit:Fruit = AppStorage.get("fruit") as Fruit;

21. @MockSetup
22. mock(){
23. this.fruit = new Fruit("apple");
24. }

26. build() {
27. Row() {
28. Column() {
29. Text(this.fruit.name)
30. .fontSize(50)
31. .fontWeight(FontWeight.Bold)
32. }
33. .width('100%')
34. }
35. .height('100%')
36. }
37. }
```

[GlobalData.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/InterfacePreviewKit/entry/src/main/ets/pages/GlobalData.ets#L21-L61)

场景二：使用路由参数，修改后的示例代码如下：

```
1. import { MockSetup } from '@ohos/hamock';

3. @Entry
4. @Component
5. struct Page {
6. @State params: object = this.getUIContext().getRouter().getParams();

8. @MockSetup
9. mock(){
10. this.params = [];
11. this.params["path"] = "path";
12. }

14. build() {
15. Row() {
16. Column() {
17. Text(this.params['path'])
18. .fontSize(50)
19. .fontWeight(FontWeight.Bold)
20. }
21. .width('100%')
22. }
23. .height('100%')
24. }
25. }
```

[InterfacePreviewNotInitialized.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/InterfacePreviewKit/entry/src/main/ets/pages/InterfacePreviewNotInitialized.ets#L21-L45)
