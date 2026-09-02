---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-kit-new-00003
title: Crypto Architecture Kit加解密多线程使用规格说明
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > Crypto Architecture Kit加解密多线程使用规格说明
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:65b49fa264fea95758bebcfae81425a0a545a710ed3ca37319a55b2660e1f084
---

## 问题现象

问题一：[Crypto Architecture Kit](../harmonyos-guides/crypto-architecture-kit-intro.md)文档中提到"不支持多线程并发操作"，具体是指什么范围？是App全局同时只能有一个线程执行解密操作，还是同一句柄下不能有多个线程同时执行解密操作？如果支持多句柄并行执行，执行线程是否有限制？可以在C语言创建的线程上执行加解密处理吗？除同一句柄的处理只能在一个线程中执行外，是否有其他地方需要负责互斥控制来确保线程安全？

问题二：ArkTS接口与C语言接口是否具备相同能力？

## 解决方案

问题一：同一加解密句柄（实例）不支持多线程并发调用，需保证同一句柄的操作在同一线程内串行执行。不同加解密句柄（实例）之间支持多线程并行执行，即不同线程可以分别使用各自独立的句柄同时进行加解密操作，执行线程没有额外限制。支持在C语言创建的线程上执行加解密处理，C接口可在Native层的C/C++线程中调用。除保证同一句柄的操作在同一线程内执行外，无需额外的全局互斥控制；不同句柄之间天然隔离，不需要互斥。

问题二：加解密相关操作都有对应的C接口，具体可参考[加解密开发指导](../harmonyos-guides/crypto-encrypt-decrypt-dev.md)。
