---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-iap-distribute-delivering
title: 发放数字商品权益
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 数字商品服务 > 应用内分发数字商品 > 发放数字商品权益
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0cc5c56faf1eb22e2a1730a3ad2fd88641dd0d4e23bd367bda69ab26bfe629ad
---

## 场景介绍

* 消耗型商品

  若应用提供消耗型商品，需要按照[确保权益发放处理](store-iap-distribute-delivering.md#消耗型非消耗型商品)消耗型商品的权益发放。
* 非消耗型商品

  若应用提供非消耗型商品，且为单机应用，则需要按照[单机应用权益发放](store-iap-distribute-delivering.md#单机应用权益发放)（非消耗型商品）处理非消耗型商品的权益发放。其他场景建议按照消耗型/非消耗型商品的[确保权益发放处理](store-iap-distribute-delivering.md#消耗型非消耗型商品)。
* 自动续期订阅商品

  若应用为非单机应用，则建议按照[确保权益发放处理](store-iap-distribute-delivering.md#自动续期订阅商品)自动续期订阅商品的权益发放。若为单机应用，则需要按照[单机应用权益发放](store-iap-distribute-delivering.md#单机应用权益发放)（自动续期订阅商品）处理自动续期订阅商品的权益发放。
* 非续期订阅商品

  若应用提供非续期订阅商品，需要按照[确保权益发放处理](store-iap-distribute-delivering.md#非续期订阅商品)非续期订阅商品的权益发放。

## 业务流程及开发步骤

### 消耗型/非消耗型商品

详细开发流程请参考[消耗型/非消耗型商品权益发放](iap-delivering-products.md)。

### 自动续期订阅商品

详细开发流程请参考[自动续期订阅商品权益发放](iap-delivering-subscriptions.md)。

### 非续期订阅商品

详细开发流程请参考[非续期订阅商品权益发放](iap-delivering-nonrenewable.md)。

## 单机应用权益发放

### 非消耗型商品

详细开发流程请参考[单机应用权益发放](iap-delivering-products.md#单机应用权益发放非消耗型商品)（非消耗型）。

### 自动续期订阅商品

详细开发流程请参考[单机应用权益发放](iap-delivering-subscriptions.md#对生效中的订阅发放权益)（自动续期订阅型）。
