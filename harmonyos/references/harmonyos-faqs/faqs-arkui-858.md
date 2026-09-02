---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-858
title: 从系统卡片跳转app页面，重复多次进入导致需要多次才能返回
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 从系统卡片跳转app页面，重复多次进入导致需要多次才能返回
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:11d08033a6d62cafabfc9544701b98fbd57af4513f5cdc79ffb54469937c20fc
---

## 问题现象

从系统卡片进入app页面，多次进入同一个页面时，返回时需要返回很多次。

## 背景知识

ArkTS的路由功能可以通过[router](../harmonyos-references/js-apis-router.md)或[Navigation](../harmonyos-guides/arkts-navigation-navigation.md)实现。Navigation有丰富的[路由操作](../harmonyos-guides/arkts-navigation-jump.md#路由操作)，包括页面跳转、页面返回、页面替换、页面删除、参数获取、路由拦截等功能，推荐使用Navigation管理页面。

## 问题定位

* 业务上确认是否固定热启动的页面返回到首页。
* 检查热启动跳转代码是否重复添加页面的路由信息入栈且未清除，以下是未清除重复路由的示例代码：

  ```ts
  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // 通过want.parameters获取参数
    const targetPage = want.parameters?.targetPage;
    console.info(`onNewWant Received parameter: ${targetPage}`)
    // 根据参数执行逻辑（例如跳转页面）
    if (targetPage === 'test1') {
      this.pathStack.pushPath({ name: targetPage.toString() });
    }
  }
  ```

## 分析结论

通过热启动跳转页面，每进入一次push一次路由，未去重。

## 修改建议

应用在接收到对应的router跳转事件后，处理跳转的时候需要判断跳转的页面是否已经在路由栈的栈顶，如果在的话需要替换当前的页面，如果不在的话，重新push这个页面到栈。参考[多次点击服务卡片拉起应用指定页面后，该页面在路由栈内存在多个，导致返回上一页面需要多次返回操作](../harmonyos-guides/arkts-ui-music-service-form.md#多次点击服务卡片拉起应用指定页面后该页面在路由栈内存在多个导致返回上一面需要多次返回操作)。
