---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-368
title: 在display.on('change')监听回调中，无法使用Window实例获取更新后的窗口大小
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 在display.on('change')监听回调中，无法使用Window实例获取更新后的窗口大小
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:34+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6cd379dca47a258d6645d6fe2310637d2d1d9a58eade3536be61033bf9e0962e
---

**解决措施**

旋转涉及[@ohos.window](../harmonyos-references/js-apis-window.md)和[@ohos.display](../harmonyos-references/js-apis-display.md)两个模块，这两个模块处于不同进程。由于display模块的更新时间（直接宽高互换）早于window模块的更新时间（需等待ArkUI布局完成），因此在display触发变化时获取窗口信息会存在时序问题（窗口信息还未更新完成，此时使用Window实例获取的还是原来的宽高）。应用可以通过display.on('change')接口监听显示设备变化，在callback中通过Display实例获取屏幕的宽度、高度和方向等信息。

**错误示例**

```
1. // The display is updated first
2. display.on('change', async (data) => {
3. let newDisplay: display.Display = display.getDefaultDisplaySync();
4. console.info('Orientation: ' + newDisplay.orientation);
5. let windowClass: window.Window = await window.getLastWindow(this.context);
6. // After updating the window, the retrieved width and height are still the original ones.
7. let windowProperties = windowClass.getWindowProperties();
8. console.info('Width: ' + windowProperties.windowRect.width +
9. ', height: ' + windowProperties.windowRect.height);
10. // Please ensure that you have obtained the relevant Window instance, that is windowClass.
11. try {
12. windowClass.getWindowAvoidArea(window.AvoidAreaType.TYPE_CUTOUT);
13. } catch (err) {
14. hilog.error(DOMAIN, 'testTag', 'Failed. Cause: %{public}s', JSON.stringify(err));
15. }
16. });
```

**正确示例**

```
1. display.on('change', (data) => {
2. console.info('Succeeded in enabling the listener for display changes. Data: ' +
3. JSON.stringify(data));
4. let newDisplay: display.Display = display.getDefaultDisplaySync();
5. console.info('Orientation: ' + newDisplay.orientation + 'width: ' +
6. newDisplay.width + ', height: ' + newDisplay.height);
7. });
```

[EntryAbilityOnDisplay2.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityOnDisplay2.ets#L50-L56)

**参考链接**

[display.on('change')](../harmonyos-references/js-apis-display.md#displayonaddremovechange)
