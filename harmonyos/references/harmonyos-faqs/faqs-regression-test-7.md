---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-regression-test-7
title: 生成回归测试包时报错提示“xxx.json中py_file字段为空，请检查该文件是否填写正确!”
breadcrumb: FAQ > DevEco Testing > 回归测试 > 生成回归测试包时报错提示“xxx.json中py_file字段为空，请检查该文件是否填写正确!”
category: harmonyos-faqs
scraped_at: 2026-11-04T08:40:46+08:00
doc_updated_at: 2026-11-03
content_hash: sha256:2f1d3a3de93e94fd5256d4fc5dfab096662da370cd249efdee633bdc78ae32d3
---

当用户在setup-regression.py文件中指定打包的json文件中未声明对应的用例py文件，则会出现该提示，请参考[应用UI测试（基于python）-测试脚本开发快速入门](../doccenter-testing/hypium-python-guidelines.md#section589563925210) 修改用例写法。
