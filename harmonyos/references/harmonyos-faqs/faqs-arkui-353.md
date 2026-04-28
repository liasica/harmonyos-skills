---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-353
title: Toggle组件响应点击后会立即渲染并回调，如何实现点击后延迟改变状态
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Toggle组件响应点击后会立即渲染并回调，如何实现点击后延迟改变状态
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2b4d6d51fc5edc542cb47bb3bf1b2474d7081f07b1c128dc97bf2a8078787b5f
---

使用hitTestBehavior和setTimeout解决。示例代码如下：

```
1. @Entry
2. @Component
3. struct ToggleDemo {
4. @State isDarkMode: boolean = false;
5. private timeoutID?: number;

7. aboutToDisappear(): void {
8. clearTimeout(this.timeoutID);
9. }

11. build() {
12. Column() {
13. Column() {
14. Toggle({ type: ToggleType.Switch, isOn: $$this.isDarkMode })
15. .onChange((isOn: boolean) => {
16. console.info('Toggle.onChange:isOn' + isOn);
17. this.isDarkMode = isOn;
18. this.getUIContext().getHostContext()!.getApplicationContext().setColorMode(this.isDarkMode ? 0 : 1);
19. })
20. }
21. // Set hitTestBehavior property to HitTestMode.Block to block Toggle component's event response.
22. .hitTestBehavior(HitTestMode.Block)
23. .onClick(() => {
24. this.timeoutID = setTimeout(() => {
25. this.isDarkMode = !this.isDarkMode;
26. }, 1500);
27. })
28. }
29. .width('100%')
30. .height('100%')
31. .padding(32)
32. }
33. }
```

[ToggleWithDelay.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ToggleWithDelay.ets#L21-L54)
