---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-201
title: 如何解决window创建的模态窗口默认焦点不在界面上，导致不响应返回事件的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何解决window创建的模态窗口默认焦点不在界面上，导致不响应返回事件的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:141976620e80433fef7da0f790b80209b3a561c8929cf7492a869685da70d8b7
---

**问题现象**

通过window创建的窗口默认焦点不在界面上，导致不响应返回事件。

**解决措施**

模态窗口是给系统权限申请弹窗用的，默认不能响应back手势事件。使用setDialogBackGestureEnabled接口设置模态窗口是否响应手势返回事件，设置为true时，模态窗口可响应onBackPress回调。参考代码如下：

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

7. export default class EntryAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. console.info('onWindowStageCreate');
10. let windowClass: window.Window | undefined = undefined;
11. let config: window.Configuration = {
12. name: "test",
13. windowType: window.WindowType.TYPE_DIALOG,
14. ctx: this.context
15. };
16. try {
17. window.createWindow(config, (err: BusinessError, data) => {
18. const errCode: number = err.code;
19. if (errCode) {
20. console.error(`Failed to create the window. Cause code: ${err.code}, message: ${err.message}`);
21. return;
22. }
23. windowClass = data;
24. windowClass.setUIContent('pages/Index');
25. let enabled = true;
26. // Enable response to back gesture event
27. let promise = windowClass.setDialogBackGestureEnabled(enabled);
28. promise.then(() => {
29. console.info('Succeeded in setting dialog window to respond back gesture.');
30. }).catch((err: BusinessError) => {
31. console.error(`Failed to set dialog window to respond back gesture. Cause code: ${err.code}, message: ${err.message}`);
32. });
33. });
34. } catch (exception) {
35. console.error(`Failed to create the window. Cause code: ${exception.code}, message: ${exception.message}`);
36. }
37. }
38. }
```

[EntryAbilityFocusUnresponsive.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityFocusUnresponsive.ets#L21-L58)

**参考链接**

[setDialogBackGestureEnabled](../harmonyos-references/arkts-apis-window-window.md#setdialogbackgestureenabled12)
