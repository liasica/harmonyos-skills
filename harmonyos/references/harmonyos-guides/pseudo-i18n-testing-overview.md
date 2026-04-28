---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pseudo-i18n-testing-overview
title: 伪本地化测试概述
breadcrumb: 指南 > 应用框架 > Localization Kit（本地化开发服务） > 本地化测试 > 伪本地化测试 > 伪本地化测试概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:48+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:433d06e1d916310648a2b3cff8ef325de5d4fef0e728c4eed45336873931571d
---

伪本地化（pseudo-localization）又称伪翻译，是在正式的本地化之前，通过模拟本地化过程帮助发现潜在问题，避免功能缺陷。这是软件测试中用来测试软件是否符合本地化与国际化的方法之一。伪翻译不是将软件的文本翻译成外语，而是在源语言软件的基础上，按规则将需要本地化的文本使用本地化文字替换，模拟本地化过程。

对于新开发的软件或界面变更较大的软件，若等待翻译完成后再进行界面测试，可能会延误整个交付周期。此外，软件开发初期，界面随时可能调整，通常会在产品成熟后再开始界面翻译和翻译测试，这可能会导致产品发布延误。采用伪本地化测试可以避免延误开发进程，确保产品正常发布。

伪本地化测试包括[翻译伪本地化](pseudo-i18n-testing-translation.md)和[界面镜像伪本地化](pseudo-i18n-testing-mirror.md)。
