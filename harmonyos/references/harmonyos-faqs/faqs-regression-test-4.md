---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-regression-test-4
title: 生成回归测试包时报错提示“测试套生成失败,请检查setup-regression.py文件后重试”
breadcrumb: FAQ > DevEco Testing > 回归测试 > 生成回归测试包时报错提示“测试套生成失败,请检查setup-regression.py文件后重试”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fbf9f7019e17056f17c95520fffa0af6db6787925a589ebe050a26a205d48707
---

请检测setup-regression.py文件的写法，使用python setup-regression.py sdist --formats=zip进行本地自验证。验证通过后，再利用插件出包。
