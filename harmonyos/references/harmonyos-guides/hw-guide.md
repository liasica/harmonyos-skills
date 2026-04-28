---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hw-guide
title: 硬件兼容性简介
breadcrumb: 指南 > NDK开发 > 硬件兼容性 > 硬件兼容性简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6168e358681f7c4617fc78c9a6bf8ecd217692821cdcb5a4790583ca11a71127
---

使用C/C++开发HarmonyOS应用原生库时，需要感知到硬件特性；HarmonyOS系统会运行在多种架构、多厂商的设备上，对于使用了HarmonyOS原生库的应用，如何保证其在不同设备上的兼容性以及体验的一致性是一个很大的挑战。

本章节将介绍HarmonyOS应用二进制接口（Application Binary Interface，简称ABI），定义了当前HarmonyOS系统支持的[ABI标准](ohos-abi.md)；同时也提供了如何使用[CPU扩展特性](cpu-features.md)的指导，方便应用在不破坏兼容性的基础上更好的利用CPU硬件特性。最后通过一些简单的示例演示如何更好的使用[ARM Neon特性](neon-guide.md)。
