---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-2
title: rcp请求是否有数据大小限制
breadcrumb: FAQ > 系统开发 > 网络 > 远场通信（Remote Communication） > rcp请求是否有数据大小限制
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:17+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:9fdd8174bf1b80f2a83314af1cf5f1eb5fbaee663eb773b2e34d868781c8c6cc
---

rcp请求默认情况下，[response](../harmonyos-references/remote-communication-rcp.md#response)响应中最大数据量为50MB，超过此限制建议通过[HttpEventsHandler](../harmonyos-references/remote-communication-rcp.md#httpeventshandler)的[onDataReceive](../harmonyos-references/remote-communication-rcp.md#section9264115918536)实现流式数据接收。

**参考链接**

[response](../harmonyos-references/remote-communication-rcp.md#response)

[HttpEventsHandler](../harmonyos-references/remote-communication-rcp.md#httpeventshandler)

[onDataReceive](../harmonyos-references/remote-communication-rcp.md#ondatareceive)
