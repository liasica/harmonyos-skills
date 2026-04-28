---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avsession-recommendation
title: 播控推荐服务
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 播控推荐服务
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1eff7cd12def7ff3ec94b43ee47436d4125bd5e4d982b9b1c26354c7b5f582e8
---

## 播控特性简介

播控推荐服务致力于为用户提供更便捷的操作路径、更精准的内容推荐服务，帮助用户发现更感兴趣的内容，助力应用从系统级入口直达服务。

播控推荐服务基于用户使用音频类应用的习惯来分配播控推荐服务的资源位，保障用户常用的应用有更多的曝光。

同时，将基于用户的听歌偏好进行内容精准推荐，推荐的内容源需要三方应用通过云侧接口捐赠给播控中心。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/ikXYBDa2RwmtjHiDEDb-_g/zh-cn_image_0000002552958564.png?HW-CC-KV=V1&HW-CC-Date=20260427T234553Z&HW-CC-Expire=86400&HW-CC-Sign=371D2A8068E15532EF0B7DE3A2114681C32B292E2C16C166AAA56EFED21A98F1)

## 推荐资源位分配原则

播控中心推荐服务作为公共系统级入口，将依据统一的分配原则，来保证该栏目资源位分配公平，且符合用户的预期。

* 面向对象：在应用市场的分类显示为“影音娱乐-音乐”、“影音娱乐-电台”的两大类应用。
* 分配原则：基于用户最近30天使用应用的总时长分配，用户使用频次高、使用时间长的应用将获得较多的资源位。如某用户使用最多的应用是“应用A”，那么“应用A”获得的曝光资源位是最多的。

## 约束与限制

当前仅支持在中国大陆区域使用。

## 接入方式

播控推荐服务当前受限开放，在使用此功能前，您需要向华为运营人员发送申请邮件，华为运营人员将在5个工作日内为您安排对接人员。

* 邮箱地址：support@huawei.com
* 邮件标题：[申请使用播控推荐服务]-[公司名称]-[APP ID或APP包名]，APP ID或APP包名等查询方法可参见[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)。
