---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-cursorcontroller
title: Class (CursorController)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (CursorController)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:104f705e6801f308decf2e67037933e3749a3d45157262fa52178dcc3b53c305
---

提供光标样式设置的能力。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 12开始支持。
* 以下API需先使用UIContext中的[getCursorController()](arkts-apis-uicontext-uicontext.md#getcursorcontroller12)方法获取CursorController实例，再通过此实例调用对应方法。

## restoreDefault12+

PhonePC/2in1TabletTVWearable

restoreDefault(): void

恢复默认的光标样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

当光标移出绿框时，通过CursorController的restoreDefault方法恢复默认光标样式。

```
1. import { pointer } from '@kit.InputKit';
2. import { UIContext, CursorController } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct CursorControlExample {
7. @State text: string = '';
8. cursorCustom: CursorController = this.getUIContext().getCursorController();

10. build() {
11. Column() {
12. Row().height(200).width(200).backgroundColor(Color.Green).position({x: 150 ,y:70})
13. .onHover((flag) => {
14. if (flag) {
15. this.cursorCustom.setCursor(pointer.PointerStyle.EAST);
16. } else {
17. console.info("restoreDefault");
18. this.cursorCustom.restoreDefault();
19. }
20. })
21. }.width('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/3D8xDinbSka0B0018-ws0Q/zh-cn_image_0000002583479407.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000020Z&HW-CC-Expire=86400&HW-CC-Sign=DDADF75D9B2988D5BC3A16B22501604706CF36F6231DF6763B7732C54956AFFC)

## setCursor12+

PhonePC/2in1TabletTVWearable

setCursor(value: PointerStyle): void

更改当前的鼠标光标样式。

说明

该接口调用后不会立即生效，而是在下一帧改变鼠标光标样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PointerStyle](arkts-apis-uicontext-t.md#pointerstyle12) | 是 | 光标样式。 |

**示例：**

当光标进入蓝框时，通过CursorController的setCursor方法修改光标样式为PointerStyle.WEST。

```
1. import { pointer } from '@kit.InputKit';
2. import { UIContext, CursorController } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct CursorControlExample {
7. @State text: string = '';
8. cursorCustom: CursorController = this.getUIContext().getCursorController();

10. build() {
11. Column() {
12. Row().height(200).width(200).backgroundColor(Color.Blue).position({x: 100 ,y:70})
13. .onHover((flag) => {
14. if (flag) {
15. this.cursorCustom.setCursor(pointer.PointerStyle.WEST);
16. } else {
17. this.cursorCustom.restoreDefault();
18. }
19. })
20. }.width('100%')
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/oW38jslURGqRMcR8Ryok2g/zh-cn_image_0000002552799758.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000020Z&HW-CC-Expire=86400&HW-CC-Sign=8AC21D0AA00C3D98C87B292DD61C646CF70499F4AF0C726869C50533C674D2F1)
