---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-publish-test-1
title: 创建任务时提示“ai模型暂未启动，请稍后再试”
breadcrumb: FAQ > DevEco Testing > 上架预检 > 创建任务时提示“ai模型暂未启动，请稍后再试”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:33+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:13253a03c76581d19a8924722cd658a8adab354a01859443e6d4649a897bad53
---

1.首次运行DevEco Testing 客户端时，正在加载AI模型，请等待3~4分钟后重新创建任务。

2.若在等待3~4分钟后仍然报错“AI模型暂未启动，请稍后再试”，则请检查环境中是否有安装必要组件Microsoft Visual C++ Redistributable 2015及更高版本（仅Windows）

3.若排除了以上因素，请检查是否有进程正在占用40001端口，若40001端口被占用会导致AI模型启动失败。
