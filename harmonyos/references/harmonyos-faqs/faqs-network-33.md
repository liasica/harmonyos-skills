---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-33
title: 网络波动情况下，底层系统是否会关闭Socket连接
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 网络波动情况下，底层系统是否会关闭Socket连接
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b89cd34b3f3597b06f45964c85a952732594b0babb559e4d94cd28c8e39fb62d
---

**问题现象**

在网络连接不稳定，频繁出现连接和断开的情况下，底层系统是否会关闭Socket连接？

**解决措施**

在网络不稳定（网络频繁断开和连接）时，底层系统会断开连接并关闭Socket端口，不会等待超时返回。
