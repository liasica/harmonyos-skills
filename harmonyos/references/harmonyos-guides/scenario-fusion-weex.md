---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-weex
title: Weex框架+H5接入智能填充
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 智能填充服务 > 三方框架+H5接入智能填充 > Weex框架+H5接入智能填充
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:19+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:ecb4658bf42c466543be90451866a38bb6370125ddaebc4d75a0347eee28cc40
---

**说明** 

目前仅支持已适配HarmonyOS的三方框架应用使用。

## 前提条件

* 设备智能填充开关必须处于打开状态，请前往“设置 > 隐私和安全 > 智能填充”页面开启开关。
* 设备已连接互联网并且登录华为账号。
* 该应用需已接入[智能填充服务](scenario-fusion-introduction-to-smart-fill.md#申请接入智能填充服务)。

## 开发准备

配置Weex已适配HarmonyOS的工程。

## 效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/1bF5cru5SNK-ap__-8zfPQ/zh-cn_image_0000002742004379.png)

## 示例代码

在Weex的form表单中给input输入框（form表单的子节点）配置[autocomplete](scenario-fusion-mappingrelationship.md#h5-autocomplete和harmonyos的contenttype的映射关系)属性以实现智能填充，代码中action需要配置表单提交接口链接，当form表单提交后，页面导航发生变化时，满足历史表单输入保存的条件时会触发对应弹窗。代码如下：

```vue
<template>
  <div class="text-auto-fill">
    <text class="header">Weex H5表单验证</text>
    <form action="">
      <div class="form-item">
        <label for="nickname" class="label">昵称</label>
        <div class="input">
          <input id="nickname" type="text" class="form-value" name="nickname" autocomplete="nickname">
        </div>
      </div>
      <div class="form-item">
        <label for="name" class="label">姓名</label>
        <div class="input">
          <input id="name" type="text" class="form-value" name="name" autocomplete="name">
        </div>
      </div>
      <div class="form-item">
        <label for="tel-national" class="label">手机号</label>
        <div class="input">
          <input id="tel-national" type="number" class="form-value" name="tel-national" autocomplete="tel-national">
        </div>
      </div>
      <div class="form-item">
        <label for="email" class="label">邮件地址</label>
        <div class="input">
          <input id="email" type="text" class="form-value" name="email" autocomplete="email">
        </div>
      </div>
      <div class="form-item">
        <label for="id-card-number" class="label">身份证</label>
        <div class="input">
          <input id="id-card-number" type="number" class="form-value" name="id-card-number" autocomplete="id-card-number">
        </div>
      </div>
      <div class="form-item">
        <label for="street-address" class="label">带街道地址</label>
        <div class="input">
          <input id="street-address" type="text" class="form-value" name="street-address" autocomplete="street-address">
        </div>
      </div>
      <div class="form-button">
        <button class="button" type="submit">提交</button>
      </div>
    </form>
  </div>
</template>
<script>
export default {
  data () {
    return {}
  }
}
</script>
<style scoped>
.header {
  width: 100%;
  display: flex;
  justify-content: center;
  font-size: 20px;
}
.form-item {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  margin-top: 20px;
  .label {
    width: 30%;
    line-height: 1.6;
    text-align: right;
  }
  .input {
    width: 50%;
    .form-value {
      width: 100%;
      line-height: 1.6;
      border-style: solid;
      border-width: 1px;
      border-color: #333333;
    }
  }
}
.form-button {
  width: 100%;
  margin-top: 20px;
  display: flex;
  align-items: center;
  .button {
    background-color:  blue;
    color: white;
    height: 25px;
    border: 0;
    font-size: 15px;
    border-radius: 10px;
    width: 120px;
    text-align: center;
  }
}
</style>
```
