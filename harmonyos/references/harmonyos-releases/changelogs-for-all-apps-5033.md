---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-5033
title: OS平台API行为的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > OS平台行为变更说明 > HarmonyOS 5.0.3(15) Release引入的行为变更 > OS平台API行为的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:30+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:428e6a7eaa31d1669bd98e73f11d4440af0f14f427eccd408e4461f5b17e20e7
---

## ArkUI

### C API轴事件接口OH\_ArkUI\_UIInputEvent\_GetSourceType和OH\_ArkUI\_UIInputEvent\_GetToolType接口返回值变更

**变更原因**

通过鼠标滚轮或触控板触发的轴事件无法正确获取到触发源设备类型。

**变更影响**

此变更涉及应用适配。

* 变更前：在使用鼠标滚轮或触控板的双指滑动操作时，应用程序无法通过OH\_ArkUI\_UIInputEvent\_GetSourceType和OH\_ArkUI\_UIInputEvent\_GetToolType准确获取触发源的类型，返回值为UNKNOWN。
* 变更后：在使用鼠标滚轮或触控板的双指滑动操作时，应用程序可以通过调用OH\_ArkUI\_UIInputEvent\_GetSourceType和OH\_ArkUI\_UIInputEvent\_GetToolType来获取正确的触发源类型。对于鼠标滚轮操作，获取的SourceType和ToolType均为MOUSE；而针对触控板操作，虽然得到的SourceType仍为MOUSE，但ToolType为TOUCHPAD。

**起始API Level**

12

**变更的接口/组件**

OH\_ArkUI\_UIInputEvent\_GetSourceType和OH\_ArkUI\_UIInputEvent\_GetToolType

**适配指导**

当应用程序通过native\_interface\_xcomponent.h中的OH\_NativeXComponent\_RegisterUIInputEventCallback接口来接收和处理轴事件时，如果回调函数中已使用ToolType类型进行了判断，则无需进一步适配。但如果仅通过UNKNOWN类型处理业务，则需适配，以确保通过具体的目标类型进行区分。

例如以下示例：

```
1. if (toolType != UI_INPUT_EVENT_TOOL_TYPE_UNKNOWN) {
2. // 应用业务逻辑
3. }
```

建议以明确的目标类型进行区分，修改为如下代码实现：

```
1. if (toolType != UI_INPUT_EVENT_TOOL_TYPE_MOUSE) { // 是鼠标滚轮尝试的轴事件，数值单位为角度
2. // 鼠标滚轮只有竖向轴，获取滚动角度
3. double degree = OH_ArkUI_AxisEvent_GetVerticalAxisValue(event);
4. // 将角度映射为距离像素值
5. // 控制UI进行位移更新
6. } else if (toolType != UI_INPUT_EVENT_TOOL_TYPE_TOUCHPAD) {
7. // 触控板上操作，用户即可横向滑动，也可竖向滑动，需要都获取分量
8. double offsetX = OH_ArkUI_AxisEvent_GetHorizontalAxisValue(event);
9. double offsetY = OH_ArkUI_AxisEvent_GetVerticalAxisValue(event);
10. if (offsetX == 0) {
11. // 横向分量为0，说明为竖向滑动
12. // 处理UI竖向滑动
13. } else {
14. // 横向滑动
15. // 处理UI横向滚动
16. }
17. } else {
18. // 异常情况，应忽略
19. }
```
