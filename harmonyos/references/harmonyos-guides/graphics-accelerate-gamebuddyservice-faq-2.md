---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-gamebuddyservice-faq-2
title: 游戏截图回调没有返回的文件描述符如何处理
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏伴随服务 > 游戏截图回调没有返回的文件描述符如何处理
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e6d7ee0c5a3fe16edc7e5e9f13074e910112996e9ff386f9ac4578c28c79eaa6
---

可能原因及处理方式：

1. **游戏处于后台**：游戏截图功能在游戏处于后台时[onGameSnapshot](../harmonyos-references/graphics-accelerate-gamebuddyservice.md#ongamesnapshot)不会触发回调。请确保游戏在前台时再获取截图。
2. **服务未就绪**：游戏伴随服务可能尚未完成初始化，请等待1秒后再尝试获取截图。
