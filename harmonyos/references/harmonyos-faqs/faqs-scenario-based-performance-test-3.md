---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-3
title: 执行python.exe -m pip install --upgrade pip命令更新pip库时报错ValueError: Unable to find resource t64.exe in package pip._vendor.distlib
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 执行python.exe -m pip install --upgrade pip命令更新pip库时报错ValueError: Unable to find resource t64.exe in package pip._vendor.distlib
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5ba58bf11ad30b7a508fef27a65b653e8a79e427651d6c2c8cb2e1401e6493eb
---

输入python -m pip uninstall pip setuptools卸载setuptools，输入pip install --upgrade setuptools重新安装 setuptools，然后重新执行python -m pip install --upgrade pip更新pip库。
