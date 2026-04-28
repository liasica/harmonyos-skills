---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-regression-test-6
title: 生成回归测试包时报错提示“测试包中需包含单个用例（json及对应的py文件），请校验setup-regression.py文件后重试”
breadcrumb: FAQ > DevEco Testing > 回归测试 > 生成回归测试包时报错提示“测试包中需包含单个用例（json及对应的py文件），请校验setup-regression.py文件后重试”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:39+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:ded253a1ea208a59db02bb624d97026ad1d45d49a6c73d5f088bcc79b0410c90
---

如果setup-regression.py文件构建的工程包中不含用例，会出现提示。回归测试要求工程包中必须包含单个用例，请检查setup-regression.py文件，并使用python setup-regression.py sdist --formats=zip进行本地验证，确保构建的工程包中仅包含单个用例。
