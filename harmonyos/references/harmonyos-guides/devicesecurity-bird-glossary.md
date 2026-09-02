---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-bird-glossary
title: 业务风险检测术语
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 业务风险检测 > 业务风险检测术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:30+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:d7fc076bafa82c22bade20e4a7c7bd8e0840481936f16bda8316419e49b1aa98
---

本术语收录Device Security Kit中BusinessRiskIntelligentDetection模块涉及的核心术语，按英文首字母排序。

## D

### Device Farm；设备农场

设备农场指黑灰产团伙利用集中控制的大量真实移动设备，常被用于实施刷量、薅羊毛等恶意欺诈活动。

## R

### Risk Factor；风险因子

导致设备产生风险的具体行为特征或运行状态，如接听涉诈电话、安装可疑应用等。

### Risk Score；风险分数

设备风险的综合评分，范围值[0, 100]，分数越高表示风险越大，帮助应用判断是否需要进行拦截操作。

### Risk Decision；风险决策结果

根据检测结果判定的设备风险结果，用于指导应用或业务执行相应的管控动作。

### Risk Tag；风险标签

用于标识设备具体风险类型的分类标识，例如钓鱼（phishing）、恶意软件（malware）、拦截（interdiction）、远控（control）等，用于区分不同的风险场景。
