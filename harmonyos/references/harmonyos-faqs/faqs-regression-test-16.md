---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-regression-test-16
title: 测试结束后hilog日志一栏显示“-”
breadcrumb: FAQ > DevEco Testing > 回归测试 > 测试结束后hilog日志一栏显示“-”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4cda2c1c9c39b4c6825397319f28a00140d4a80dc98329d733e88795aeb3d6fd
---

用户手动停止任务后，Hypium进程会直接关闭，不会生成hilog。如果任务正常结束时缺少hilog，请确认test包中config文件夹下的user\_config.xml文件中的devicelog参数设置为ON。如果没有，请添加该参数，重新打包即可解决。
