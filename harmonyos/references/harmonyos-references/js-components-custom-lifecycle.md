---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-custom-lifecycle
title: 生命周期定义
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 自定义组件 > 生命周期定义
category: harmonyos-references
scraped_at: 2026-04-28T08:03:20+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c32b5ce8cda3dba2507e5b0791726a38f4b22bf5200d3b8c82322cb7731dbf67
---

说明

从API version 5 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

我们为自定义组件提供了一系列生命周期回调方法，便于开发者管理自定义组件的内部逻辑。生命周期主要包括：onInit，onAttached，onDetached，onLayoutReady，onDestroy，onShow和onHide。下面我们依次介绍一下各个生命周期回调的时机。

| 属性 | 类型 | 描述 | 触发时机 |
| --- | --- | --- | --- |
| onInit | Function | 初始化自定义组件 | 自定义组件初始化生命周期回调，当自定义组件创建时，触发该回调，主要用于自定义组件中必须使用的数据初始化，该回调只会触发一次调用。 |
| onAttached | Function | 自定义组件装载 | 自定义组件被创建后，加入到Page组件树时，触发该回调，该回调触发时，表示组件将被进行显示，该生命周期可用于初始化显示相关数据，通常用于加载图片资源、开始执行动画等场景。 |
| onLayoutReady | Function | 自定义组件布局完成 | 自定义组件插入Page组件树后，将会对自定义组件进行布局计算，调整其内容元素尺寸与位置，当布局计算结束后触发该回调。 |
| onDetached | Function | 自定义组件卸载 | 自定义组件卸载时，触发该回调，常用于停止动画或异步逻辑停止执行的场景。 |
| onDestroy | Function | 自定义组件销毁 | 自定义组件销毁时，触发该回调，常用于资源释放。 |
| onShow | Function | 自定义组件Page显示 | 自定义组件所在Page显示后，触发该回调。 |
| onHide | Function | 自定义组件Page隐藏 | 自定义组件所在Page隐藏后，触发该回调。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- comp.hml -->
2. <div class="item">
3. <text class="text-style">{{ value }}</text>
4. </div>
```

```
1. //comp.js
2. export default {
3. data: {
4. value: "组件创建"
5. },
6. onInit() {
7. console.info("组件创建")
8. },
9. onAttached() {
10. this.value = "组件挂载",
11. console.info("组件挂载")
12. },
13. onShow() {
14. console.info("Page显示")
15. },
16. onHide() {
17. console.info("Page隐藏")
18. }
19. }
```
