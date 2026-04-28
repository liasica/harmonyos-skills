---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-faq-5
title: 关于实况窗数量约束的问题
breadcrumb: 指南 > 应用服务 > Live View Kit（实况窗服务） > Live View Kit常见问题 > 关于实况窗数量约束的问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4350064839049d4d43722fb8d532108b10b8a35c53dbb5992fe802413e0202cd
---

1. 创建实况时的id约束：可以一次性创建多个实况窗，需要保证其id唯一，同一id在同一时刻只能创建一个实况窗。（当该id的实况窗结束后，Live View Kit可以通过该id再次创建，Push Kit在12小时内该id无法再次创建。）
2. 展示实况窗时的交互约束：在通知中心通过滑动最多展示24条实况窗。通过点击胶囊弹出的实况窗列表，无法滑动，只能展示5条实况窗。
