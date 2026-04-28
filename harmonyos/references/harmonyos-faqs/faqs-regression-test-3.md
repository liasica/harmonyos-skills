---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-regression-test-3
title: 生成回归测试包时，如果出现“setup-regression.py解析失败，请检查setup-regression.py的写法是否规范”的错误提示，应如何处理
breadcrumb: FAQ > DevEco Testing > 回归测试 > 生成回归测试包时，如果出现“setup-regression.py解析失败，请检查setup-regression.py的写法是否规范”的错误提示，应如何处理
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0b104696e30b51e0efe16a286ae3ac5a9eb8571bb52f49cfe105e2c8a4258dc9
---

若setup-regression.py编写不规范，会出现提示。编写setup-regression.py文件时，需去除注释，参数以“参数名=参数值”的形式设置。

```
1. # setup-regression.py example of file writing
2. from setuptools import setup
3. setup(
4. name='hypiumTest',
5. version='1.0.0.0',
6. author='xxx',
7. # py_modules Specify the hypium use case py file that needs to be packaged
8. py_modules=['testcases.Example'],
9. include_package_data=True
10. )
```

[setup-regression.py](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ScanKit/entry/src/main/ets/pages/setup-regression.py#L6-L15)
