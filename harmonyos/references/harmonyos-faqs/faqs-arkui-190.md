---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-190
title: 如何获取窗口的宽高信息
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何获取窗口的宽高信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:48+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:285441202654f6c12c709576781c5823ad9a075219d8491ed91067c6df335e62
---

获取指定窗口对象Window后，在该对象上使用[getWindowProperties()](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)获取窗口各个属性，在属性windowRect中获取窗口宽高信息。如果要在页面中获取窗口宽高信息，需要注意获取的正确时机。页面生命周期[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)阶段，不代表此时窗口可见，仅代表当前组件已创建，此时获取到的窗口尺寸信息（windowRect）可能有误。建议在页面生命周期[onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)阶段获取，该阶段会在窗口可见后调用，此时可以拿到窗口正确的宽高信息。参考代码如下：

```
1. //If you need to get the window width and height information in the page, it is recommended to put the following code in the onPageShow stage of the page life cycle, rather than calling it in the aboutToAppear stage of the page life cycle
2. let windowClass: window.Window | undefined = undefined;
3. try {
4. let promise = window.getLastWindow(this.context);
5. promise.then((data) => {
6. //Get window object
7. windowClass = data;
8. try {
9. //Get window properties
10. let properties = windowClass.getWindowProperties();
11. let rect = properties.windowRect;
12. //rect.width: Window Width, rect.height: Window height
13. } catch (exception) {
14. console.error('Failed to obtain the window properties. Cause: ' + JSON.stringify(exception));
15. }
16. console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
17. }).catch((err: BusinessError) => {
18. console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(err));
19. });
20. } catch (exception) {
21. console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(exception));
22. }
```

[EntryAbilityForWindow.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityForWindow.ets#L39-L60)
