---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-88
title: aa命令常见问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > aa命令常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a29dcb9476f47d7d6f34b742945bd239d394eff381980c859cad5057530f66a1
---

## 问题现象

通过hdc shell aa start -U传递一个url参数时，应用实际接收到的url中缺失部分参数，如实际执行如下命令：

```shell
hdc shell aa start -U "www.example.com?yy=11&xx=2"
```

应用侧获取到的url缺失xx=2参数。

## 背景知识

[aa工具](../harmonyos-guides/aa-tool.md)即Ability assistant（Ability助手），是用于启动应用和启动测试用例的工具，为开发者提供基本的应用调试和测试能力，例如启动应用组件、强制停止进程、打印应用组件相关信息等。

## 问题定位

1、aa命令生效只是参数丢失，说明环境没有问题。

2、通过-U传递url参数时需要遵守url编码规范，特殊字符需要转义。

3、查看传递的url中包含'&'特殊字符，但没有进行转义，可以判断特殊字符存在问题，特殊字符转义后再进行测试参数正常，从而可以判断参数丢失就是特殊字符没有转义导致。

## 分析结论

使用-U命令传递的url中包含特殊字符'&'，特殊字符未做特殊处理，导致命令行解析异常，丢失了字符'&'后面的数据。

## 修改建议

1. 通过"\"转义特殊字符，如下所示：

hdc shell aa start -U "www.example.com?yy=11\&xx=2"。

2. aa命令整体添加双引号，同时给-U后面的url参数添加单引号，如下所示：

hdc shell "aa start -U 'www.example.com?yy=11&xx=2'"。
