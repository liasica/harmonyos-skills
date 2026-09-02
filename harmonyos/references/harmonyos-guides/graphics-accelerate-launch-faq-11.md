---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-11
title: 团结引擎1.8.1～1.9.0版本在Tablet设备上调用秒启接口异常应该如何解决
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏启动加速服务 > 团结引擎1.8.1～1.9.0版本在Tablet设备上调用秒启接口异常应该如何解决
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:51+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:73fbea3b3dd3b9e51a08dc77a2eb74d2e850be52406738c207b227794a748191
---

**现象描述**

在Tablet设备上，使用团结引擎1.8.1～1.9.0版本开发的应用，在[onWindowStageWillDestroy](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagewilldestroy12)生命周期中调用this.tuanjiePlayer.onWindowStageWillDestroy时，会因接口内部未被捕获的异常而导致应用崩溃。

**原因分析**

团结引擎1.8.1～1.9.0版本将秒级启动能力集成到了引擎内部，在Tablet设备上，this.tuanjiePlayer.onWindowStageWillDestroy接口内部存在未被捕获的异常，属于该版本在特定设备上的缺陷。

**处理步骤**

在调用时添加try-catch进行异常保护。

```typescript
onWindowStageWillDestroy(): void {
  try {
    this.tuanjiePlayer.onWindowStageWillDestroy();
  } catch (error) {
    console.error(`tuanjiePlayer onWindowStageWillDestroy error: ${error}`);
  }
}
```

**说明** 

该问题为引擎在Tablet设备上的缺陷，建议升级至团结引擎1.9.1或更高版本以获得根本修复。若暂时无法升级，请务必添加上述异常保护。
