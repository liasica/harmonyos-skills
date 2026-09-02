---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-2
title: rcp请求是否有数据大小限制
breadcrumb: FAQ > 系统开发 > 网络 > 远场通信（Remote Communication） > rcp请求是否有数据大小限制
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:1add2c3a535b02f8378e647161dc0c4d3478ada37ef0a317894eb7bfb08ae327
---

rcp请求默认情况下，[response](../harmonyos-references/remote-communication-rcp.md#response)响应中最大数据量为50MB，超过此限制建议通过[HttpEventsHandler](../harmonyos-references/remote-communication-rcp.md#httpeventshandler)的[onDataReceive](../harmonyos-references/remote-communication-rcp.md#ondatareceive)实现流式数据接收。

**参考链接**

[response](../harmonyos-references/remote-communication-rcp.md#response)

[HttpEventsHandler](../harmonyos-references/remote-communication-rcp.md#httpeventshandler)

[onDataReceive](../harmonyos-references/remote-communication-rcp.md#ondatareceive)
